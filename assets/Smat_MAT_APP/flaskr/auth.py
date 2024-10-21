# import libraies
from werkzeug.exceptions import abort
import re
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
# import from modules
from flaskr.db import get_db


bp = Blueprint('auth', __name__, url_prefix='/auth')
# defines the route for the module with as auth/<name>
# the url_prefix means that 'auth' does not have to be
# written to the indivual routes


def secure_login(role):
    # function to arort is security is on and
    # the current user is not in the list of allowed roles, 'role'

    # checks security status. status 1 is on and 0 is off
    db = get_db()
    secure = db.execute('SELECT status FROM security').fetchone()

    # aborts with 'Forbidden' if security is on and no user is logged in
    if g.user is None and secure['status'] == 1:
        return abort(403)

    # returns an continues if there is no user logged in and security is off
    if g.user is None and secure['status'] == 0:
        return

    # aborts with 'Forbidden' if security is on and
    # the user role is not in the 'role' list
    if (not g.user['user_role'] in role
       and secure['status'] == 1):
        return abort(403)

    # returns and continues if security checks are passed
    return


def password_check(password):
    # function to check the validity of a new password

    # list of failed checked is set to be empty
    check = []

    # defines the minimum number of characters for an allowed password
    min_length = 3
    # checkd password length
    if len(password) < min_length:
        # adds an error message if the check fails
        check.append('Passwords must contain at least %s characters'
                     % (str(min_length)))

    # defined a RegEx pattern contains a digit
    digit_test = r'\d'
    # searches the password for a digit
    if re.search(digit_test, password) is None:
        # adds an error message if the check fails
        check.append('Passwords must contain at least 1 number')

    # defined a RegEx pattern to contain a space
    space_test = r'\s'
    # searches the password for a space
    if re.search(space_test, password) is not None:
        # adds an error message if the check fails
        check.append('Passwords must not contain any spaces')

    # defined a RegEx pattern to contain a capital letter
    caps_test = r'[A-Z]'
    # searches the password for a capital letter
    if re.search(caps_test, password) is None:
        # adds an error message if the check fails
        check.append('Passwords must contain at least one captial letter')

    # defined a RegEx pattern to contain a lowercase letter
    lower_test = r'[a-z]'
    # searches the password for a lowercase letter
    if re.search(lower_test, password) is None:
        # adds an error message if the check fails
        check.append('Passwords must contain at least one lower case letter')

    # defined a RegEx pattern to contain only alpha-numeric charachers
    alpha_num_test = r'^[a-zA-Z0-9]+'
    # checks the password against the pattern
    x = re.match(alpha_num_test, password).group()
    if x != password:
        # adds an error message if the check fails
        check.append('Passwords must not cointain any special characters')

    # returns a list of errors
    return (check)


@bp.route('/register', methods=('GET', 'POST'))
# defined the route to register a new user
def register():
    # if security setting is on, the user role must be Admin
    secure_login(['Admin'])

    # checks security setting
    db = get_db()
    secure = db.execute('SELECT status FROM security').fetchone()

    # The user attributes are requested from a form
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_role = request.form['user_role']
        db = get_db()
        error = []
        # error messages are generated
        # if the username or password are not sepcified
        if not username:
            error.append('Username is required.')
        elif not password:
            error.append('Password is required.')

        # error message is generated if the user role is not allowed
        elif (user_role != 'Student'
              and user_role != 'Teacher'
              and user_role != 'Admin'):
            error.append('Incorrect Role')

        # checks the validity of the password
        checks = password_check(password)

        # adds any password check errors to the error list
        if checks != '':
            for check in checks:
                error.append(check)

        # adds the user to the database
        # if there are no errors or security is off
        if error == [] or secure['status'] == 0:
            try:
                db.execute(
                        "INSERT INTO user (username, password, user_role)\
                              VALUES (?, ?, ?)",
                        (username, generate_password_hash(password),
                         user_role),
                    )
                db.commit()
            # generates an error message if the user exists
            except db.IntegrityError:
                error.append(f'User {username} is already registered.')
            else:
                # if adding the user is successful, redirects to the main menu
                return redirect(url_for('auth.display_menu'))

        # displays all error messages from the list
        for message in error:
            flash(message)

    # displays the form using the 'register' template
    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
# defined the route to the login page
def login():
    # checks security setting
    db = get_db()
    secure = db.execute('SELECT status FROM security').fetchone()
    # The login details are requested from a form
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()

        # error message cleared
        error = None

        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        # checks the number of incorrect logins for the user
        counter = user['login_counter']
        # locks the accoount after 3 unsuccessful attempts if security is on
        if counter >= 3 and secure['status'] == 1:
            return ('Account Locked')
        # generates an erro message if the username does not exist
        if user is None:
            error = 'Incorrect username.'
        # checks the password
        elif not check_password_hash(user['password'], password):
            # if the password is incorrect,
            # the number of unsuccessful attempts incremented
            # and an error message is generates
            counter += 1
            counter = str(counter)
            error = 'Incorrect password ' + counter + ' Incorrect attempts'
            db.execute(
                'UPDATE user  SET login_counter =? '
                'WHERE user.id = ?', (counter, user['id']))
            db.commit()
        # if the login is successful the uncessful login attempts are set to 0
        if error is None:
            counter = 0
            db.execute('UPDATE user SET login_counter =?', (counter,))
            db.commit()
            session.clear()
            session['user_id'] = user['id']
            # the user is redirected to the menu page after a successful login
            return redirect(url_for('auth.display_menu'))
        # error messages are displayed
        flash(error)
    # displays the form using the 'login' template
    return render_template('auth/login.html')


@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    # function to delete a specified user, 'id'
    # if security setting is on, the user role must be Admin
    secure_login(['Admin'])
    # deletes the user from the database
    db = get_db()
    db.execute('DELETE FROM user WHERE id = ?', (id,))
    db.commit()
    # redirects the user to the display all users ('index') page
    return redirect(url_for('auth.index'))


@bp.route('/index')
# defined the route to the index page to display all users
def index():
    # if security setting is on, the user role must be Admin
    secure_login(['Admin'])
    # gets all users from the database
    db = get_db()
    users = db.execute(
        'SELECT u.id,  username, user_role'
        ' FROM user u '
        ' ORDER BY u.id'
    ).fetchall()
    # displays the users using the 'idex' template
    return render_template('auth/index.html', users=users)


# runs the function before each request to make allow each function to
# ccess teh current logged in user as teh 'g' object
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
# defined the route to the index page to display all users
def logout():
    # clears the logged in user data
    session.clear()
    # redirects to the 'login' page
    return redirect(url_for('auth.login'))


@bp.route('/menu')
# defined the route to the menu page
def display_menu():

    # checks security
    db = get_db()
    secure = db.execute('SELECT status FROM security').fetchone()

    # if security is off, the full 'Admin' menu will be used
    if secure['status'] == 0:
        role = '%admin%'
    # if security is on and no user is logged in,
    # the app aborts with the 'Forbidden' message
    else:
        if secure['status'] == 1 and g.user is None:
            abort(403)
        # the role parameter is taken as the user role
        # the '%' tags are used for the a Contains (LIKE) search - below
        else:
            role = '%' + (str(g.user['user_role']).lower()) + '%'

    # selects a menu table where the access column contains the specified role
    menu = db.execute(
            'SELECT * FROM menus '
            'WHERE access LIKE ? ', (role,)
        ).fetchall()

    # displays the menu page using the 'menu' template
    return render_template('auth/menu.html', menu=menu)


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
# defined the route to update a specified user with id, 'id'
def update(id):

    # if security is on, the user must loggin in with an allowed role
    secure_login(['Admin', 'Teacher', 'Student'])

    # checks security settings
    db = get_db()
    secure = db.execute('SELECT status FROM security').fetchone()

    # gets existing user
    user = db.execute(
        'SELECT u.id,  username, user_role'
        ' FROM user u '
        ' WHERE u.id = ?', (id,)
    ).fetchone()

    # The user details are requested from a form
    if request.method == 'POST':
        password = request.form['password']
        try:
            username = request.form['username']
        except KeyError:
            username = user['username']

        # clear error list
        error = []
        checks = ''
        # check passworkd format
        if secure['status'] == 1:
            checks = password_check(password)
        # adds any password checks to the error messages
        if checks != '':
            for check in checks:
                error.append(check)

        # if there are no errors, or the security settings are off
        # the user is deleted from the database
        if error == [] or secure['status'] == 0:

            user = db.execute(
                'UPDATE user SET password = ?, username = ?, login_counter = ?'
                ' WHERE id = ? ',
                (generate_password_hash(password), username, id, 0, ),
                )
            db.commit()
            # displays successful message
            flash('Password Changed')
            # redirects to the user display page
            return redirect(url_for('auth.display_menu'))

        # displays any error messages
        for message in error:
            flash(message)

    # displays the form page using the 'update' template
    return (render_template('auth/update.html', user=user, id=id))


@bp.route('/update')
# defined the route to update my password
def update_password():
    # this is the function for change my password
    # checks security settings
    db = get_db()
    secure = db.execute('SELECT status FROM security').fetchone()
    # if the security setting is on, the id is the loggin in user id
    # this allows the change my password option
    if secure['status'] == 1:
        id = g.user['id']
    else:
        # if the security is no on the id is set to is=1
        id = 1
    # redirects to the updae function specifying the id
    return redirect(url_for('auth.update', id=id))


@bp.route('/security', methods=('GET', 'POST'))
# defined the route to security settings
def security():
    # checks security setting
    db = get_db()
    secure = db.execute('SELECT * FROM security').fetchone()
    # if security is off, then the role is set to Admin to allow access
    if secure['status'] == 0:
        role = 'Admin'
    # if security is on, check the user role
    else:
        role = str(g.user['user_role'])
    # if the role is not Admin, then deny access, Unauthorised
    if role != 'Admin':
        abort(401)
    if request.method == 'POST':
        try:
            # checks if the security checkbox is checked
            s = request.form['security']
            if s == 'True':
                flash('Security On')
            # updates security setting status to on
            # if the checkbox is ticked
            db.execute('UPDATE security SET status =?', (1,))
            db.commit()
        except KeyError:
            # if the security checkbox is unchecked
            # the security setting is set to off
            db.execute('UPDATE security SET status =?', (0,))
            db.commit()
    # updates the security setting
    secure = db.execute('SELECT * FROM security').fetchone()
    # displays the security settings page using the 'security' template
    return render_template('auth/security.html', secure=secure)

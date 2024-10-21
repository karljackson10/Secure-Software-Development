# import libraies and modules
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

# from flaskr.auth import login_required, login, secure_login
from flaskr.auth import secure_login

from flaskr.db import get_db

# sets the blueprint route as assignments/<name>
bp = Blueprint('assignments', __name__)


@bp.route('/assignments/index')
# defined the route for the request to show all assignments
def index():
    # if security is on, then the user
    # must be logged in with an authorised role
    secure_login(['Admin', 'Teacher', 'Student'])
    # checks security status 0=off, 1=on
    db = get_db()
    secure = db.execute('SELECT * FROM security').fetchone()
    # if security is off and no user is logged in,
    # all assignments will be displayed
    if secure['status'] == 0 and g.user is None:
        posts = db.execute(
            'SELECT p.id, title, body, created, author_id, username'
            ' FROM post p JOIN user u ON p.author_id = u.id'
            ' ORDER BY created DESC'
        ).fetchall()
        return render_template('assignments/index.html', posts=posts)

    # if a student is not logged in, all assignmnets will be displayed
    if g.user['user_role'] != 'Student':
        posts = db.execute(
            'SELECT p.id, title, body, created, author_id, username'
            ' FROM post p JOIN user u ON p.author_id = u.id'
            ' ORDER BY created DESC'
        ).fetchall()
    # if a student is logged in, the assignments will be dislayed
    # if they have been assigned to them
    else:
        posts = db.execute(
            ' SELECT *'
            ' FROM marks m '
            ' JOIN user u ON m.student_id = u.id'
            ' JOIN post p ON m.assignment_id = p.id'
            ' WHERE u.id = ?', (g.user['id'],)
        ).fetchall()
    # displays the assignments using the 'index' template
    return render_template('assignments/index.html', posts=posts)


def get_post(id):
    # the function returns any assigment posted with the specified id
    # used in the update and delete functions

    # queries the database for an assignment with teh specified id, 'id'
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        # Not found error is shown when there is no match
        abort(404, f"Post id {id} doesn't exist.")

    # returns the assignment with its attributes
    return post


@bp.route('/assignments/create', methods=('GET', 'POST'))
# defined the route to create a new assignments
def create():
    # if security is on, then the user must be logged in
    # as either Admin or Teacher
    secure_login(['Admin', 'Teacher'])

    # if security is off and the user is not logged in,
    # the user id will be set to '1'
    if g.user is None:
        id = 1
    else:
        id = g.user['id']

    # the title and description(body)of the assignment
    # is requested from a form
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None
        # ensure a title is returned from the form
        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            # asdds teh assignment and its attributes to the list
            # the current user is the author
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, id)
            )
            db.commit()
            # disolays the list of assignments
            return redirect(url_for('assignments.index'))
    # displays the form using the 'create' template
    return render_template('assignments/create.html')


@bp.route('/assigments/<int:id>/update', methods=('GET', 'POST'))
# defined the route to update an assignments with a specified id, 'id'
def update(id):
    # if security is on, then the user must be logged in
    # with an Admin or Teacher role
    secure_login(['Admin', 'Teacher'])
    # gets the assigmnent posted with the specified id
    post = get_post(id)

    # the title and description(body)
    # of the assignment is requested from a form
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None
        # ensure a title is returned from the form
        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            # Updates the specified assignment in the database
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            # displays the list of assignments
            return redirect(url_for('assignments.index'))
    # displays the form using the 'update' template
    return render_template('assignments/update.html', post=post)


@bp.route('/assigments/<int:id>/delete', methods=('POST',))
# defined the route to delete an assignments with a specified id, 'id'
def delete(id):
    # if security is on, then the user must be logged in with an Admin role
    secure_login(['Admin', 'Teacher'])
    # gets the assignment posted with id, 'id'
    get_post(id)
    # deletes the assignment from the database
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    # displays the form using the 'update' template
    return redirect(url_for('assignments.index'))

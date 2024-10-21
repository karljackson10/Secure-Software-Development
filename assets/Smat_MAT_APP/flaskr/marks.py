# import libraries
from flask import (
    Blueprint, g, redirect, render_template, request, url_for)
from flaskr.auth import secure_login
from flaskr.db import get_db

bp = Blueprint('marks', __name__)


@bp.route('/marks/index')
# defined the route to display all assignments in the markbook
def index():
    # if security is on, the user must be loggin in with an allowed role
    secure_login(['Admin', 'Teacher', 'Student'])

    # checks if the user is logged in
    if g.user is not None:
        # if the user is a student, redirect to the individual mark page
        if str(g.user['user_role']).lower() == 'student':
            id = g.user['id']
            return (redirect(url_for('marks.student', id=id)))

    # gets all of the assignments posted
    db = get_db()
    posts = db.execute(
        ' SELECT *'
        ' FROM post p '
        ' JOIN user u ON p.author_id = u.id'
        ' ORDER BY created ASC'
    ).fetchall()
    # displays all assignmnets in the markbook with the 'index' template
    return render_template('marks/index.html', posts=posts)


@bp.route('/marks/<int:id>/view')
# defined the route to display all marks
# for a specified assignment (id) in the markbook
def view(id):
    # if security is on, the user must be logged in in with an allowed role
    secure_login(['Admin', 'Teacher', 'Student'])

    # gets all the marks for an assignment
    db = get_db()
    marks = db.execute(
        ' SELECT *'
        ' FROM marks m '
        ' JOIN user u ON m.student_id = u.id'
        ' WHERE m.assignment_id = ?'
        ' ORDER BY m.student_id ASC', (id,)
    ).fetchall()

    # get the attributes for the assignment posted
    post = db.execute(
        ' SELECT title, id, author_id'
        ' FROM post p '
        ' WHERE p.id = ? ', (id,)

    ).fetchone()

    # displays the markbook for an assignment using the 'view' template
    return render_template('marks/view.html',
                           marks=marks, post=post, assignment=id)


@bp.route('/marks/<int:id>/assign', methods=('GET', 'POST'))
# defined the route to display allocate users to an assignment
def assign(id):
    # if security is on, the user must be logged in in with an allowed role
    secure_login(['Admin', 'Teacher'])

    # gets all the marks for an assignment
    db = get_db()
    marks = db.execute(
        ' SELECT *'
        ' FROM user u  '
        ' LEFT JOIN marks m ON m.student_id = u.id AND m.assignment_id = ?'
        ' ORDER BY u.id ASC', (id,)
    ).fetchall()

    # get the attributes for the assignment posted
    post = db.execute(
        ' SELECT title, author_id'
        ' FROM post p '
        ' WHERE p.id = ? ', (id,)

    ).fetchone()

    # displays the assign users to an assignment using the 'assign' template
    return render_template('marks/assign.html',
                           marks=marks, post=post, assignment=id)


@bp.route('/<int:staff>/<int:assignment>/<int:student>/add_assignment',
          methods=('GET', 'POST',))
# defined the route to add a student to an assignment
def add_assignment(staff, assignment, student):

    # if security is on, the user must be logged in in with an allowed role
    secure_login(['Admin', 'Teacher'])

    # inserts a student into the markbook for a
    # specified assignment and allocated to specified staff
    db = get_db()
    db.execute(
                'INSERT INTO marks (staff_id, assignment_id, student_id )\
                      VALUES (?, ?, ?)',
                (staff, assignment, student),
                    )
    db.commit()
    # redirects to the assign users to an assignment
    # using the 'assign' template
    return redirect(url_for('marks.assign', id=assignment))


@bp.route('/<int:assignment>/<int:student>/remove_assignment',
          methods=('GET', 'POST',))
# defined the route to remove a student to an assignment
def remove_assignment(assignment, student):

    # if security is on, the user must be logged in in with an allowed role
    secure_login(['Admin', 'Teacher'])
    db = get_db()
    # removes a student from the markbook for a
    # specified assignment, allocated to specified staff
    db.execute(
            ' DELETE FROM marks '
            'WHERE assignment_id = ? AND student_id = ?',
            (assignment, student,))
    db.commit()
    # redirects to the assign users for an assignment page
    # using the 'assign' template
    return redirect(url_for('marks.assign', id=assignment))


@bp.route('/marks/<int:assignment>/<int:student>/update',
          methods=('GET', 'POST'))
# defined the route to update a student's marks and feedback for an assignment
def update(assignment, student):

    # if security is on, the user must be logged in in with an allowed role
    secure_login(['Admin', 'Teacher'])

    # gets the marks for a specified studnet for a specified assignment
    db = get_db()
    marks = db.execute(
        ' SELECT *'
        ' FROM marks m '
        ' JOIN user u ON m.student_id = u.id'
        ' WHERE m.assignment_id = ? AND u.id = ?'
        ' ORDER BY m.student_id ASC', (assignment, student,)
    ).fetchone()

    # gets the title of the assignment
    title = db.execute(
        ' SELECT title'
        ' FROM post p '
        ' WHERE p.id = ? ', (assignment,)
    ).fetchone()

    # gets the marks and feedback from a form
    if request.method == 'POST':
        mark = request.form['mark']
        feedback = request.form['feedback']

        # updates the marks and feedback for the specied student assignment
        marks = db.execute(
            'UPDATE marks SET mark = ?, feedback = ?'
            ' WHERE assignment_id = ? AND student_id=? ',
            (mark, feedback, assignment, student,),
            )
        db.commit()
        # redirects to the markbook for the assigment using the 'view' template
        return redirect(url_for('marks.view', id=assignment))

    # displays the form to update the  marks  using the 'update' template
    return render_template('marks/update.html', assignment=assignment,
                           title=title, student=student, marks=marks)


@bp.route('/marks/<int:id>/student')
# defined the route to student's marksfor all their assignments
def student(id):

    # if security is on, the user must be logged in in with an allowed role
    secure_login(['Admin', 'Teacher', 'Student'])

    # gets all teh marks for the specified student
    db = get_db()
    marks = db.execute(
        ' SELECT *'
        ' FROM marks m '
        ' JOIN user u ON m.student_id = u.id'
        ' JOIN post p ON m.assignment_id = p.id'
        ' WHERE u.id = ?', (id,)
    ).fetchall()

    # gets the student username
    student = db.execute(
        ' SELECT username '
        ' FROM user u'
        ' WHERE u.id = ?', (id,)
    ).fetchone()

    # displays the student markbook using the 'student' template
    return render_template('marks/student.html', marks=marks, student=student)


@bp.route('/marks/<int:assignment>/<int:student>/submit',
          methods=('GET', 'POST'))
# defined the route to student's submission page
def submit(assignment, student):

    # if security is on, the user must be logged in in with an allowed role
    secure_login(['Admin', 'Teacher', 'Student'])

    # gets the marks and work submitted for the
    # specified studnet and specified assignment
    db = get_db()
    work = db.execute(
        ' SELECT *'
        ' FROM marks m'
        ' JOIN user u ON m.student_id = ?'
        ' JOIN post p ON m.assignment_id = ?',
        (student, assignment,)

    ).fetchone()

    # gets work submission from the a form
    if request.method == 'POST':
        work = request.form['work']

        # updates the work submission and stores in the database
        work = db.execute(
            'UPDATE marks SET work = ?'
            ' WHERE assignment_id = ? AND student_id=? ',
            (work,  assignment, student,),
            )
        db.commit()
        # redirects to the student's markbok page
        return redirect(url_for('marks.student', id=student))

    # displays the student submission form using the 'submit' template
    return render_template('marks/submit.html', work=work)

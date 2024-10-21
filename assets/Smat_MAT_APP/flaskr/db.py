# import libraries
import sqlite3
# import os
import click
from flask import current_app, g
# from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.security import generate_password_hash


def get_db():
    # returns the database to allow queries
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    # closes database
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    # initiates database
    db = get_db()

    # defines the menu options and access rights
    menu = [
        ['Diplay user', './index', 'admin'],
        ['Register new user', './register', 'admin'],
        ['View Assignments', '../assignments/index',
         'admin, teacher, student'],
        ['New Assignment', '../assignments/create', 'admin, teacher'],
        ['View Marks', '../marks/index', 'admin, teacher, student'],
        ['Change My Password', './update', 'admin, teacher, student'],
        ['Security Settings', './security', 'admin'],
        ['Log Out', './logout', 'admin, teacher, student']
    ]

    # defined the schema for the database
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

    # sets default security setting to on (1)
    db.execute(
                "INSERT INTO security ( status ) VALUES (?)",
                (1,),
                    )

    # sets default Admin user
    db.execute(
                "INSERT INTO user (username, password, user_role)\
                     VALUES (?, ?, ?)",
                ('admin', generate_password_hash('123'), 'Admin'),
                    )
    # sets dummy student user
    db.execute(
                "INSERT INTO user (username, password, user_role)\
                     VALUES (?, ?, ?)",
                ('student1', generate_password_hash('123'), 'Student'),
                    )
    # sets dummy assignment
    db.execute(
                "INSERT INTO post (author_id, title, body) VALUES (?, ?, ?)",
                (1, 'Test 1', 'Test Content'),
                    )

    # insert dummy marks and feedback to the database
    db.execute(
                "INSERT INTO marks\
                     (staff_id, assignment_id, student_id,\
                          mark, work, feedback)\
                VALUES (?, ?, ?, ?, ?, ?)",
                (1, 1, 2, 7, 'student work', 'ver good'),
                    )

    # inserts the menu items into the database
    for item in menu:
        db.execute(
                "INSERT INTO menus (choice, link, access)\
                     VALUES (?,?,?)", (item),
            )

    db.commit()


@click.command('init-db')
def init_db_command():
    # clear the existing data and create new tables.
    init_db()
    # send message to terminal
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

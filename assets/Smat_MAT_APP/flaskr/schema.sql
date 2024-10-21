--Delete tables if they exist
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS marks;
DROP TABLE IF EXISTS menus;
DROP TABLE IF EXISTS security;


--Creates the user table
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  user_role TEXT DEFAULT 'Student',
  login_counter INT DEFAULT 0
);


--Creates the assignment posts table
CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);


--Creates the marks table
CREATE TABLE marks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  staff_id INTEGER NOT NULL,
  assignment_id INTEGER NOT NULL,
  student_id INTEGER,
  mark INTEGER,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  work VARBINARY,
  feedback TEXT NULL,
  FOREIGN KEY (staff_id) REFERENCES user (id),
  FOREIGN KEY (assignment_id) REFERENCES post (id)
);


--Creates the menus table
--This is not linked to the database
--This is used to display the correct menu
--Which is dependant on the user role
CREATE TABLE menus (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  choice TEXT NOT NULL,
  link TEXT NOT NULL,
  access TEXT
);


--Creates the security table
--This is not linked to the database
--This is used to turn the security on or off
CREATE TABLE security (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  status INT NOT NULL DEFAULT 1
);
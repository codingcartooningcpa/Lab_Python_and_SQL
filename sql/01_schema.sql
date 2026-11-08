-- Registration database: one Student table for the Chapter 9 lab.
-- Runs automatically the first time the codespace starts.
-- To start over at any time, run:  python reset_db.py

DROP TABLE IF EXISTS Student;

CREATE TABLE Student (
    StudentID  INT          PRIMARY KEY,
    FirstName  VARCHAR(30),
    LastName   VARCHAR(30)  NOT NULL,
    Major      VARCHAR(30)
);

INSERT INTO Student (StudentID, FirstName, LastName, Major) VALUES
    (101, 'Ada',       'Lovelace', 'Nursing'),
    (102, 'Grace',     'Hopper',   'Nursing'),
    (103, 'Alan',      'Turing',   'Nursing'),
    (104, 'Katherine', 'Johnson',  'Mathematics'),
    (105, 'Dorothy',   'Vaughan',  'Mathematics'),
    (106, 'Edgar',     'Codd',     'Computer Science'),
    (107, 'Barbara',   'Liskov',   'Computer Science'),
    (108, 'Mary',      'Jackson',  'Engineering');

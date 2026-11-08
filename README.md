# CTS 2433 – Python + MySQL Lab (Chapter 9)

This project runs entirely in your browser. You get VS Code, Python, and a
real MySQL server, with nothing to install on your computer.

## Start your codespace

1. Sign in to GitHub.
2. On this page, click the green **Code** button, open the **Codespaces** tab,
   and click **Create codespace on main**.
3. Wait 2–4 minutes the first time. VS Code opens in your browser.
4. Open a terminal: **Terminal → New Terminal** (or press <kbd>Ctrl</kbd>+<kbd>`</kbd>).

## Run the lab, one step at a time

Type each command in the terminal and press Enter.

| Command | What it shows |
|---|---|
| `python step0_check_connection.py` | Python can reach MySQL (run this first) |
| `python step1_select.py` | Connect → execute → fetch → close |
| `python step2_user_input.py` | A value typed by the user, sent with a placeholder |
| `python step3_insert_commit.py` | Why `commit()` is required |
| `python step4_sql_injection.py` | Unsafe vs. safe queries |
| `python step5_stored_procedure.py` | Creating and calling a stored procedure |
| `python reset_db.py` | Put the Student table back to its starting data |

## The database

Database `Registration`, table `Student`:

| StudentID | FirstName | LastName | Major |
|---|---|---|---|
| 101 | Ada | Lovelace | Nursing |
| 102 | Grace | Hopper | Nursing |
| 103 | Alan | Turing | Nursing |
| 104 | Katherine | Johnson | Mathematics |
| 105 | Dorothy | Vaughan | Mathematics |
| 106 | Edgar | Codd | Computer Science |
| 107 | Barbara | Liskov | Computer Science |
| 108 | Mary | Jackson | Engineering |

## When you are done

Your codespace stops by itself after 30 minutes of no activity. To save your
free hours, you can stop it sooner at <https://github.com/codespaces>
(click **…** next to it → **Stop codespace**). Delete it there when the lab
is over.

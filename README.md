This is my first attempt at a personal project.

I'm trying to automate the process of checking 2 different websites for their interest rates every day and saving to a SQLite database.

The 2 issues I'm currently running into are with the re.search function not finding the HTML code on Ford's website
and the SQL database storing NaN instead of the day and rates when I try to use the INSERT INTO function.

The file "delete.py" is used to delete a row in the SQL table so that you can rerun "rates.py" and have it store data again.

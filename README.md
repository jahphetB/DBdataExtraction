# DBdataExtraction
In this project, We will extract information from Chinook.db using Python and SQL, and present the information on graphs using Python graph modules. 
Goals of this project:
1) See artists' sales graph, sorted by revenue or country.
2) Filter top selling tracks(as many tracks as requested).
3) Filter top selling albums(as many albums as requested).

Getting Started:
To code along with this project, follow these steps:
1. Set up your Replit environment since it's a convenient platform for working with databases using SQLite.
2. Create a Python Repl within Replit.
3. Download the Chinook database from GitHub and upload it to the Python Repl you just created.
4. Connect the database to Python and start coding. You can refer to the [official SQLite3 documentation] (https://docs.python.org/3/library/sqlite3.html) for guidance.

Exploring Chinook.db:
If you want to explore the nature of the Chinook.db database, follow these steps:
1. Create an SQLite Repl.
2. Upload the Chinook.db database.
3. Create an SQLite file and name it "sch.sql."
4. In "sch.sql," write the following commands:
   .tables
   .schema
5. In your SQLite Repl, open the Chinook database and set the output mode to "box" with headers on. Run the commands from "sch.sql" by pasting the following code into "main.sql":
   .open Chinook.db
   .mode box
   .headers on
   .read sch.sql
6. Hit the run button to execute the commands.

Testing and Updates:
I will be testing my code on (https://replit.com/) and regularly updating the code in my GitHub repository (DBdataExtraction). 

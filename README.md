# DBdataExtraction
In this project, we aim to extract and visualize information from the Chinook.db database using Python and SQLite. I will present the extracted data through graphs created with Python graph modules. Our primary objective is to build a filter widget that can be integrated into websites, enabling users to extract important information from databases like Chinook.db. The features of our filter widget include:

1) Artists' Sales Graph: Display a graph of artists' sales, which can be sorted by revenue or country.

2) Filter Top-Selling Tracks: The ability to filter and display the top-selling tracks, with the option to specify the number of tracks to be shown.

3) Filter Top-Selling Albums: Providing a filter option to display the top-selling albums, with the flexibility to specify the number of albums to be shown.

For now, these are our initial goals. However, I have plans to expand the functionality of our code to make it versatile and adaptable for various customized purposes.

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

.tables \n
.schema

6. In your SQLite Repl, open the Chinook database and set the output mode to "box" with headers on. Run the commands from "sch.sql" by pasting the following code into "main.sql":

.open Chinook.db \n
.mode box \n
.headers on \n
.read sch.sql \n

7. Hit the run button to execute the commands.

Testing and Updates:
I will be testing my code on (https://replit.com/) and regularly updating the code in my GitHub repository (DBdataExtraction). 

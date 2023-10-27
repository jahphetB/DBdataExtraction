# DBdataExtraction
In this project, we aim to extract and visualize information from the Chinook.db database using Python and SQLite. We will present the extracted data through graphs created with Python graph modules. Our primary objective is to build a filter widget that can be integrated into websites, enabling users to extract important information from databases like Chinook.db. The features of our filter widget include:

1) Artists' Sales Graph: Display a graph of artists' sales, which can be sorted by revenue or country.

2) Filter Top-Selling Tracks: The ability to filter and display the top-selling tracks, with the option to specify the number of tracks to be shown.

3) Filter Top-Selling Albums: Providing a filter option to display the top-selling albums, with the flexibility to specify the number of albums to be shown.

For now, these are our initial goals. However, we have plans to expand the functionality of our code to make it versatile and adaptable for various customized purposes.

To code along:
  1) Set up your Replit.
  2) create a python Repl.
  3) Download the Chinook database from Git Hub and upload it on the Python Repl that you just created.
  4) Connect the database to Python, and start coding. Check out(https://docs.python.org/3/library/sqlite3.html).
     
To see the nature of Chinook.db:
  1) Create an SQLite Repl.
  2) Upload Choonk.db.
  3) Create an SQLite file and name it sch.sql.
  4) Write ".table" and ".schema" in sch.sql.
  5) Paste the following code on main.sql.
.open Chinook.db
.mode box
.headers on 
.read sch.sql
  6) Hit the run button. 
  

I will test my code on Replite.com and post all my up-to-date code on my Github repository (DBdataExtraction).

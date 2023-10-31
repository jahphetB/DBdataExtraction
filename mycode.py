import sqlite3
import matplotlib.pyplot as plt

#Connect Chinook.db to python, and intialiaz a cursor
con = sqlite3.connect("Chinook.db")
cur = con.cursor()

# Find Artists Sales then sort them by country or track
def get_artist_data():

    # Ask users to enter the name of an artist who they want to see their data.
    # code

    # then

    # Ask users if they want to see Revenue by Track or Country.
    # code

    def by_country():
        pass
    
    def by_track():
        pass

# Find top selling tracks in Chinook.db
def get_top_tracks():

    # Ask users how many top selling tracks they would like to see.
    # code

    # Arrage tracks in a dictionary in a way that the keys of the dictionary are tracks and the values are revenue (quantity times price)
    def track_and_revenue():
        pass

    # A function to sort and extract whatever many top selling tracks the user want to see. 
    def sort_tracks():
        pass

# Find Top selling albums
def get_top_albums():

    # Ask users how many top selling albums they would like to see and store the value in tops. 
    # code

    # Get as many top selling albums as the users want and sort them. 
    def sort_albums():
        pass

def main():

    # Ask users if they want to see sales information about specific artist or top selling tracks or albums
    # code
    pass

main()




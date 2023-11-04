import sqlite3
import matplotlib.pyplot as plt

#Connect Chinook.db to python, and intialiaz a cursor
con = sqlite3.connect("Chinook.db")
cur = con.cursor()

# Find Artists Sales then sort them by country or track
def get_artist_data():

    # Ask users to enter the name of an artist who they want to see their data.
    Artist_name = str(input("Enter artist name?"))

    # Ask users if they want to see Revenue by Track or Country.
    Track_or_Country = int(input("If you want to see Revenue of each track enter 1.\nIf you want to see Revenue by Country enter 2:\n"))

    # SQL query to retrieve the track name, unit price, country of sale, and quantity sold for all tracks. 
    Artist_work_info = cur.execute("select Track.Name, InvoiceLine.Quantity, InvoiceLine.UnitPrice, Invoice.BillingCountry from Artist join Album on Artist.ArtistID = Album.ArtistID join Track on Album.AlbumID = Track.AlbumID join InvoiceLine on Track.TrackID = InvoiceLine.TrackID join Invoice on InvoiceLine.InvoiceID = Invoice.InvoiceID where Artist.Name = ?", (Artist_name,))
    Trax = Artist_work_info.fetchall()

    def by_country():
        dict_for_graph_country = {}
        for item in Trax:
            track, quantity, unitprice, country = item
            if country in dict_for_graph_country:
                dict_for_graph_country[country] += quantity * unitprice
            else:
                dict_for_graph_country[country] = quantity * unitprice
        colors = ['green', 'red', 'yellow', 'blue']
        colors = colors * (len(dict_for_graph_country) // len(colors) + 1 )
        colors = colors[:len(dict_for_graph_country)]
        plt.bar(dict_for_graph_country.keys(), dict_for_graph_country.values(), color=colors)
        plt.xlabel("Country")
        plt.ylabel("Total sale by country")
        plt.title(f"{Artist_name}'s track sales by country")
        return plt.show()
  

    def by_track():
        dict_for_graph_track = {}
        for item in Trax:
            track, quantity, unitprice, country = item
            if track in dict_for_graph_track:
                dict_for_graph_track[track] += quantity * unitprice
            else:
                dict_for_graph_track[track] = quantity * unitprice
  
        colors = ['green', 'red', 'yellow', 'blue']
        colors = colors * (len(dict_for_graph_track) // len(colors) + 1 )
        colors = colors[:len(dict_for_graph_track)]
        plt.bar(dict_for_graph_track.keys(), dict_for_graph_track.values(), color = colors)
        plt.xlabel("Tacks")
        plt.ylabel("Total sale per track")
        plt.title(f"{Artist_name}'s track sales")
        return plt.show()
    
    if Track_or_Country == 1:
        by_track()
    elif Track_or_Country == 2:
        by_country()
  

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
    user_input = int(input("What would you like to see?\n  - If you want to see sales graphs of your favorite artist, please enter 1.\n  - If you would like to see top selling tracks, please enter 2.\n  - If you would like to see top selling albums, please enter 3.\nEnter a number : "))
    if user_input == 1:
        get_artist_data()
    if user_input == 2:
        get_top_tracks()
    if user_input == 3:
        get_top_albums()


main()
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
  
  #
  # Top selling tracks in Chinook.db
  #
  
  # Ask users how many top selling tracks they would like to see.
  tops = int(input("How many top selling tracks would you like to see?\n"))
  
  # SQL query to retrieve track names, billing country, price, and quantity sold. 
  All_artist_work_info = cur.execute("select Track.Name, InvoiceLine.Quantity, InvoiceLine.UnitPrice, Invoice.BillingCountry from Artist join Album on Artist.ArtistID = Album.ArtistID join Track on Album.AlbumID = Track.AlbumID join InvoiceLine on Track.TrackID = InvoiceLine.TrackID join Invoice on InvoiceLine.InvoiceID = Invoice.InvoiceID")
  all_info_tuple = All_artist_work_info.fetchall()
  
  # Arrage tracks in a dictionary in a way that the keys of the dictionary are tracks and the values are revenue (quantity times price). 
  def track_and_revenue():
    all_track_revenue = {}
    for item in all_info_tuple:
      track, quantity, price, country = item
      if track in all_track_revenue:
        all_track_revenue[track] += quantity * price
      else:
        all_track_revenue[track] = quantity * price
    return all_track_revenue
  
  # A dictionary to store top selling tracks
  top_tracks = {}
  
  # A function to extract whatever many top selling tracks the user want to see. 
  def sort_tracks():
    all_track_revenue = track_and_revenue()
    for i in range(tops):
      for item in all_track_revenue.items():
        track, revenue = item
        top = max(all_track_revenue.values())
        top_track = ""
        if revenue == top:
          top_track = track
          top_tracks[track] = revenue
          all_track_revenue.pop(top_track)
          break #Exit the loop onec a top track has been found. 
  
  colors = ['green', 'red', 'yellow', 'blue']
  colors = colors * (tops // len(colors) + 1 )
  colors = colors[:tops]
  
  sort_tracks()
  plt.bar(top_tracks.keys(), top_tracks.values(), color = colors)
  plt.xlabel("Tacks")
  plt.ylabel("Revenue")
  plt.title(f"top {tops} selling tracks")
  return plt.show()
  
  
def get_top_albums():
  
  #
  # Top selling albums
  #
  
  # Ask users how many top selling albums they would like to see and store the value in tops. 
  tops = int(input("How many top selling albums would you like to see?\nEnter a number: "))
  
  # Sql quary to extract artists name, album Ids, album titles and albums revenue. 
  albums_info = cur.execute("select Artist.Name, Album.AlbumID, Album.Title, sum(InvoiceLine.Quantity * InvoiceLine.UnitPrice) from Artist join Album on Artist.ArtistID = Album.ArtistID join Track on Album.AlbumID = Track.AlbumID join InvoiceLine on Track.TrackID = InvoiceLine.TrackID join Invoice on InvoiceLine.InvoiceID = Invoice.InvoiceID group by Album.Title")
  
  albums_info_tuble = albums_info.fetchall()
  
  # Put album titles and their revenue in a dictionary. The key of the dictionary is the title of albums and the value of the dictionary is reveue of albums.
  album_with_revenue = {}
  for item in albums_info_tuble:
    id1, id, title, revenue = item
    if title in album_with_revenue:
      album_with_revenue[title] += revenue
    else:
      album_with_revenue[title] = revenue
  
  # Get as many top selling albums as they users asks from album_with_revenue. 
  dict_for_graph_album ={}
  def sort_albums():
    for i in range(tops):
      top = max(album_with_revenue.values())
      title = ""
      for title2, revenue in album_with_revenue.items():
        if top == revenue:
          title = title2
          dict_for_graph_album[title] = top
          album_with_revenue.pop(title)
          break
  sort_albums()
  
  colors = ['green', 'red', 'yellow', 'blue']
  colors = colors * (tops // len(colors) + 1 )
  colors = colors[:tops]
  
  plt.bar(dict_for_graph_album.keys(), dict_for_graph_album.values(), color = colors)
  plt.xlabel("Albums")
  plt.ylabel("Revenues")
  plt.title(f"Top {tops} selling albums in the Chinook database.")
  return plt.show()
  
def main():
  # Ask users if they want to see sales information about specific artist or top selling tracks or albums
  user_input = int(input("What would you like to see?\n  - Sales graphs of your favorite artist? please enter 1.\n  - Top selling tracks? please enter 2.\n  - Top selling albums? please enter 3.\nEnter a number : "))
  if user_input == 1:
    get_artist_data()
  if user_input == 2:
    get_top_tracks()
  if user_input == 3:
    get_top_albums()

main()
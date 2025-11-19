class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    def __init__(self,name,  artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1
    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment 
    @classmethod
    def add_to_genres(cls, genre):  
        cls.genres.append(genre)
    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)

    # @classmethod
    # def add_to_genre_count(cls):
    #     for genre in cls.genres:
    #     return(cls.genre_count)    



    pass

a_milli = Song("A Milli", "Lil Wayne", "Hip-Hop") 
humble = Song("HUMBLE", "Kendrick Lamar", "Rap") 
sing_for_the_moment = Song("Sing For The Moment", "Eminem", "Rap")  

print(Song.genre_count)


# names = ["Collins", "Collins", "Mark", "John"] 

# name_counts = {}

# for name in names:
#     if name in name_counts:
#      name_counts[name] += 1
#     else:
#         name_counts[name] = 1    
    
# print(name_counts)    


# names_2 ={}
# names_ex= ["Collins", "Collins", "Mark", "John"] 
# for name in names_ex:
#     # if name in names_2:
#     #  names_2[name] += 1
#     # else:
#     #     names_2[name] = 1  
#     names_2[name] = names_2.get(name, 0) + 1 

# print(names_2)           





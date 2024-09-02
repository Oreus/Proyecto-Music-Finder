songs_db = [
    {"title": "Blinding Lights", "artist": "The Weeknd", "genre": "Synthwave", "length": 200, "release_year": 2019},
    {"title": "Levitating", "artist": "Dua Lipa", "genre": "Pop", "length": 203, "release_year": 2020},
    {"title": "Save Your Tears", "artist": "The Weeknd", "genre": "Synthpop", "length": 215, "release_year": 2020},
    {"title": "Don't Start Now", "artist": "Dua Lipa", "genre": "Pop", "length": 183, "release_year": 2019},
    {"title": "Good 4 U", "artist": "Olivia Rodrigo", "genre": "Pop Rock", "length": 178, "release_year": 2021},
    {"title": "Peaches", "artist": "Justin Bieber", "genre": "R&B", "length": 198, "release_year": 2021},
    {"title": "Watermelon Sugar", "artist": "Harry Styles", "genre": "Pop", "length": 173, "release_year": 2019},
    {"title": "Montero (Call Me By Your Name)", "artist": "Lil Nas X", "genre": "Hip-Hop", "length": 137, "release_year": 2021},
    {"title": "Dynamite", "artist": "BTS", "genre": "K-Pop", "length": 199, "release_year": 2020},
    {"title": "Stay", "artist": "The Kid LAROI", "genre": "Pop", "length": 141, "release_year": 2021}
]

def genre_search(genre_wanted):
    song_list = []
    for song in songs_db:
        if(song["genre"] == genre_wanted):
            song_list.append(song)
    return song_list

def readable_results(songs_found):
    for song in songs_found:
        print(song)
    return

genre_wanted = input('''Genre : 
1. Rock
2. Pop
3. R&B
4. K-Pop
5. Hip-Hop
6. Synthwave
7. Synthpop
8. Pop Rock
Enter the genre wanted: ''')

songs_found = genre_search(genre_wanted)

print(readable_results(songs_found))
songs_db = [    {"title": "Blinding Lights", "artist": "The Weeknd", "genre": "Synthwave", "length": 200, "release_year": 2019},
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

def get_recommendations(genre=None, year=None, min_length=None, max_length=None):
    recommendations = []
    for song in songs_db:
        if genre and song["genre"].lower() != genre.lower():
            continue
        if year and song["release_year"] != year:
            continue
        if min_length and song["length"] < min_length:
            continue
        if max_length and song["length"] > max_length:
            continue
        recommendations.append(song)
    return recommendations

def readable_results(songs_found):
    if not songs_found:
        print("No songs found matching your criteria.")
        return
    print("Recommended Songs:")
    for song in songs_found:
        print(f"{song['title']} by {song['artist']} ({song['release_year']}) - {song['length']} seconds")
    return

while True:
    genre_input = input("Enter genre (leave blank for any): ")
    year_input = input("Enter release year (leave blank for any): ")
    min_length_input = input("Enter minimum song length in seconds (leave blank for any): ")
    max_length_input = input("Enter maximum song length in seconds (leave blank for any): ")

    year_input = int(year_input) if year_input else None
    min_length_input = int(min_length_input) if min_length_input else None
    max_length_input = int(max_length_input) if max_length_input else None

    recommended_songs = get_recommendations(
        genre=genre_input,
        year=year_input,
        min_length=min_length_input,
        max_length=max_length_input
)

    readable_results(recommended_songs)

    repeat = input("Do you want to search again? (yes/no): ").strip().lower()
    if repeat != 'yes':
        print("Thank you for using the recommendation system!")
        break
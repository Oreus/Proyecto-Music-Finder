import math

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

matrix = [[song["length"], song["release_year"], song["genre"]] for song in songs_db]

def calculate_distance(song1, song2):
    length_diff = song1[0] - song2[0]
    year_diff = song1[1] - song2[1]
    
    distance = math.sqrt(length_diff**2 + year_diff**2)
    
    if song1[2].lower() != song2[2].lower():
        distance += 100 
    
    return distance

def recommend_similar_songs(target_song_index, threshold=150):
    target_song = matrix[target_song_index]
    recommendations = []
    
    for i, song in enumerate(matrix):
        if i == target_song_index:
            continue  
        distance = calculate_distance(target_song, song)
        if distance <= threshold:  
            recommendations.append(songs_db[i])
    
    return recommendations

def readable_results(songs_found):
    if not songs_found:
        print("No songs found matching your criteria.")
        return
    print("Recommended Songs:")
    for song in songs_found:
        print(f"{song['title']} by {song['artist']} ({song['release_year']}) - {song['length']} seconds - {song['genre']}")
    return

while True:
    print("Available songs:")
    for i, song in enumerate(songs_db):
        print(f"{i}: {song['title']} by {song['artist']}")

    song_choice = int(input("Select a song number to get recommendations based on it: "))
    
    similarity_threshold = int(input("Enter similarity threshold (higher means more flexibility): "))
    
    similar_songs = recommend_similar_songs(song_choice, threshold=similarity_threshold)
    readable_results(similar_songs)

    repeat = input("Do you want to search for another song? (yes/no): ").strip().lower()
    if repeat != 'yes':
        print("Thank you for using the recommendation system!")
        break

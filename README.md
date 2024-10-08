# Proyecto Music Finder
This project aims to help users discover new music based on their existing preferences. Whether you're looking for songs similar to your favorite tracks or exploring new genres, this tool provides personalized recommendations to enhance your listening experience.

## Project Overview
In a world full of music, finding new songs that match your taste can be overwhelming. This project addresses this challenge by offering a sophisticated recommendation system that suggests songs based on user-defined parameters.

## Key Features
Genre-Based Recommendations: Input your favorite genre and other specific criteria to find music that fits your taste.
Customizable Parameters: Tailor your search with parameters such as release year, song length, and artist to get more precise recommendations.
Advanced Matching Algorithm: Utilizes a robust algorithm to compare user input with a curated database of songs and deliver accurate suggestions.

## How It Works
The program will function by accessing a database of songs that I will provide for it. The user will then put into the program the genre of the music they wish to find. The prorgram will also ask them for other criteria, such as song length, artist, or realease year. The program will then take the information that was given to it, and use that set of parameters to search the given data base for results matching the request. The program will then give between 1-5 results based on how many songs within the database match the request.

## Algorithm
### Inputs:
- genre 
- song_length (optional)
- artist (optional)
- release_year (optional)
### Process:
1. Ask the user for the genre.
2. Ask the user for song_length (optional).
3. Ask the user for artist (optional).
4. Ask the user for release_year (optional).
5. Define matching_songs as an empty list.
6. For each song in the database:
- If the song’s genre matches the user’s genre:
  - If song_length matches (or is not provided):
    - If artist matches (or is not provided):
      - If release_year matches (or is not provided):
        - Add the song to matching_songs.
7. If matching_songs is not empty:
- If the length of matching_songs > 5:
  - Randomly select 5 songs from matching_songs.
- Otherwise, select all songs from matching_songs.
- Display the selected songs to the user.
8. If matching_songs is empty:
- Notify the user that no matches were found and suggest expanding or modifying the search criteria.
9. Ask the user if they want to perform another search or end the session.
### Outputs:
- List of matching songs (maximum 5 songs).

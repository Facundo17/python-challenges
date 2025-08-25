"""
Create a program that starts with a predefined list of your favorite movies. For example:

favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]

Place the above list in your .py script and then add some code that does the following:

1 Adds a new movie to the list (e.g., “Godfather”).

2 Removes a specific movie from the list (e.g., “The Matrix”).

3 Prints out the total number of movies in the list.

4 Prints out the movies in alphabetical order.    
"""

favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Pacific Rim"]

while True:
    print("\nFavorite Movies Organizer")
    print("1. Add a new movie")
    print("2. Remove a specific movie")
    print("3. Show total number of movies")
    print("4. Show movies in alphabetical order")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == '1':
        new_movie = input("Enter the name of the movie to add: ")
        favorite_movies.append(new_movie)
        print(f'"{new_movie}" has been added to your favorite movies.')

    elif choice == '2':
        movie_to_remove = input("Enter the name of the movie to remove: ")
        if movie_to_remove in favorite_movies:
            favorite_movies.remove(movie_to_remove)
            print(f'"{movie_to_remove}" has been removed from your favorite movies.')
        else:
            print(f'"{movie_to_remove}" is not in your favorite movies list.')

    elif choice == '3':
        print(f'Total number of movies in your list: {len(favorite_movies)}')

    elif choice == '4':
        print("\nMovies in alphabetical order:")
        for movie in sorted(favorite_movies):
            print(f"- {movie}")

    elif choice == '5':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
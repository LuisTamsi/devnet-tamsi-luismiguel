"""
Midterm Practical Exam — Movie Collection Manager
Student: [your name]
"""

movies = []


def display_menu():
    print(" === Movie Collection Manager === ")
    print("1. Add a movie")
    print("2. View all movies")
    print("3. Count watched vs unwatched")
    print("4. Find a movie")
    print("5. Exit")

    


def add_movie(movie_list):
    # ask for title, director, and status
    # build the movie string
    # add it to the list
    movie_title = input("Title of the movie: ")
    movie_director = input("Director of the movie: ")
    movie_status = input("Status: watched or unwatched: ")

    if movie_status.lower() != "watched" and movie_status.lower() != "unwatched":
        print("Invalid Status")
        return

    movie_format = f"{movie_title.title()} - {movie_director.title()} - {movie_status.title()}"
    movie_list.append(movie_format)
    print("Movie added successfully.")




def view_movies(movie_list):
    if not movie_list:
        print("No available movies")
    else:
        print("=====List of movies available=====")
        for  i, movie in enumerate(movie_list, start=1):
            print(f"{i}. {movie}")
        print("=" * 15)    




def count_watched_unwatched(movie_list):
    watched_counter = 0
    unwatched_counter = 0

    for movie in movie_list:
        if "Watched" in movie: 
            watched_counter += 1
        elif "Unwatched" in movie:
            unwatched_counter += 1
            
    return watched_counter, unwatched_counter


     

def find_movie(movie_list):
    # ask for a movie title
    # search the list
    # search should be case-insensitive
    # print the result or "Movie not found."
    movie_title = input("Search for movie title: ")
    
    for movie in movie_list:
        if movie_title.title() in movie:
            print(f"Search found: {movie}")
        else:
            print("Movie not found.")





def main():
    while True:
        display_menu()
        choice = int(input("Choose an option: "))
        match choice:
            case 1:
                add_movie(movies)
            case 2:
                view_movies(movies)
            case 3:
                watched, unwatched = count_watched_unwatched(movies)
                print("=" * 10)
                print(f"Number of watched movies: {watched}")
                print(f"Number of unwatched movies: {unwatched}")
                print("=" * 10)
            case 4: 
                find_movie(movies)
            case 5:
                print("Leaving...")
                exit()
            case _:
                print("Invalid choice")

main()




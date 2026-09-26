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


    movie_format = f"{movie_title} - {movie_director} - {movie_status}"

    movie_list.append(movie_format)

    print("Movie added successfully.")




def view_movies(movie_list):
    if not movie_list:
        print("No available movies")
    else:
        for  i, movie in enumerate(movie_list, start=1):
            print("List of movies available.")
            print(f"{i}. {movie}")


def count_watched_unwatched(movie_list):
    # loop through the list
    # count Watched vs Unwatched
    # return both counts
    pass


def find_movie(movie_list):
    # ask for a movie title
    # search the list
    # search should be case-insensitive
    # print the result or "Movie not found."
    pass


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
                pass
            case 4: 
                pass
            case 5:
                break

main()




def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        "full_name": "Mandeep kaur",
        "student_id": 10313759,
        "pizza_toppings": ["ONIONS", "CHEESE", "PEPPERS"],
            "movies": [
                {"tittle": "idiot3", "punjab": "comedy"},
                {"tittle": "back to the future", "angry man": "sci-fi"},
            ],
       }

    # TODO: Step 3 - Add another movie to the data structure
    new_movie = {"tittle": "anchorman", "genre": "horror"}
    about_me["movies"].append(new_movie)
    
    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me["mandeep kaur"]
    first_name = full_name.split()[0]
    student_id = about_me["10313759"]
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    add_pizza_toppings : ['cheese','onion']
                      
     
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    pizza_topping_1:['black olives','garlic','onion']
    pizza_toppiing_2: ['cheese','mushrooms','pepperoni']
    pizza_topping_3: ['bacon,onion','tomoto']

    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    movie_genres 
    def print_movie_genres(movie_data):
    genres = [movie['genre'] for movie in movie_data]
    print(f"I like to watch {', '.join(genres[:-1]) + ', and ' if len(genres) > 1 else ''}{genres[-1]} movies.")

def main():
    movies = [
        {'genre': 'Action'},
        {'genre': 'Comedy'},
        {'genre': 'Drama'},
        {'genre': 'Science Fiction'},
    ]
    print_movie_genres(movies)

if __name__ == "__main__":
    main()


    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    def print_favorite_movies(movie_list):
    titles = [movie.title() for movie in movie_list]
    print(f"Some of my favourite movies are {', '.join(titles[:-1]) + ', and ' if len(titles) > 1 else ''}{titles[-1]}!")

def main():
    favorite_movies = [
        "dune",
        "the hangover",
        "the lord of the rings"
    ]
    print_favorite_movies(favorite_movies)

if __name__ == "__main__":
    main()

    return
    
if __name__ == '__main__':
    main()
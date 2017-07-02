import classes
import functions

# Initialize Movie instances

''' Batman Begins movie: movie title,
storyline, poster image url and movie trailer url'''
batman_begins = classes.Movie(
    'Batman Begins',
    'A rich dude in his bat suite',
    'https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg',
    'https://www.youtube.com/watch?v=qHhHIbNuok8')

'''The Lord of the Rings movie: movie title,
storyline, poster image url and movie trailer url'''
the_lord_of_the_rings = classes.Movie(
    'The Lord of the Rings',
    'An unforgiving war between the Good and the Bad',
    'https://upload.wikimedia.org/wikipedia/en/8/87/Ringstrilogyposter.jpg',
    'https://www.youtube.com/watch?v=r5X-hFf6Bwo')

'''A Good Year movie: movie title,
storyline, poster image url and movie trailer url'''
a_good_year = classes.Movie(
    'A Good Year',
    'A rich banker found his true love',
    'https://upload.wikimedia.org/wikipedia/en/4/47/A_Good_Year.jpg',
    'https://www.youtube.com/watch?v=-vxmYKvN8fo')

'''Interstellar movie: movie title,
storyline, poster image url and movie trailer url'''
interstellar = classes.Movie(
    'Interstellar',
    'An interstellar mission for the future of humanity',
    'https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg',
    'https://www.youtube.com/watch?v=zSWdZVtXT7E')

'''High School Musical 3 movie: movie title,
storyline, poster image url and movie trailer url'''
high_school_musical_3 = classes.Movie(
    'High School Musical 3',
    'A bunch of high school kids in their senior year',
    'https://upload.wikimedia.org/wikipedia/en/a/af/HSM_3_Poster.JPG',
    'https://www.youtube.com/watch?v=bEQXcbqvbT0')

'''Dark Water movie: movie title, storyline,
poster image url and movie trailer url'''
dark_water = classes.Movie(
    'Dark Water',
    'A single mom and the ghost in her apartment',
    'https://upload.wikimedia.org/wikipedia/en/4/41/Darkwaterposter.jpg',
    'https://www.youtube.com/watch?v=JcpJVEp047Q')

# Create a list of Movie instances
list_of_movies = [batman_begins,
                  the_lord_of_the_rings,
                  a_good_year,
                  interstellar,
                  high_school_musical_3,
                  dark_water]

# Create the movie page
functions.open_movies_page(list_of_movies)

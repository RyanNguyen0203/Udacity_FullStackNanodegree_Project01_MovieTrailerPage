import webbrowser


class Movie(object):
    """ A class for movie-related information and methods """

    def __init__(self, title, storyline, poster_url, trailer_url):
        ''' Initialize Movie instance with instance variables:
        title, storyline, poster_url, trailer_url'''
        self.title = title
        self.storyline = storyline
        self.poster_url = poster_url
        self.trailer_url = trailer_url

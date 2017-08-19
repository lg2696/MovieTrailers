#Import the browser and the fresh_tomatoes module.
import webbrowser
import fresh_tomatoes

class Movie():
    def __init__(self, movie_title, movie_storyline,poster_image, trailer_youtube):
        #def __init__ () is a constructor and is reserved in Python which creates space in memory always called self any possible instance variables, and the 4 pieces of info become arguments to the __init__ function
        #__init__ gets called and lists all the arguments to pass to entertainment_center.py.
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #a new vsriable called show_trailer introduced that acts like a container for the instances above.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

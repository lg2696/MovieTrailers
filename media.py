import webbrowser
import fresh_tomatoes

class Movie():
    def __init__(self, movie_title, movie_storyline,poster_image, trailer_youtube):
        #def __init__ () is a constructor that creates space in memory always called self and possibly instance variable, and the 4 pieces of info become arguments to the __init__ function
        #__init__ gets called and lists all the arguments to pass to entertainment_center.
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

#added def url to attempt to rid error from line 165 on fresh_tomatoes

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

#imported for show_trailer 
import webbrowser

#define a the class movie
class Movie():
    #supply documentation
    """Showcasing Kate's favorite movies - or at least the movies that
       stuck with her.
       
       Click on the image to view a trailer of the movie you may
       be interested in."""

    #a class variable for ratings
    VALID_RATINGS = ["G","PG","PG-13","R"]

    #the init method to initially build an instance                    
    def __init__(self, movie_title, movie_storyline, poster_image, url,
                 comment):
 	self.title = movie_title
 	self.storyline = movie_storyline
 	self.kates_comment = comment 
 	self.poster_image_url = poster_image
 	self.trailer_youtube_url = url
    
    #a method to open a browser and show the instance's trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        

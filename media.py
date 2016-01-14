import webbrowser #imported for show_trailer 

class Movie():
    """Showcasing Kate's favorite movies - or at least the movies that
       stuck with her.
       
       Click on the image to view a trailer of the movie you may
       be interested in."""
    
    VALID_RATINGS = ["G","PG","PG-13","R"]
                     
    def __init__(self, movie_title, movie_storyline, poster_image, url,
                 comment):
 	self.title = movie_title
 	self.storyline = movie_storyline
 	self.kates_comment = comment 
 	self.poster_image_url = poster_image
 	self.trailer_youtube_url = url


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        

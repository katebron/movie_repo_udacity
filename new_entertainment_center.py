import fresh_tomatoes
import media

tarnation = media.Movie("Tarnation", "Documentery about a person's experience"
                        " growing up with a mentally unstable mother in Texas",
                        "https://upload.wikimedia.org/wikipedia/en/9/9b/TarnationPOSTER11.jpg",
                        "https://www.youtube.com/watch?v=mLDQL23nutw",
                        "The music is the best part of this.")

short_term_12 = media.Movie("Short Term 12", "A look at the lives of foster kids "
                            " in a state home and the staff who take care of them"
                            ,"http://ia.media-imdb.com/images/M/MV5BMTEwNjE2OTM4NDZeQTJeQWpwZ15BbWU3MDE2MTE4OTk@._V1_SX214_AL_.jpg",
                            "https://www.youtube.com/watch?v=ey8Z7aqXcW0",
                            "Fantastic acting; not overly dramatic but heart-breaking")

tiny_furniture = media.Movie("Tiny furniture", "A semi-fictional look at the life of Lena Dunham, pre-girls. By Lena Dunham",
                              "https://upload.wikimedia.org/wikipedia/en/e/e4/Tiny_furniture_poster.jpg",
                              "https://www.youtube.com/watch?v=PF_jWPJwKIE",
                              "A prequel to girls")

fargo = media.Movie("Fargo","Mad-cap yet violent Coen brothers thriller set in Minnesota",
                    "http://filmmakeriq.com/wp-content/uploads/2013/05/Fargo-Poster.jpg",
                    "https://www.youtube.com/watch?v=EB4PmbfG4bw",
                    "Still haven't seen the tv show")

logans_run = media.Movie("Logan's Run", "A future where people who reach the age of 30 transcend to another place",
                         "http://cstpdx.com/sites/clinton/files/images/logansrunmovieposter.jpg",
                         "https://www.youtube.com/watch?v=USADM5Gk9Gs",
                         "A favorite from childhood. Can't beat the poster")

the_lady_eve = media.Movie("The Lady Eve", "Screwball comedy in which a con-woman falls for her mark",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/f/f0/1941.lady.eve.jpg/220px-1941.lady.eve.jpg",
                           "https://www.youtube.com/watch?v=ZeVAJre7PWU",
                           "I didn't know classic movies could make me laugh so much "
                           " - very funny and smart")

boyhood = media.Movie("Boyhood","A look at the same boy and family, filled over 12 years",
                      "http://ecx.images-amazon.com/images/I/A1Dos9L1WHL._SL1500_.jpg",
                      "https://www.youtube.com/watch?v=Ys-mbHXyWX4",
                      "The closest thing to my childhood on film, thanks to "
                      " central Texas location, "
                      " including my old high school")
 
#tarnation.show_trailer()
movies = [tarnation, short_term_12, tiny_furniture, fargo, logans_run, the_lady_eve, boyhood]

fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)

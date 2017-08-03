import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

the_phantom_of_the_opera = media.Movie("The Phantom of the Opera",
                                       """A young soprano becomes the obsession
                                       of a disfigured musical genius who lives
                                       beneath the Paris Opera House.""",
                                       "https://upload.wikimedia.org/wikipedia/en/d/d6/Poto2.jpg",
                                       "https://www.youtube.com/watch?v=N91AL8sAh9o")

moulin_rouge = media.Movie("Moulin Rouge!",
                           """A poet falls for a beautiful courtesan
                           whom a jealous duke covets.""",
                           "https://upload.wikimedia.org/wikipedia/en/9/9f/Moulin_rouge_poster.jpg",
                           "https://www.youtube.com/watch?v=dtEgAx80NC4")

movies = [toy_story, avatar, the_phantom_of_the_opera, moulin_rouge]
fresh_tomatoes.open_movies_page(movies)

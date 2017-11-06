import movie
import fresh_tomatoes

#Toy Story
toy_story4 = movie.Movie("Toy Storyi 4",
                        "A story of a boy and his toys",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=Bj4gS1JQzjk")

#Avatar
avatar = movie.Movie("Avatar",
                    "A Marine on an aliean planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#Casino Royale
casino_royale = movie.Movie("Casino Royale",
                            "Jame's bond action movie",
                            "https://upload.wikimedia.org/wikipedia/en/1/15/Casino_Royale_2_-_UK_cinema_poster.jpg",
                            "https://www.youtube.com/watch?v=36mnx8dBbGE")

#Ratatouille
ratatouille = movie.Movie("Ratatouille",
                    "He's dying to become a chef",
                    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                    "https://www.youtube.com/watch?v=c3sBBRxDAqk")
#midnight in paris
midnight_in_paris = movie.Movie("Midnight in Paris",
                                "Written and directed by Woody Allen",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")


#the Hunger games
the_hunger_games = movie.Movie("The Hunger Games",
                                "The world will be watching",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY",
                                "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [toy_story4, avatar, casino_royale, ratatouille, midnight_in_paris, the_hunger_games]
#fresh_tomatoes.open_movies_page(movies)
print(

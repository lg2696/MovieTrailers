#Import code content of these modules that should all be in the same folder
import fresh_tomatoes
import media
#The code below lists and defines multiple instances found under self in media
dead_poets_society = media.Movie("Dead Poets Society",
                        "English teacher John Keating inspires his students to look at poetry with a different perspective of authentic knowledge and feelings.",
                        "https://upload.wikimedia.org/wikipedia/en/4/49/Dead_poets_society.jpg",
                        "https://www.youtube.com/watch?v=V1j5ViWIyII")
        
#print (dead_poets_society.storyline)

what_dreams_may_come = media.Movie("What Dreams May Come",
                        "After he dies in a car crash, a man searches heaven and hell for his beloved wife.",
                        "https://upload.wikimedia.org/wikipedia/en/9/91/Whatdreamsposter.jpeg",
                        "https://www.youtube.com/watch?v=POhHxK-pOTY")
#print(what_dreams_may_come.storyline)

back_to_the_future = media.Movie("Back to the Future",
                        "Marty McFly, a 17-year-old high school student, is accidentally sent 30 years into the past in a time-traveling DeLorean invented by his close friend, the maverick scientist Doc Brown.",
                        "https://i.ytimg.com/vi/UpEbGV-mjq0/movieposter.jpg",
                        "https://www.youtube.com/watch?v=UpEbGV-mjq0")
#print (back_to_the_future.storyline)

the_sound_of_music = media.Movie("The Sound of Music",
                        "A woman leaves an Austrian convent to become a governess to the children of a Naval officer widower.",
                        "https://upload.wikimedia.org/wikipedia/en/c/c6/Sound_of_music.jpg",
                        "https://www.youtube.com/watch?v=5bkV3x296vs")
#print(the_sound_of_music.storyline)

when_harry_met_sally = media.Movie("When Harry met Sally",
                        "Harry and Sally have known each other for years, and are very good friends, but they fear sex would ruin the friendship.",
                        "https://upload.wikimedia.org/wikipedia/en/1/1c/WhenHarryMetSallyPoster.jpg",
                        "https://www.youtube.com/watch?v=6I9bILPjOUY")
#print (when_harry_met_sally.storyline)

chocolat = media.Movie("Chocolat",
                        "A woman and her daughter open a chocolate shop in a small French village that shakes up the rigid morality of the community.",
                        "https://upload.wikimedia.org/wikipedia/en/0/08/Chocolat_sheet.jpg",
                        "https://www.youtube.com/watch?v=0t9xI6EVkuA")

#The next line of oode created a movie array.
movies =[dead_poets_society,what_dreams_may_come,back_to_the_future,the_sound_of_music,when_harry_met_sally,chocolat]
fresh_tomatoes.open_movies_page(moviesprint.media.Movie.__doc__)

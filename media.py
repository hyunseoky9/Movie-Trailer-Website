import fresh_tomatoes

#This module specifies class Movie that instantiates objects with certain movie's information including 
#title, poster image, and youtube trailer.

class Movie():
    """ 
        This class makes instances of movie that has title, poster image, and trailer attributes.

        Attributes:
            title: string of the movie title
            image: string of poster image url
            trailer: string of youtube trailer url
    """
    def __init__(self,title,image,trailer):
    """ 
        Inits Movie with title, image, and trailer information
    """    
    self.title = title
    self.poster_image_url = image
    self.trailer_youtube_url = trailer

    def show_trailer(self):
    """
        Opens a webbrowser with youtube trailer that's specified in the trailer_youtube_url
    """
    webbrowser.open(self.trailer_url)
#three objects created by Movie class.
Avengers = Movie('The Avengers',
    'https://en.wikipedia.org/wiki/The_Avengers_(2012_film)#/media/File:TheAvengers2012Poster.jpg',
    'https://www.youtube.com/watch?v=eOrNdBpGMv8')
Iron_man = Movie('Iron Man',
    'https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=imgres&cd=&cad=rja&uact=8&ved=0ahUKEwism92t_YnWAhVB4GMKHbYdCZkQjRwIBw&url=http%3A%2F%2Fgoogle.com%2Fsearch%3Ftbm%3Disch%26q%3DIron%2520Man&psig=AFQjCNFhfzh5Tz1fe2eDe7aW0SmX683XGA&ust=1504561194332529',
    'https://www.youtube.com/watch?v=8hYlB38asDY')
Beautiful_mind = Movie('Beautiful Mind',
    'https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=imgres&cd=&cad=rja&uact=8&ved=0ahUKEwjT9MXE_YnWAhVW-GMKHXUnAeAQjRwIBw&url=http%3A%2F%2Fgoogle.com%2Fsearch%3Ftbm%3Disch%26q%3DA%2520Beautiful%2520Mind&psig=AFQjCNHItC7ryxp-f1SVs3fs8pUHbeCF2w&ust=1504561242330094',
    'https://www.youtube.com/watch?v=YWwAOutgWBQ')

movies = [Avengers, Iron_man, Beautiful_mind]

fresh_tomatoes.open_movies_page(movies) #creates an html page based on the movie objects created and opens it.
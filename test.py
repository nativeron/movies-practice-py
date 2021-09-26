from movie import Movie
from catalogue import Catalogue


option = None

while option !=4:
    try:
        print('options : ')
        print('1 . Add a movie')
        print('2 . See movies')
        print('3 . Remove catalogue')
        print('4 . Exit')
        option= int(input('please write your option (number): '))

        if option == 1:
            name_movie = input('What is the name of the movie?')
            movie = Movie(name_movie)
            Catalogue.add_movie(movie)
        elif option ==2:
            Catalogue.list_movies()
        elif option ==3:
            Catalogue.delete_movie()

    except Exception as ex:
        print(f'an error ocurred{ex}')
        option = None
else: 
    print('okey')
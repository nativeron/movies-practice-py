import os

class Catalogue:

    file_route = 'movies.txt'

    @classmethod
    def add_movie(cls, movie):
        with open (cls.file_route,'a', encoding='utf8') as file:
            file.write(f'{movie.name}\n')

    @classmethod
    def list_movies(cls):
        with open(cls.file_route, 'r' , encoding='utf8') as file:
            print('Catalogue')
            print(file.read())
    
    @classmethod
    def delete_movie(cls):
        os.remove(cls.file_route)
        print(f'the file {cls.file_route} was removed')
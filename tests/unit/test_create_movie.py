# TODO: Feature 2
# Maggie
# test krevat's code
# call create movie from krevat's code, make sure it returns proper movie
# make sure when we call list all movies it is there
# assert statements go here
# make sure movie is created
# no false positives (validate that something you didn't add isn't in there.)
# method side
# check ratings are an integer
# check that input isn't empty
from src.repositories.movie_repository import get_movie_repository, _movie_repo
#from src.repositories.movie_repository import _movie_repo

movie_repository = get_movie_repository()

def test_movie_created():
    movie_repository.create_movie('Spiderman', 'Sam Raimi', 4)
    movie = movie_repository.get_movie_by_title('Spiderman')
    assert movie.title == 'Spiderman'
    assert movie.director == 'Sam Raimi'
    assert movie.rating == 4

# make sure 2 or more movies could be added to the list of movies
def test_multiple_movies_added():
    movie_repository.clear_db()
    movie_repository.create_movie('title', 'director', None)
    movie_repository.create_movie('Spiderman', 'Sam Raimi', None)
    assert len(_movie_repo.get_all_movies()) == 2


# cannot do validation tests because I only worked on this feature
# TODO: Feature 2
from src.repositories.movie_repository import get_movie_repository
import pytest
from flask.testing import FlaskClient

movie_repository = get_movie_repository()

# testing page elements exist
def test_create_page(test_app):
    response = test_app.get("/movies/new")

    # To Do test submit button
    assert b'<button type="submit" class="btn btn-primary">Submit</button>' in response.data

def test_redirect(test_app):
    response = test_app.post("/movies", data={ 
        "title": "Spiderman",
        "director": "Sam Raimi",
        "rating": "4"
    }, follow_redirects = True)
    assert len(response.history) == 1
    assert response.request.path == '/movies'

# testing inputs come through and exist on page
def test_valid(test_app):
    movie_repository.clear_db()
    response = test_app.post("/movies", data={ 
        "title": "Spiderman",
        "director": "Sam Raimi",
        "rating": "4"
    })
    assert response.status_code == 302
    movie_repository.get_all_movies()
    test_movie = movie_repository.get_movie_by_title("Spiderman")
    assert test_movie.title == "Spiderman"

def test_invalid(test_app):
    response = test_app.post("/movies", data={
        "director": "Sam Raimi",
        "rating": "4"
    })
    assert response.status_code == 400

    response = test_app.post("/movies", data={
        "title": "Spiderman",
        "rating": "4"
    })
    assert response.status_code == 400

    response = test_app.post("/movies", data={
        "title": "Spiderman",
        "director": "Sam Raimi"
    })
    assert response.status_code == 400

def test_create_movies_page_form(test_app):
    response = test_app.get('/movies/new')
    assert response.status_code == 200


def test_empty_movie_title(test_app):
    movie_repository.clear_db()
    response = test_app.post("/movies", data={
        "title": "",
        "director": "Sam Raimi",
        "rating": "4",
    })
    assert response.status_code == 400

def test_empty_movie_director(test_app):
    movie_repository.clear_db()
    response = test_app.post("/movies", data={
        "title": "Spiderman",
        "director": "",
        "rating": "4",
    })
    assert response.status_code == 400

def test_empty_movie_rating(test_app):
    movie_repository.clear_db()
    response = test_app.post("/movies", data={
        "title" : "Spiderman",
        "director": "Sam Raimi",
        "rating": "",
    })
    assert response.status_code == 400

    #assert _movie_repo is None



# Would have needed Group Members for this:
# normally test that creating the movie means that it was listed,
# also I would test that the actually happens
# but was doing one feature solo so Professor said only do one feature
# I chose create movie feature


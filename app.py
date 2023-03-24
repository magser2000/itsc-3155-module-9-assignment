from flask import Flask, redirect, render_template, request, abort

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
# makes instance movie_repository.create_movie()
movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


#def create_movie(self, title: str, director: str, rating: int) -> Movie:
#"""Create a new movie and return it"""
# Create the movie instance
# new_id = randint(0, 100_000)  # Sufficiently unique ID for our purposes
# movie = Movie(new_id, title, director, rating)
# Save the instance in our in-memory database
# self._db[new_id] = movie
# Return the movie instance
# return movie

@app.post('/movies')
def create_movie():

    # create branch
    # pull request

    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    # Getting the director name, movie title, movie_id,  

    # name and id in html should = the three orange values below
    title = request.form.get('title')
    director = request.form.get('director')
    rating = request.form.get('rating', type = int)

    if not title or not director or not rating or rating < 1 or rating > 5:
        # Bad request 400 error if there is nothing or rating values aren't valid
        return abort(400)
    
    movie_repository.create_movie(title, director, rating)

    print(movie_repository.get_all_movies())
    # check it returns 302 in unit tests for redirect if it has requirements
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    return render_template('get_single_movie.html')


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    return render_template('edit_movies_form.html')


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass

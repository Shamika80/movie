from movie_data import movies

def resolve_movie(obj, info, id):
    for movie in movies:
        if movie["id"] == id:
            return movie
    return None

def resolve_movies(obj, info, genre=None, search=None):
    filtered_movies = movies
    if genre:
        filtered_movies = [movie for movie in filtered_movies if movie["genre"] == genre]
    if search:
        filtered_movies = [movie for movie in filtered_movies if search.lower() in movie["title"].lower()]
    return filtered_movies

def resolve_add_movie(obj, info, title, genre, director, releaseDate=None, rating=None):
    new_movie = {
        "id": str(len(movies) + 1), 
        "title": title, 
        "genre": genre, 
        "director": director, 
        "releaseDate": releaseDate, 
        "rating": rating
    }
    movies.append(new_movie)
    return new_movie

def resolve_update_movie(obj, info, id, title=None, genre=None, director=None, releaseDate=None, rating=None):
    for movie in movies:
        if movie['id'] == id:
            if title: movie['title'] = title
            if genre: movie['genre'] = genre
            if director: movie['director'] = director
            if releaseDate: movie['releaseDate'] = releaseDate
            if rating: movie['rating'] = rating
            return movie
    return None

def resolve_delete_movie(obj, info, id):
    for i, movie in enumerate(movies):
        if movie['id'] == id:
            del movies[i]
            return movie 
    return None
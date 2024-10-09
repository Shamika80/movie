# Movie Database GraphQL API

This project implements a GraphQL API for managing a movie database. It allows users to perform CRUD operations on movies and genres, as well as query data based on different criteria.

## Features

* **Movie Management:**
    * Add new movies with details like title, description, genre, director, and release year.
    * Update existing movie information.
    * Delete movies from the database.
* **Genre Management:**
    * Add new genres.
    * Update existing genre names.
    * Delete genres.
* **Querying:**
    * Retrieve movies by ID.
    * Filter movies by genre.
    * Search for movies by title.
    * Get movie details, including associated genre(s).

## Technologies Used

* **Python:** Programming language for the backend.
* **GraphQL:** Query language for the API.
* **Ariadne:** Python library for building GraphQL APIs.
* **SQLAlchemy:**  ORM for database interaction.
* **PostgreSQL:** (or your chosen database) Database to store movie data.
* **Flask:** (optional)  Python web framework if you are using it.

## Installation

1. Clone the repository: `git clone <repository_url>`
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:   
 `source venv/bin/activate`
4. Install the dependencies: `pip install -r requirements.txt`
5.   
 Configure the database connection in `movie_data.py`.
6. Run the application: `python app.py`

## Usage

The API can be accessed at `/graphql`. You can use a GraphQL client like GraphiQL or Altair to interact with the API.



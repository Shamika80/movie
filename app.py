from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify

from resolvers import resolve_movie, resolve_movies, resolve_add_movie, resolve_update_movie, resolve_delete_movie 

query = ObjectType("Query")
query.set_field("movie", resolve_movie)
query.set_field("movies", resolve_movies)

mutation = ObjectType("Mutation")
mutation.set_field("addMovie", resolve_add_movie)
mutation.set_field("updateMovie", resolve_update_movie)
mutation.set_field("deleteMovie", resolve_delete_movie)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)

@"app".route("/graphql", methods=["GET"]) 

def graphql_playground():
 return PLAYGROUND_HTML, 200 @"app".route("/graphql", methods=["POST"]) 
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug="app".debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code 
    if __name__ == "__main__":
     app.run(debug=True) 

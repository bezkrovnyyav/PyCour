# WSGI pt. 1
- Write a simple wsgi compatible application that prints the username, remote address, user agent, path and your surname(see below).

- Add a simple middleware that adds the key SURNAME with the value of your surname to the environ.

- Add another middleware that changes the formatting of all the symbols to be lowercase (except of the first ones in sentence and your surname).

- Use two middlewares simultaneously.
 
# WSGI pt.2

- Implement the framework from the lecture.

- Build the application that implements the CRUD from lecture, add getting the data from user (use parametrized routes, query params, data sent by post, put, patch requests to get the data from user), process it and return the result (all using .json format). Save the data to database.

- Implement the middleware that logs every access to /secured endpoint.

- Use gunicorn as server.

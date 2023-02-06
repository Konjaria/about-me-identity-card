# Import the Flask class from the flask module
from flask import Flask
# Import the render_template function from the flask module
from flask import render_template

# Create an instance of the Flask class and store it in the app variable
# The first argument passed to the Flask class is the name of the application's module or package
app = Flask(__name__)

# Define a route using the @app.route decorator
# The homepage route will be the root URL '/'
@app.route('/')
def homepage():
    # Return the contents of the 'index.html' template
    return render_template('index.html')

# The following block of code is executed only if the script is run as the main module (not imported as a module)
# This is a common pattern used to determine if the code is being run as a standalone application
if __name__ == "__main__":
    # Call the run() method of the Flask class to start the application's development web server
    app.run()

import os  # Import the os module for interacting with the operating system (not used in this script, but often useful)
from flask import Flask, render_template, request  # Import Flask and functions to render HTML templates and handle requests
from waitress import serve  # Import the 'serve' function from waitress to run the app in production
from random import randint  # Import randint to generate random integers

app = Flask(__name__)  # Create a new Flask web application instance

@app.route('/')  # Define the route for the homepage ('/')
@app.route('/index')  # Also define the route for '/index'
def index():
    # Choose a random author
    num = randint(0, len(quotes["names"]) - 1)  # Pick a random index for the author list
    name = quotes["names"][num]  # Get the author's name using the random index
    # Choose a random quote for that author
    if isinstance(quotes[name], list):  # Check if the author has multiple quotes (stored as a list)
        quote = quotes[name][randint(0, len(quotes[name]) - 1)]  # Pick a random quote from the list
    else:
        quote = quotes[name]  # If only one quote, just use it
    # Pass quote and author to template
    return render_template('index.html', quote=quote, author=name)  # Render the HTML template and pass the quote and author

# Dictionary to store quotes and authors
quotes = {
    "names": ["Descartes", "Aristotle", "Carl Jung", "Plato", "Bruce Lee"],  # List of author names

    "Descartes": 
    [
        "I think therefore I am",
        "The reading of all good books is like conversation with the finest men of past centuries."
    ],
    "Aristotle": 
    [
        "The high-minded man must care more for the truth than for what people think.", 
        "You will never do anything in this world without courage. It is the greatest quality of the mind next to honor.", 
        "Knowing yourself is the beginning of all wisdom.", 
        "The educated differ from the uneducated as much as the living differ from the dead."
    ],
    "Carl Jung": 
    [
        "Your visions will become clear only when you can look into your own heart. Who looks outside, dreams; who looks inside, awakes.",
        "Until you make the unconscious conscious, it will direct your life and you will call it fate.",
        "People will do anything, no matter how absurd, to avoid facing their own souls.",
        "Where wisdom reigns, there is no conflict between thinking and feeling."
    ],
    "Plato": "One of the penalties for refusing to participate in politics is that you end up being governed by your inferiors.",  # Plato has only one quote (string)

    "Bruce Lee": "I fear not the man who has practiced 10,000 kicks once, but I fear the man who has practiced one kick 10,000 times."
}

if __name__ == "__main__":  # This block runs only if this script is executed directly (not imported)
    serve(app, host="0.0.0.0", port=1000)  # Start the web server on all network interfaces at port 3000 using waitress
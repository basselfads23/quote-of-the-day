import os
from flask import Flask, render_template, request
from waitress import serve
from random import randint

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    # Choose a random author
    num = randint(0, len(quotes["names"]) - 1)
    name = quotes["names"][num]
    # Choose a random quote for that author
    if isinstance(quotes[name], list):
        quote = quotes[name][randint(0, len(quotes[name]) - 1)]
    else:
        quote = quotes[name]
    # Pass quote and author to template
    return render_template('index.html', quote=quote, author=name)


quotes = {
    
    "names": ["Descartes", "Aristotle", "Carl Jung", "Plato"],

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
    "Plato": "One of the penalties for refusing to participate in politics is that you end up being governed by your inferiors."

}

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=3000)
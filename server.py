import logging
import os

from flask import Flask
from flask import request

import minimax


app = Flask(__name__)


@app.route("/", methods=['GET'])
def handle_info():
    print("INFO")

    return {
        "apiversion": "1",
        "author": "",  # TODO: Your Battlesnake Username
        "color": "#888888",  # TODO: Personalize
        "head": "beluga",  # TODO: Personalize
        "tail": "default",  # TODO: Personalize

    }


@app.route("/start", methods=['POST'])
def handle_start():
    """
    This function is called everytime your snake is entered into a game.
    request.json contains information about the game that's about to be played.
    """
    data = request.get_json()

    print(f"{data['game']['id']} START")
    return "ok"


@app.route("/move", methods=['POST'])
def handle_move():
    """
    Valid moves are "up", "down", "left", or "right".
    """
    data = request.get_json()
    sim = minimax.Simulation(data["board"])
    maxv, move = sim.findMax(data)

    if move == [0, 1]:
        move = "right"
    elif move == [0, -1]:
        move = "left"
    elif move == [1, 0]:
        move = "up"
    else:
        move = "down"
    return {"move": move}


@app.route("/end", methods=['POST'])
def end():
    """
    This function is called when a game your snake was in ends.
    It's purely for informational purposes, you don't have to make any 
    decisions here.
    """
    data = request.get_json()

    print(f"{data['game']['id']} END")
    return "ok"


if __name__ == "__main__":
    logging.getLogger("werkzeug").setLevel(logging.ERROR)

    print("Starting Battlesnake Server...")
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port, debug=True)

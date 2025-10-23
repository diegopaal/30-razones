# app.py
import os
import random
from flask import Flask, render_template, request
from memories import MEMORIES

app = Flask(__name__)

@app.route("/")
def index():
    # Si ?shuffle=1, mezcla el orden (no lineal)
    memories = MEMORIES.copy()
    if request.args.get("shuffle") == "1":
        random.seed()  # usa entropía del sistema
        random.shuffle(memories)

    return render_template("index.html", memories=memories)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

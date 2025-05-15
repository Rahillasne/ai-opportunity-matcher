from flask import Flask, render_template, request
import json
from match_engine import rank_jobs

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        with open("jobs_data.json") as f:
            jobs = json.load(f)
        ranked = rank_jobs(user_input, jobs)
        return render_template("index.html", jobs=ranked)
    return render_template("index.html", jobs=[])

if __name__ == "__main__":
    app.run(debug=True)

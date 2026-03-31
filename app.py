from flask import Flask, render_template,jsonify

app = Flask(__name__)

SKILL = [
    {
        "id":1,
        "skill":"Python",
        "level":"advance",
        "expirence":"apple"
    },
    {
        "id":2,
        "skill":"java",
        "level":"intermediate",
        "expirence": "google"
    },
    {
        "id":3,
        "skill":"c++",
        "level":"basic"
    }
]

@app.route("/")
def home():
    return render_template("index.html",skill = SKILL)

@app.route("/api/skill")
def list_skill():
    return jsonify(SKILL)

if __name__ == "__main__":
    app.run(debug=True)
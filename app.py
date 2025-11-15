from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = "mysecret"

users = {}
notes = {}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        action = request.form["action"]

        if action == "signup":
            if username in users:
                return render_template("home.html", message="User already exists!", color="red")
            users[username] = password
            return render_template("home.html", message="Signup successful! Now login.", color="green")
        else:
            if username in users and users[username] == password:
                session["username"] = username
                return redirect(url_for("note"))
            return render_template("home.html", message="Invalid credentials!", color="red")

    return render_template("home.html")

@app.route("/note", methods=["GET", "POST"])
def note():
    if "username" not in session:
        return redirect(url_for("home"))

    if request.method == "POST":
        text = request.form["text"]
        name = request.form["name"]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        notes[name] = {"text": text, "time": timestamp}
        return render_template("saved.html", name=name, time=timestamp)

    return render_template("note.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

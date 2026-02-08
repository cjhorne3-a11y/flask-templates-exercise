from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title="Chris's Homepage")

@app.route("/about")
def about():
    return render_template("about.html", title="About Chris")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact Chris")

if __name__ == "__main__":
    app.run(debug=True)

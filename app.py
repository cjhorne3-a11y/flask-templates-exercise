from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title="Chris's Homepage")

@app.route("/about")
def about():
    return render_template("about.html", title="About Chris")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        return render_template(
            "contact.html",
            title="Contact Chris",
            name=name,
            email=email,
            submitted=True
        )

    return render_template(
        "contact.html",
        title="Contact Chris",
        submitted=False
    )

if __name__ == "__main__":
    app.run(debug=True)

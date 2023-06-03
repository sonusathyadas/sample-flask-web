from flask import Flask, render_template, jsonify
from data import books

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("pages/home.html", title="Home", books= books)

@app.route("/about")
def about():
    return render_template("pages/about.html", title="About")

@app.errorhandler(404) 
def invalid_route(e): 
    return render_template("pages/notfound.html")

# Add Api route
@app.route("/api/books")
def get_books():
    return jsonify(books)

if __name__ == "__main__":
    app.run( debug=True)

# either run using 'python app.py' command 
# OR run using 'flask --app app run'



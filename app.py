from flask import (Flask, jsonify, render_template, request, flash, session, redirect)
from models import db, connect_db
import requests
from jinja2 import StrictUndefined 

app = Flask(__name__)
app.secret_key = 'SECRET!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///movie-ratings'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.jinja_env.undefined = StrictUndefined
connect_db(app)
db.create_all()


API_KEY = os.environ['BIGFLIX_KEY']

@app.route('/')
def homepage():
    """Show the homepage."""

    return render_template("hi")

# @app.route('/movie_result', methods = ['GET'])
# def get_movie(): 
#     """Show a movie result"""


#     url = "https://devru-bigflix-movies-download-v1.p.rapidapi.com/search.php"
#     querystring = {"term":"movie"}
#     headers = {
#     'x-rapidapi-key': "b1a3a0c183msh560e608cd1b67b3p1dc0b5jsn39714f5c5791",
#     'x-rapidapi-host': "devru-bigflix-movies-download-v1.p.rapidapi.com"
#     }
#     response = requests.request("GET", url, headers=headers, params=querystring)

#     movie_data = response.json()
#     print(movie_data)
#     # print(response.text)

#     return render_template('movie_result.html', data=movie_data )

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
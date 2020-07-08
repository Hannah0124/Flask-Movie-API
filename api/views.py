from flask import Blueprint, jsonify 

main = Blueprint('main', __name__)

# endpoint
@main.route('/add_movie', methods=['POST'])

def add_movie():

  return 'Done', 201  # success

# endpoint
@main.route('/movies')

def movies():
  
  movies = []

  return jsonify({'movies' : movies})



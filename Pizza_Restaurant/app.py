from flask import Flask, jsonify, request
from models import db, Restaurant, Pizza, Price, Ingredient, RestaurantPizza
from sqlalchemy.exc import IntegrityError
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
from flasgger import Swagger

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
swagger = Swagger(app)

db.init_app(app)

with app.app_context():
    db.create_all()
    
migrate = Migrate(app, db)
    
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    """
    Get all restaurants
    ---
    responses:
      200:
        description: List of all restaurants
    """
    restaurants = Restaurant.query.all()
    return jsonify([restaurant.to_dict() for restaurant in restaurants])

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    """
    Get a specific restaurant
    ---
    parameters:
    - name: id
      in: path
      type: integer
      required: true
    responses:
      200:
        description: Restaurant details
      404:
        description: Restaurant not found
    """
    restaurant = Restaurant.query.get(id)
    if restaurant is None:
        return jsonify({'error': 'Restaurant not found'}), 404
    return jsonify(restaurant.to_dict())

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    """
    Delete a specific restaurant
    ---
    parameters:
    - name: id
      in: path
      type: integer
      required: true
    responses:
      204:
        description: Restaurant deleted
      404:
        description: Restaurant not found
    """
    restaurant = Restaurant.query.get(id)
    if restaurant is None:
        return jsonify({'error': 'Restaurant not found'}), 404
    try:
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    except AssertionError as e:
        return jsonify({'errors': str(e)}), 400

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    """
    Get all pizzas
    ---
    responses:
      200:
        description: List of all pizzas
    """
    pizzas = Pizza.query.all()
    return jsonify([pizza.to_dict() for pizza in pizzas])

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    """
    Create a new restaurant pizza
    ---
    parameters:
    - name: body
      in: body
      required: true
      schema:
        id: restaurant_pizza
        properties:
          price:
            type: number
          pizza_id:
            type: integer
          restaurant_id:
            type: integer
    responses:
      201:
        description: Restaurant pizza created
      400:
        description: Validation error
    """
    data = request.get_json()
    try:
        restaurant_pizza = RestaurantPizza(price=data['price'], pizza_id=data['pizza_id'], restaurant_id=data['restaurant_id'])
        db.session.add(restaurant_pizza)
        db.session.commit()
        return jsonify(restaurant_pizza.to_dict()), 201
    except AssertionError as e:
        return jsonify({'errors': str(e)}), 400
    except IntegrityError:
        return jsonify({'errors': 'validation errors'}), 400

if __name__ == "__main__":
     app.run(debug=True)

from random import randint, choice
from models import db, Restaurant, Pizza, Price, Ingredient
from app import app

restaurants = [
    {"name": "Dominion Pizza", "address": "Address 1"},
    {"name": "Pizza Hut", "address": "Address 2"}
]
with app.app_context():
    Restaurant.query.delete()
    db.session.commit()
    
with app.app_context():
    print('🍕 Obtaining Restaurants')
    for restaurant in restaurants:
        existing_restaurant = Restaurant.query.filter_by(name=restaurant["name"]).first()
        if existing_restaurant is None:
            new_restaurant = Restaurant(name=restaurant["name"], address=restaurant["address"])
            db.session.add(new_restaurant)
            db.session.commit()

pizzas = [
    {"name": "Cheese", "pizza": "pizza1"},
    {"name": "Pepperoni", "pizza": "pizza2"}
]
with app.app_context():
    print('🍕 Odering Pizza')
    for pizza in pizzas:
       new_pizza = Pizza(name=pizza["name"], pizza_id=pizza["pizza"])
       db.session.add(new_pizza)
       db.session.commit()

ingredients = [
    {"ingredient": "Dough", "pizza": "pizza1"},
    {"ingredient": "Tomato Sauce", "pizza": "pizza1"},
    {"ingredient": "Cheese", "pizza": "pizza1"},
    {"ingredient": "Dough", "pizza": "pizza2"},
    {"ingredient": "Tomato Sauce", "pizza": "pizza2"},
    {"ingredient": "Cheese", "pizza": "pizza2"},
    {"ingredient": "Pepperoni", "pizza": "pizza2"}
]
with app.app_context():
    print('🍕 Placing Toppings on Pizzas')
    for ingredient in ingredients:
       new_ingredient = Ingredient(name=ingredient["ingredient"], pizza_id=ingredient["pizza"])
       db.session.add(new_ingredient)
       db.session.commit()

prices = [
    {"price": "5", "pizza": "pizza1"},
    {"price": "10", "pizza": "pizza2"}
]
with app.app_context():
    print('🍕 Obtaining Price')
    for price in prices:
       new_price = Price(value=price["price"], pizza_id=price["pizza"])
       db.session.add(new_price)
       db.session.commit()
       
print("🍕 Your Pizza is on the way!")
from random import randint, choice
from models import db, Restaurant, Pizza, Price, Ingredient
from app import app

restaurants = [
    {"name": "Dominion Pizza", "restaurant.id": "1"},
    {"name": "Pizza Hut", "restaurant.id": "2"}
]
with app.app_context():
    print('🍕 Obtaining Restaurants')
    for restaurant in restaurants:
        new_restaurant = Restaurant(name=restaurant["name"], id=restaurant["restaurant.id"])
        db.session.add(new_restaurant)
        db.session.commit()

pizzas = [
    {"name": "Cheese", "restaurant.id": "1", "pizza": "pizza1"},
    {"name": "Cheese", "restaurant.id": "2", "pizza": "pizza2"}
]
with app.app_context():
    print('🍕 Odering Pizza')
    for pizza in pizzas:
       new_pizza = Pizza(name=pizza["name"], id=pizza["restaurant.id"], pizza=pizza["pizza"])
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
    print('🍕 Placing Toppings')
    for ingredient in ingredients:
       new_ingredient = Ingredient(ingredient_name=ingredient["ingredient"], pizza=ingredient["pizza"])
       db.session.add(new_ingredient)
       db.session.commit()

prices = [
    {"price": "5", "pizza": "pizza1"},
    {"price": "10", "pizza": "pizza2"}
]
with app.app_context():
    print('🍕 Obtaining Price')
    for price in prices:
       new_price = Price(price=price["price"], pizza=price["pizza"])
       db.session.add(new_price)
       db.session.commit()
       
print("🍕 Your Pizza is on the way!")
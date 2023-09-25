from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():
    # Restaurants
    restaurant1 = Restaurant(name='Dominion Pizza')
    restaurant2 = Restaurant(name='Pizza Hut')

    # Pizzas
    pizza1 = Pizza(name='Cheese', restaurant_id=restaurant1.id)
    pizza2 = Pizza(name='Pepperoni', restaurant_id=restaurant2.id)

    # Prices
    price1 = Price(value=5, pizza=pizza1)
    price2 = Price(value=10, pizza=pizza2)

    # Ingredients For Pizzas
    ingredient1 = Ingredient(name='Dough', pizza=pizza1)
    ingredient2 = Ingredient(name='Tomato Sauce', pizza=pizza1)
    ingredient3 = Ingredient(name='Cheese', pizza=pizza1)
    ingredient4 = Ingredient(name='Dough', pizza=pizza2)
    ingredient5 = Ingredient(name='Tomato Sauce', pizza=pizza2)
    ingredient6 = Ingredient(name='Cheese', pizza=pizza2)
    ingredient7 = Ingredient(name='Pepperoni', pizza=pizza2)

    # Sessions
    db.session.add_all([restaurant1, restaurant2, pizza1, pizza2, price1, price2, ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6, ingredient7])

    # Commit sessions
    db.session.commit()

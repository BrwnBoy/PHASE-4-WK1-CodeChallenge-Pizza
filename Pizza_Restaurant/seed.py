from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():
    # Restaurants
      restaurant1 = Restaurant(id=1, name='Dominion Pizza')
      restaurant2 = Restaurant(id=2, name='Pizza Hut')

    # Pizzas
      pizza1 = Pizza(name='Cheese', restaurant_id=restaurant1.id)
      pizza2 = Pizza(name='Pepperoni', restaurant_id=restaurant2.id)

    # Prices
      pizza1.prices = [5.00]
      pizza2.prices = [10.00]

    # Ingredients For Pizzas
      pizza1.ingredients = ['Dough', 'Tomato Sauce', 'Cheese']
      pizza2.ingredients = ['Dough', 'Tomato Sauce', 'Cheese', 'Pepperoni']

    # Sessions
      db.session.add(restaurant1)
      db.session.add(restaurant2)
      db.session.add(pizza1)
      db.session.add(pizza2)

    # Commit sessions
      db.session.commit()

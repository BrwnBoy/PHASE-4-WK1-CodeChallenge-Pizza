from random import randint, choice, sample

from faker import Faker

from app.models import db, Pizza, Restaurant, RestaurantPizza
from app import app

faker = Faker()

with app.app_context():
    Pizza.query.delete()
    Restaurant.query.delete()
    RestaurantPizza.query.delete()  

    pizzas = []
    # List of pizza toppings
    # List of pizza toppings
    toppings = [
    "Pepperoni",
    "Mushrooms",
    "Onions",
    "Sausage",
    "Bacon",
    "Extra Cheese",
    "Green Peppers",
    "Black Olives",
    "Pineapple",
    "Spinach",
    "Jalapenos",
    "Artichoke Hearts",
    "Anchovies",
    "Tomatoes",
    "Ham",
    "Chicken",
    "Feta Cheese",
]
    
    # Function to generate a random pizza name
    def generate_pizza():
        num_toppings = faker.random_int(min=1, max=len(toppings))
        selected_toppings = [toppings[i] for i in range(num_toppings)]
        return f"{', '.join(selected_toppings)} Pizza"

    for i in range(10):
    # Generate a random pizza name
        pizza_name = generate_pizza()
        p = Pizza(name=pizza_name, ingredients=choice(toppings))
        pizzas.append(p)

    db.session.add_all(pizzas)

    restaurants = []
    for i in range(10):
        r = Restaurant(name=faker.company(), address=faker.address())
        restaurants.append(r)

    db.session.add_all(restaurants)

    restaurant_pizzas = []
    for i in range(20):
        rp = RestaurantPizza(
            price=randint(1, 30), pizza_id=randint(1, 10), restaurant_id=randint(1, 10)
        )
        restaurant_pizzas.append(rp)

    db.session.add_all(restaurant_pizzas)
    db.session.commit()    
       
print("🍕 Your Pizza is on the way!")
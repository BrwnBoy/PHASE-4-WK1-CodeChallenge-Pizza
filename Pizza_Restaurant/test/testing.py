import unittest
from flask import Flask
from models import db, Restaurant, Pizza, RestaurantPizza
from app import app

class PizzaRestaurantTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_restaurants(self):
        res = self.client().get('/restaurants')
        self.assertEqual(res.status_code, 200)

    def test_get_restaurant(self):
        restaurant = Restaurant(name='Test Restaurant', address='Test Address')
        db.session.add(restaurant)
        db.session.commit()
        res = self.client().get(f'/restaurants/{restaurant.id}')
        self.assertEqual(res.status_code, 200)

    def test_delete_restaurant(self):
        restaurant = Restaurant(name='Test Restaurant', address='Test Address')
        db.session.add(restaurant)
        db.session.commit()
        res = self.client().delete(f'/restaurants/{restaurant.id}')
        self.assertEqual(res.status_code, 204)

    def test_get_pizzas(self):
        res = self.client().get('/pizzas')
        self.assertEqual(res.status_code, 200)

    def test_create_restaurant_pizza(self):
        pizza = Pizza(name='Test Pizza', ingredients='Test Ingredients')
        restaurant = Restaurant(name='Test Restaurant', address='Test Address')
        db.session.add(pizza)
        db.session.add(restaurant)
        db.session.commit()
        res = self.client().post('/restaurant_pizzas', json={'price': 10, 'pizza_id': pizza.id, 'restaurant_id': restaurant.id})
        self.assertEqual(res.status_code, 201)

    def test_create_restaurant_pizza_validation_error(self):
        pizza = Pizza(name='Test Pizza', ingredients='Test Ingredients')
        restaurant = Restaurant(name='Test Restaurant', address='Test Address')
        db.session.add(pizza)
        db.session.add(restaurant)
        db.session.commit()
        res = self.client().post('/restaurant_pizzas', json={'price': 50, 'pizza_id': pizza.id, 'restaurant_id': restaurant.id})
        self.assertEqual(res.status_code, 400)

if __name__ == "__main__":
    unittest.main()
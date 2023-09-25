# PHASE-4-WK1-CodeChallenge-Pizza
**Authour**: *Brian Mwangi Maina.*

## Prequisites:

**Technologies Used**

<li>Python
<li>JSON
<li>PostMan

**Setup/Installation Requirements**

*To run the application, in your terminal*

<li>Open the terminal and clone the repository to your local machine://git@github.com:BrwnBoy/PHASE-4-WK1-CodeChallenge-Pizza.git//
<li>cd into *PHASE-4-WK1-CodeChallenge-Pizza*
<li>Finally, open up vs.code by typing in (code .) while in the repository.

### What Goes Into Making The Programs Run:

(1)**Models**: *The application uses SQLAlchemy to define three models: Restaurant, Pizza, and RestaurantPizza. The Restaurant and Pizza models represent restaurants and pizzas, respectively. The RestaurantPizza model represents the many-to-many relationship between restaurants and pizzas, and also includes the price of a specific pizza at a specific restaurant.*

(2)**Validations**: *The application includes validations on the Restaurant and RestaurantPizza models. For example, it ensures that a restaurant's name is unique and less than 50 words in length, and that the price of a pizza at a restaurant is between 1 and 30.*

(3)**Routes**: *The application defines several routes for interacting with the data:
GET /restaurants and GET /pizzas:*return a list of all restaurants or pizzas, respectively.*
GET /restaurants/:*id returns details about a specific restaurant, including the pizzas it serves.*
DELETE /restaurants/:*id deletes a specific restaurant and all associated RestaurantPizza records.*
POST /restaurant_pizzas:*creates a new RestaurantPizza record, associating a pizza with a restaurant at a specific price.*

(4)**Running the server and making requests**: *The application is designed to be run as a server that responds to HTTP requests. You can use a tool like Postman to send these requests and view the responses.*

(5)**Error handling**: *The application includes error handling to return appropriate error messages and status codes when things go wrong. For example, if you try to get details for a restaurant that doesn't exist, it will return a "Restaurant not found" error.*

**In summary, this Flask application provides a RESTful API for managing a database of pizza restaurants and pizzas. It includes routes for creating, reading, and deleting data, and it uses SQLAlchemy for data modeling and validation.**



#### License 

Copyright (c) 2023 Brian Mwangi Maina

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
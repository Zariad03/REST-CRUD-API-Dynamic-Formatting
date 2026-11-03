RESTful API with Dynamic Formatting

Project Description

This project uses Python and Flask to create a RESTful API for managing a list of books. Each book includes an ID, title, author, and rating. The API uses JSON to share information, and the webpage displays the books in a table.

Technologies Used

* Python
* Flask
* HTML
* CSS
* JavaScript
* JSON

How to Run

1. Install Flask using pip install flask.
2. Run the application using python app.py.
3. Open http://127.0.0.1:5000 in a browser that supports Flask.

API Endpoints

* GET /goodbooks - View all books.
* GET /goodbooks/1 - View one book.
* POST /goodbooks - Add a book.
* PUT /goodbooks/1 - Update a book.
* DELETE /goodbooks/1 - Delete a book.

Reflection

This assignment helped me understand how RESTful APIs communicate with webpages. I used Python and Flask to create endpoints that allow users to view, add, update, and delete book information. I learned how JSON sends information between the API and the webpage. I also used JavaScript to retrieve the book data and display it in a table instead of entering the information manually. The conditional formatting highlights books with ratings of 4 or higher, making the results easier to read. One challenge was understanding how the frontend sends requests to the API. Overall, this project gave me more practice with Python and showed me how different technologies work together.
RESTful API with Dynamic Formatting

Project Description

This project is a simple book application I created using Python and Flask. It allows users to view a list of books, add new books, make changes, and delete books. Each book includes a title, author, ID, and rating. The webpage displays the information in a table.

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

* GET /goodbooks – View all books.
* GET /goodbooks/1 – View one book.
* POST /goodbooks – Add a new book.
* PUT /goodbooks/1 – Update a book.
* DELETE /goodbooks/1 – Delete a book.

Reflection

Working on this assignment helped me get a better understanding of how different applications communicate with each other. I used Python and Flask to create an API that shares book information through JSON. This connects to technical interoperability because the webpage and API communicate using different technologies. Semantic interoperability comes into play because the information needs to be organized so both systems understand what each field means, such as the book title, author, and rating. Organizational interoperability could allow places like libraries and bookstores to share book information. I also learned that an LLM could use information from an API to answer questions or help someone find a book. This project helped me see how these technologies can work together.
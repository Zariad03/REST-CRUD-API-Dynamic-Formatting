from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

books = [
    {"id": 1, "title": "Divergent", "author": "Veronica Roth", "rating": 5},
    {"id": 2, "title": "The Fault in Our Stars", "author": "John Green", "rating": 5},
    {"id": 3, "title": "The Hunger Games", "author": "Suzanne Collins", "rating": 5},
    {"id": 4, "title": "The Maze Runner", "author": "James Dashner", "rating": 4},
]


# Display the webpage
@app.route("/")
def home():
    return render_template("index.html")


# GET: Display all books
@app.route("/goodbooks", methods=["GET"])
def get_books():
    return jsonify(books)


# GET: Display one book
@app.route("/goodbooks/<int:book_id>", methods=["GET"])
def get_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return jsonify(book)

    return jsonify({"error": "Book not found"}), 404


# POST: Add a new book
@app.route("/goodbooks", methods=["POST"])
def add_book():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Book information is required"}), 400

    title = data.get("title")
    author = data.get("author")
    rating = data.get("rating")

    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "A book title is required"}), 400

    if not isinstance(author, str) or not author.strip():
        return jsonify({"error": "An author is required"}), 400

    if (
        not isinstance(rating, int)
        or isinstance(rating, bool)
        or rating < 1
        or rating > 5
    ):
        return jsonify({"error": "Rating must be between 1 and 5"}), 400

    new_id = max([book["id"] for book in books], default=0) + 1

    new_book = {
        "id": new_id,
        "title": title.strip(),
        "author": author.strip(),
        "rating": rating,
    }

    books.append(new_book)

    return jsonify(new_book), 201


# PUT: Update a book
@app.route("/goodbooks/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Book information is required"}), 400

    for book in books:
        if book["id"] == book_id:
            title = data.get("title", book["title"])
            author = data.get("author", book["author"])
            rating = data.get("rating", book["rating"])

            if not isinstance(title, str) or not title.strip():
                return jsonify({"error": "A book title is required"}), 400

            if not isinstance(author, str) or not author.strip():
                return jsonify({"error": "An author is required"}), 400

            if (
                not isinstance(rating, int)
                or isinstance(rating, bool)
                or rating < 1
                or rating > 5
            ):
                return jsonify({"error": "Rating must be between 1 and 5"}), 400

            book["title"] = title.strip()
            book["author"] = author.strip()
            book["rating"] = rating

            return jsonify(book)

    return jsonify({"error": "Book not found"}), 404


# DELETE: Remove a book
@app.route("/goodbooks/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return jsonify({"message": "Book deleted successfully"})

    return jsonify({"error": "Book not found"}), 404


if __name__ == "__main__":
    app.run()

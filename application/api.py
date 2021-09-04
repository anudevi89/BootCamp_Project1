from application.app import app
from flask import request,jsonify
from application.models import Books
from application.app import db
import json


# Import your models here
from application.models import User

@app.route("/")
def home():
    return {"Status": "Success"}, 200

@app.route("/books",methods=["POST"])
def BookDetails():
    params = request.json
    title = params.get("title")
    author = params.get("author")
    # Create a question python object
    bookDetails = Books(title=title, author=author)
    # Make an actual entry in DB
    db.session.add(bookDetails)
    db.session.commit()
    return {
        "Status": "Success",
        "data": {
            "title": bookDetails.title,
            "author": bookDetails.author,
            "genre" : bookDetails.genre
        },
    }


@app.route("/recommend", methods=["GET"])
def Recommend():
    result = []
    book_lists = Books.query.all()
    print(book_lists.count)
    print(book_lists)
    for bookDetails in book_lists:
     #if bookDetails:
        result.append({
                "Data": {
                    "title": bookDetails.title,
                    "author": bookDetails.author,
                    "genre": bookDetails.genre
                },
            })
    return jsonify(result)
     #else:
        # return {"status": "ERROR", "message": "Invalid Credentials"}, 401



# Write your API endpoints here
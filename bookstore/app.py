from flask import Flask, render_template, request, redirect, url_for, make_response


# instantiate the app
app = Flask(__name__)

# Create a list called categories. The elements in the list should be lists that contain the following information in this order:
#   categoryId
#   categoryName
#   An example of a single category list is: [1, "Biographies"]
categories = [
    {'categoryId': 1, 'categoryName': 'Manga'},
    {'categoryId': 2, 'categoryName': 'Superheroes'},
    {'categoryId': 3, 'categoryName': 'Non-Fiction'},
    {'categoryId': 4, 'categoryName': 'Life'}
]

# Create a list called books. The elements in the list should be lists that contain the following information in this order:
#   bookId     (you can assign the bookId - preferably a number from 1-16)
#   categoryId (this should be one of the categories in the category dictionary)
#   title
#   author
#   isbn
#   price      (the value should be a float)
#   image      (this is the filename of the book image.  If all the images, have the same extension, you can omit the extension)
#   readNow    (This should be either 1 or 0.  For each category, some of the books (but not all) should have this set to 1.
#   An example of a single category list is: [1, 1, "Madonna", "Andrew Morton", "13-9780312287863", 39.99, "madonna.png", 1]
books = [
    {'bookId': 1, 'categoryId': 1, 'title': 'Naruto', 'author': 'Masashi Kishimoto', 'isbn': '13-9781591169818', 
     'price': 9.99, 'image': 'naruto.png', 'readNow': 1},
    {'bookId': 2, 'categoryId': 1, 'title': 'One Piece', 'author': 'Eiichiro Oda', 'isbn': '13-9781591168392',
        'price': 8.99, 'image': 'onepiece.png', 'readNow': 0},
    {'bookId': 3, 'categoryId': 2, 'title': 'Batman: Year One', 'author': 'Frank Miller', 'isbn': '13-9781401207526',
        'price': 12.99, 'image': 'batman_year_one.png', 'readNow': 1},
     {"bookId": 4, "categoryId": 2, "title": "Superman: Red Son",
     "author": "Mark Millar", "isbn": "13-9781401241892",
     "price": 11.99, "image": "superman_redson.png", "readnow": 0},

    {"bookId": 5, "categoryId": 3, "title": "Sapiens",
     "author": "Yuval Noah Harari", "isbn": "13-9780062316097",
     "price": 14.99, "image": "sapiens.png", "readnow": 1},

    {"bookId": 6, "categoryId": 3, "title": "Educated",
     "author": "Tara Westover", "isbn": "13-9780399590504",
     "price": 13.99, "image": "educated.png", "readnow": 0},

    {"bookId": 7, "categoryId": 4, "title": "Yotsuba&! Vol.1",
     "author": "Kiyohiko Azuma", "isbn": "13-9780316073876",
     "price": 8.99, "image": "yotsuba1.png", "readnow": 1},
 
    {"bookId": 8, "categoryId": 4, "title": "March Comes in Like a Lion Vol.1",
     "author": "Chica Umino", "isbn": "13-9784088673423",
     "price": 9.49, "image": "march1.png", "readnow": 0},
]
# set up routes
@app.route('/')
def home():
    #Link to the index page.  Pass the categories as a parameter
    return render_template('index.html', categories=categories)

@app.route('/category')
def category():
    # Store the categoryId passed as a URL parameter into a variable
    selectedCategory = request.args.get('categoryId')

    # Create a new list called selected_books containing a list of books that have the selected category
    selected_books = [b for b in books if b['categoryId'] == int(selectedCategory)]

    # Link to the category page.  Pass the selectedCategory, categories and books as parameters
    return render_template('category.html', selectedCategory=selectedCategory, categories=categories, books=selected_books)

@app.route('/search')
def search():
    #Link to the search results page.
    return render_template('base.html')

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template


if __name__ == "__main__":
    app.run(debug = True)

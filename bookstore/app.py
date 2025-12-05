from flask import Flask, render_template, request, redirect, url_for, make_response


# instantiate the app
app = Flask(__name__)

# Create a list called categories. The elements in the list should be lists that contain the following information in this order:
#   categoryId
#   categoryName
#   An example of a single category list is: [1, "Biographies"]
###Each entry should be a dictionary with an id and a name
categories = [
    {"categoryId": 1, "categoryName": "Manga"},
    {"categoryId": 2, "categoryName": "Superheroes"},
    {"categoryId": 3, "categoryName": "Non-Fiction"},
    {"categoryId": 4, "categoryName": "Slice-of-Life"},
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
###Each entry should be a dictionary containing: title, author, ISBN, price, categoryId, and image file name
books = [
    {'bookId': 1, 'categoryId': 1, 'title': "Naruto Vol 1", 'author': "Masashi Kishimoto", 'isbn': "978-1591165677", 'price': 9.99, 'image': "Naruto-Vol-1.png", 'readNow': 1},
    {'bookId': 2, 'categoryId': 1, 'title': "One Piece Vol 1", 'author': "Eiichiro Oda", 'isbn': "978-1591168395", 'price': 9.99, 'image': "One-Piece-Vol-1.png", 'readNow': 0},
    {'bookId': 3, 'categoryId': 1, 'title': "Jujutsu Kaisen Vol 1", 'author': "Gege Akutami", 'isbn': "978-1974708183", 'price': 9.99, 'image': "Jujutsu-Kaisen-Vol-1.png", 'readNow': 1},
    {'bookId':4, 'categoryId':1, 'title':"Attack on Titan Vol 1", 'author':"Hajime Isayama", 'isbn':"978-1612620244", 'price':9.99, 'image':"Attack-on-Titan-Vol-1.png", 'readNow':0},
    {'bookId':5, 'categoryId':2, 'title':"Absolute Batman Vol 1 The Zoo", 'author':"Scott Snyder", 'isbn':"978-1401275953", 'price':19.99, 'image':"Absolute-Batman-Vol-1-The-Zoo.png", 'readNow':1},
    {'bookId':6, 'categoryId':2, 'title':"Superman Vol 1", 'author':"Gene Luen Yang", 'isbn':"978-1401275954", 'price':14.99, 'image':"Superman-Vol-1.png", 'readNow':0},
    {'bookId':7, 'categoryId':2, 'title':"The New Teen Titans Vol 1", 'author':"Marv Wolfman", 'isbn':"978-1401275955", 'price':17.99, 'image':"The-New-Teen-Titans-Vol-1.png", 'readNow':1},
    {'bookId':8, 'categoryId':2, 'title':"Young Justice Book One", 'author':"Peter David", 'isbn':"978-1401275956", 'price':12.99, 'image':"Young-Justice-Book-One.png", 'readNow':0},
    {'bookId':9, 'categoryId':3, 'title':"The Complete Maus A Survivor Tale", 'author':"Art Spiegelman", 'isbn':"978-0679748403", 'price':24.99, 'image':"The-Complete-Maus-A-Survivor-Tale.png", 'readNow':1},
    {'bookId':10, 'categoryId':3, 'title':"The Beats A Graphic History", 'author':"Harvey Pekar, Ed Piskor", 'isbn':"978-1603094501", 'price':19.99, 'image':"The-Beats-A-Graphic-History.png", 'readNow':0},
    {'bookId':11, 'categoryId':3, 'title':"The Complete Persepolis Volumes 1 and 2", 'author':"Marjane Satrapi", 'isbn':"978-0375714573", 'price':22.99, 'image':"The-Complete-Persepolis-Volumes-1-and-2.png", 'readNow':1},
    {'bookId':12, 'categoryId':3, 'title':'Gender Queer A Memoir', 'author':'Maia Kobabe','isbn':'978-1-5493-0400-2','price':8.99,'image':'Gender-Queer-A-Memoir.png','readNow':0},
    {'bookId':13, 'categoryId':4, 'title':'Freestyle A Graphic Novel', 'author':'Gale Galligan','isbn':'978-1-60309-452-5','price':14.99,'image':'Freestyle-A-Graphic-Novel.png','readNow':1},
    {'bookId':14, 'categoryId':4, 'title':'Strangers in Paradise', 'author':'Terry Moore','isbn':'978-1-60309-024-4','price':19.99,'image':'Strangers-in-Paradise.png','readNow':0},
    {'bookId':15, 'categoryId':4, 'title':'Giant Days', 'author':'John Allison','isbn':'978-1-60309-329-0','price':12.99,'image':'Giant-Days.png','readNow':1},
    {'bookId':16, 'categoryId':4, 'title':'The Walking Man', 'author':'Jiro Taniguchi','isbn':'978-1912097364','price':29.99,'image':'The-Walking-Man.png','readNow':1}
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
    selected_books = [book for book in books if str(book['categoryId']) == selectedCategory]
    # Link to the category page.  Pass the selectedCategory, categories and books as parameters
    return render_template('category.html',categories=categories, books=selected_books, selectedCategory=selectedCategory)

@app.route('/search')
def search():
    #Link to the search results page.
    return render_template()

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template


if __name__ == "__main__":
    app.run(debug = True)

from flask import Flask, render_template, request
from recommendation import recom, plot1
from recommendation import ls01,sort_summary, all_books_df, books_titles

## initialize app
app = Flask(__name__)  #create an instance
#most_rated_books = change(ls01)

most_rated_books = [books.capitalize() for books in ls01]

@app.route('/')
def index():
        

    return render_template('index.html', most_rated_books=most_rated_books, books_titles=books_titles )

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        book_name = request.form['book_name'].lower().strip()
        #print(book_name)
        if book_name == '':
            return render_template('index.html', message = 'Please enter required fields', books_titles=books_titles )
        
        if recom(book_name):
            recommended_books = recom(book_name)
            recommended_books = sort_summary(book_name, recommended_books)
            encoded = plot1(recommended_books)

            recommended_books_summ = list(all_books_df[all_books_df['BookTitle'].isin(recommended_books)]["Summary"])
            recommended_books_auth = list(all_books_df[all_books_df['BookTitle'].isin(recommended_books)]["authors"])
            recommended_books = [book.capitalize() for book in recommended_books]
            

            return render_template('success.html', recommended_books=recommended_books,
             book_name=book_name, most_rated_books=most_rated_books
              ,recommended_books_summ=recommended_books_summ
              ,recommended_books_auth=recommended_books_auth
              ,books_titles=books_titles, encoded=encoded)
        else:
            return render_template('index.html',books_titles=books_titles
            ,message = f'{book_name} is not in our list, try another book.' )
            


if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=False)
=======
    app.debug = False
    app.run()
>>>>>>> f4ef12441c37c83efcbf449932d6274049fe0974
    
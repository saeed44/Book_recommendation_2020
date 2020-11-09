
from surprise import dump
import pandas as pd
import os
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
# import matplotlib.pyplot as plt
import base64
from io import BytesIO
import matplotlib.pyplot as plt

# load the trained algorithm
temp_file = os.path.expanduser('trained_algo_surprise')
_, loaded_algo = dump.load(temp_file)

# find item-item similarity matrix
item_sim_matrix = pd.DataFrame(cosine_similarity(loaded_algo.qi, loaded_algo.qi))

def recom(book_name):
    
    try:
        ind = loaded_algo.trainset.to_inner_iid(book_name)
    except ValueError:
        ind=None

    if ind:
        sorted_series = item_sim_matrix.iloc[ind].sort_values(ascending=False)
    
        # make the list of recommended books
        recommended_books = []
        for index in sorted_series[1:11].index:
            book_title = loaded_algo.trainset.to_raw_iid(index)
            recommended_books.append(book_title)
        
        return recommended_books




def plot1(recommended_books):
<<<<<<< HEAD

    df_recommended = pd.DataFrame(recommended_books, columns=["BookTitle"])
    
    df = df_recommended.merge(df_final_books, how='inner', on="BookTitle")

    ave_rating = df_final_books[["Rating"]].mean()[0] 
    
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15,5))
    

    df.plot.bar(ax=axes[0], x="BookTitle", y="RatingCount", rot=90); axes[0].set_xlabel(" ");
    axes[0].set_ylabel("Number of Ratings");
    axes[0].tick_params('x', labelrotation=-45)
=======
    
    df = df_final_books[df_final_books["BookTitle"].isin(recommended_books)]
    ave_rating = df_final_books[["Rating"]].mean()[0] 
    
    fig, axes = plt.subplots(nrows=1, ncols=2)
    
    df.plot.bar(ax=axes[0], x="BookTitle", y="RatingCount", rot=90); axes[0].set_xlabel(" ");
    axes[0].set_ylabel("Number of Ratings");

>>>>>>> f4ef12441c37c83efcbf449932d6274049fe0974
    
    df.plot(ax=axes[1], x="BookTitle", y="Rating", rot=90, 
                    marker='o', xticks=[i for i in range(len(recommended_books))]);
    axes[1].set_xlabel(" ");
<<<<<<< HEAD
    axes[1].set_ylabel("Rating");
    axes[1].set_xlim(-.2,len(recommended_books)-0.8);
    axes[1].set_title('Total Average rating = {}'.format(round(ave_rating,1)));
    plt.setp(axes[0].get_xticklabels(), rotation=-45, ha="left",
         rotation_mode="anchor")
    plt.setp(axes[1].get_xticklabels(), rotation=-45, ha="left",
         rotation_mode="anchor")

    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png' , bbox_inches='tight')
=======
    axes[1].set_ylabel("Average Rating");
    axes[1].set_xlim(-.2,len(recommended_books)-0.8);
    
    axes[1].set_title('Average rating = {}'.format(round(ave_rating,1)));
    
    fig.subplots_adjust(wspace=.3)
    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png', bbox_inches='tight')
>>>>>>> f4ef12441c37c83efcbf449932d6274049fe0974
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

    return encoded







def most_rated():
    ls = list(pd.read_csv("most_rated_books.csv")["BookTitle"])
    return ls

ls01 = list(pd.read_csv("most_rated_books.csv")["BookTitle"])

#def change(ls):
#    counter=0
#    while True:
#        yield ls[counter]
 #       counter+=1
  #      if counter == len(ls):
   #         counter=0

# sort books based on similarity of the contents (from summary)
df_final_books = pd.read_csv("Books_final.csv")

cos_sim_tfidf_df = pd.read_csv("cos_sim_tfidf.csv")

books = list(df_final_books["BookTitle"])

index_to_title = {i:title for i,title in zip([i for i in range(0,len(books))],books)}

cos_sim_tfidf_df.rename(index=index_to_title, inplace=True)

def sort_summary(book,book_list):
    
    ls = list(cos_sim_tfidf_df.loc[book_list,[book]].sort_values([book],ascending=False).index)
    return ls

all_books_df = pd.read_csv("Books_final.csv")

books_titles = list(df_final_books["BookTitle"])



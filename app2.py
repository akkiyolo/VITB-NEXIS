from flask import Flask, render_template, url_for
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict

app = Flask(__name__)

# Load the news data
news_data = pd.read_csv('news_data.csv')
news_data.columns = news_data.columns.str.strip()

# Initialize the TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(news_data['content'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get recommendations based on content similarity and category
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = news_data.loc[news_data['title'] == title].index[0]
    category = news_data.loc[news_data['title'] == title, 'category'].values[0]
    sim_scores = [
        (i, score) for i, score in enumerate(cosine_sim[idx]) 
        if news_data.loc[i, 'category'] == category and i != idx
    ]
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    article_indices = [i[0] for i in sim_scores[:5]]
    return news_data[['title', 'category', 'image_url']].iloc[article_indices].to_dict(orient='records')

@app.route('/')
def index():
    grouped_articles = defaultdict(list)
    for _, row in news_data.iterrows():
        grouped_articles[row['category']].append({
            'title': row['title'],
            'image_url': row['image_url']
        })
    return render_template('index.html', grouped_articles=grouped_articles)

@app.route('/recommend/<string:title>')
def recommend(title):
    recommendations = get_recommendations(title)
    return render_template('recommend.html', title=title, recommendations=recommendations)

@app.route('/category/<string:category>')
def category_news(category):
    filtered_articles = news_data[news_data['category'] == category][['title', 'image_url']].to_dict(orient='records')
    return render_template('category_news.html', category=category, articles=filtered_articles)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

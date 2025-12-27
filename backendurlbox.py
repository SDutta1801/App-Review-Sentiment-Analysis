import requests
import json
from bs4 import BeautifulSoup
from textblob import TextBlob
from flask import Flask, request, render_template , redirect , url_for

app = Flask(__name__)

@app.route('/analyser', methods=['GET','POST'])
def analyser():
    if request.method == 'POST':
        app_name = request.form['app_name']
        google_reviews = get_google_reviews(app_name)
        apple_reviews = get_apple_reviews(app_name)
        google_sentiment = analyze_sentiment(google_reviews)
        apple_sentiment = analyze_sentiment(apple_reviews)
        return redirect(url_for('results', app_name=app_name, google_sentiment=google_sentiment, apple_sentiment=apple_sentiment, google_reviews=google_reviews, apple_reviews=','.join(apple_reviews)))
    return render_template('analyser.html')

@app.route('/results', methods=['GET'])
def results():
    app_name = request.args.get('app_name')
    google_sentiment = request.args.get('google_sentiment')
    apple_sentiment = request.args.get('apple_sentiment')
    google_reviews = request.args.get('google_reviews')
    if google_reviews is None:
        google_reviews = []
    else:
        google_reviews = google_reviews.split(',')
    apple_reviews = request.args.get('apple_reviews')
    if apple_reviews is None:
        apple_reviews = []
    else:
        apple_reviews = apple_reviews.split(',')
    #google_reviews = [review.strip() for review in google_reviews]
    #apple_reviews = [review.strip() for review in apple_reviews]
    return render_template('results.html', app_name=app_name, google_sentiment=google_sentiment, apple_sentiment=apple_sentiment, google_reviews=google_reviews, apple_reviews=apple_reviews)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')



def get_google_reviews(app_name):
    query = '+'.join(app_name.split())
    url = f'https://play.google.com/store/search?q={query}&c=apps'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find('div', {'class': 'ZmHEEd'})
    if result is None:
        return []
    result = result.find('a')
    app_id = result['href'].split('=')[1]
    reviews_url = f'https://play.google.com/store/apps/details?id={app_id}&showAllReviews=true'
    response = requests.get(reviews_url)
    reviews = []
    for review in response.json()['reviews']:
        reviews.append(review['comment'])
    return reviews


def get_apple_reviews(app_name):
    query = '+'.join(app_name.split())
    url = f'https://itunes.apple.com/search?term={query}&entity=software'
    response = requests.get(url)
    result = response.json()['results'][0]
    app_id = result['trackId']
    reviews_url = f'https://itunes.apple.com/rss/customerreviews/id={app_id}/json'
    response = requests.get(reviews_url)
    reviews = []
    for review in response.json()['feed']['entry']:
        reviews.append(review['content']['label'])
    return reviews

def analyze_sentiment(reviews):
    polarity = 0
    for review in reviews:
        blob = TextBlob(review)
        polarity += blob.sentiment.polarity
    if len(reviews) > 0:
        polarity /= len(reviews)
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

if __name__ == '__main__':

    app.run(debug=True)

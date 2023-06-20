import requests
from nltk.sentiment import SentimentIntensityAnalyzer
from newsdataapi import NewsDataApiClient


# Function to fetch news articles from an API
def fetch_news_articles():
    api = NewsDataApiClient(apikey="pub_1763638f05a3a2cb3a90433d7e539bf39d53c")
    response_econ = api.news_api(q="economy", country="us")
    response_geo = api.news_api(q="Geopolitical events", country="us")
    response_gov = api.news_api(q="Government policy changes", country="us")
    response_interest = api.news_api(q="Interest rates", country="us")
    response_mark = api.news_api(q="Market sentiment", country="us")

    responses = [
        (response_econ, "Economy"),
        (response_geo, "Geopolitical Events"),
        (response_gov, "Government Policy Changes"),
        (response_interest, "Interest Rates"),
        (response_mark, "Market Sentiment")
    ]
    
    #response = [response_econ]
    return responses

# Function to perform sentiment analysis on news articles
def perform_sentiment_analysis(articles):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = []
    for article in articles["results"]:
        text = article["content"]
        if type(text) == str:
            sentiment = sid.polarity_scores(text)
            sentiment_scores.append(sentiment["compound"])
    return sentiment_scores

# Function to calculate the sentiment score
def calculate_sentiment_score(sentiment_scores):
    sentiment_score = sum(sentiment_scores) / len(sentiment_scores)
    return sentiment_score

# Main function
def main():

    # Fetch news articles
    allArticles = fetch_news_articles()
    mean = 0

    for articles, articleName in allArticles:

        # Perform sentiment analysis
        sentiment_scores = perform_sentiment_analysis(articles)

        # Calculate sentiment score
        sentiment_score = calculate_sentiment_score(sentiment_scores)

        print(articleName + " Sentiment Score:", sentiment_score)

        mean += sentiment_score

    mean /= len(allArticles)
    print("\n----------------------------------\n")
    print('Total Mean Sentiment: ' + str(mean))

# Run the main function
if __name__ == "__main__":
    main()

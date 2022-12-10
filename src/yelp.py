from yelpapi import YelpAPI
import os

api_key = os.environ.get('YELP_API_KEY', None)

client = YelpAPI(api_key)
    
def search_yelp(restaurant_name): 
    response = client.search(term=restaurant_name, location='Fremont, CA')
    business = response['businesses'][0]
    rating = business['rating']
    review_count = business['review_count']
    reviews = client.reviews(business['id'])

    return {
        'name': business['name'],
        'rating': rating,
        'review_count': review_count,
        'reviews': [{'user': review['user']['name'], 'text': review['text']} for review in reviews['reviews']]
    }
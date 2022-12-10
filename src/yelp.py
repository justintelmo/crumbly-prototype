from yelpapi import YelpAPI
import os

api_key = os.environ.get('YELP_API_KEY', None)

client = YelpAPI(api_key)
    
def search_yelp(restaurant_name): 
    response = client.search_query(term=restaurant_name, location='fremont, ca', sort_by='rating', limit=5)
    business = response['businesses'][0]
    reviews = client.reviews_query(restaurant_name)
    
    
    return {
        'business': business,
        'reviews': reviews['reviews']
    }
    # return {
    #     'name': business['name'],
    #     'rating': rating,
    #     'review_count': review_count,
    #     'reviews': [{'user': review['user']['name'], 'text': review['text']} for review in reviews['reviews']]
    # }
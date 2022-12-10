from yelpapi import YelpAPI
import os

api_key = os.environ.get('YELP_API_KEY', None)

client = YelpAPI(api_key)
    
def search_yelp(restaurant_name): 
    reviews = client.reviews_query(restaurant_name)
    
    
    return {
        'reviews': reviews['reviews']
    }
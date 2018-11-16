import requests
import config
from response import page_speed_response

api_key = config.key
url = config.url
strategy = config.strategy

params = {
    'url': url,
    'category': ['accessibility','seo', 'best-practices','performance','pwa'],
    'strategy': strategy,
    'key': api_key
}
endpoint = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

def request(params):
    response = requests.get(endpoint, params=params)
    return response.json()


page_speed_response(request(params))




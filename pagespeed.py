import requests
import config
from response import *

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

def page_speed(params):
    response = requests.get(endpoint, params=params)
    data = response.json()
    seo_audit(data)
    best_practices(data)

page_speed(params)




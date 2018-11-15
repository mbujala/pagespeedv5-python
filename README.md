# Google Page Speed Insight API V5 for python
The program offers an interface for the Google PageSpeed Insights API. It is written in Python and provides an easy way to check the speed of the page.
## Quickstart
First, edit the config.py file. Enter the adress of your site, your api key (you can generate your own here: https://console.developers.google.com/apis/credentials) and chose audit type: for mobile or desktop.
```python
key="your_api_key"
url="http://yourpage.com/"
# strategy can be "mobile" or "desktop"
strategy="desktop"
```
After that just run the pagespeed.py
## Notes
Program wokr on v5 of the PageSpeed Insights API witch was released in November 2018

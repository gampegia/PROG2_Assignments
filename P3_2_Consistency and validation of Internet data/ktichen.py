import requests
import backoff
import simplejson as json


URL = "http://160.85.252.148/"


@backoff.on_exception(backoff.expo,
                      (requests.exceptions.Timeout,
                       requests.exceptions.HTTPError,
                       requests.exceptions.ConnectionError))
def get_url_content(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-2xx status codes
    return response.text  #return json content

content = get_url_content(URL)
print(content.split(","))
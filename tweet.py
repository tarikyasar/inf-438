import requests
import json
from kafka import KafkaProducer

bearer_token = "AAAAAAAAAAAAAAAAAAAAAPrlYAEAAAAAYYX6xGCLE1V46qGzm8gl4Hz29jw%3DKu9MLLCP8CwZyEyZOEK7ZYm6147I3FJT5L6LCGAJJtbqNoH3dY"

search_url = "https://api.twitter.com/2/tweets/search/recent"

producer = KafkaProducer(bootstrap_servers="localhost:9092")

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


tweet_fields = "tweet.fields=text,author_id,created_at"

query = {'query': '#istanbulkar','tweet.fields': 'author_id'}

json_response = connect_to_endpoint(search_url, query)

producer.send("veri-tabanlari", bytes(json.dumps(json_response), 'utf-8')).get(timeout=30)

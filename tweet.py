import requests
import json
import sys
from kafka import KafkaProducer
from pyspark.sql import SparkSession

if (len(sys.argv) < 2):
	print("Hata!")
	print("Ornek calistirma sekli: python3 tweet.py trend")
	print("trend = #trend ama hashtagsiz")
	quit()

query = "#" + sys.argv[1]

# Buraya kendi API anahtarinizi gireceksiniz
bearer_token = ""

search_url = "https://api.twitter.com/2/tweets/search/recent"

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("local[*]", "9092") \
    .getOrCreate()

producer = KafkaProducer(bootstrap_servers="localhost:9092")

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

# Gelecek olan cevapta olmasi istenen alanlar
tweet_fields = "text,author_id,created_at,lang"

# Sorgu detaylari
query = {'query': query,'tweet.fields': tweet_fields}

json_response = connect_to_endpoint(search_url, query)

with open('json_data.json', 'w') as outfile:
	json.dump(json_response['data'], outfile)

df = spark.read.json('json_data.json')

df.show()

producer.send("veri-tabanlari", bytes(json.dumps(json_response), 'utf-8')).get(timeout=30)

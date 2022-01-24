import requests
import json
from kafka import KafkaProducer
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

bearer_token = "AAAAAAAAAAAAAAAAAAAAAPrlYAEAAAAAYYX6xGCLE1V46qGzm8gl4Hz29jw%3DKu9MLLCP8CwZyEyZOEK7ZYm6147I3FJT5L6LCGAJJtbqNoH3dY"

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Create a local StreamingContext with two working thread and batch interval of 1 second
sc = SparkContext("local[2]", "NetworkWordCount")
ssc = StreamingContext(sc, 1)

# Create a DStream that will connect to hostname:port, like localhost:9999
lines = ssc.socketTextStream("localhost", 9999)

# Split each line into words
words = lines.flatMap(lambda line: line.split(" "))

# Count each word in each batch
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)

# Print the first ten elements of each RDD generated in this DStream to the console
wordCounts.pprint()
producer = KafkaProducer(bootstrap_servers="localhost:9092")

ssc.start()             # Start the computation
ssc.awaitTermination()  # Wait for the computation to terminate

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

query = {'query': '#akpyeverilenheroy','tweet.fields': 'author_id'}

json_response = connect_to_endpoint(search_url, query)

f = open('json_response.json')

data = json.load(f)

producer.send("vt", bytes(json.dumps(json_response), 'utf-8')).get(timeout=30)

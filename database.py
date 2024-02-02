from pymongo.mongo_client import MongoClient

# This URI is public accessible so needs to be handled properly
uri = "mongodb+srv://sud:1234@cluster0.qnwdzgg.mongodb.net/?retryWrites=true&w=majority"


# Create a new client and connect to the server
client = MongoClient(uri)
db = client["ecommerce"]

products_collection = db["products"]
orders_collection = db["orders"]


# Created index over price column since most of the queries are filtered out based on the price of the product
products_collection.create_index("price")

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Unable to connect to MongoDB")
    print(e)


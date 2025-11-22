import os
import random
from faker import Faker
from pymongo import MongoClient

# MongoDB connection
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_DB = os.getenv("MONGO_DB", "graphql")

client = MongoClient(MONGO_HOST, MONGO_PORT)
db = client[MONGO_DB]

# Remove existing data
db.authors.drop()
db.books.drop()

fake = Faker()

print("Generating mock data...")

authors = []
for i in range(1, 201):
    authors.append({"id": i, "name": fake.name()})

db.authors.insert_many(authors)

books = []
for i in range(1, 1001):
    books.append(
        {"id": i, "title": fake.catch_phrase(), "author_id": random.randint(1, 200)}
    )

db.books.insert_many(books)

print("Data generation complete")

import random
from faker import Faker

fake = Faker()
db = {
    "authors": [],
    "books": [],
}

print("Generating mock data...")

for i in range(1, 201):
    db["authors"].append({"id": i, "name": fake.name()})

for i in range(1, 1001):
    db["books"].append(
        {"id": i, "title": fake.catch_phrase(), "author_id": random.randint(1, 200)}
    )

print("Data generation complete")

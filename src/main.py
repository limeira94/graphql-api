import os
import strawberry
from strawberry.fastapi import GraphQLRouter
from fastapi import FastAPI
from typing import List
from pymongo import MongoClient

# MongoDB connection
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_DB = os.getenv("MONGO_DB", "graphql")

client = MongoClient(MONGO_HOST, MONGO_PORT)
db = client[MONGO_DB]


@strawberry.type
class Author:
    id: int
    name: str

    @strawberry.field
    def books(self) -> List["Book"]:
        books_data = db.books.find({"author_id": self.id}, {"_id": 0})
        return [Book(**book) for book in books_data]


@strawberry.type
class Book:
    id: int
    title: str
    author_id: int

    @strawberry.field
    def author(self) -> Author:
        author_data = db.authors.find_one({"id": self.author_id}, {"_id": 0})
        return Author(**author_data)


@strawberry.type
class Query:
    @strawberry.field
    def authors(self) -> List[Author]:
        authors_data = db.authors.find({}, {"_id": 0})
        return [Author(**author) for author in authors_data]

    @strawberry.field
    def books(self) -> List[Book]:
        books_data = db.books.find({}, {"_id": 0})
        return [Book(**book) for book in books_data]


schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

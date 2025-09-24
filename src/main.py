import strawberry
from strawberry.fastapi import GraphQLRouter
from fastapi import FastAPI
from typing import List

from src.create_db import db


@strawberry.type
class Author:
    id: int
    name: str

    @strawberry.field
    def books(self) -> List["Book"]:
        return [Book(**book) for book in db["books"] if book["author_id"] == self.id]


@strawberry.type
class Book:
    id: int
    title: str
    author_id: int

    @strawberry.field
    def author(self) -> Author:
        author_data = next(
            (author for author in db["authors"] if author["id"] == self.author_id), None
        )
        return Author(**author_data)


@strawberry.type
class Query:
    @strawberry.field
    def authors(self) -> List[Author]:
        return [Author(**author) for author in db["authors"]]

    @strawberry.field
    def books(self) -> List[Book]:
        return [Book(**book) for book in db["books"]]


schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

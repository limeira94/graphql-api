from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_all_authors():
    graphql_query = """
        query GetAllAuthors {
            authors {
                id
                name 
                books {
                    id
                    title
                }
            }
        }
    """
    response = client.post("/graphql", json={"query": graphql_query})

    assert response.status_code == 200

    response_json = response.json()
    assert "data" in response_json
    assert "authors" in response_json["data"]

    authors = response_json["data"]["authors"]
    assert len(authors) == 200

    first_author = authors[0]
    assert "id" in first_author
    assert "name" in first_author
    assert "books" in first_author
    assert isinstance(first_author["books"], list)


def test_get_all_books():
    graphql_query = """
        query GetAllBooks {
            books {
                id    
                title
                author {
                    id
                    name
                }
            }
        }
    """
    response = client.post("graphql", json={"query": graphql_query})

    assert response.status_code == 200

    response_json = response.json()
    assert "data" in response_json
    assert "books" in response_json["data"]

    books = response_json["data"]["books"]
    assert len(books) == 1000

    first_book = books[1]
    assert "id" in first_book
    assert "title" in first_book
    assert "author" in first_book
    assert "name" in first_book["author"]

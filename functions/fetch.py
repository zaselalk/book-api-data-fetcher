import json
import requests
from functions.seeds import generate_description
import uuid


def fetch_book_data(url):
    response = requests.get(url[1])
    json_data = json.loads(response.text)

    # Extract relevant data from JSON object
    books = json_data.get("results", [])
    modified_books = []
    print(f"Collecting.. {url[0]} books.")
    for book in books:
        try:
            book_item = {}

            unique_id = uuid.uuid4()
            unique_id_str = str(unique_id)

            book_item.update({"id": unique_id_str})
            book_item.update({'title': book['title']})
            book_item.update(
                {"image": book['formats']['image/jpeg'] or 'none'})
            book_item.update({"author": book['authors'][0]['name']})
            book_item.update({"category": url[0]})
            book_item.update({"sample": generate_description(3)})
            book_item.update({"discription": generate_description(20)})

            modified_books.append(book_item)

        except Exception as e:
            print("Error ", e)
            continue

    return modified_books

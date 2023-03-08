import json
from functions.fetch import fetch_book_data


urls = [["science", "https://gutendex.com/books/?topic=science"],
        ["mathematics", "https://gutendex.com/books/?topic=mathematics"],
        ["adventure", "https://gutendex.com/books/?topic=adventure"],
        ["historical", "https://gutendex.com/books/?topic=historical"],
        ["technology", "https://gutendex.com/books/?topic=technology"],
        ["stories", "https://gutendex.com/books/?topic=stories"],
        ["romance", "https://gutendex.com/books/?topic=romance"],
        ["biology", "https://gutendex.com/books/?topic=biology"],
        ["self", "https://gutendex.com/books/?topic=self"],
        ["cook", "https://gutendex.com/books/?topic=cook"]]


modified_books = []

for url in urls:
    books = fetch_book_data(url)
    modified_books.extend(books)

js_array = json.dumps(modified_books)

with open("books.js", "w") as f:
    f.write(js_array)

print(f"JS array created with {len(modified_books)} books")

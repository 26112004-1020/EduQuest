import requests
from bs4 import BeautifulSoup

def search_project_gutenberg(book_title, max_results=5):
    base_url = "https://www.gutenberg.org/ebooks/search/?query="
    book_title = book_title.replace(" ", "+")
    search_url = base_url + book_title

    try:
        response = requests.get(search_url)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code

        soup = BeautifulSoup(response.text, 'html.parser')

        results = soup.find_all('li', class_='booklink', limit=max_results)
        if results:
            for i, result in enumerate(results, start=1):
                title = result.find('span', class_='title').get_text()
                author = result.find('span', class_='subtitle').get_text() if result.find('span', class_='subtitle') else "Unknown Author"
                link = "https://www.gutenberg.org" + result.find('a')['href']
                print(f"{i}. Title: {title}\n   Author: {author}\n   Link: {link}\n")
        else:
            print("No results found on Project Gutenberg for this book.")

    except requests.HTTPError as e:
        print("Failed to retrieve the search results due to HTTP error.")
    except requests.RequestException as e:
        print("Failed to retrieve the search results due to a network problem.")


def search_open_library(book_title, max_results=5):
    base_url = "https://openlibrary.org/search?q="

    book_title = book_title.replace(" ", "+")
    search_url = base_url + book_title

    try:
        response = requests.get(search_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        results = soup.find_all('li', class_='searchResultItem', limit=max_results)
        if results:
            for i, result in enumerate(results, start=1):
                title = result.find('a', class_='title').get_text().strip()
                author = result.find('a', class_='author').get_text().strip() if result.find('a', class_='author') else "Unknown Author"
                link = "https://openlibrary.org" + result.find('a', class_='title')['href']
                print(f"{i}. Title: {title}\n   Author: {author}\n   Link: {link}\n")
        else:
            print("No results found on Open Library for this book.")

    except requests.HTTPError as e:
        print("Failed to retrieve Open Library search results due to HTTP error.")
    except requests.RequestException as e:
        print("Failed to retrieve Open Library search results due to a network problem.")

if __name__ == "__main__":
    book_title = input("Enter the title of the book you want to search for: ")
    max_results = int(input("Enter the maximum number of results you want to see (default 5): ") or 5)

    print("\nSearching Project Gutenberg...")
    search_project_gutenberg(book_title, max_results)

    print("\nSearching Open Library...")
    search_open_library(book_title, max_results)

from get_metadata import json_read, json_write, BASE_URL
import requests
from bs4 import BeautifulSoup


def get_iaf_library_images():
    iaf_library_data = json_read('iaf_library_data.json')
    for url in (BASE_URL, f'{BASE_URL}&page_n=2', f'{BASE_URL}&page_n=3'):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        books = soup.findAll("div", {"class": "Book"})
        for book in books:
            book_ref = book.findAll("a")[1].attrs['href']
            img = book.find('img', {'src': True})
            image_link = f'iaflibrary.org.il/{img.attrs["src"]}'
            iaf_library_data[book_ref]['front_page_image'] = image_link
    json_write('iaf_library_data.json', iaf_library_data)


def main():
    get_iaf_library_images()


if __name__ == '__main__':
    main()

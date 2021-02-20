from get_metadata import json_read, json_write, IAF_PREFIX
import requests
from bs4 import BeautifulSoup


def get_iaf_images():
    response = requests.get("https://www.iaf.org.il/52-he/IAF.aspx")
    soup = BeautifulSoup(response.content, "html.parser")
    iaf_data = json_read('iaf_data.json')
    for link, issue in iaf_data.items():
        a = soup.find('a', {'href': f'https://{link}'}) or soup.find('a', {'href': f'{link.split(IAF_PREFIX)[1]}'}) or \
            soup.find('a', {'href': f'http://{link}'}) or soup.find('a', {'href': f'http://{link}?'})
        if a:
            img = a.find('img', {'src': True})
            image_link = f'{IAF_PREFIX}{img.attrs["src"]}'
            issue['front_page_image'] = image_link
        else:
            pass
    json_write('iaf_data.json', iaf_data)


def main():
    get_iaf_images()


if __name__ == '__main__':
    main()

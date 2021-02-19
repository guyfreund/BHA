from get_metadata import json_read, json_write, ALL_DATA_FILE_PATH
from bs4 import BeautifulSoup
import requests
import logging
import datetime

logging.basicConfig(level=logging.INFO)


def create_index_entry(title, description, author, link, start_page=None):
    return {
        "title": title,
        "description": description,
        "start_page": start_page,
        "author": author,
        "link": link
    }


def get_iaf_index():
    all_data = json_read(ALL_DATA_FILE_PATH)
    try:
        for k, v in all_data.items():
            if k.startswith("www.iaf.org.il") and 'index' not in v:
                index = {}
                links = {}
                response = requests.get(f'http://{k}')
                soup = BeautifulSoup(response.content, "html.parser")
                col_twelve_class = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['col-12'])
                for element in col_twelve_class:
                    try:
                        obj = element.find('a', {'id': True, 'href': True})
                        if obj:
                            attrs = obj.attrs
                            if attrs:
                                links[element.find('span', {'id': True, 'class': True}).text] = attrs['href']
                        else:
                            index[element.find('span', {'id': True, 'class': True}).text] = []
                            eid = element.find('span', {'id': True, 'class': True}).attrs['id'].split('_titleText')[0]
                            items = soup.find_all(lambda tag: tag.name == 'div' and tag.get('onclick') and tag.get('id') and tag.get('id').startswith(eid))
                            for item in items:
                                item_link = item.attrs['onclick'].split('location.href=')[1].strip("'")
                                description = item.find('div', {'class': 'inner_bit_text'}).text.strip()
                                title = item.find('h3', {'class': 'inner_bit_text'}).text.strip()
                                response = requests.get(item_link)
                                temp_soup = BeautifulSoup(response.content, "html.parser")
                                author = temp_soup.find('div', {'class': 'line'}).text.strip()
                                index[element.find('span', {'id': True, 'class': True}).text].append(create_index_entry(title, description, author, item_link))
                    except Exception as e:
                        logging.exception('wow')
                        raise e

                for name, link in links.items():
                    index[name] = []
                    response = requests.get(link)
                    soup = BeautifulSoup(response.content, "html.parser")
                    items = soup.find_all(lambda tag: tag.name == 'div' and tag.get('onclick'))
                    for item in items:
                        item_link = item.attrs['onclick'].split('location.href=')[1].strip("'")
                        description = item.find('div', {'class': 'inner_bit_text'}).text.strip()
                        title = item.find('h3', {'class': 'inner_bit_text'}).text.strip()
                        response = requests.get(item_link)
                        soup = BeautifulSoup(response.content, "html.parser")
                        author = soup.find('div', {'class': 'line'}).text.strip()
                        index[name].append(create_index_entry(title, description, author, item_link))
                all_data[k].update({'index': index})
                logging.info(f' {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")} #{v["מספר גיליון חדש"]} {[f"{e}: {len(l)}" for e, l in v["index"].items()]}')
    except Exception as e:
        logging.exception(str(e))
    finally:
        json_write(ALL_DATA_FILE_PATH, all_data)


def main():
    get_iaf_index()


if __name__ == '__main__':
    main()

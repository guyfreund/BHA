# coding=utf8
from get_metadata import json_write, json_read
import json
import os


HEB_TO_ENG = {
    "כותר": "title",
    "מספר גיליון חדש": "new_issue_number",
    "מספר גיליון": "issue_number",
    "לינק": "issue_link",
    "חודש": "one_month",
    "חודש התחלה": "to_month",
    "חודש סוף": "from_month",
    "שנת הוצאה": "year",
    "הוצאה לאור": "publisher",
    "עורך": "editor",
    "תוכן עניינים": "index_link",
    "מספר עמודים": "number_of_pages"
}


def handle_month(issue):
    metadata = issue.get('metadata')
    month = metadata.get('month', {})
    month_to = month.get('to')
    month_from = month.get('from')
    one_month = metadata.get('one_month')
    to_month = metadata.get('to_month')
    from_month = metadata.get('from_month')
    if month_to == to_month and month_from == from_month and all([month_to, to_month, from_month, month_from]):
        issue['metadata']['month'] = month
    elif month_to == one_month and not month_from and all([month_to, one_month]):
        issue['metadata']['month'] = month
    elif month_to == month_from and month_to == one_month and all([month_to, month_from, one_month]):
        issue['metadata']['month'] = {'to': month_to, 'from': ''}
    elif one_month:
        issue['metadata']['month'] = {'to': one_month, 'from': ''}
    else:
        if month_to and month_from:
            issue['metadata']['month'] = {'to': month_to, 'from': month_from}
        elif to_month and from_month:
            issue['metadata']['month'] = {'to': to_month, 'from': from_month}
    for key in ('one_month', 'to_month', 'from_month'):
        if key in issue:
            del issue[key]
        if key in issue['metadata']:
            del issue['metadata'][key]


def get_old_number(new_number):
    if '-' in new_number:
        small, large = new_number.split('-')
        return f'{int(small) + 101}-{int(large) + 101}'
    else:
        return str(int(new_number) + 101)


def handle_iaf_library():
    iaf_library_data = json_read('iaf_library_data.json')
    for link, data in iaf_library_data.items():
        number = data["מספר גיליון"]
        try:
            issue = json_read(f'schemes/{number}.json')
        except UnicodeDecodeError:
            try:
                with open(f'schemes/{number}.json', 'r', encoding='ISO-8859-8') as f:
                    file_data = f.read()
                    issue = json.loads(file_data)
            except UnicodeDecodeError:
                try:
                    with open(f'schemes/{number}.json', 'r', encoding='cp1255') as f:
                        file_data = f.read()
                        issue = json.loads(file_data)
                except Exception as e:
                    raise e
        if 'metadata' not in issue:
            issue['metadata'] = {}
        for k, v in data.items():
            if k in HEB_TO_ENG:
                issue['metadata'][HEB_TO_ENG[k]] = v
        handle_month(issue)
        json_write(f'database/{number}.json', issue)


def handle_iaf():
    iaf_data = json_read('iaf_data.json')
    for link, data in iaf_data.items():
        old_number = get_old_number(data["מספר גיליון חדש"])
        issue = {'metadata': {'issue_number': old_number, 'publisher': 'חיל האויר'}}
        for k, v in data.items():
            if k == "index":
                index = []
                for _, y in v.items():
                    index += y
                issue["index"] = index
            else:
                issue['metadata'][HEB_TO_ENG.get(k, k)] = v
        handle_month(issue)
        json_write(f'database/{old_number}.json', issue)


def main():
    if not os.path.isdir('database'):
        os.mkdir('database')
    handle_iaf()
    handle_iaf_library()


if __name__ == '__main__':
    main()

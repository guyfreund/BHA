import csv
import json

issue_dict = {}
fieldnames = ['title', 'issue title', 'issue link', 'front page image', 'issue number', 'year', 'month',
              'publisher', 'editor',
              'deputy editor', 'price', 'subscription price',
              'currency', 'photographers', 'number of pages', 'subscription only', 'index link',
              'index:1', 'index:2', 'index:3', 'index:4', 'index:5', 'index:6', 'index:7', 'index:8', 'index:9',
              'index:10', 'index:11', 'index:12', 'index:13', 'index:14', 'index:15'
    , 'index:16', 'index:17', 'index:18', 'index:19', 'index:20', 'index:21', 'index:22', 'index:23'
    , 'index:24', 'index:25', 'index:26', 'index:27', 'index:28', 'index:29', 'index:30', 'index:31'
    , 'index:32', 'index:33', 'index:34', 'index:35', 'index:36', 'index:37', 'index:38', 'index:39',
              'index:40', 'index:41', 'index:42', 'index:43', 'index:44', 'index:45', 'index:46',
              'index:47', 'index:48', 'index:49', 'index:50']


def get_front_images(issue_number):
    with open('iaf_library_data.json', mode='r') as iaf_json:
        json_dict = json.load(iaf_json)
        for k in json_dict.keys():
            if json_dict[k]['issue_number'] in issue_number:
                return json_dict[k]['front_page_image']


def fill_csv(f, issue_number):
    file_data = f.read()
    issue = json.loads(file_data)
    fill_metadata(issue['metadata'])
    if 'front page image' not in issue_dict.keys():
        issue_dict['front page image'] = handle_link(get_front_images(issue_number), 'image')
    if 'index' in issue.keys():
        fill_index(issue['index'])

    writer.writerow(issue_dict)
    issue_dict.clear()


# <a href="http://XXX">XXX</a>
def handle_link(link, title):
    if title in 'image':
        return f'<a href=http://www.{link}>{title}</a>'
    return f'<a href={link}>{title}</a>'


def from_dict_to_str(article):
    ret = ""
    for k, v in article.items():
        if type(v) is str:
            v = v.replace(",", "")
        ret = ret + k + ':' + f'{str(v)}\n'
    return ret


def fill_index(index):
    index_num = 1
    for article in index:
        if (index_num > 50):
            break;
        article = from_dict_to_str(article)
        issue_dict[f'index:{index_num}'] = article
        index_num += 1
    while index_num < 50:
        issue_dict[f'index:{index_num}'] = ""
        index_num += 1


def fill_metadata(issue):
    issue_dict['issue title'] = check_n_get_val(issue, 'title')
    issue_dict['title'] = check_n_get_val(issue, 'title')
    if 'issue_link' in issue.keys():
        issue_dict['issue link'] = handle_link(issue['issue_link'], issue['issue_link'])
    else:
        issue_dict['issue link'] = '-'
    if 'front page image' in issue.keys():
        issue_dict['front page image'] = handle_link(issue['front_page_image'], 'image')
    issue_dict['issue number'] = check_n_get_val(issue, 'issue_number')
    issue_dict['year'] = check_n_get_val(issue, 'year')
    issue_dict['month'] = check_n_get_val(issue, 'month', 'to')
    issue_dict['publisher'] = check_n_get_val(issue, 'publisher')
    issue_dict['editor'] = check_n_get_val(issue, 'editor')
    issue_dict['deputy editor'] = check_n_get_val(issue, 'deputy_editor')
    price = check_n_get_val(issue, 'price', 'amount')
    if type(price) is str:
        issue_dict['price'] = price
    if type(price) is int:
        issue_dict['price'] = str(price) if price > 0 else ""
    price = check_n_get_val(issue, 'subscription_price', 'amount')
    if type(price) is str:
        issue_dict['price'] = price
    if type(price) is int:
        issue_dict['subscription price'] = str(price) if price > 0 else ""
    issue_dict['currency'] = check_n_get_val(issue, 'price', 'type')
    issue_dict['photographers'] = check_n_get_val(issue, 'photographers')
    issue_dict['number of pages'] = check_n_get_val(issue, 'number_of_pages')
    issue_dict['subscription only'] = check_n_get_val(issue, 'subscription_only')
    if 'index_link' in issue.keys():
        issue_dict['index link'] = handle_link(issue['index_link'], 'index')
    else:
        issue_dict['index link'] = '-'


def handle_quotes(val):
    if(type(val) is list):
        val = ','.join(val)
    if(type(val) is str):
        return val.replace('"', '\"')
    return val


def check_n_get_val(issue, field, op_field=None):
    if field in issue.keys():
        if op_field is not None:
            if op_field in issue[field].keys():
                return handle_quotes(issue[field][op_field])
        else:
            return handle_quotes(issue[field])

    return ""


with open('AllDataAsCSV.csv', mode='w', encoding='utf-8') as iaf_file:
    writer = csv.DictWriter(iaf_file, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()

    json_index = 1
    print(json_index)
    while json_index < 350:
        try:
            with open(f'database\\{json_index}.json', 'r', encoding='utf-8', newline='') as f:
                fill_csv(f, str(json_index))
                json_index += 1
        except FileNotFoundError:
            try:
                with open(f'database\\{json_index}-{json_index + 1}.json', 'r', encoding='utf-8') as f:
                    issue_number_str = f'{json_index}-{json_index + 1}'
                    fill_csv(f, issue_number_str)
                    json_index += 2
            except FileNotFoundError:
                json_index += 1
                continue

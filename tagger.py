from get_metadata import json_read, json_write
import time
import os


def handle_month():
    one_month = input("One month? כ/ל ").lower()
    if one_month in ['כ', 'כן']:
        return input("month: "), ""
    else:
        from_month = input("from: ")
        to_month = input("to: ")
        return from_month, to_month


def handle_photographers():
    photographers = []
    photographer = input("photographer: ")
    while photographer:
        photographers.append(photographer)
        photographer = input("photographer: ")
    return photographers


def handle_index():
    index = []
    print("index")
    title = input("title: ")
    description = input("description: ")
    start_page = input("start_page: ")
    if start_page and start_page.isdigit():
        start_page = int(start_page)
    author = input("author: ")
    while any([title, description, start_page, author]):
        index.append({
            "title": title,
            "description": description,
            "start_page": start_page,
            "author": author
        })
        title = input("title: ")
        description = input("description: ")
        start_page = input("start_page: ")
        if start_page and start_page.isdigit():
            start_page = int(start_page)
        author = input("author: ")
    return index


def handle_subscription_only():
    ans = input("subscription only? כ/ל").lower()
    if ans in ['כ', 'כן']:
        return True
    return False


def handle_price():
    amount = input("amount: ")
    if amount:
        amount = float(amount)
    coin_type = input("type: ")
    return amount, coin_type


def main():
    start = time.time()
    scheme = json_read("scheme.json")
    issue = {"metadata": {}, "index": {}}

    try:
        for field in scheme["metadata"]:
            if field == "month":
                from_month, to_month = handle_month()
                issue["metadata"]["month"] = {"from": from_month, "to": to_month}
            elif field == "price":
                print("price")
                amount, coin_type = handle_price()
                issue["metadata"]["price"] = {"amount": amount, "type": coin_type}
            elif field == "photographers":
                issue["metadata"]["photographers"] = handle_photographers()
            elif field == "subscription_price":
                print("subscription_price")
                amount, coin_type = handle_price()
                issue["metadata"]["subscription_price"] = {"amount": amount, "type": coin_type}
            elif field == "number_of_pages":
                num = input("number_of_pages: ")
                if num and num.isdigit():
                    num = int(num)
                issue["metadata"]["number_of_pages"] = num
            elif field == "subscription_only":
                issue["metadata"]["subscription_only"] = handle_subscription_only()
            else:
                issue["metadata"][field] = input(f"{field}: ")

        issue["index"] = handle_index()

    except Exception as e:
        raise e
    finally:
        end = time.time()
        json_write(os.path.join("schemes", f"{issue['metadata']['issue_number']}.json"), issue)
        print(f"{(end - start) / 60} minutes")


if __name__ == "__main__":
    main()

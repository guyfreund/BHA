from get_metadata import json_read, json_write
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
    start_page = int(input("start_page: "))
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
        start_page = int(input("start_page: "))
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
    type = input("type: ")
    return amount, type


def main():
    scheme = json_read("scheme.json")
    issue = {}

    try:
        for field in scheme["metadata"]:
            if field == "month":
                from_month, to_month = handle_month()
                scheme["metadata"]["month"] = {"from": from_month, "to": to_month}
            elif field == "price":
                print("price")
                amount, coin_type = handle_price()
                scheme["metadata"]["price"] = {"amount": amount, "type": coin_type}
            elif field == "photographers":
                scheme["metadata"]["photographers"] = handle_photographers()
            elif field == "subscription_price":
                print("subscription_price")
                amount, coin_type = handle_price()
                scheme["metadata"]["subscription_price"] = {"amount": amount, "type": coin_type}
            elif field == "number_of_pages":
                num = input("number_of_pages: ")
                if num and num.isdigit():
                    num = int(num)
                scheme["metadata"]["number_of_pages"] = num
            elif field == "subscription_only":
                scheme["metadata"]["subscription_only"] = handle_subscription_only()
            else:
                scheme["metadata"][field] = input(f"{field}: ")

        scheme["index"] = handle_index()

    except Exception as e:
        raise e
    finally:
        json_write(os.path.join("schemes", f"{issue['issue_number'].json}"), issue)


if __name__ == "__main__":
    main()

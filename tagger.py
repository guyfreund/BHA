from get_metadata import json_read, json_write
import os


def handle_month():
    one_month = input("One month? Y/N ").lower()
    if one_month:
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


def main():
    scheme = json_read("scheme.json")
    issue = {}

    for field in scheme["metadata"]:
        if field == "month":
            from_month, to_month = handle_month()
            scheme["metadata"]["month"] = {"from": from_month, "to": to_month}
        elif field == "price":
            scheme["metadata"]["price"] = {"amount": float(input("amount: ")), "type": input("type: ")}
        elif field == "photographers":
            scheme["metadata"]["photographers"] = handle_photographers()
        elif field == "subscription_price":
            scheme["metadata"]["subscription_price"] = {"amount": float(input("amount: ")), "type": input("type: ")}
        elif field == "number_of_pages":
            scheme["metadata"]["number_of_pages"] = int(input("number_of_pages: "))
        else:
            scheme["metadata"][field] = input(f"{field}: ")

    scheme["index"] = handle_index()

    json_write(os.path.join("schemes", f"{issue['issue_number'].json}"), issue)


if __name__ == "__main__":
    main()

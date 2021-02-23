from get_metadata import json_read, json_write
import os


def handle_month():
    one_month = input("\nOne month? Y/N ").lower()
    if one_month:
        return input("\nmonth: "), ""
    else:
        from_month = input("\nfrom: ")
        to_month = input("\nto: ")
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

    for field in scheme:
        if field == "month":
            from_month, to_month = handle_month()
            scheme["month"] = {"from": from_month, "to": to_month}
        elif field == "price":
            scheme["price"] = {"amount": float(input("\namount: ")), "type": input("\ntype: ")}
        elif field == "photographers":
            scheme["photographers"] = handle_photographers()
        elif field == "subscription_price":
            scheme["subscription_price"] = {"amount": float(input("\namount: ")), "type": input("\ntype: ")}
        elif field == "index":
            scheme["index"] = handle_index()
        elif field == "number_of_pages":
            scheme["number_of_pages"] = int(input("number_of_pages: "))
        else:
            scheme[field] = input(f"{field}: ")

    json_write(os.path.join("schemes", f"{issue['issue_number'].json}"), issue)


if __name__ == "__main__":
    main()

"""
module for handling menu data
"""

from tabulate import tabulate

pages = {
    "page_1": {
        "Kow Ladna": 17.00,
        "Lemon Chicken": 20.00,
        "Pad Cashew": 17.00,
        "Pad Pak": 17.00,
        "Pad Tofu": 17.00,
        "Pad Ped": 17.00,
        "Pad Prik King": 17.00,
        "Salt & Pepper Shrimp": 17.00,
        "Pad Thai": 15.00,
        "Pad See Iew": 15.00,
    },
    "page_2": {
        "Seafood Curry": 20.00,
        "Gang Panang": 16.00,
        "Pineapple Curry": 16.00,
        "Eggplant Curry": 17.00,
        "Red Curry": 17.00,
        "Green Curry": 16.00,
        "Yellow Curry": 16.00,
        "Khảo Soi": 17.00,
    },
    "page_3": {
        "Bibimbap": 18.00,
        "Bulgogi": 20.00,
        "Kalbi": 25.00,
        "Korean Spicy Pork": 20.00,
        "Kimchi Jigae": 18.00,
        "Ginseng Chicken Soup": 23.00,
        "Bulgogi Tang": 38.00,
    },
    "page_4": {
        "Soft Drink": 3.00,
        "Thai Iced Tea": 5.00,
        "Thai Iced Coffee": 5.00,
        "Bubble Tea": 5.00,
        "Shirley Temple": 5.00,
        "Orange Juice": 4.00,
        "Milk": 4.00,
        "Coffee": 3.00,
        "Green Tea": 4.00,
        "Ginseng Tea": 4.00,
    },
    "page_5": {
        "Banana Cheesecake": 4.00,
        "Coconut Ice Cream": 4.00,
        "Mango Sticky Rice": 10.00,
    },
}


def order(dish_name):
    """
    Writes to a file called order.txt to save what the user has ordered,
    this will be used for a function that computes the total check.
    """
    for page in pages:
        for dish, price in pages[page].items():
            if dish_name == dish.lower() or dish_name == dish:
                with open("order.txt", "a") as order:
                    order.write(f"{dish}|{price:.2f}\n")
                print(f"\n{dish} sucessfully added to your order ✅\n")
                match = True
            else:
                continue

    try:
        if not match:
            print("\nINVALID DISH NAME ❎\n")
    except UnboundLocalError:
        print("\nINVALID DISH NAME ❎\n")


def total():
    """
    Reads from order.txt and prints out a table of what the user has ordered
    with a total that includes the sum of all dishes + tax.
    """
    total = 0
    headers = ["Order", "Price"]
    table = []
    with open("order.txt", "r") as order:
        for line in order:
            item = line.rstrip().split("|")
            total += float(item[1])
            item[1] = f"${item[1]}"
            table.append(item)
    tax = total * 0.07
    total_tax = ["Tax", f"${tax:.2f}"]
    total_items = ["Total", f"${(total + tax):.2f}"]
    table.append(total_tax)
    table.append(total_items)
    return tabulate(table, headers, tablefmt="rounded_outline")


def page(num_page):
    """
    Prints out user's desired menu page
    """
    match num_page:
        case "1":
            headers = ["Entrée¹/⁵", "Price"]
            table = [
                [entrée, f"${price:.2f}"] for entrée, price in pages["page_1"].items()
            ]
        case "2":
            headers = ["Curries²/⁵", "Price"]
            table = [
                [curry, f"${price:.2f}"] for curry, price in pages["page_2"].items()
            ]
        case "3":
            headers = ["Korean³/⁵", "Price"]
            table = [[dish, f"${price:.2f}"] for dish, price in pages["page_3"].items()]
        case "4":
            headers = ["Beverages⁴/⁵", "Price"]
            table = [
                [beverage, f"${price:.2f}"]
                for beverage, price in pages["page_4"].items()
            ]
        case "5":
            headers = ["Desserts⁵/⁵", "Price"]
            table = [
                [dessert, f"${price:.2f}"] for dessert, price in pages["page_5"].items()
            ]
        case _:
            headers = ["invalid", "invalid"]
            table = ["invalid", "invalid"]
    return tabulate(table, headers, tablefmt="rounded_outline")

def main():
    user_input = input()
    page(user_input)
    order(user_input)
    print(total())

if __name__ == "__main__":
    main()

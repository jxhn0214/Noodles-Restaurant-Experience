"""
Progam that emulates an ordering experience at a local restaurant. Solidifying
python/programming concepts like list comprehensions, function definitions, dictionaries,
lists, error handling, read/write from/to files, importing modules/api, and etc.
"""

import menu
from tabulate import tabulate


def main():
    page_list = ["1", "2", "3", "4", "5"]
    print(
        "CONTROLS:\n"
        "• Enter a page number to traverse to\n"
        "• Enter a dish name to order\n"
        "• Enter, 'Done!' to finish ordering\n"
    )
    print(menu.page("1"))
    while True:
        user_input = input(":").strip()
        if user_input == "Done!":
            break
        elif user_input in page_list:
            print(menu.page(user_input))
        else:
            menu.order(user_input)
    print(menu.total())

    with open("order.txt", "w") as order:  # clear order
        order.write("")


main()

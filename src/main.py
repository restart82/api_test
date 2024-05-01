from config import *
from tasks import *

# print(DEVICE_NUMBER)
# add_device()
# delete_device()
# get_device_list()
# update_device()

main_menu = "1. Add devices\n" \
    "2. Get devices list\n" \
    "3. Update devices\n" \
    "4. Delete devices\n" \
    "5. Exit\n"


def ui():
    print(main_menu)
    command = input(" >>")
    match command:
        case '1':
            print("POST")
        case '2':
            print("GET")
        case '3':
            print("PUT")
        case '4':
            print("DELETE")
        case '5':
            exit()
        case _:
            print("command not correct")
    while True:
        if input("print 'c' to continue >>") == 'c':
            break
    print("\n")


while True:
    ui()


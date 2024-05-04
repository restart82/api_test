from tasks import *

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
            for i in range(DEVICE_NUMBER):
                add_device(dev_id_list[i], name_list[i])
        case '2':
            print("GET")
            get_device_list()
        case '3':
            print("PUT")
            for i in range(DEVICE_NUMBER):
                update_device(dev_id_list[i], name_list_v2[i])
        case '4':
            print("DELETE")
            for i in range(DEVICE_NUMBER):
                delete_device(dev_id_list[i])
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


def enter_info(list_of_info):
        info = input("Введите любые данные: ")
        list_of_info.append(info)

def get_info(list_of_info):
    print(f"Ваш список данных: {list_of_info}")

def main():
    list_of_info=[]
    enter_info(list_of_info)
    get_info(list_of_info)
main()
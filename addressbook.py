class Contact:
    def __init__(self,name,phone,email,addr):
        self.name = name
        self.phone = phone
        self.email = email
        self.addr = addr

    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)


def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

def set_contact():
    name = input("Name  : ")
    phone = input("PH   : ")
    email = input("Email: ")
    addr = input("Addr  : ")
    contact = Contact(name,phone,email,addr)
    return contact

def delete_contact(contact_list,name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]

def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")
    return int(menu)

def run():
    contact_list = []
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            name = input("Delete Name : ")
            delete_contact(contact_list, name)
        elif menu == 4:
            break
        else:
            print("Error")

if __name__ = "__main__":
    run()
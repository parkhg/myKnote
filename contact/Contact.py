# encoding = UTF-8

"""
    연락처 관리 프로그램

    2020.08.20
    --------------------------------------------
    1. class 이용
    2. Console Menu
    3. Menu별 함수처리
    4. file load and file save
"""


# Class
class Contact:
    def __init__(self, name, phoneno, email, addr):
        self.name = name
        self.phoneno = phoneno
        self.email = email
        self.addr = addr

    def print_info(self):
        print("Name : ", self.name)
        print("Phone : ", self.phoneno)
        print("EMail : ", self.email)
        print("Address :", self.addr)


# 1.연락처 입력
def set_contact():
    name = input("Name : ")
    phone = input("Phone : ")
    email = input("Email : ")
    addr = input("Address : ")
    # print(name, phone, email, addr)
    # Class에 저장
    contact = Contact(name, phone, email, addr)
    return contact


# 2.연락처 출력
def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()


# 3.연락처 삭제
def delete_contact(contact_list, name):
    # 반복문 사용 시 몇 번째 반복문인지 확인에 사용하며, 인덱스 번호와 컬렉션의 원소를 tuple 형태로 반환
    for i, contact in enumerate(contact_list):
        print("index : {}, value : {}".format(i, contact.name))
        if contact.name == name:
            del contact_list[i]


# 4.저장 후 종료
def save_contact(contact_list):
    fp = open("contact_db.txt", "wt")
    for contact in contact_list:
        fp.write(contact.name + '\n')
        fp.write(contact.phoneno + '\n')
        fp.write(contact.email + '\n')
        fp.write(contact.addr + '\n')
    fp.close()


# 0. Open File Data
def load_contact(contact_list):
    fp = open("contact_db.txt", "rt")
    lines = fp.readlines()
    print(lines)

    # data record : 4개
    num = len(lines) / 4
    num = int(num)

    for i in range(num):
        # rstrip : 인자로 전달된 문자를 String의 왼쪽에서 제거합니다
        name = lines[4*i+0].rstrip("\n")
        phoneno = lines[4*i+1].rstrip("\n")
        email = lines[4*i+2].rstrip("\n")
        addr = lines[4*i+3].rstrip("\n")

        # class 이용하여 저장
        contact = Contact(name, phoneno, email, addr)
        contact_list.append(contact)

    # file close
    fp.close()

# -------------------------------------------------
# Menu Display
# -------------------------------------------------
def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택 : ")
    return int(menu)


def run():
    # print("Contact Run")
    # name_card = Contact("PHG", '010.3360.5717', 'parkhg@gmail.com', '전주시')
    # name_card.print_info()
    # set_contact()

    # 연락처 저장 리스트
    contact_list = []
    # 기존 저장된 연락처 load
    load_contact(contact_list)

    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)

        elif menu == 2:
            print_contact(contact_list)

        elif menu == 3:
            name = input("Name : ")
            delete_contact(contact_list, name)

        elif menu == 4:
            save_contact(contact_list)
            break

        else:
            pass


if __name__ == '__main__':
    run()

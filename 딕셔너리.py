# 딕셔너리
# 리스트와 튜플에서는 정수인 인덱스를 가지고 순차적으로 각 요소에 접근할 수 있었다면, 딕셔너리는 단어의 뜻 그대로
# ‘사전'과 같이 별도의 키를 통해 각 요소를 접근 할 수 있도록 만들어진 데이터 타입 입니다. * c++ 및 자바에서는 Map이라고 부름

#선언
# menu = {"coffe":2000, "tea":1500,"cake":2000}
# print(menu)
# print(menu["coffe"])
# print(menu.get("tea")) # get함수를 통해 값을 확인 할 수 있다.
"""------------------------------------------------------------------------------------------------"""


from aext_panels_server.exceptions import FileNotFound

# 값 추가 및 삭제, 키 존재 여부 확인
# 추가 : 딕셔너리[키] = 값 새로운 키와 값을 추가 할 수 있습니다.
# menu["milk"]=2000

# 삭제: del 딕셔너리[키] 형식으로 써 주면 됩니다.
# del menu["tea"]

# 키존재 여부 확인 :  if 키 in 딕셔너리KEY 입니다.
# if "tea" in menu:

# 키로 값 확인 : 딕셔너리[키]  또는 딕셔너리.get(키)
# print(menu["tea"])
# print(menu.get("coffe"))


# 딕셔너리의 데이터를 한꺼번에 바꿀 때 , 딕셔너리에 한버에 추가해 줄때
# update 함수 사용
# menu.update({"coffe":4000,"tea":2000,"cake":4000})
# menu.update({"A":2000,"B":4000,"c":1000})
# print(menu)

"""------------------------------------------------------------------------------------------------"""

#정보얻기
# keys(), values(), items() 함수의 반환값으로 딕셔녀리의 정보를 확인 할 수 있습니다.

# 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
# print(menu.keys()) # 리스트로 반환
# print(menu.values()) # 리스트로 반환
# print(menu.items()) # 딕셔너리 키와 값을 모두 반환
# print("coffe" in menu) # True 로 반환

# for 반복문 사용하기
# for key in menu:
#      print(key, ":", menu[key])

# 문제
# [1] 메뉴보기 [2] 메뉴조회 [3]메뉴추가 [4]메뉴 삭제 [5]종료
#카테고리별로 조회 추가
# def k (a):
#
#    for key, value in menu.items():
#        if a ==value[0]:
#            print(key,value[0],value[1],value[2])
#
# import json
#
# menu = {
#     "americano": ["Coffee", 2000, "기본 커피 입니다."],
#     "Espresso": ["Coffee", 2500, "진한 커피 입니다."],
#     "Latte": ["Coffee", 4000, "우유가 들어 있는 커피 입니다."],
#     "ColdBrew": ["Coffee", 4500, "연유가 들어 있는 커피 입니다."],
#     "GreenTea": ["Tea", 4500, "녹차 입니다."],
#     "BlackTea": ["Tea", 4500, "홍차 입니다."],
#     "MilkTea": ["Tea", 4000, "우유가 포함된 차 입니다."],
#     "PeachAde": ["Ade", 5000, "복숭아 에이드 입니다."],
#     "GreenAde": ["Ade", 5000, "포도 에이드 입니다."],
#     "LemonAde": ["Ade", 4500, "레몬 에이드 입니다."]
# }
# file_name = "menu.json"
#
# def load_menu():
#     global menu
#     try:
#         with open(file_name, "r", encoding="utf-8") as file:
#             menu = json.load(file)
#     except FileNotFoundError:
#         print("해당하는 파일이 없습니다.")
#     except json.JSONDecodeError:
#         print("JSON 디코딩 실패.")
#
# def save_menu():
#     with open(file_name, "w", encoding="utf-8") as file:
#         json.dump(menu, file, ensure_ascii=False, indent=4)
#
# def print_menu():  # 메뉴 조회
#     for key in menu:
#         print(f"{key}: {menu[key][1]}")  # Display only price
#
# def get_menu(key):  # 메뉴 정보 조회
#     if key in menu:
#         print(menu[key])
#     else:
#         print("찾는 메뉴가 없습니다.")
#
# def add_menu(key, category, price, desc):  # 메뉴 추가
#     if key not in menu:
#         menu[key] = [category, price, desc]
#         print(f"{key} 메뉴가 추가 되었습니다.")
#     else:
#         print("메뉴가 이미 존재 합니다.")
#
# def del_menu(name):
#     if name in menu:
#         del menu[name]
#         print(f"{name} 메뉴가 삭제 되었습니다.")
#     else:
#         print("삭제 할 메뉴가 없습니다.")
#
# while True:
#     print("메뉴를 선택 하세요 : ")
#     sel = input("[1] 메뉴 보기 [2] 메뉴 조회 [3] 메뉴 추가 [4] 메뉴 삭제 [5] 저장 및 종료 [6] 종료하기 [7] : ")
#     if sel == "1":
#         print_menu()
#     elif sel == "2":
#         name = input("조회 할 메뉴를 입력 하세요 : ")
#         get_menu(name)
#     elif sel == "3":
#         name = input("추가 할 메뉴를 입력 하세요 : ")
#         cate = input("카테고리 입력 : ")
#         price = int(input("가격 입력 : "))
#         desc = input("제품 설명 : ")
#         add_menu(name, cate, price, desc)
#     elif sel == "4":
#         name = input("삭제할 메뉴를 입력 하세요 : ")
#         del_menu(name)
#     elif sel == "5":
#         save_menu()
#         break
#     elif sel == "6":
#         load_menu()
#         break
#     elif sel == "7":
#         b = input("카테고리를 입력하세요")
#         k(b)
#     else:
#         print("잘못 된 입력 입니다. 다시 시도하세요.")

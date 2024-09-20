# 함수로 영화표 예매하기
# 사용자로 부터 좌석번호를 입력받아 예매하는 시스템, 좌석은 10개
# 예매가 완료되면 해당 좌석값을 1로변경 (초기값은 0)
# 이미 예매가 완료된 좌석은 재구매 불가
# 좌석당 가격은 12000원
# 프로그램 종료 시 매출액 출력

# seat = [0]*10 #0으로 최기화 된 10개의 리스트 생성
# price = 12000
#
# def print_seat():
#     for e in seat :
#         if e == 0 :
#             print("[]", end=" ")
#         else :
#             print("[v]", end="")
#     print()
# def select_seat():
#     print_seat()
#     num = int(input("좌석 번호를 입력하세요:")) -1
#     if seat[num] == 0 :
#         seat[num] = 1
#         print("예약이 완료되었습니다")
#         print_seat()
#     else:
#         print("이미 예약한 좌석입니다.")
# def total_acoount():
#     cnt = 0
#     for e in seat :
#         if e==1 :
#             cnt +=1
#     return  price*cnt
# while True :
#     print("[1] 예매하기 ")
#     print("[2] 종료하기 ")
#     sel = int(input("메뉴선택: "))
#     if sel == 1: select_seat()
#
#     else: print(f"총매출액: {total_acoount()}" )
def second_num(ls, n):
    cnt = 0
    for i in range(len(ls)):
        if ls[i] == n:
            if cnt > 0 : return i+1
            else: cnt += 1
    return -1

ls = list(map(int, input("리스트 입력 : ").split()))
n = int(input("찾는 숫자 : "))
print(second_num(ls, n))



# 내장함수 : 원래 제공되는 것, import 필요 없음
# input(): 사용자로부터 입력을 받는 함수입니다.
# int(): 정수로 형변환을 해주는 함수입니다.
# range(): 순차적인 정수를 생성하는 함수입니다.
# len(): 컨테이너(문자열, 리스트 등)의 길이를 반환하는 함수입니다.
# print(): 값을 출력하는 함수입니다.
# sum(): 숫자들의 합을 계산하는 함수입니다
# sorted(): 순서가 있는 자료형을 정렬하는 함수입니다.
# max(), min(): 최댓값과 최솟값을 반환하는 함수입니다.
from tarfile import version

from dask.array.linalg import solve_triangular
from dask.array.random import random
from numpy.matrixlib.defmatrix import matrix

# print(max(1,2,3,4,0))# 매개변수사용
# print(max([1,3,4,5,5,6])) # 리스트 사용
# print(min (1,2,3,4,0))
# print(min([1,3,4,5,5,6]))

# 시퀀스 자료형의 값을 모두  더 해줌
# print(sum([1,4,5,6,2,3]))# 리스트일 경우만 동작
# print(sum[1,3,5,6,7])/5) # 평균

# 몫과 나머지를 반환#(언패킹)튜플 형태로 반환(여러개의 값을 반환 받을 수 있음)
# print(divmod(sum ([1,2,3,4,5]),5)
"""------------------------------------------------------------------------------------------------"""
# 정렬
# a = [1,23,52,32,64,23,75,12]
# print(sorted(a))# 오름차순

# print(sorted(a, reverse=True)) # 내림차순
"""------------------------------------------------------------------------------------------------"""
# 실습
# 입력 받은 값에서 제일 큰값
# 입력 받은 값에서 제일 작은 값
# 총점, 평균
# n= list(map(int, input(" 정수를 입력하세요 ").split()))
#
# print( max(n))
# print(min(n))
# print(sum(n))
# print(sum(n)/len(n))
# print(divmod(sum(n),len(n)))

# 중첩 리스트(2차원 배열과 동일 합니다.)
# a=[[1,2,3,4],["A","B","C"]]
# print(matrix[0])
# print(matrix[0][2])

"""------------------------------------------------------------------------------------------------"""
# 외장함수
# import 해서 사용하는 함수, 파이썬에서 기본적으로 제공하는 것

#외부 모듈(pip를 통해 다운로드 받아야함)
# pip install
# pip list
# pip #version

#랜덤 함수 : 지정한 범위내에서 임의의 숫자를 만들어 내는 것
# import random
# a= random.randint(1, 56) # 1~56 이하
# a= random.randrange(1,56) # 1~56 미만
# print(a)

# 날짜 및 시간 관련 처리 모듈

# from datetime import datetime # 내부에서 datetime함수를 가져 옴.
# datetime.today()  #현재 날짜 가져오기
# datetime.today().year #현재 연도 가져오기
# datetime.today().month #현재 월 가져오기
# datetime.today().day    #현재 일 가져오기
# datetime.today().hour   ## 현재 시간 가져오기
#
# print(datetime.today().month)
# print(datetime.today().day)
# print(datetime.today().hour)
# print(datetime.today().minute)
# print(datetime.today().second)

# math 모듈 : 수학과 관련 기능을 처리 할 때 사용







#-*-coding:utf-8

# 변수
# c나 java와 같은 다른 언어와 달리 변수 선언 시 자료형을 입력할 필요가 없음
# C#과 javascript에는 var타입이 존재함
# php에는 변수 선언시 $로 통일함
# 위의 언어들은 모두 값의 자료형을 자동으로 유추함

# 파이썬은 변수 선언 시 자료형을 입력하지 않음
# 파이썬은 모든 데이터형이 모두 객체형임
# 파이썬은 자바와 달리 모든 자료형이 참조형임

# 자바에서의 값타입과 참조타입의 차이점
# int num1 = 100;
# int num2 = 100;

# String java1 = "자바";
# String java2 = new String("자바");

# if(java1 == java2) //false

# 모든 자료형이 참조형이기 때문에 참조하는 곳이 같은지 확인하는 is 명령어를 사용하여 확인함
# 값을 확인해도 동일함
import sys

a = 3
b = 3
print("a와 b가 참조하는 곳은 같다. : {0}".format(a is b))

if (a == b):
    print("a와 b가 참조하는 곳은 같다.")
else:
    print("a와 b가 참조하는 곳은 다르다.")

c = 3
print(sys.getrefcount(3))
d = 3
print(sys.getrefcount(3))
e = 3
print(sys.getrefcount(3))
f = 3
print(sys.getrefcount(3))

# 변수 선언의 여러가지 방법
# 두개의 변수과 두개의 값을 동시에 선언하고 순서대로 대입
a, b = ("python", "life")
print("변수 a의 값 : {0}".format(a))
print("변수 b의 값 : {0}".format(b))

# String java1 = "자바"; //자바의 기본 변수 선언
# String java1, java2 = "자바"; //자바에서 동시에 2개 변수 선언

# 변수를 튜플 형태로 선언한 뒤 값도 튜플 형태로 대입함
# 튜플은 괄호를 임력하지 않아도 튜플로 인식함
print()
(a, b) = "python", "life"
print("변수 a의 값 : {0}".format(a))
print("변수 b의 값 : {0}".format(b))
# 변수를 리스트 형태로 선언하고 값도 리스트 형태로 대입함
print()
[a, b] = "python", "life"
print("변수 a의 값 : {0}".format(a))
print("변수 b의 값 : {0}".format(b))
# 변수를 2개 이상 선언하고 하나의 값으로 대입
print()
a = b = "python"
print("변수 a의 값 : {0}".format(a))
print("변수 b의 값 : {0}".format(b))
# 변수의 값 스와핑
# 파이썬은 두 변수의 값을 서러의 값으로 대입할때 같은 함수를 만들 필요가 없음
# a = 10
# b = 20
# temp = 0

# temp = a
# a = b # a = 20
# b = temp # b = 20

a = 3
b = 5
a, b = b, a
print("변수 a의 값 : {0}\n변수 b의 값 : {1} ".format(a, b))

# 변수 삭제 하기
# del() 메모리에서 해당 변수 삭제
print()
a = 3
b = 5
print("변수 a의 값 : {0} ".format(a))
print("변수 b의 값 : {0} ".format(b))
print("a의 참조 카운트 : {0}".format(sys.getrefcount(a)))
print("b의 참조 카운트 : {0}".format(sys.getrefcount(b)))
del (a)
del (b)
# del 함수를 사용하여 변수 a와b 를 삭제하여 변수 a,b를 더이상 사용할수 없음
# print("del 사용 후 a의 참조 카운트 : {0}".format(sys.getrefcount(a)))
# print("del 사용 후 b의 참조 카운트 : {0}".format(sys.getrefcount(b)))

# 리스트 복사
# 리스트를 복사하는 일반적인 방법은 반복문을 사용하여 리스트의 내용을 다른 리스트에 대입하는 방법

# 반복문을 사용하여 리스트 복사
a = [1, 2, 3]
print("원본 리스트 출력 : {0}".format(a))
b = a
# 변수 b에 리스트 a를 대입
# 변수 b에 리스트 값 [1, 2, 3]이 대입된 것이 아니라 변수 b에 리스트 a의 주소가 대입됨
print("리스트 b 출력 : {0}".format(b))
# 리스트 a의 index 2의 값 수정 
a[2] = 10
print("리스트 a의 수정후 출력 : {0}".format(a))
# 리스트 b의 요소를 수정하지 않았으나 리스트 a와 같이 값이 수정됨
# 변수 b에 리스트 a의 주소가 대입 되었기에 리스트a의 요소가 수정되면 b의 요소도 수정 된것 처럼 보임
# 동일한 주소를 참조하고 있기 때문
print("리스트 b 출력 : {0}".format(b))

print("a와 b는 같다 : {0}".format(a is b))

# 다른 언어에서 복사 함수를 사용하지 않고 배열이나 리스트를 다른 리스트로 복사하는 방법
count = 0
c = []
while (count < len(a)):
    c.append(a[count])
    count += 1

print("리스트 c 출력 : {0}".format(c))
a[2] = 100
print("리스트 a 출력 : {0}".format(a))
print("리스트 b 출력 : {0}".format(b))
print("리스트 c 출력 : {0}".format(c))

print()
a = [1, 2, 3]
b = a[:]
print("리스트 a 출력 : {0}".format(a))
print("리스트 b 출력 : {0}".format(b))
a[2] = 100
print("수정 후 리스트 a 출력 : {0}".format(a))
print("수정 후 리스트 b 출력 : {0}".format(b))
print("a와 c는 같다 : {0}".format(a is c))

print()

from copy import copy
a = [1, 2, 3]
b = copy(a)
print("리스트 a 출력 : {0}".format(a))
print("리스트 b 출력 : {0}".format(b))

# 연습문제
print()
print("연습문제")
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:14]
print(yyyymmdd)
print(num)

print()
pin = "881120-1068234"
print(pin[7])

print()
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

print()
a = ["Life", "is", "too", "short"]
result = " ".join(a)
print(result)

print()
a = (1, 2, 3)
a = a + (4,)
print(a)

print()
a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print(a)
print(result)

print()
a = {1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5}
aSet = set(a)
b = list(aSet)
print(b)

print()
a = b = [1, 2, 3]
a[1] = 4
print(b)
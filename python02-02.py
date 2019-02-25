# 문자열 사용하기
# 파이썬은 문자 타입과 문자열 타입의 구분이 없음!
# 문자열은 ""로 감싼 문자는 모두 문자열로 표현
# 문자열로 표시 문자 " ", ' ',""" """,''' ''' 총 4개의 타입이 존재!

print("문자열 출력하기")
print("\" 를 통해서 문자열 출력")
print('\' 를 통해서 문자열 출력')

str = """ 쌍따옴표를 3개 사용하는 방식은 입력하는 그대로 
화면에 출력하기 위함"""
print(str)

str = ''' 홀따옴표를 3개 사용하는 방식은 입력하는 그대로 
화면에 출력하기 위함'''
print(str)

# 문자열 사용시 이스케이프 문자 사용 가능!
# \n : 문자열 안에서 줄바꿈을 실행
# \t : 문자열 안에서 tap 키를 누른 효과
# \a : 컴퓨터에서 알람 효과
# \b : 백 스페이스 효과
# \" : 문자열 안에서 문자로서의 "를 출력 
# \' : 문자열 안에서 문자로서의 '를 출력
# \\ : 문자열 안에서 문자로서의 \를 출력
# 000 : 널 문자

multiline = "Life is too short\nYou need python"
print(multiline)
multiline = "Life is too short\fYou need python"
print(multiline)

# 문자열 연산
# 파이썬은 다른 언어와 달리 여러가지 연산자를 지원함
# +, *
# + : 다른 언어와 같은 기능을 하는 연산자로 문자열끼리 연결시켜 하나의 문자열로 만듬
# * : 다른 언어에는 없는 기능으로 문자열을 반복해서 출력할 수 있는 기능을 지원함

head = "python"
tail = " is fun!!"
print(head + tail)

a = "python "
print(a * 2)

print("=" * 50)
print("My program")
print("=" * 50)

# 문자열 인덱싱
# 문자열은 문자 타입의 배열과 같다
# 시작 인덱스는 0임
# 해당하는 위치의 인덱스 번호를 사용하면 그 위치의 문자를 알수 있다.
# 자바에서 배열의 사용하듯이 파이썬에서도 사용할 수 있음
# a = "my first python program!!"
# 위와 같은 문자열이 있을 경우 y를 출력하고 싶은 경우 배열처럼 변수명[index] 로 사용함
# a[10]

a = "my first python program!!"
print(a[10])
print(a[0:10])
print(a[9:15])
# 파이썬에서 문자열 처리 시 특정 위치의 글자르 ㄹ출력할 때 엑셀에서 특정 셀 범위 설정하는 방법과 같이 사용이 가능함.
# a[시작번호 :  끝번호]
# a[0:10]
# 문자열 변수 a에서 엔덱스 번호 0~10까지의 문자를 출력함
# java에서는 Substring, split이라는 메서드를 사용하여 문자열을 잘라서 특정 위치의 문자열을 가지고 와야 하지만 파이썬에서는 문자 슬라이싱을 통해서 쉽게 구현이 가능하다

# 문자열 슬라이싱 시 시작번호나 끝 번호를 입력하지 않으면 처음부터 끝번호까지 출력하거나, 시작번호부터 끝까지 출력함
print(a[15:])
print(a[:15])

#변수와 함께 사용 시 원하는 부분의 글자면 변수에 저장이 가능함

b = a[:15]
c = a[15:]
d = a[9:15]
print(b)
print(c)
print(d)

print("=" * 100)
print()

# 문자열 포매팅
# 문자열을 화면에 출력할때 문자열 포맷을 통하여 사용자가 원하는 형태로 출력할 수 있음
# 문자열 포맷 코드
# %s : 문자열 출력
# %c : 문자 1개 출력
# %d : 정수 출력
# %f : 실수 출력
# %o : 8진수 출력
# %x : 16진수 출력
# %% : 문자 % 출력

# %s 는 해당 위치에 문자열을 출력함
# 어떠한 타입의 값도 모두 문자열로 출력함!

print("I have %d apples" % 3)#정수인 3을 %d에 대입
print("I have %s apples" % 3)#정수인 3 을 문자열로 %s에 대입
print("rate is %f apples" % 3.14)#실수인 3을 %f에 대입
print("rate is %s apples" % 3.14)  #실수인 3.14 을 문자열로 %s에 대입
# 문자열에 %문자를 출력할 경우 %%를 두번 친다
print("Error is %d%%." % 98)

# 문자열 출력 코드 %s에 총 문자열의 크기를 입력하여 표시하면 입력한 문자열의 크기만큼 글자가 입력됨
# - 부하가 있을경우 왼쪽 정렬, 없을경우 오른쪽 정렬
print("%10s jane" % "hi!")
print("%-10s jane" % "hi!")
# 숫자형에도 %와 기호 사이에 범위 숫자를 입력하면 그 길이만큼 자리를 확보함
print("%0.4f" % 3.42134234)
print("%10.4f" % 3.42134234)

print("%4d" % 10)

# 파이썬 문자열 함수
# count() : 문자 개수 확인
# len() : 문자열의 길이
# find() : 문자 위치 확인
# join() : 문자 삽입
# upper() : 소문자를 대문자로 바꾸기
# lower() : 대문자를 소문자로 바꾸기
# strip() : 문자열 양쪽공백 삭제하기
# reprace() : 문자열 변경하기
# split() : 문자열 나누기

a = "hobby"
print("변수 b의 개수는 : %s" % a.count('b'))
print("변수 b의 길이는 : %s" % len(a))

a = "python is best choice"
print("문자 'b' 가 처음 나온 위치는 : %s" % a.find('b'))

#2019 - 02 - 25 수업내용

a = ","
print(a.join('abcd'))

a = "hi"
print("영문 대문자로 출력 : %s " % a.upper())

a = "HI"
print("영문 소문자로 출력 : %s " % a.lower())

print("왼쪽 공백 지우기")
a = "     hi"
print("원본 문장 : %s " % a)
print("변환된 문장 : %s " % a.lstrip())
print("오른쪽 공백 지우기")
a = "hi     "
print("원본 문장 : %s " % a)
print("변환된 문장 : %s " % a.rstrip())
print("양쪽 공백 지우기")
a = "    hi    "
print("원본 문장 : %s " % a)
print("변환된 문장 : %s " % a.strip())

a = "Life is too short"
print(a.replace("Life", "Your leg"))

#split()을 사용하면 지정한 문자로 문자열을 나누어서 문자열 배열에 출력함
a = "Life is too short"
print(a.split())
a = "a:b:c:d"
print(a.split(':'))
print()
print()
test = 10.0
print("화면에 출력한 코드 %d" % test)
print("화면에 출력한 코드 %f" % test)

test1 = 100
print("화면에 출력한 코드 %d" % test1)
print("화면에 출력한 코드 %f" % test1)

print()
print("=" * 100)
print()

#문자열 코드를 사용하지 않고 format() 함수를 이용하여 문자열을 형식에 맞게 출력
#문자열 코드 대신 {0} 을 사용하여 각종 데이터가 들어갈 부분을 표현
#입력될 데이터가 여러개일 경으{0},{1},{2},{n}으로 표현
#값은 format(첫번째값, 두번째값, 세번째값, n번째 값)으로 데이터를 입력
print(".format() 이용하여 문자열을 쉽게 표현하기")
#숫자대입하기
print("I eat {0} apple".format(3))
print("I eat %d apple" % 3)
#문자열 대입하기
print("I eat %s apple" % "five")
print("I eat {0} apple".format("five"))
#변수 대입하기
number = 3
print("I eat %s apple" % number)
print("I eat {0} apple".format(number))
# 정수와 실수 대입하기
number1 = 100
number2 = 100.0
print("정수출력 : %d \n소수출력 : %f" % (number1, number2))
print("정수출력 : %d \n소수출력 : %f" % (number1, number2))
print("정수출력 : {0} \n소수출력 : {1}".format(number1, number2))
    
#두개 이상의 값 넣기
number = 10
day = "three"
print("I eat {0} apples. so I was sick for {1} days.".format(number, day))

#format() 함수 사용시 {index} 대신 {변수이름} 으로 사용이 가능함
print("I eat {number} apples. so I was sick for {day} days.".format(number=5, day=3))

#{index} 와 {변수이름} 을 동시에 혼용해서 사용이 가능함
print("I eat {0} apples. so I was sick for {day} days.".format(10, day=3))

#문자열 왼쪽 정렬
print("문자열 왼쪽 정렬 : %-10s jane" % "hi")
print("문자열 왼쪽 정렬 : {0:<10} jane".format("hi"))

#문자열 오른쪽 정렬
print("문자열 오른쪽 정렬 : %10s jane" % "hi")
print("문자열 오른쪽 정렬 : {0:>10} jane".format("hi"))

#문자열 중앙 정렬
print("문자열 중앙 정렬 : {0:^10} jane".format("hi"))

#공백채우기
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))
#소수점 표현하기
print("{0:0.4f}".format(3.4213423))
print("{0:10.5f}".format(3.4213423))

#문자 {} 표현하기 (%를 화면에 출력하듯이 2번 입력)
print("{{   and    }}".format())

#파이썬에서 리스트 선언
#파이썬에서 리스트는 자바에서 배열과 같은 기능을 함
# 자바에서는 배열에 자료형을 입력하기 때문에 같은 자료혀으이 데이터마 입력할 수 있으나 파이썬에서는 자료형을 입력하지 않기 때문에 어떠한 자료형도 하나의 리스트에 입력이 가능함

print("리스트 사용 하기")
a = []
print("빈 리스트 : {0}".format(a))
b = [1, 2, 3]
print("숫자형 리스트 : {0}".format(b))
c = ['Life', 'is', 'too', 'short']
print("문자형 리스트 : {0}".format(c))
d = [1, 2, 'Life', 'is']
print("혼합 리스트 : {0}".format(d))
e = [1, 2, ['Life', 'is']]
print("리스트 자체 리스트 : {0}".format(e))
# 자바의 배열과 같이 인뎃싱이 가능함
# index 번호는 0번부터 시작(list[index])
#리스트의 사용방법은 자바의 배열 사용방법과 기본적으로 같음
#  값 출력 : a[index]
#  값 입력 : a[index]
# 리스트의 마지막 요소 출력 : a[-1]
a = [1, 2, 3]
print("리스트 a의 index 1번 출력 : {0}".format(a[1]))
print("리스트를 사용해서 연산하기 : {0}".format(a[0] + a[2]))
print("리스트를 사용해서 마지막 요소 출력하기 : {0}".format(a[-1]))
print("리스트의 마지막 요ㅅ")
print("리스트의 길이 출력하기 {0}".format(len(a)))
# 리스트 안의 리스트 사용하기
# 리스트 안에 리스트를 입력하면 하나의 리스트 요소로 리스트를 가질 수 있다.
# 리스트 안의 리스트의 요소에 접근하려면 자바의 2차원 배열을 사용하는 것처럼 접근이 가능하다
# 출력 : a[첫번째 리스트 index][2번째 리스트 index]
# 입력 : a[첫번째 리스트 index][2번째 리스트 index] = 값
a = [1, 2, 3, ["a", "b", "c"]]
print("배열 a의 2번째 요소 출력 : {0}".format(a[2]))
print("배열 a의 3번째 요소 출력 : {0}".format(a[3]))
print("배열 a의 3번째 요소의 1번째출력 : {0}".format(a[3][0]))
# 리스트 슬라이싱
# 문자열 슬라이싱 방법과 동일함
a = [1, 2, 3, 4, 5]
print("리스트 슬라이싱하기 : {0}".format(a[0:2]))
b = "12345"
print("문자열 슬라이싱하기 : {0}".format(b[0:2]))

print()
print("처음부터 지정한 위치까지 출력 : {0}".format(a[:2]))

a = [1, 2, 3, ["a", "b", "c"], 4, 5]
# 리스트 a의 2번째 요소의 값 3 을 출력하고, 3번째 요소인 리스트 전체를 출력, 끝나는 요소가 리스트 a의 5번째 요소 앞의 요소값 4 출력
print("중첩된 리스트 출력 : {0}".format(a[2:5]))
# 리스트 a의 3번째 요소인 리스트의 처음부터 2번째 요소 앞까지 출력
print("중첩된 리스트 출력 : {0}".format(a[3][:2]))

# 리스트 연산자
# 기존 리스트에 다른 리스트를 연산하여 하나의 리스트로 만ㄷ,ㅁ
# +연산자 : 기존의 리스트에 추가함
# *연산자 : 기존의 리스트를 곱하여 추가함
print()

a = [1, 2, 3]
b = [4, 5, 6]
print("두 연산자자의 합 : {0}".format(a + b))
print("* 연산자를 사용하여 a리스트를 {0}번 반복한 리스트 생성 : {1}".format(3, a * 3))

# 리스트의 수정, 변경과 삭제 
a = [1, 2, 3]
print("원본 리스트 출력 : {0}".format(a))
a = [2]
print("수정한 리스트 출력 : {0}".format(a))

# 연속된 범위 수정
# 리스트의 값을 입력할 경우 같은 하나의 인덱스를 선택하더라도 a[1:2] 와 a[1]은 다름
# a[1:2]의 경우는 범위 설정을 통하여 하나의 인덱스값만 출력한 형태이나, a[1]은 하나의 인덱스만을 선택한 형태임\

print()
a = [1, 2, 3]
print("리스트a의 1:2값 출력 : {0}".format(a[1:2]))
a[1:2] = ["a", "b", "c"]
print("리스트a의 1:2값 출력 : {0}".format(a))
b[1] = ["a", "b", "c"]
print("리스트 b의 index 1에 리스트 넣기 : {0}".format(b))

# 리스트 요소 삭제
# 리스트의 요소에 빈 리스트를 입력하면 해당 리스트의 인덱스가 삭제 됨
print("삭제전 리스트 출력 : {0}".format(a))
a[1:3] = []
print("삭제 후 리스트 출력 : {0}".format(a))
a[1:2] = []
print("요소 하나만 삭제 : {0}".format(a))

# del() 함수를 사용하여 리스트 요소 삭제
# del(삭제할 리스트 요소)
print("삭제 전 리스트 출력 : {0}".format(a))
del (a[1])
print("삭제 후 리스트 출력 : {0}".format(a))

# 리스트 관련 함수
# 입력 함수 insert, append
print()
# insert()는 입력하려는 위치 index번호에 지정한 값을 입력함
# insert() 함수는  index() 함수와 같이 사용하는 형태가 많음
a = [1, 2, 3]
print("원본 리스트 : {0}".format(a))
a.insert(1, 100)
print("insert를 이용하여 값 추가 : {0}".format(a))

# appen()는 리스트의 가장 마지막 요소 뒤에 지정한 값을 추가함
a = [1, 2, 3]
print("원본 리스트 : {0}".format(a))
a.append(100)
print("append를 이용하여 값 추가 : {0}".format(a))

# 제거함수 remove, pop

print()
# remove 함수는 지정한 값을 리스트에서 첫번째로 검색되는 index를 삭제
a = [1, 2, 3, 1, 2, 3]
print("원본 리스트 : {0}".format(a))
a.remove(3)
print("remove를 이용해 삭제 : {}0".format(a))
# pop 함수는 해당하는 인덱스의 값을 반환하고 리스트에서 삭제
a = [1, 2, 3, 1, 2, 3]
print("원본 리스트 : {0}".format(a))
a.pop(1)
print("pop을 이용해 삭제 : {0}".format(a))

# sort, reverse
# 리스트 내부의 값을 오름차순으로 정렬 후 풀력
print()
a = [1, 4, 3, 2]
print("원본 리스트 : {0}".format(a))
a.sort()
print("sort 사용하여 정렬 된 리스트 : {0}".format(a))
# 정렬은 하지 않고 리스트 내부의 값의 순서만
a = [1, 4, 3, 2]
print("원본 리스트 : {0}".format(a))
a.sort()
print("reverse 사용하여 정렬 된 리스트 : {0}".format(a))

# 위치 찾기 index
a = [1, 2, 3]
print("index 함수를 이용하여 리스트의 값 찾기 : {0}".format(a.index(3)))

# 리스트에 포함된 지정한 값의 수 확인 count

print()
a = [1, 4, 3, 2, 5, 3]
print("리스트 a에 포함된 3의 총 개수 확인 : {0}".format(a.count(3)))

# 리스트 확장 extend(append 사용해도 무관)
a = [1, 2, 3]
print("원본 리스트 : {0}".format(a))
a.extend([4, 5, 6])
print("확장된 리스트 : {0}".format(a))

a = a + [7, 8, 9]
print("+연산자 사용 : {0}".format(a))
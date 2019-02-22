# 주석을 남기기 위한 기호 '#' 이다.
# 파이썬이 지원하는 숫자형
# 정수, 실수, 복소수, 8진수, 16진수
# 8진수 :  0o숫자(영문 소문자 혹은 대문자 o를 사용)
# 16진수 : 0x숫자(영문 소문자 혹은 대문자 x를 사용)
print()
print("정수형 출력")
print(123)
print(-178)
print()
print("실수형 출력")
print(3.14)
print(-3.14)
print()
print("8진수 출력")
print(0o123)
print(-0o123)
print()
print("16진수 출력")
print(0x1234)
print(-0x1234)
print()
print("복소수 출력")
a = 1 + 2j
b = 3 - 4j
print(a)
print(b)
print()
print("복소수 실수 부분")
a = 1 + 2j
print(a.real)
print()
print("복소수 허수 부분")
a = 1 + 2j
print(a.imag)
print()
print("복소수 켤레복소수 부분")
a = 1 + 2j
a.conjugate()
print(a)
print()
print("복소수 절대값 부분")
a = 1 + 2j
print(abs(a))


#숫자형을 활용하기 위한 연산자
# 기본 4칙연산
# +, -, *, /, **(제곱연산), %(나머지연산), //(나눈 몫만 출력)

print()
print("사칙연산")
a = 3
b = 4
c = a + b
print("a + b = %s" %c)
c = a - b
print("a - b = %s" %c)
c = a * b
print("a + b = %s" %c)
c = a / b
print("a / b = %s" %c)
c = a % b
print("a %s b = %s" % ("%", c))
c = a ** b
print("a ** b = %s" %c)
c = a // b
print("a // b = %s" %c)
# ###-*-coding:utf-8

# 딕셔너리 사용하기
# 딕셔너리는 key와 value로 구성되어있는 자료형
# 기존의 배열 및 리스트, 튜플은 index와 value로 구성되어있는 자료형
# index가 없기 때문에 자료의 저장 순서가 없음
# 딕셔너리는 {} 기호를 사용
# key와 value의 구분은 : 을 사용
# 각 데이터의 구분은 ,로 구분

dic = {"name": "pey", "phone": "01012345678", "birth": "1118"}
print("딕셔너리 사용한 자료형 : {0}".format(dic))
print("딕셔너리 원하는 값 자료형 : {0}".format(dic["name"]))

testlist = ["pey", "01012345678", "1118"]
#리스트를 for문을 통하여 모든값을 출력
for value in testlist:
    print(value)
#딕셔너리의 모든값을 for문을 통하여 출력
for value in dic:
    print(dic[value])
 
 #자바의 경우 일반적인for문으로 hsahmap의 내용을 모두 출력할 수 있음
# foreach 문을 사용하여 hashmap의 내용을 출력해야함

# 딕셔너리에 key와 value 추가하기

# 변수 a에 딕셔너리를 직접 대입함

a = {1: "a"}
print("원본 딕셔너리 출력 : {0}".format(a))\
# 딕셔너리 변수 a에 a[key] = value 형태로 값을 대입함
a[2] = "b"
print("추가된 딕셔너리 출력 : {0}".format(a))
a[10] = "c"
print("다시 추가된 딕셔너리 출력 : {0}".format(a))
a["dic"] = "딕셔너리"
print("다시 또 추가된 딕셔너리 출력 : {0}".format(a))
a[10] = "10"
print("key 가 10인 요소 수정 : {0}".format(a))
a["list"] = [1, 2, 3, 4, 5]
print("딕셔너리 요소로 리스트 추가 : {0}".format(a))
a["tuple"] = ("a","b","c","d","e")
print("딕셔너리 요소로 튜플 추가 : {0}".format(a))

# 딕셔너리 요소 삭제
# del() 함수를 사용 딕셔너리의 요소 삭제

print()

del (a["tuple"])
del (a["list"])
print("del함수를 이용하여 요소 삭제 : {0}".format(a))

# 딕셔너리 key 리스트 (keys)
# 해당 딕셔너리의 key만 객체로 반환 

print()

dic = {"name": "pey", "phone": "01012345678", "birth": "1118"}
print("key함수를 사용하여 딕셔너리의 key값 출력 : {0}".format(dic.keys()))

for k in dic.keys():
    print(k)
print("dict_keys 객체를 list로 변경 : {0}".format(list(dic.keys())))
print("dict_keys 객체를 tuple로 변경 : {0}".format(tuple(dic.keys())))

# 딕셔너리 value 리스트 (values)
print()

print("value를 이용하여 딕셔너리의 내용을 객체로 출력 : {0}".format(dic.values()))
# list함수와 tuple 함수를 이용하여 형 변환
print("dict_values 객체를 list로 변경 : {0}".format(list(dic.values())))
print("dict_values 객체를 tuple로 변경 : {0}".format(tuple(dic.values())))

# 딕셔너리에서 key와 value 동시에 얻기(item)
print()
print("items 함수를 이용해서 dic_items 객체 얻기 : {0}".format(dic.items()))
print("dics_items 객체를 list로 변경 : {0}".format(list(dic.items())))

# 딕셔너리 내용 삭제 clear
# 딕셔너리의 내용을 모두 삭제함
print()
print("원본 딕셔너리 내용 출력 : {0}".format(dic))
print("clear함수를 이용하여 딕셔너리 삭제 : {0}".format(dic.clear()))

# 딕셔너리 key를 이용하여 value 얻기(get)
# 기존의 딕셔너리 value 사용방법인 dic[key]와 결과값은 동일하지만 dic[key] 방식은 없는 키를 통해서 value를 호출하면 에러가 발생하지만 get 함수를 사용 시 없는 키를 통하여 value를 호출하면 None 이 발생
print()

dic = {"name": "pey", "phone": "01012345678", "birth": "1118"}
print("dic[key] 방식으로 없는 키 사용 : {0}".format(dic["tel"]))
print("dic.get(key)방식으로 없는 키 사용 : {0}".format(dic["tel"]))

# 자료형의 참과 거짓
# 문자열은 빈 문자열이 아니면 true, 빈 문자열이면 false
# 빈 리스트가 아니면 true, 빈 리스트면 false
# 튜플은 리스트와 동일
# 딕셔너리도 리스트와 동일
# 숫자형은 0이 아닌 모든 수는 true, 0은 false
# 값 None은 false
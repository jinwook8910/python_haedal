print(5+7)
print(5-7)
print(5*7)
print(5/7)
print(5//7) #소수점을 버린 몫을 구하기.
print(2**2) #2의 2승.

print('"안녕하세요"라고 말했습니다')
print('안녕하싱교')
print("안녕하시오")
print("반갑소" + " 나도 반갑소")

#리스트 (숫자기반 데이터 저장배열)
array = [273, "문자열", True]
print(array) #리스트 전체를 출력
print(array[0]) #인덱스를 사용한 부분출력
array[0] = 555
print(array)

#딕셔너리 (문자열로 데이터 저장. key와 value를 사용)
포켓몬1 = {"이름":"피카추", "타입":"전기", "공격력":55} #문자열로 key를 사용
print(포켓몬1["이름"])

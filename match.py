import random

print("0 ~ 50 까지의 숫자를 입력하세요.")

num = random.randint(0, 50)  # randint 함수는 인자로 들어온 a, b 사이의 랜덤한 정수(int)를 반환

count = 0
while True:
    count += 1  # 숫자가 하나씩 올라감
    print(f"{count} 번째 도전")  # 숫자가 올라가면서 도전횟수가 올라감
    user = int(input("당신의 선택은? >>>>  "))

    if user > num:  # 만약 숫자보다 사용자가 입력한 숫자가 더 크다면
        print("정답보다 크다")
    elif user < num:
        print("정답보다 작다")
    else:
        print("정답")
        break   # 종료

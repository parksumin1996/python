coffee = 10

while True:
        print("돈을 받았으니 커피를 줍니다.")
        coffee = coffee - 10
        print("남은 커피의 수는 %d개입니다." % coffee)
        if coffee ==0:
                print("커피가 다 떨어졌습니다. 판매를 중다합니다")
        break

print("휴식이 길어지면몸이 아파집니다")

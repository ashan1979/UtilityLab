heart_beats = list(map(float, input("Enter Your Heart Beat Numbers Separated by a space: ").split()))
king = heart_beats[0]
valley = heart_beats[0]
# print(king)

for beat in heart_beats:
    if beat > king:
        king = beat

    if beat < valley:
        valley = beat
print(f"The lowest beat your heart recorded is: {valley}")
print(f"The highest beat your heart recorded is: {king}")
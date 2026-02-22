heart_beats = list(map(int, input("Enter Your Heart Beat Numbers Separated by a space:").split()))
king = heart_beats[0]
# print(king)

for beat in heart_beats:
    if beat > king:
        king = beat


print(king)
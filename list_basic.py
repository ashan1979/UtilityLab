heart_beats = [70, 80, 90]
king = heart_beats[0]
# print(king)

for beat in heart_beats:
    if beat > king:
        king = beat


print(king)
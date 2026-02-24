input_a = float(input("Enter a number: "))
input_b = float(input("Enter another number: "))

if input_a > input_b:
    winner = input_a
elif input_a < input_b:
    winner = input_b
else:
    winner = "It's a tie"

print(winner)
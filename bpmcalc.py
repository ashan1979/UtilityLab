# 1. input
bpm_input = input("Enter the song Tempo (BPM): ")

# 2. Process

ms_result = 60000 / float(bpm_input)

# 3. OUTPUT

print("------------------------")
print(f"Quarter Note Delay: {ms_result} ms")
print(f"Eighth Note Delay: {ms_result / 2} ms")
print("------------------------")

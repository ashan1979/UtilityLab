bpm = float(input("Enter the Song BPM: "))
beats_per_bar = int(input("How many Beats per Bar(3/4): "))

# The Logic

ms_per_bar = 60000 / bpm
total_bar_ms = ms_per_bar * beats_per_bar

print(f"One full bar at {bpm} BPM in {beats_per_bar}/4 time is {total_bar_ms}ms.")
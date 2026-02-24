while True:
    try:
        bpm = float(input("Enter the Song BPM: "))

        if bpm <= 0:
            print("Song cannot be 0 or Less")
        else:
            break
    except ValueError:
        print("Please enter a number")

beats_per_bar = int(input("How many Beats per Bar(3/4): "))

    # The Logic

ms_per_beat = 60000 / bpm
total_bar_ms = ms_per_beat * beats_per_bar

print(f"One full bar at {bpm} BPM in {beats_per_bar}/4 time is {total_bar_ms}ms.")

print(f"The BPM for 4 bars is {total_bar_ms * 4} ms")
print(f"The the 8th note bpm in milliseconds is {ms_per_beat / 2} ms")
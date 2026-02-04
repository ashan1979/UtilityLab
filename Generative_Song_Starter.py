import random

def generate_session_vibe():
    # 1. Defining the 'Palette'
    keys = ["C", "Db", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
    scales = ["Major", "Minor", "Dorian", "Phrygian", "Lydian", "Mixolydian"]

    # 2. Weighted Randomness for Time Signatures
    # We make 4/4 much more likely (80%) than others
    time_sigs = ["4/4", "3/4", "6/8", "7/8"]
    weights = [0.8, 0.1, 0.07, 0.03]

    selected_time = random.choices(time_sigs, weights=weights)[0]

    # 3. Range-based Randomness
    bpm = random.randint(70, 165)

    # 4. Dictionary of 'Moods'
    moods = {
        "Dark": ["Industrial", "Techno", "Doom"],
        "Bright": ["Pop", "Funk", "Disco"],
        "Atmospheric": ["Ambient", "Shoegaze", "Post-Rock"]
    }

    vibe_category = random.choice(list(moods.keys()))
    sub_genre = random.choice(moods[vibe_category])

    print("--- 🎹 NEW SESSION SEED ---")
    print(f"Genre: {vibe_category} ({sub_genre})")
    print(f"Key: {random.choice(keys)} {random.choice(scales)}")
    print(f"Tempo: {bpm} BPM")
    print(f"Meter: {selected_time}")
    print("----------------------------")

if __name__ == "__main__":
    generate_session_vibe()
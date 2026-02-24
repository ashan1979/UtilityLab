import time
import sys

# Settings
width = 20
height = 8
delay = 0.05

def draw_spot(r, c, char):
    #move cursor to row r, col c and print char
    # \033[{row}:{col}]J os the ANSI code for 'Position Cursor'
    sys.stdout.write(f"\033[{r};{c}H{char}")
    sys.stdout.flush()

# 1. Clear screen once at the start
print("\033[2j")

# 2.  Draw the permanent frame first
for c in range(1, width + 1):
    draw_spot(1, c, "-")
    draw_spot(height, c, "-")
for r in range(1, height + 1):
    draw_spot(r,1, "|")
    draw_spot(r, width, "|")

# 3. The travelling asterisk

while True:
    # 1. Top Edge (Left to Right)
    for c in range(1, width + 1):
        draw_spot(1, c, "*")
        time.sleep(delay)
        draw_spot(1, c, "-")

    # 2. Right Edge (Top to Bottom)
    for r in range(2, height + 1):
        draw_spot(r, width, "*")
        time.sleep(delay)
        draw_spot(r, width, "|")

    # 3. Bottom Edge(Right to Left)
    for c in range(width -1, 0, -1):
        draw_spot(height, c, "*")
        time.sleep(delay)
        draw_spot(height, c, "-")

    # 4. Left Edge (Bottom to Top)
    for r in range(height -1, 1, -1):
        draw_spot(r, 1, "*")
        time.sleep(delay)
        draw_spot(r, 1, "|")
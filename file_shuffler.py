import random
import os

def shuffle_workload():
    # 1. A list of tasks or files you're procrastinating on
    tasks = os.listdir('.')

    print(f"Original order: {tasks}")

    # 2. random.shuffle() mixes the list 'in place'
    # (it changes the actual list, doesn't make a new one)
    random.shuffle(tasks)

    print((f"Shuflled Priority: {tasks}"))

    # 3. random.choice() to pick the 'Task of the Hour'
    focus_task = random.choice(tasks)
    print(f"\n🚀 Your focus right now: {focus_task}")

if __name__ == "__main__":
    shuffle_workload()
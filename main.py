import json

def add_problem():
    name = input("Problem Name: ")
    difficulty = input("Difficulty (Easy/Medium/Hard): ")
    topic = input("Topic: ")

    problem = {
        "name": name,
        "difficulty": difficulty,
        "topic": topic,
        "revision_count": 0
    }

    try:
        with open("data/problems.json", "r") as file:
            data = json.load(file)

    except:
        data = []

    data.append(problem)

    with open("data/problems.json", "w") as file:
        json.dump(data, file, indent=4)

    print("\nProblem Added Successfully!")


# ADD THIS FUNCTION HERE
def view_problems():
    try:
        with open("data/problems.json", "r") as file:
            data = json.load(file)

        if not data:
            print("No problems found.")
            return

        print("\nSolved Problems:\n")

        for idx, problem in enumerate(data, start=1):
            print(f"{idx}. {problem['name']}")
            print(f"   Difficulty: {problem['difficulty']}")
            print(f"   Topic: {problem['topic']}")
            print(f"   Revisions: {problem['revision_count']}")
            print()

    except:
        print("No problems found.")

while True:

    print("\n===== LeetCode Progress Manager =====")
    print("1. Add Problem")
    print("2. View Problems")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_problem()

    elif choice == "2":
        view_problems()

    elif choice == "3":
        break

    else:
        print("Invalid Choice")
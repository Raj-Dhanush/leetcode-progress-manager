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

def search_problem():
    search_word = input("Enter the problem name to be searched: ")
    try:
        with open("data/problems.json", "r") as file:
            data = json.load(file)
        for problem in data:
            if problem["name"].lower() == search_word.lower():
                print("\nProblem Found\n")

                print(f"Name: {problem['name']}")
                print(f"Difficulty: {problem['difficulty']}")
                print(f"Topic: {problem['topic']}")
                print(f"Revisions: {problem['revision_count']}")

                return
        print("Problem not found")
    except:
        print("No problems found")

def update_revision_count():
    search_name = input("Enter problem name: ")
    try:
        with open("data/problems.json", "r") as file:
            data = json.load(file)
        for problem in data:
            if problem["name"].lower() == search_name.lower():
                problem["revision_count"] += 1
                with open("data/problems.json","w") as file:
                    json.dump(data, file, indent = 4)
                
                print("Revision Count updated")
                return
        print("Problem not found")
    except:
        print("No problems found")

while True:

    print("\n===== LeetCode Progress Manager =====")
    print("1. Add New Problem")
    print("2. View Problems")
    print("3. Search Problem")
    print("4. Update Revision Count")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_problem()

    elif choice == "2":
        view_problems()

    elif choice == "3":
        search_problem()

    elif choice == "4":
        update_revision_count()
    elif choice == "5":
        break
    else:
        print("Invalid Choice")


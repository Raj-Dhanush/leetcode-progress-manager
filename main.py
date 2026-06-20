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


add_problem()
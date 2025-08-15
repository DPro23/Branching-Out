import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    if age.isdigit():
        filtered_users = [user for user in users if user["age"] == int(age)]

        for user in filtered_users:
            print(user)
    else:
        print("'Age' must be an integer.")


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Only 'name' and 'age' are supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = input("Enter an age to filter users: ").strip()
        filter_users_by_age(age_to_search)
    else:
        print("Filtering by that option is not yet supported.")
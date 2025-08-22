import json


def get_users():
    """ Gets and returns users from users.json """
    with open("users.json", "r", encoding="utf-8") as file:
        users = json.load(file)

    return users


def filter_users_by_name(name):
    """
    Gets a string to filter and print all the matching users by 'name'
    from users.json
    """
    users = get_users()

    filtered_users = [
        user for user in users if user["name"].lower() == name.lower()
    ]

    if len(filtered_users) == 0:
        print("❌ No user found")

    for user in filtered_users:
        print("😄", user)


def filter_users_by_age(age):
    """
    Gets an integer to filter and print all the matching users by 'age'
    from users.json
    """
    users = get_users()

    if age.isdigit():
        filtered_users = [user for user in users if user["age"] == int(age)]

        for user in filtered_users:
            print("😄", user)
    else:
        print("❌ 'Age' must be an integer.")


def filter_users_by_email(email):
    """
    Gets an email to filter and print all the matching users by 'email'
    from users.json
    """
    users = get_users()

    if '@' in email:
        filtered_users = [user for user in users if user["email"] == email]

        for user in filtered_users:
            print("😄", user)
    else:
        print("❌ 'email' is not valid.")


def main():
    """Run the CLI providing options for filtering users"""
    filter_dispatcher = {
        'name': filter_users_by_name,
        'age': filter_users_by_age,
        'email': filter_users_by_email
    }

    filter_option = input(
        "What would you like to filter by? "
        "(Only 'name', 'age' and 'email' are supported): ").strip().lower()

    if filter_option in filter_dispatcher:
        search_value = input(f"Enter the {filter_option} to filter users: ").strip()
        filter_dispatcher[filter_option](search_value)
    else:
        print("❌ Filtering by that option is not supported.")


if __name__ == "__main__":
    main()

from re import search
from tabulate import tabulate
from csv import DictReader, DictWriter
from werkzeug.security import check_password_hash, generate_password_hash
from pandas import read_csv


def main():
    while True:
        index = [(1, "Log In"), (2, "Register")]
        print(
            tabulate(
                index,
                headers=["Input", "Login Page"],
                numalign="center",
                stralign="center",
                tablefmt="grid",
            )
        )
        choice = choice_function(int(input("Input: ")), len(index))

        if choice == 1:
            print(tabulate(["LOG IN"]))

            user = input("User: ")
            password = input("Password: ")

            while True:
                index = verify_login(user, password)
                print(
                    tabulate(
                        index[1:],
                        headers=[*index[0]],
                        numalign="center",
                        stralign="center",
                        tablefmt="grid",
                    )
                )
                choice = choice_function(int(input("Input: ")), len(index) - 2)
                if choice == 3:
                    break

                if choice == 1:
                    print(tabulate(["ADD CASH"]))
                    amount = get_amount(input("Amount: "))
                    add_amount(user, amount)
                else:
                    print(tabulate(["WITHDRAW CASH"]))
                    while True:
                        amount = get_amount(input("Amount: "))
                        if amount <= float(index[1][1].removeprefix("$")):
                            break
                        print("Cannot withdraw this amount")

                    sub_amount(user, amount)

        else:
            print(tabulate(["REGISTER"]))

            user = user_confirmer(input("User: "))
            password = password_confirmer(
                input("Password: "), input("Confirm Password: ")
            )
            register(user, password)


def choice_function(choice, n):
    if choice in range(1, n + 1):
        return choice
    else:
        raise ValueError("Input out of range")


def get_amount(inpt):
    if amount := search(r"^(\d+(?:\.\d{1,2})?)$", inpt):
        return float(amount.group(1))
    else:
        raise ValueError("Invalid Amount")


def user_confirmer(user):
    if not search(r"^\w+$", user):
        raise ValueError("Username must only contain alphanumeric letters")

    with open("registered.csv") as file:
        accounts = DictReader(file)
        for account in accounts:
            if user == account["user"]:
                raise ValueError("Username taken")

    return user


def password_confirmer(password, confirm):
    if password == confirm and search(r"^[\w_@./#&+!?-]+$", password):
        return password
    elif not search(r"^[\w_@./#&+!?-]+$", password):
        raise ValueError("Password must not contain whitespaces")
    elif password != confirm:
        raise ValueError("Passwords do not match")


def add_amount(user, amount) -> None:
    data = read_csv("registered.csv")
    data.loc[data["user"] == user, "balance"] = data["balance"] + amount
    data.to_csv("registered.csv", index=False)


def sub_amount(user, amount) -> None:
    data = read_csv("registered.csv")
    data.loc[data["user"] == user, "balance"] = data["balance"] - amount
    data.to_csv("registered.csv", index=False)


def verify_login(user, password):
    with open("registered.csv") as file:
        accounts = DictReader(file)
        for account in accounts:
            if user == account["user"] and check_password_hash(
                account["password"], password
            ):
                return (
                    ("User", account["user"]),
                    ("Balance", "${:,.2f}".format(float(account["balance"]))),
                    (1, "Add Cash"),
                    (2, "Withdraw Cash"),
                    (3, "Log Out"),
                )

    raise ValueError("Invalid User or Password")


def register(user, password):
    with open("registered.csv", "a") as file:
        writer = DictWriter(file, fieldnames=["user", "balance", "password"])
        writer.writerow(
            {
                "user": user,
                "balance": float(100),
                "password": generate_password_hash(password),
            }
        )


if __name__ == "__main__":
    main()

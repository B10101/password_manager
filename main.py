from random import choice, randrange
from string import punctuation


def create_password():
    lines = []
    liberty = []
    with open(r"nouns/12.txt", 'r') as fp:
        lines = fp.readlines()
    with open(r"verbs/1syllableverbs.txt","r") as ve:
        liberty = ve.readlines()
    noun = choice(lines).strip()
    verb = choice(liberty).upper().strip()
    number = randrange(1,100)
    special_character = choice(punctuation)
    password = verb+special_character+str(number)+noun
    return password


def details():
    print("user name: ")
    username = input()
    print("Name of website: ")
    website = input()
    return f"username = {username}, website = {website}"


def main():
    password = create_password()
    print(f"suggested password: {password}")
    print("Do you prefer the password? Answer with Y/N")
    answer = input().upper()
    if answer == "Y":
        detail = f"{details()},password = {password} \n"
        with open("save.txt","a") as pop:
            pop.writelines(detail)
    else:
        main()


if __name__ == "__main__":
    main()

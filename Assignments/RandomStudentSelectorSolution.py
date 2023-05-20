import random

def prompt():
    print()
    print("RANDOM STUDENT SELECTOR")
    print("---------------------")
    print("Press 'P' to pick a name")
    print("Press 'L' to list")
    print("Press 'U' to update the list")
    print("Press 'R' to reset eligibility")
    print("Press 'Q' to quit")
    print("Press any other key for a random name")
    print("===>", end=' ')


def select_random_name():
    result = ''
    if len(names) == 0:
        result = 'list empty'
    elif all(used):
        result =  'all used'
    else:
        index = random.randint(0, len(names) - 1)
        while used[index]:  # loop until eligible name is found
            index = random.randint(0, len(names) - 1)
        used[index] = True
        result = names[index]
    return result


def list_names():
    print("Name     Eligible")
    for i in range(len(names)):
        print("{:8s} {}".format(names[i], not used[i]))


def update_list():
    global names
    global used
    new_names = input("Enter a space-separated list of names: ").split()
    names = new_names
    used = [False] * len(names)


def reset_eligibility():
    global used
    used = [False] * len(names)


def run():
    while True:
        prompt()
        key = input().upper()
        if key == "Q":
            break
        elif key == "P":
            name = select_random_name()
            if name == 'all used':
                print('sorry no names are eligible to be selected')
            elif  name == 'list empty':
                print('sorry names list is empty')
            else:
                print("Selected name: {}".format(name))
                used[names.index(name)] = True
        elif key == "L":
            list_names()
        elif key == "U":
            update_list()
        elif key == "R":
            reset_eligibility()
        else:
            name = select_random_name()
            print("Selected name: {}".format(name))

names = ["Bob", "Pete", "Mary"]
used = [False] * len(names)
run()

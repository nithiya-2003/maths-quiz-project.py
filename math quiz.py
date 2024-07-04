import random

def display():
    title = "A Simple Math Quiz"
    print("*" * len(title))
    print(title)
    print("*" * len(title))

def user_input():
    choice = int(input("Enter the operation of your choice: "))

    while choice < 1 or choice > 5:
        print("Invalid menu option. Try again.....")
        choice = int(input("Enter the operation of your choice: "))

    return choice

def sol(p):
    print("Enter your answer for:")
    print(p)
    result = float(input("="))  # Use float to handle division properly
    return result

def dis_op():
    li_op = ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Division", "5. Exit"]
    for op in li_op:
        print(op)

def problem(operation):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    if operation == 1:
        problem = f"{num1} + {num2}"
        solution = num1 + num2
    elif operation == 2:
        problem = f"{num1} - {num2}"
        solution = num1 - num2
    elif operation == 3:
        problem = f"{num1} * {num2}"
        solution = num1 * num2
    elif operation == 4:
        problem = f"{num1} / {num2}"
        solution = num1 / num2

    return problem, solution

def main():
    display()
    while True:
        dis_op()
        op = user_input()
        if op == 5:
            break
        prob, an = problem(op)
        ans = sol(prob)
        if ans == an:
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer is {an}")

main()

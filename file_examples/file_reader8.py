with open('plan.txt', 'r') as file:
    for line in file:
        print(line)
        print(len(line.strip()))

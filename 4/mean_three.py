# mean_three.py
def mean_three(x, y, z):
    return round((x + y + z) / 3, 2)

if __name__ == "__main__":
    print(mean_three(1, 3, 4.3))
    print(mean_three(3.1, 2, 5))
    
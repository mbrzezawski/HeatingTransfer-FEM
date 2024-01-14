from utils import solve
from draw import show_result


if __name__ == "__main__":
    n = int(input())
    x, y = solve(n)
    print(show_result(x, y))
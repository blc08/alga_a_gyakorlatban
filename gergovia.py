import sys

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    iterator = iter(input_data)
    while True:
        try:
            n = int(next(iterator))
            if n == 0:
                exit()
            a = []
            gergovia = [int(next(iterator)) for _ in range(n)]

            balance = 0
            work = 0
            for house in gergovia:
                balance += house
                work += abs(balance)
            print(work)
        except StopIteration:
            exit(0)

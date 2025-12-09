import sys

def get_max_bond(get_men, get_women):
    get_men.sort(reverse=True)
    get_women.sort(reverse=True)
    sum:int=0
    for i in range(len(get_men)):
        sum+= get_men[i] * get_women[i]
    return sum

if __name__ == '__main__':
    input_data = sys.stdin.read().split()

    iterator = iter(input_data)
    try:
        t = int(next(iterator))
        for _ in range(t):
            n = int(next(iterator))
            men = [int(next(iterator)) for _ in range(n)]
            women = [int(next(iterator)) for _ in range(n)]
            print(get_max_bond(men, women))
    except StopIteration:
        exit(0)

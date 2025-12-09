# for x in range(5000):
#     cube_of_x = x*x*x
#     if cube_of_x % 1000 == 888:
#         print(x, cube_of_x)

t = int(input())
for _ in range(t):
    k = int(input())

    k_th = 192 + (k - 1) * 250
    print(k_th)
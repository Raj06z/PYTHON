def collatz(n):
    while n != 1:
        print(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    print(n)  

num = int(input("Enter number: "))
collatz(num)
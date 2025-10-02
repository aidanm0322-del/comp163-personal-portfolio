n = int(input())
print("=== Challenge 1: Collatz Conjecture ===")
print("Enter starting number: Sequence:", end=" ")

count = 0
print(n, end="")

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (n * 3) + 1  
    print(" ", end="")
    print(n, end="")
    count += 1

print() 
print(f"Steps: {count}")
print()
print("=== Challenge 2: Prime Number Checker ===")
print("Enter a number: Testing divisors from ")

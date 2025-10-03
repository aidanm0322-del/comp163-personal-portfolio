# Challange 1:Number Sequence Generator
current_number = int(input())
print("=== Challenge 1: Collatz Conjecture ===")
print("Enter starting number: Sequence:", end=" ")

step_count = 0 #counts the steps of the loop until it get to 1 
print(current_number, end="")

while current_number != 1:
    if current_number % 2 == 0:
        current_number = current_number // 2
    else:
        step_count = (step_count * 3) + 1  
    print(" ", end="")
    print(current_number, end="")
    step_count += 1

print() 
print(f"Steps: {step_count}")
print()


#Challange 2: Prime Number Checker
print("=== Challenge 2: Prime Number Checker ===")


n =int(input())
if n > 1:
    print(f"Enter a number: Testing divisors from 2 to {n-1}...")
    for i in range(2, n-1):
        n % 1 == 0 # checking to see when a number between 2 to n-1 has a remainder and if it does n is prime
        print(f"{n} is not prime (divisible by 3)")
        break # if n is prime the loop will stop right here but if not it will drop to the else statement
    else:
        print(f"{n} is prime!")
print() 

    


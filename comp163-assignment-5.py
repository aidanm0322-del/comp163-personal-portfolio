#I used ai to help me debug the code and figure out why certian statements where printing the wrong information and also understand how to format the 

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
        current_number = (current_number*3) + 1  
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
    for i in range(2, n): #I had ai help me debug the range for loop because it would print 17 is not prime
        if n % i == 0: # checking to see when a number between 2 to n-1 has a remainder and if it does n is prime
            print(f"{n} is not prime (divisible by 3)")
            break # if n is prime the loop will stop right here but if not it will drop to the else statement
    else:
        print(f"{n} is prime!")
print()


# Challange 3: Multipilcation Table Grid
print(f"=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")

for header in range(1,11):
    print(f"{header:4}", end="") #Prints the header number from 1 to 10 
print()

for row in range(1,11):
    print(f"{row:2}", end="") #Prints the row numbers from 1 to 10
    for col in range(1,11):
        product= row * col
        print(f"{product:4}", end="") # Prints the products of row * coulumn 
    print()
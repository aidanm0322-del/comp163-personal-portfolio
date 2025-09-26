#Step 1: Foundation Setup 
student_name=("Aidan Miles")
current_gpa=4.0
study_hours=10
social_points=50
stress_level=30

#Display Messages 
print("Hello Aidan Miles these are your stats")
print(f"Current Gpa is:{current_gpa}")
print(f"Study Hours are:{study_hours}")
print(f"Social Points are:{social_points}")
print(f" Stress level is:{stress_level}")

# Choice Print Statements 
print("Choose your course load:")
print("A) light (12 credits)") 
print("B) standard (15 credits)")
print("C) Heavy (18 credits)")

#Step 2: Course Planning Decision 
choice=input("Your choice is: ")

if choice == "A":
    current_gpa == 4.0 
    study_hours <+ 18
    social_points <+ 30
    stress_level >- 10
    print(f"Your maintanied a {current_gpa} gpa with great study habits, social life and stress level is {stress_level} ")

elif choice == "B":
    current_gpa == 3.0 
    study_hours <+ 10
    social_points >+ 10
    stress_level <+ 20
    print(f" You maintained 3.0 gpa with okay study habits a great social life and low stress level")

elif choice == "C":
    current_gpa == 3.5
    study_hours <-15
    social_points <-10
    stress_level <- 20
    print(f" You maintained a 3.5 gpa with great atudy habits low social points and low stress levels" )
#If user inputs something other than A,B,C then print Invalid
else: 

    print("Invalid Input") 

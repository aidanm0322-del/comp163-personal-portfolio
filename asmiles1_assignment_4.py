#Step 1: Foundation Setup 
student_name=("Aidan Miles")
current_gpa=4.0
study_hours=10
social_points=50
stress_level=30

#Display Messages 
print("Hello Aidan Miles these are your stats")
print(f"Current Gpa is: {current_gpa}")
print(f"Study Hours are: {study_hours}")
print(f"Social Points are: {social_points}")
print(f" Stress level is: {stress_level}")

# Choice Print Statements 
print("Choose your course load:")
print("A) light (12 credits)") 
print("B) standard (15 credits)")
print("C) Heavy (18 credits)")

#Step 2: Course Planning Decision 
choice=input("Your choice is: ")

if choice == "A":
    if current_gpa == 4.0:
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
    print(f"You maintained a 3.5 gpa with great atudy habits low social points and low stress levels" )

else: 
    print("Invalid Input")

study_options = ["Programming", "Math", "English", "History"]


print(f"{study_options}")

choice2=study_options
choice2 = input("Choose from study options list: ")

if choice2 in study_options and choice2 == "Programming":
    current_gpa <= .1
    social_points =- 10
    print(f"Your gpa went up .1 and social points went down - 10")

elif choice2 in study_options and choice2 == "Math":
    current_gpa =+.2 
    social_points =-20
    print("Your gpa went up .2 and social points went down by 20")

elif choice2 in study_options and choice2 == "English":
    current_gpa =+ .1
    social_points =-10
    print("Your gpa went up by .1 and social points went down by 10")

elif choice2 in study_options and choice2 == "History":
    current_gpa =+ .1
    social_points =-5

elif choice2 == "History" or choice2 == "Programming":
    current_gpa =+.3
    social_points =-15 

elif "Comp 163" not in study_options:
    print("Class Invalid")

if current_gpa is not float:
    print("Gpa must be float")
    

elif current_gpa == 4.0 and stress_level >= 40:
    print("Ending 2: Achiveing Scholar")
    print("You achived a perfect 4.0 gpa but you stress levels are high and social life was terrible")

elif current_gpa >= 3.5 and stress_level >= 50:
    print(" Ending 1: Good Scholar ")
    print("You achieved near-perfect academic results, but at a severe cost. Your stress level is dangerously high, and your social life suffered. You need a long vacation!")

elif current_gpa >= 2.5 and stress_level >= 70:
    print("Ending 3: Alright")
    print("You did alright but your stress levels was high but you also had a great social life") 










    

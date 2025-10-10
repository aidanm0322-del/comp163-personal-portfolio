#This program takes a users 4 inputs name, phone number, email and address and formats it a specific way and then in the end prints all the users information that was inputted. 

#Used Ai to help me with index errors also used it to help with syntax errors when certain print statements where printing in the incorrect lines due to the loops. 

#Format that the user inputs their information
print("Enter contact information (format: name|phone|email|address):")
print()
print("=== CONTACT DIRECTORY ===")
print()

#inputs 
contact_number = 1
contact_count = 0
contacts=[]

#Loop for contact inputs 
while True:
    contact = input()
    if contact == "" or contact.lower() == "done":
        break

    contact_count += 1
    parts = contact.split("|")
    
    #name format
    name = parts[0]
    name = name.strip()
    name = name.title()
    
    name_parts=name.split()
    if len(name_parts) >= 2:
        first=" ".join(name_parts[:-1])
        last=name_parts[-1]
        last_first = f"{last},{first}"
    else:
        last_first=name

    #phone format 
    phone = parts[1]
    digits_only = ""
    for char in phone:
        if char.isdigit():
            digits_only += char
    phone_num = f"    ({digits_only[0:3]}) {digits_only[3:6]}-{digits_only[6:]}"
    
    #email format 
    email = parts[2]
    email = email.strip()
    email = email.lower()
    
    #Address format 
    address = parts[3]
    address = address.strip()
    address = address.title()
    address = address.replace("Nc", "NC")

    print(f"CONTACT {contact_number}:")
    print(f"Name:     {name}")
    print(f"Phone:{phone_num}")
    print(f"Email:    {email}")
    print(f"Address:  {address}")
    print()
   
    contacts.append(f"{last_first:<30}{phone_num:<23}{email}")
   
    contact_number += 1
    
print(f"=== DIRECTORY SUMMARY ===")
print(f"Total contacts processed: {contact_count}")
print()
print("=== FORMATTED FOR PRINTING ===")

#format for print loop 
for line in contacts:
    print(line)



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
    
   
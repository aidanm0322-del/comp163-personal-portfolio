
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

    #Address format 
    address = parts[3]
    address = address.strip()
    address = address.title()
    address = address.replace("Nc", "NC")



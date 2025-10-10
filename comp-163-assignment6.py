contact_1=input()
contact_2=input()
contact_3=input()

#Contact 1 Directory 
name=contact_1.split("|")[0]
name=name.title()
name=name.strip()
phone=contact_1.split("|")[1]
digits_only = ""
address=address.strip()
address=address.title()
address=address.replace("Nc","NC")

#Contact 2 Directory 








print("Enter contact information (format: name|phone|email|address):")
print()
print("=== CONTACT DIRECTORY ===")
print()
print("CONTACT 1:")
print(f"Name:     {name}")
print(f"Address:  {address}")

contact_1=input()
contact_2=input()
contact_3=input()

#Contact 1 Directory 
name=contact_1.split("|")[0]
name=name.title()
name=name.strip()
phone=contact_1.split("|")[1]
digits_only = ""
for char in phone: #Got this from the hint section for phone number
    if char.isdigit():
        digits_only += char
phone_num = f"    ({digits_only[0:3]}) {digits_only[3:6]}-{digits_only[6:]}"
email=contact_1.split("|")[2]
email=email.strip()
email=email.lower()
address=contact_1.split("|")[3]
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
print(f"Phone:{phone_num}")
print(f"Email:    {email}")
print(f"Address:  {address}")

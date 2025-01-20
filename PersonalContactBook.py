import json
from os import system
from time import sleep


FILE_NAME = "contacts.json"

#global variable for some task
global val    

#wait function
def wait_time(time=0.7): # Default time value!
    sleep(time)

#Helper function
def convert_string(name):
    return "".join(map(str,name))
#Convert json to txt.
def json_to_txt(dic):
    file=open("contacts.txt","w")
    names=[]
    for name in dic.keys():
        names.append(name)
    phone_numbers=[]
    emails=[]
    addresses=[]
    name_width = 15
    phone_width = 15
    email_width = 30
    address_width = 20
    for _,data in dic.items():
      
        number=int(convert_string(data["phone"]))
        email=data["email"]    
        address=data["address"]
        phone_numbers.append(number)
        addresses.append(address or "Null")
        # if email has so store email otherwise Null
        emails.append(email or "Null")    
            
    file.write(f"{" "*32}CONTACT BOOK\n")
    file.write(f"| {'Name':<{name_width}} | {'Phone':<{phone_width}} | {'Email':<{email_width}} | {'Address':<{address_width}} \n")
    
    for i in range(len(names)):
        file.write(f"| {names[i]:<{name_width}} | {phone_numbers[i]:<{phone_width}} | {emails[i]:<{email_width}} | {addresses[i]:<{address_width}} \n")
        
        
    file.close()

#Deleted contacts
def deleted_data(name,data):
    print("Done!")
    name_width = 15
    phone_width = 15
    email_width = 30
    address_width = 20
    file_read=open("backup.txt")
    content=(file_read.readlines())
    count=0
    for word in content:
        words=word.split()
        for letter in words:
            if f"|{convert_string(data["phone"])}"==letter:
                count+=1
    print(count)
    if count>0:
        print("Already exist in backup contact book data")
        return        
    
    file=open("backup.txt","a")
    if not data: 
        file.write(f"{" "*23}CONTACT BOOK(BACKUP DATA)\n")
        file.write(f"{'| Name':<{name_width}}  |{"Phone":<{phone_width}}|{"Email":<{email_width}}|{"Address":<{address_width}} \n")
    for i in range(len(name)):
        address=data["address"]
        email=data["email"]
        phone=data["phone"]
        file.write(f"| {name[i]:<{name_width}}|{convert_string(phone):<{phone_width}}|{email or 'null':<{email_width}}|{address:<{address_width}}\n")
    file_read.close()
    file.close()
    
# Load contacts from file
def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4,sort_keys=True)

# Add a new contact
def add_contact(contacts): # Unique identity is Phone number.
    phone_number_list=[]
    for _,item in contacts.items():
        number=int(convert_string(item["phone"]))
        phone_number_list.append(number)
        
    
    name=""   
    email=""
    phone=""
    #Email and Phone number validation check
    co=0
    global val
    val=0
    phone_numbers=[]
    while True: 
        if not name:
            name = input("Enter contact name: ").strip() 
        if name and (not phone) and (not email):   # i know it's complicated to understand this logic but it's good way add intergeting in this 
                                                   # contact management system.
                                                   # 1) First if has name ,then (phone variable which is assign empty string,that reason it     true).
                                                   #2) Second is if email is correct which describe condition below.
                                                   #3) Third and list condition is when we enter phone number if it's less then 10,then it start again for entering number,but entered number has some value like we enter some 348056 which not 10-digit number ,so the condition (not phone) now it's false,But perviouse when not entered the number that time it ture can understand whole thing my friends.
            email = input("Enter email address: ").strip() # Email vaildation                        
                
                    
        # For number vaildation!
        if (email.find("@gmail.com")) and (len(email)>=11 and len(email)<=250):
            
            phone = input("Enter phone number: ").strip()   #Phone number vaildation            
            if not phone:
                continue
            phone_numbers.append(convert_string(phone))
            for numbers in phone_number_list:
                if int(phone)==numbers: #phone number type-cast beasuse it's by-default string.
                    print("User already exist")
                    return
                
            for i in phone:
                if i.isalpha():
                    co+=1
            print(co)    
            if co>0: 
                print("Please enter phone number correct format")
                co=0
            else:
                if len(phone)==10 :
                    break
                else:
                    print("Error:please enter 10 digit number correctly")     
                    
            
    address=input("Enter address:")
    contacts[name] = {"phone": phone_numbers, "email": email,"address":address}
    print(f"Contact '{name}' added successfully!")

# Search for a contact
def search_contact(contacts):
    name = input("Enter the name to search: ").strip()
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name].get('email', 'N/A')}")
        print(f"Phone: {contacts[name]['address']}")        
    else:
        print(f"Contact '{name}' not found!")

# Update an existing contact
def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").strip()
    if name in contacts:
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ").strip()
        email = input(f"Enter new email (current: {contacts[name].get('email', 'N/A')}): ").strip()
        address=input(f"Enter new address (current:{contacts[name]["address"]})").strip()
        contacts[name]['phone'] = [phone] or contacts[name]['phone']
        contacts[name]['email'] = email or contacts[name]['email']
        contacts[name]['address'] = address or contacts[name]['address']        
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found!")

# Delete a contact
def delete_contact(contacts):
    names=[]
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        data=(contacts[name])
        names.append(name)
        print(data)
        print(names)
        deleted_data(names,data)
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found!")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"  Phone: {int(convert_string(info['phone']))}")
            print(f"  Email: {info.get('email', 'N/A')}")
            print(f"  Address: {info.get("address")}")
            
            print("-" * 30)


# Main menu
def main():
    system("cls")
    contacts = load_contacts()
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
            wait_time(1.8)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
            wait_time(1.8)            
        elif choice == "5":
            view_contacts(contacts)
            wait_time(1.8)
            
        elif choice == "6":
            save_contacts(contacts)
            json_to_txt(contacts)                
            print("Contacts saved! Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")
            

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exit for program..")
   
   

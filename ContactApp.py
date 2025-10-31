# 📘 Contact Book App

contacts = {}  # Empty dictionary to store contacts

def display_contact(name, info):
    print(f"\n👤 Name: {name}")
    print(f"   Age: {info['Age']}")
    print(f"   Mobile: {info['Mobile']}")

while True:
    print('\n📖 Contact Book App')
    print('1. Create Contact')
    print('2. View Contact')
    print('3. Update Contact')
    print('4. Delete Contact')
    print('5. Search Contact')
    print('6. Count Contacts')
    print('7. Exit')

    choice = input('Enter your choice (1–7): ').strip()

    # 1️⃣ Create Contact
    if choice == '1':
        name = input('Enter name: ').strip()
        if name in contacts:
            print(f'⚠️ Name "{name}" already exists!')
        else:
            age = input('Enter age: ')
            mobile = input('Enter mobile number: ')
            contacts[name] = {'Age': age, 'Mobile': mobile}
            print(f'✅ Contact "{name}" created successfully!')

    # 2️⃣ View Contact (Exact match)
    elif choice == '2':
        name = input('Enter contact name to view: ').strip()
        if name in contacts:
            display_contact(name, contacts[name])
        else:
            print(f'❌ Contact "{name}" not found!')

    # 3️⃣ Update Contact
    elif choice == '3':
        name = input('Enter name to update: ').strip()
        if name in contacts:
            print(f"Current Details → Age: {contacts[name]['Age']}, Mobile: {contacts[name]['Mobile']}")
            new_age = input('Enter new age (leave blank to keep same): ').strip()
            new_mobile = input('Enter new mobile number (leave blank to keep same): ').strip()

            if new_age:
                contacts[name]['Age'] = new_age
            if new_mobile:
                contacts[name]['Mobile'] = new_mobile

            print(f'✅ Contact "{name}" updated successfully!')
        else:
            print(f'❌ Contact "{name}" not found!')

    # 4️⃣ Delete Contact
    elif choice == '4':
        name = input('Enter name to delete: ').strip()
        if name in contacts:
            del contacts[name]
            print(f'🗑️ Contact "{name}" deleted successfully!')
        else:
            print(f'❌ Contact "{name}" not found!')

    # 5️⃣ Search Contact (Partial match)
    elif choice == '5':
        search_name = input('Enter name to search: ').strip()
        found = False
        for name, info in contacts.items():
            if search_name.lower() in name.lower():
                display_contact(name, info)
                found = True
        if not found:
            print(f'❌ No contact found with "{search_name}".')

    # 6️⃣ Count Contacts
    elif choice == '6':
        print(f'📇 Total contacts saved: {len(contacts)}')

    # 7️⃣ Exit
    elif choice == '7':
        print('👋 Goodbye! Closing the Contact Book...')
        break

    # Invalid Input
    else:
        print('⚠️ Invalid choice! Please enter a number between 1 and 7.')

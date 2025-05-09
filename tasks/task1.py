users = []

def create_user(id, name, email):
    users.append({'id': id, 'name': name, 'email': email})

def read_users():
    for user in users:
        print(user)

def update_user(id, name, email):
    for user in users:
        if user['id'] == id:
            user['name'] = name
            user['email'] = email

def delete_user(id):
    for user in users:
        if user['id'] == id:
            users.remove(user)

while True:
    print("\n1. Create\n2. Read\n3. Update\n4. Delete\n5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        i = int(input("ID: "))
        n = input("Name: ")
        e = input("Email: ")
        create_user(i, n, e)
    elif choice == '2':
        read_users()
    elif choice == '3':
        i = int(input("ID to update: "))
        n = input("New name: ")
        e = input("New email: ")
        update_user(i, n, e)
    elif choice == '4':
        i = int(input("ID to delete: "))
        delete_user(i)
    elif choice == '5':
        break
    else:
        print("Invalid choice.")
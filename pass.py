def add_password():
    website = input("Website name: ")
    password = input("Password: ")
    
    # 'a' mane append mode, jate purono data muche na jay
    with open("passwords.txt", "a") as f:
        f.write(f"{website} | {password}\n")
    print("Successfully saved!")

def view_passwords():
    try:
        with open("passwords.txt", "r") as f:
            print("\n--- Your Saved Passwords ---")
            for line in f.readlines():
                print(line.strip())
    except FileNotFoundError:
        print("No passwords saved yet.")

# Main Loop
while True:
    mode = input("\nDo you want to (add) a new password, (view) existing ones, or (q)uit? ").lower()
    if mode == "q":
        break
    elif mode == "add":
        add_password()
    elif mode == "view":
        view_passwords()
    else:
        print("Invalid mode.")

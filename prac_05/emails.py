
def main():
    email_to_user = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        verification = input(f"Is your name {name}? (Y/n)")
        if verification.upper() != "Y" and verification != "":
            name = input("Name: ")
        email_to_user[email] = name
        email = input("Email: ")

    for email, name in email_to_user.items():
        print(f"{name} ({email})")

def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name

main()
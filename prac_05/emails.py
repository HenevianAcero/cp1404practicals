"""
CP1404 Practical 5
emails.py
Estimated time: 40 mins
Actual time: 1hr

"""


email_to_user = {}
def main():
    email = input("Email: ")
    while email != "":
        user = get_user_from_email(email)
        verification = input(f"Is your name {user}? [Y/n]")
        if verification.upper() != "Y" and verification != "":
            user = input("Enter name: ")
        email_to_user[email] = user
        email = input("Email: ")
    # email = email_to_user.get(user, 0)
    for email, user in email_to_user.items():
        print(f"{user} {email}")
def get_user_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    user = " ".join(parts).title()
    return user

main()
# La Casa de Papel

## Method

```
Word on the street is Bob's about to make a big withdrawal. Too bad you're the one holding his ID. Can you charm Alice into making the transfer before she catches on?

ncat --ssl la-casa-de-papel.chals.nitectf2024.live 1337
```

Python script provided for the menu: 

```python
import hashlib
import base64
import pyfiglet

def secret():
    return "XXXXXXXXXXXXXXXXXXXXX"  # Length = 21

def md5(secret, msg):
    hash = hashlib.md5(secret + msg).hexdigest().encode()
    return base64.b64encode(hash).decode()

def menu(secret):
    while True:
        print("\n1. Practice Convo")
        print("2. Let's Fool Alice!")
        print("3. Crack the Vault")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            practice_convo(secret)
        elif choice == '2':
            fool_alice(secret)
        elif choice == '3':
            crack_the_vault()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def practice_convo(secret):
    message = input("Send a message: ")
    hash = md5(secret, message.encode('latin-1'))
    print(f"Here is your encrypted message: {hash}")

def fool_alice(secret):
    print("\nBot: Okay, let's see if you're the real deal. What's your name?")
    user_name = input("Your name: ").encode('latin-1')
    user_name = user_name.decode('unicode_escape').encode('latin-1')
    print("\nBot: Please provide your HMAC")
    user_hmac = input("Your HMAC: ").encode('latin-1')

    if b"Bob" in user_name:
        hash = base64.b64decode(md5(secret, user_name))
        if user_hmac == hash:
            print("\nAlice: Oh hey Bob! Here is the vault code you wanted:")
            with open('secret.txt', 'r') as file:
                secret_content = file.read()
                print(secret_content)
        else:
            print("\nAlice: LIARRRRRRR!!")
    else:
        print("\nAlice: IMPOSTERRRR")

def crack_the_vault():
    print("\nVault Person: Enter password")
    passs = input("Password: ")

    with open('secret.txt', 'r') as file:
        secret_content = file.read().strip()
        if passs == secret_content:
            with open('flag.txt', 'r') as flag_file:
                flag_content = flag_file.read().strip()
                print(f"\nVault Unlocked! The flag is: {flag_content}")
        else:
            print("Incorrect password!")

if __name__ == "__main__":
    secret_key = secret().encode()
    ascii_art = pyfiglet.figlet_format("La Casa de Papel")
    print(ascii_art)
    menu(secret_key)
```

In this script we have multiple functions but this solve was pretty simple compared to the rest of crypto :'( it gave me lots of pain
I first tried to understand the script and the key to cracking it was looking at the ``md5`` function where it takes a supposed secret key and our message. It then combines our key and message. This is then returned as a base64 encoded string of the MD5 hash.

The practice convo essentially shows us how our input messages get encrypted as we are passing it to the ``md5`` function.


Now looking at the ``fool_alice()`` is where it gets intresting. This essentially checks to authenticate what we entered is *bob*. It asks for our username which should be ``Bob`` and a hmac. 

once it has authenticated our username as bob it makes a hash out of our user_name and secret and decodes it using base64. Now this hash is compared to the hmac we entered before and if its the same it accesses the secret.txt (as prompted it is the vault key) else it kicks us out.

Now in the ``crack_the_vault()`` it seems as though we just enter the vault passphrase from before and if authenticated then we recieve the flag.

Solving this now was fairly easy. We just need to find the base64 decoded output of ``md5`` function when we enter ``Bob`` as an input. 

So we first initiate a practice conversation entering ``Bob`` to see what the md5 function spits out.

```
1. Practice Convo 
2. Let's Fool Alice!
3. Crack the Vault 
4. Exit
Choose an option: 1
Send a message: Bob
Here is your encrypted message: YjRlMGE4MDI0MjhjYjM1ZjY5YzBlOTUyZDk2MTcyZDY=
```

Once we have the encrypted message we just need to find the base64 decoded of it.
I used [cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=WWpSbE1HRTRNREkwTWpoallqTTFaalk1WXpCbE9UVXlaRGsyTVRjeVpEWT0&oeol=FF)

Where i got the base64 decoded value of bob which is ``b4e0a802428cb35f69c0e952d96172d6``

Now i can just simulate a conversation with Alice by selecting option 2 for the flag.

```
1. Practice Convo 
2. Let's Fool Alice!
3. Crack the Vault 
4. Exit
Choose an option: 2

Bot: Okay, let's see if you're the real deal. What's your name?
Your name: Bob

Bot: Please provide your HMAC
Your HMAC: b4e0a802428cb35f69c0e952d96172d6

Alice: Oh hey Bob! Here is the vault code you wanted:
G0t_Th3_G0ld_B3rl1nale
```

Now from here i have the vault unlocker ``G0t_Th3_G0ld_B3rl1nale``

From here i can just pick option 3 to crack the vault returning me the flag.

```
1. Practice Convo 
2. Let's Fool Alice!
3. Crack the Vault 
4. Exit
Choose an option: 3

Vault Person: Enter password
Password: G0t_Th3_G0ld_B3rl1nale

Vault Unlocked! The flag is: nite{El_Pr0f3_0f_Prec1s10n_Pl4ns}
```

## Flag

> flag: nite{El_Pr0f3_0f_Prec1s10n_Pl4ns}
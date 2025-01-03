# Access Granted!

## Solving

```
First things first. MogamBro is so dumb that he might be using the same set of passwords everywhere, so lets try cracking his PC's password for some luck.
```
**Now for this challenge I Had to search up the flag format for this challenge which seems to be ``BITSCTF{<password>}``**


In this challenge we are expected to find the flag which is most probably the memory dump.

The reason we look here is because it contains everything that was in the computer's RAM at the time it was captured. Since the passwords for auth are loaded into memory when user's log in these credentials will also be found in the memory dumps.

When logging into a window's machine the system auths a user by loading an ``NT hash`` of the user's password. This is then used for verifying the user during login and for accessing network resources. 

For this we can use Volatility and get the full list of the hashes in the system

Now running this command ``vol -q -f memdump.mem windows.hashdump`` we get:

```
PS C:\Users\arygu\Aryan's files\Forensics\summer\summer\mogambro> vol -q -f memdump.mem windows.hashdump
Volatility 3 Framework 2.8.0

User    rid     lmhash  nthash

Administrator   500     aad3b435b51404eeaad3b435b51404ee        8a320467c7c22e321c3173e757194bb3
Guest   501     aad3b435b51404eeaad3b435b51404ee        31d6cfe0d16ae931b73c59d7e0c089c0
DefaultAccount  503     aad3b435b51404eeaad3b435b51404ee        31d6cfe0d16ae931b73c59d7e0c089c0
WDAGUtilityAccount      504     aad3b435b51404eeaad3b435b51404ee        74d0db3c3f38778476a44ff9ce0aefe2
MogamBro        1000    aad3b435b51404eeaad3b435b51404ee        8a320467c7c22e321c3173e757194bb3
PS C:\Users\arygu\Aryan's files\Forensics\summer\summer\mogambro>
```

From here we can see the password for ``MogamBro`` under nthash ``8a320467c7c22e321c3173e757194bb3`` which also seems to be the administrator password. Now to crack nthash we can use a password cracker like [CrackStation](https://crackstation.net/).

![image](https://github.com/user-attachments/assets/3adbf394-cc01-455a-a4cb-9984aae0bb29)

To which we get the password ``adolfhitlerrulesallthepeople`` which will be our flag encased in the **BITSCTF{}**

## Flag

> BITSCTF{adolfhitlerrulesallthepeople}

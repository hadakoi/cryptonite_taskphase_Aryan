# Lottery

## Solving

```
Now that you know the CVE, figure out how the attacker crafted the payload & executed it to compromise the 'secret'.
```
Considering the name of the challenge we see that it is based on the CVE that we examined in ``0.69 day`` where it uses the ``lottery.exe``

Using virusTotal we realise the file is packed using ``PyInstaller``

![image](https://github.com/user-attachments/assets/5d59238c-1bff-4c79-8291-292b5348550e)

We first use [pyinstxtractor](``https://github.com/extremecoders-re/pyinstxtractor``) to extract the contents of this Pyinstaller generated file

After extracting the ``.pyc`` file we can use [uncompyle6](``https://github.com/rocky/python-uncompyle6/``) to get our readable python source file back.

From here we obtain the source code for the encoding process that created secret.png.enc

```python
# uncompyle6 version 3.9.1
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.6.12 (default, Feb  9 2021, 09:19:15)
# [GCC 8.3.0]
# Embedded file name: lottery.py
import os, tempfile
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def generate_key():
    key = os.urandom(32)
    fp = tempfile.TemporaryFile(mode="w+b", delete=False)
    fp.write(key)
    return key


def encrypt_file(file_path, key):
    iv = b'urfuckedmogambro'
    with open(file_path, "rb") as file:
        data = file.read()
        padded_data = pad(data, AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_data = cipher.encrypt(padded_data)
    file.close()
    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    os.remove(file_path)


if __name__ == "__main__":
    key = generate_key()
    file_path = "secret.png"
    encrypt_file(file_path, key)
    print("Dear MogamBro, we are fucking your laptop with a ransomware & your secret image is now encrypted! Send $69M to recover it!")
```
What this script essentially does is encrypt a file in this case our ``secret.png`` using AES encryption in CBC cipher block chaining mode.

Now the intresting part of the script is we get a ``generate_key()`` function. Which generates a random 32 byte key creates a temp file to store the key and writes it into it. Normally tho this key would not be logged.

in the encrypt_file section we see the ``iv`` Initalization vector which is used for encryption luckily we already have this.

Now our job would be just to find the key. we know it was logged earlier in a temp file. As we had used this ``fp = tempfile.TemporaryFile(mode="w+b", delete=False)`` we understand that it will probably be logged here ``C:\Users\<username>\AppData\Local\Temp\`` as it creates the file in the system's default temporary directory. We also know that it Will have a size of **32**

Now searching here we find a 32 bit file with the hex ``FBF60E95C2F3C96F36E1195538E34E30CF1A290F1C14CD5E699E476A3BE2BC5E``.

![image](https://github.com/user-attachments/assets/83a48772-34ae-41b2-ae1d-c6554ccfe99e)

Now we have the ``IV = urfuckedmogambro`` and the ``key = FBF60E95C2F3C96F36E1195538E34E30CF1A290F1C14CD5E699E476A3BE2BC5E`` Now we can just use a online decrypter such as [**cyberchef**](https://gchq.github.io/CyberChef/#recipe=AES_Decrypt(%7B'option':'Hex','string':'FBF60E95C2F3C96F36E1195538E34E30CF1A290F1C14CD5E699E476A3BE2BC5E'%7D,%7B'option':'UTF8','string':'urfuckedmogambro'%7D,'CBC','Raw','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)Render_Image('Raw')&oeol=FF) where we can input it directly.

We can also have an option to render the image as it is which we choose to do so.

Hence we recieve the flag.

![image](https://github.com/user-attachments/assets/9c232c87-adb1-44c4-b9af-cdbc52a66519)

## Flag

> BITSCTF{1_r3c3ived_7h3_b0mbz}

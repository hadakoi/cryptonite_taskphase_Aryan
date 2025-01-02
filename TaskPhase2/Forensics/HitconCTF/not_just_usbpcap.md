# not just usbpcap

## Solving

```
I recorded one's USB traffic on his computer, can you find the hidden secret?
```

At first we look at the USB devices present here, where I bruteforced for devices using the filter item where i can enter filters for usb with ``usb.device_address  == x`` going through numbers 1 - whatever i feel where 

I find the first address of 9 being valid and it is a mouse. Now these inputs seem to be displaying mouse strokes for an optical Mouse.

![image](https://github.com/user-attachments/assets/bc26cea9-5322-4597-b632-0091696bd064)

Now i want to try and extract these keystrokes to see how they work for which I use this github repo [mouse-pcap-visualizer](https://github.com/WangYihang/USB-Mouse-Pcap-Visualizer)

``poetry run python usb-mouse-pcap-visualizer.py -i release-7ecaf64448a034214d100258675ca969d2232f54.pcapng.pcap -o data.csv``

However upon putting our ``.csv`` file into this [USB Mouse Pcap Visualizer](https://usb-mouse-pcap-visualizer.vercel.app/) all we get back is a bunch of gibberish ;-; so it would seem

![image](https://github.com/user-attachments/assets/50f25131-4ed5-4f2b-9613-6773d8877bcb)

Hence this is a bust now moving on to bruteforcing more usb devices the very next device ``usb.device_address  == 10`` seems to provide us with a keyboard of sorts.

![image](https://github.com/user-attachments/assets/1823a97f-cd83-4133-842e-c4d72301e7d7)

[USB-keyboard-Parser](https://github.com/TeamRocketIst/ctf-usb-keyboard-parser/tree/master) Using this i can extract and find out what was typed:

``tshark -r release-7ecaf64448a034214d100258675ca969d2232f54.pcapng -Y 'usbhid.data.key.variable' -T fields -e usbhid.data | sed 's/../:&/g2' > keyboard.data`` to extract the data of the keystrokes

From here i can run the 

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
KEY_CODES = {
    0x04:['a', 'A'],
    0x05:['b', 'B'],
    0x06:['c', 'C'],
    0x07:['d', 'D'],
    0x08:['e', 'E'],
    0x09:['f', 'F'],
    0x0A:['g', 'G'],
    0x0B:['h', 'H'],
    0x0C:['i', 'I'],
    0x0D:['j', 'J'],
    0x0E:['k', 'K'],
    0x0F:['l', 'L'],
    0x10:['m', 'M'],
    0x11:['n', 'N'],
    0x12:['o', 'O'],
    0x13:['p', 'P'],
    0x14:['q', 'Q'],
    0x15:['r', 'R'],
    0x16:['s', 'S'],
    0x17:['t', 'T'],
    0x18:['u', 'U'],
    0x19:['v', 'V'],
    0x1A:['w', 'W'],
    0x1B:['x', 'X'],
    0x1C:['y', 'Y'],
    0x1D:['z', 'Z'],
    0x1E:['1', '!'],
    0x1F:['2', '@'],
    0x20:['3', '#'],
    0x21:['4', '$'],
    0x22:['5', '%'],
    0x23:['6', '^'],
    0x24:['7', '&'],
    0x25:['8', '*'],
    0x26:['9', '('],
    0x27:['0', ')'],
    0x28:['\n','\n'],
    0x29:['[ESC]','[ESC]'],
    0x2a:['[BACKSPACE]', '[BACKSPACE]'],
    0x2C:[' ', ' '],
    0x2D:['-', '_'],
    0x2E:['=', '+'],
    0x2F:['[', '{'],
    0x30:[']', '}'],
    0x32:['#','~'],
    0x33:[';', ':'],
    0x34:['\'', '"'],
    0x36:[',', '<'],
    0x37:['.', '>'],
    0x38:['/', '?'],
    0x39:['[CAPSLOCK]','[CAPSLOCK]'],
    0x2b:['\t','\t'],
    0x4f:[u'→',u'→'],
    0x50:[u'←',u'←'],
    0x51:[u'↓',u'↓'],
    0x52:[u'↑',u'↑']
}


#tshark -r ./usb.pcap -Y 'usb.capdata' -T fields -e usb.capdata > keyboards.txt
def read_use(file):
    with open(file, 'r') as f:
        datas = f.read().split('\n')
    datas = [d.strip() for d in datas if d] 
    cursor_x = 0
    cursor_y = 0
    offset_current_line = 0
    lines = []
    output = ''
    skip_next = False
    lines.append("")
    for data in datas:
        shift = int(data.split(':')[0], 16) # 0x2 is left shift 0x20 is right shift
        key = int(data.split(':')[2], 16)

        if skip_next:
            skip_next = False
            continue
        
        if key == 0 or int(data.split(':')[3], 16) > 0:
            continue
        
        if shift != 0:
            shift=1
            skip_next = True
        
        if KEY_CODES[key][shift] == u'↑':
            lines[cursor_y] += output
            output = ''
            cursor_y -= 1
        elif KEY_CODES[key][shift] == u'↓':
            lines[cursor_y] += output
            output = ''
            cursor_y += 1
        elif KEY_CODES[key][shift] == u'→':
            cursor_x += 1
        elif KEY_CODES[key][shift] == u'←':
            cursor_x -= 1
        elif KEY_CODES[key][shift] == '\n':
            lines.append("")
            lines[cursor_y] += output
            cursor_x = 0
            cursor_y += 1
            output = ''
        elif KEY_CODES[key][shift] == '[BACKSPACE]':
            output = output[:-1]
            #lines[cursor_y] = output
            cursor_x -= 1
        else:
            output += KEY_CODES[key][shift]
            #lines[cursor_y] = output
            cursor_x += 1
    #print(lines)
    if lines == [""]:
        lines[0] = output
    if output != '' and output not in lines:
        lines[cursor_y] += output
    return '\n'.join(lines)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Missing file to read...')
        exit(-1)
    sys.stdout.write(read_use(sys.argv[1]))
```

as such we get this output

```shell
hadakoi@Laptop:~/ctfsolve/Test$ python3 script.py keyboard.data
rraaddiioo..cchhaall..hhiittccoonnccttff..ccoomm


Sssoorrrryy,,  nnoo  ffllaagg  hheerree..  Tttrryy  hhaarrddeerr..

Buutt  ii  ccaann  tteellll  yyoouu  tthhaatt  tthhee  ffllaagg  ffoorrmmaatt  iiss  hhiittccoonn{lloowweerr--ccaassee--eenngglliisshh--sseeppaarraatteedd--wwiitthh--ddaasshh}

Aggaaiinn,,  tthhiiss  iiss  nnoott  tthhee  ffllaagg  :(



C88776633!
hadakoi@Laptop:~/ctfsolve/Test$
```
So now we have the flag format. however we have gone through most of the usb devices and considering the name its not ``just`` usbpcap hence we have to also look at bluetooth devices.

We end up seeing the Pixel buds A series. 

![image](https://github.com/user-attachments/assets/863b1c7e-3fb7-4b40-99ae-3d7c8f45f17a)

Over here I sort it by Length where i can see that it is withinfact being sent in audio layers.

![image](https://github.com/user-attachments/assets/9f0d477a-fd50-43f5-9ff2-7d1f2a35d183)

From here i had to consult another writeup that gave me a fair idea on what to do: [writeup](https://github.com/10secTW/ctf-writeup/blob/0c9f9cdfb597d34133f7e82715d8be44a6eff119/2023/HITCON%20CTF/Not%20Just%20usbpcap/Not%20Just%20usbpcap.md) and another writeup [writeup2](https://zysgmzb.club/index.php/archives/271)

Over here we can find something called the ``Setconfig`` packet where we see that the audio is MPEF AAC LC 48000 Hz 2 channels format.

![image](https://github.com/user-attachments/assets/fbd820ee-9cc7-4194-9eb9-3824e503ca70)

Now upon looking at the starting packet header we see that it is ``47FC000B08C800300FFFF91`` followed by AAC audio data in the LATM format. Now these must be converted to ADTS headers ``FFF94C8052DFFC`` for playback.

![image](https://github.com/user-attachments/assets/54faaf6a-0959-42f4-9e18-ca37ea418a00)

As such we can first extract the LATM data

``tshark -r release-7ecaf64448a034214d100258675ca969d2232f54.pcapng -T fields -e data.data | sed '/^\s*$/d' > audio.txt``

After this we can design a script to convert the audio payload we got 

```python
# Open the audio.txt file for reading
with open('audio.txt', 'r') as f:
    # Open a new binary file ('output.latm') for writing
    with open('audio.latm', 'wb') as ff:
        for i in f:
            # Remove any spaces, newline characters, and colons from the hex string
            clean_hex = i.strip().replace(':', '')
            
            # Convert the cleaned hex string to bytes and prepend the fixed LATM header
            data = bytes.fromhex("FFF1108052DFFD") + bytes.fromhex(clean_hex)
            
            # Write the resulting bytes to the 'output.latm' file
            ff.write(data)
```

After this we can do a format conversion.

``ffmpeg -i audio.latm flag.wav``


Listening to the bluetooth audio:

```
Welcome back to "Secret Flags Unveiled" on HITCON Radio! I'm John, your host for this intriguing journey into the world of secret flags.

Today, we'll explore the secret flag, where flag served as vital information for scoring in CTFs.

The secret flags are crucial to the success of HITCON CTF, and one of them is going to be revealed. Listen carefully, you get only one chance.

Flag start.
secret flags unveiled with bluetooth radio.
Flag end.

Just simply wrap the text you heard with the flag format. If you find some information missing, just dig deeper in the packet.

Stay tuned for more secret flags. This is John, signing off from "Secret Flags Unveiled" on HITCON Radio. Keep those flags flying high!
```

Hence based on the format we have and the flag we got we can formulate our flag :D


## Flag

> hitcon{secret-flags-unveiled-with-bluetooth-radio}

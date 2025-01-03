# I'm wired in


## Solving

```
MogamBro got scared after knowing that his PC has been hacked and tried to type a SOS message to his friend through his 'keyboard'. Can you find the contents of that message, obviously the attacker was logging him!
```

We understand from this we need to possibly look for where keystrokes may have been logged.

Now looking in desktop we see they have provided us with a ``keylog.pcapng`` file which we need to use wireshark.

Now opening this in wireshark we see something intresting within the information ``URB_INTERRUPT``

![image](https://github.com/user-attachments/assets/a4beb354-20b8-46ab-9129-c1a616752f09)

Looking at the cases where it is going from host to destination we see that it always has a length of 35.

It also is transferring **HID** data sent from our keyboard. Now essentially we only have to look at these things.

**NOTE:** usb.transfer_type can identify interrupt transfers as we have seen before.

The filter **usb.transfer_type == 0x1** identifies interrupt transfers from the keyboard to the device

The filter **frame.len == 35** ensures we are only capturing packets that match the expected size of HID reports.

We can also condition **!(usb.capdata==00:00:00:00:00:00:00:00)** ensures we exclude empty or invalid reports, leaving only meaningful data.

so we end up with a filter on wireshark as ``usb.transfer_type == 0x1 and frame.len == 35 and !(usb.capdata==00:00:00:00:00:00:00:00)``

Hence after this filter is applied we can then create a new pcapng with just these packets.

Now i use this and make my own script and command as i have a pcappng file that is only with the important data.
[Keyboard-Parser](https://github.com/TeamRocketIst/ctf-usb-keyboard-parser/tree/master)

we can use this command script 

``tshark -r sorted.pcapng -Y 'usb.data_len == 8' -T fields -e usb.capdata -E separator=: | python3 script.py``

With this as the script


```python
# USB HID Keycode to Character Mapping (with lowercase and uppercase)
HID_MAP = {
    0x04: ['a', 'A'], 0x05: ['b', 'B'], 0x06: ['c', 'C'], 0x07: ['d', 'D'],
    0x08: ['e', 'E'], 0x09: ['f', 'F'], 0x0A: ['g', 'G'], 0x0B: ['h', 'H'],
    0x0C: ['i', 'I'], 0x0D: ['j', 'J'], 0x0E: ['k', 'K'], 0x0F: ['l', 'L'],
    0x10: ['m', 'M'], 0x11: ['n', 'N'], 0x12: ['o', 'O'], 0x13: ['p', 'P'],
    0x14: ['q', 'Q'], 0x15: ['r', 'R'], 0x16: ['s', 'S'], 0x17: ['t', 'T'],
    0x18: ['u', 'U'], 0x19: ['v', 'V'], 0x1A: ['w', 'W'], 0x1B: ['x', 'X'],
    0x1C: ['y', 'Y'], 0x1D: ['z', 'Z'], 0x1E: ['1', '!'], 0x1F: ['2', '@'],
    0x20: ['3', '#'], 0x21: ['4', '$'], 0x22: ['5', '%'], 0x23: ['6', '^'],
    0x24: ['7', '&'], 0x25: ['8', '*'], 0x26: ['9', '('], 0x27: ['0', ')'],
    0x28: ['\n', '\n'], 0x29: ['[ESC]', '[ESC]'], 0x2A: ['[BACKSPACE]', '[BACKSPACE]'],
    0x2C: [' ', ' '], 0x2D: ['-', '_'], 0x2E: ['=', '+'], 0x2F: ['[', '{'],
    0x30: [']', '}'], 0x32: ['#', '~'], 0x33: [';', ':'], 0x34: ['\'', '"'],
    0x36: [',', '<'], 0x37: ['.', '>'], 0x38: ['/', '?'], 0x39: ['[CAPSLOCK]', '[CAPSLOCK]'],
    0x2B: ['\t', '\t'], 0x4F: [u'→', u'→'], 0x50: [u'←', u'←'], 0x51: [u'↓', u'↓'],
    0x52: [u'↑', u'↑']
}

# Function to decode keystrokes
def decode_keystrokes(file_path):
    decoded_text = ""
    shift_pressed = False

    with open(file_path, "r") as file:
        for line in file:
            hex_bytes = line.strip().split(':')
            modifier = int(hex_bytes[0], 16)
            keycode = int(hex_bytes[2], 16)

            # Check if Shift is pressed (left or right)
            shift_pressed = (modifier & 0x02) != 0

            if keycode in HID_MAP:
                char = HID_MAP[keycode][1] if shift_pressed else HID_MAP[keycode][0]
                decoded_text += char

    return decoded_text

# Main execution
if __name__ == "__main__":
    keystrokes_file = "keystrokes.txt"
    result = decode_keystrokes(keystrokes_file)
    print("Decoded Text:")
    print(result)
```

This all outputs -> 

```shell
hadakoi@Laptop:~/ctfsolve$ tshark -r sorted.pcapng -Y 'usb.data_len == 8' -T fields -e usb.capdata -E separator=: | python3 script1.py
Decoded Text:
I haveebeen haakee  !!!
HELLMEE
BITSCTF{I_-7h1nk_th3y_4Re_k3yl0991ng_ME!}
```

[YT video for Something Similar](https://www.youtube.com/watch?v=EnOgRyio_9Q)

## Flag

> BITSCTF{I_-7h1nk_th3y_4Re_k3yl0991ng_ME!}

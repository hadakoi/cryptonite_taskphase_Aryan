# spelling-quiz

## Method

```
I found the flag, but my brother wrote a program to encrypt all his text files. 
He has a spelling quiz study guide too, but I don't know if that helps.

```

In this challenge we are provided a zip folder that contains 3 files.

``studyguide.txt``, ``encrypt.py``, ``flag.txt``

The python file:
```python
import random
import os

files = [
    os.path.join(path, file)
    for path, dirs, files in os.walk('.')
    for file in files
    if file.split('.')[-1] == 'txt'
]

alphabet = list('abcdefghijklmnopqrstuvwxyz')
random.shuffle(shuffled := alphabet[:])
dictionary = dict(zip(alphabet, shuffled))

for filename in files:
    text = open(filename, 'r').read()
    encrypted = ''.join([
        dictionary[c]
        if c in dictionary else c
        for c in text
    ])
    open(filename, 'w').write(encrypted)
```

Flag: ``brcfxba_vfr_mid_hosbrm_iprc_exa_hoav_vwcrm``

The ``studyguide.txt`` contains nearly 272543 lines of text with 3178401 chars.

From the source code of the encrypt.py file seems to encrypt all ``.txt`` files in the directory and its subdirectories replacing each letter of the alphabet with a randomly shuffled letter.

The entire process goes like this:

1. Creates a list of letters of the alphabet. 

2. It then shuffles them all randomly. 

3. From here it creates a type of dictionary to match each letter to a shuffled one. for e.g ``a`` in plain text is mapped to ``b`` in cipher text. meaning all *a* present in the text file before encryption become ``b`` after.

4. Then using this ``key`` of sorts it encrypts the text files present in the directories the script file is in.

From this we understand that it is a ``Monoalphabetic Substitution Cipher``

Meaning 1 letter is mapped to another. and theres no specific order like in caeser cipher where its just a shift.


To solve this hence i can use a [Monoalphabetic Substitution Cipher](https://www.guballa.de/substitution-solver)

I can give a couple lines of the study plan then the flag at the end hence solving it. 

The more lines of the studyguide I would provide there is a better frequency distribution it can look at and compare. Essentially using statistics of how many times letter has appeared and trying random combinations it solves it.

hence i enter

```
icgocnfwnwtr
sxlyrxaic
dcrrtfrxcv
uxbvwavcq
lwvicwtiwm
pwtmwnxvicq
avingciisa
ylwtmrcawx
mwaxdcrrxuwlwvq
yciflwnf
mwaxsrtwvq
iovabxcabqwtd
bcrwtnlwtxvwit
srlxtwkwtd
bcriurmwrtv
nflicxlyicsxswmr
titrlrnvcilqvwn
xanrcvxwtxulr
vficxniblxavwra
bwttxnlrv
bxbrcerwdfva
wtnxctxvwit
titborcwlwvq
otbcrywtrm
ucxaalwgr
vcxtabiawvwpr
dlqnrcil
wmilxvcwkrc
fqbrcixcvwx
brcwsrmollxcq
crtmwvwit
sitavcwnwmr
rzvcxabrnvcxl
sitosrtvxllq
nfilrfrsxvwt
iprccrxlwas

brcfxba_vfr_mid_hosbrm_iprc_exa_hoav_vwcrm
```

To recieve: 

```
orkurchicine
malfeasor
greenheart
baptistry
litorinoid
vindicatory
stockrooms
flindersia
disagreeability
frohlich
disamenity
outsparspying
preinclination
melanizing
preobedient
chloralformamide
nonelectrolytic
ascertainable
thoracoplasties
pinnaclet
paperweights
incarnation
nonpuerility
unprefined
brasslike
transpositive
glycerol
idolatrizer
hyperoartia
perimedullary
rendition
monstricide
extraspectral
monumentally
cholehematin
overrealism

perhaps_the_dog_jumped_over_was_just_tired
```

At the end then we see our flag.


## Flag

> picoCTF{perhaps_the_dog_jumped_over_was_just_tired}
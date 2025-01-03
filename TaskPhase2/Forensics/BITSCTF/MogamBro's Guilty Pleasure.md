# MogamBro's Guilty Pleasure

## Solving

```
MogamBro was spammed with a lot of emails, he was able to evade some but fell for some of them due to his greed. Can you analyze the emails & figure out how he got scammed, not once but twice!
```

Back in the emails folder we ended up seeing this email as well

``50% Discount available on the Mimikyu plushie.eml``

Opening it we see a large amount of text 

![image](https://github.com/user-attachments/assets/f8b3d5e6-f9a3-4b29-bc65-d8de634572c0)

```
Dear Friend , We know you are interested in receiving
red-hot information . We will comply with all removal
requests . This mail is being sent in compliance with
Senate bill 1622 , Title 9 ; Section 305 . THIS IS
NOT MULTI-LEVEL MARKETING ! Why work for somebody else
when you can become rich as few as 24 weeks ! Have
you ever noticed nearly every commercial on television
has a .com on in it plus nearly every commercial on
television has a .com on in it ! Well, now is your
chance to capitalize on this ! WE will help YOU deliver
goods right to the customer's doorstep and deliver
goods right to the customer's doorstep ! You can begin
at absolutely no cost to you . But don't believe us
! Mrs Jones of New Mexico tried us and says "I've been
poor and I've been rich - rich is better" ! We are
licensed to operate in all states . We IMPLORE you
- act now ! Sign up a friend and you get half off !
Thanks . Dear Salaryman ; Your email address has been
submitted to us indicating your interest in our letter
. If you no longer wish to receive our publications
simply reply with a Subject: of "REMOVE" and you will
immediately be removed from our mailing list . This
mail is being sent in compliance with Senate bill 1627
, Title 6 , Section 303 . This is not multi-level marketing
. Why work for somebody else when you can become rich
as few as 70 WEEKS ! Have you ever noticed people love
convenience and most everyone has a cellphone ! Well,
now is your chance to capitalize on this . WE will
help YOU process your orders within seconds plus turn
your business into an E-BUSINESS . You are guaranteed
to succeed because we take all the risk . But don't
believe us ! Prof Ames of Louisiana tried us and says
"I've been poor and I've been rich - rich is better"
! We are licensed to operate in all states . Do not
delay - order today ! Sign up a friend and you'll get
a discount of 50% . Thank-you for your serious consideration
of our offer . 
```

Now from this after putting into a cipher Indentifier we can get a fair idea that it is stegnography.

We can also confirm this by just searching up any of the bill xxxx, Title x, Section xxx which leads to articles of steganography.

Which essentially leads us to understand that there is a message hidden within this text.

From here we understand this is basically spam is essentially asking us to decode the spam hence we use this decoder [``spammimic``](https://www.spammimic.com/decode.shtml)

hence returning us our flag ``BITSCTF{sp4m_2_ph1sh_U}�``

## Flag

> BITSCTF{sp4m_2_ph1sh_U}

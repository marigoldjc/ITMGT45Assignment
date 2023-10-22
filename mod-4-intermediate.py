#!/usr/bin/env python
# coding: utf-8

# ### Assingment: Python (Intermediate)
# #### Thinking Like a Programmer
# ##### Shift Letter

# In[33]:


def shift_letter(letter, shift): 
    result = "" 
    for char in letter:  
         if char.isupper(): 
            result += chr((ord(char) + shift - 65) % 26 + 65)
         else: 
            result += char 
    return result 


# In[45]:


letter = str(input("Letter: "))
if letter == " ":
    shift = str(input("Number of shifts: "))
else:
    shift = int(input("Number of shifts: "))
        
if letter == " " and shift == "_":
    print(" ")
else:
    lettershift = shift_letter(letter, shift)
    print(lettershift)


# ##### Ceasar Cipher

# In[48]:


def ceasar_cipher(message, shift):
    result = "" 
    for char in message: 
        if char.isalpha(): 
            if char.isupper(): 
                result += chr((ord(char) + shift - 65) % 26 + 65) 
            else: 
                result += chr((ord(char) + shift - 97) % 26 + 97) 
        else: 
            result += char 
    return result 


# In[49]:


message = str(input("String of uppercase English letters and spaces: "))
shift = int(input("Number of shifts: "))

ceasar = ceasar_cipher(message, shift)
print(ceasar)


# ##### Shift By Letter

# In[157]:


def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "  # If the letter is a space, return it as is.

    letter_value = ord(letter) - ord("A")
    shift_value = ord(letter_shift) - ord("A")

    shifted_value = (letter_value + shift_value) % 26
    shifted_letter = chr(shifted_value + ord("A"))

    return shifted_letter


# In[158]:


letter = str(input("Letter: "))
letter_shift = str(input("Letter for shifting: "))

result = shift_by_letter(letter, letter_shift)
print(str(result))


# ##### Vigenere Cipher

# In[16]:


def vigenere_cipher(message, key):
    vigenere_cipher = []
    message = message.upper()
    key = key.upper()
    
    key_repeated = key
    while len(key_repeated) < len(message):
        key_repeated += key
        
    for i in range(len(message)):
        if message[i] == " ":
            vigenere_cipher.append(" ")
        else:
            x = (ord(message[i])+ ord(key[i])) % 26
            x += ord('A')
            vigenere_cipher.append(chr(x))
    return("".join(vigenere_cipher))


# In[17]:


message = str(input("Message: "))
key = str(input("Key: "))
vigenere = vigenere_cipher(message, key)
print(vigenere)


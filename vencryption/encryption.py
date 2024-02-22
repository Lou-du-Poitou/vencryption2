## Vencryption (c) 2024 - Made by V / Lou du Poitou ##
##
# GitHub => https://github.com/Lou-du-Poitou/
# Python => https://pypi.org/user/lou_du_poitou/
# Link => https://encryption.nexcord.pro/
##

# --- --- --- #
## HELP COMMAND ##
def help(category:str=None) -> None:
    try:
        if category == None:
            print(f"\nVENCRYPTION module --> HOME: \n ------- \nYou just used the command: help(category:str=None)\nThe different categories are: \n ------- \n 1 ==> Crypt \n 2 ==> Decrypt \n 3 ==> Hach \n 4 ==> Key \n 0 ==> Exit \n ------- \n Made by V / Lou du Poitou - Vencryption (c) 2024 \n ------- \n")
            cat = str(input(">>> Which category do you want help with ? "))
            help(cat)
        elif category == "1" or category.lower().strip() == "crypt":
            print("\nVENCRYPTION module --> CRYPT: \n ------- \nEncrypts a string based on one key.\nSyntax :\n ------- \n crypt(text:bytes, key:str) -> bytes \n\n text: Your encoded text\n key: Character string \n ------- \n Made by V / Lou du Poitou - Vencryption (c) 2024 \n ------- \n")
            cat = str(input(">>> Which category do you want help with ? "))
            help(cat)
        elif category == "2" or category.lower().strip() == "decrypt":
            print("\nVENCRYPTION module --> CRYPT: \n ------- \nAllows you to decrypt a string based on one key.\nSyntax :\n ------- \n decrypt(text:bytes, key:str) -> bytes \n\n text: Your encoded text\n key: Character string \n ------- \n Made by V / Lou du Poitou - Vencryption (c) 2024 \n ------- \n")
            cat = str(input(">>> Which category do you want help with ? "))
            help(cat)
        elif category == "3" or category.lower().strip() == "hach":
            print("\nVENCRYPTION module --> HACH: \n ------- \nGet hash key of a text.\nSyntax :\n ------- \n getHach(text:str) -> str \n\n text: Character string \n ------- \n Made by V / Lou du Poitou - Vencryption (c) 2024 \n ------- \n")
            cat = str(input(">>> Which category do you want help with ? "))
            help(cat)
        elif category == "4" or category.lower().strip() == "key":
            print("\nVENCRYPTION module --> KEY: \n ------- \nFunction used by the program to generate a key.\nSyntax :\n ------- \n createKey(text:str) -> list \n\n text: Character string \n ------- \n Made by V / Lou du Poitou - Vencryption (c) 2024 \n ------- \n")
            cat = str(input(">>> Which category do you want help with ? "))
            help(cat)
        elif category == "0" or category.lower().strip() == "exit":
            print("\nVENCRYPTION module --> EXIT: \n ------- \nYou just left the help command\n Going back ?\n ------- \n ==> help(category:str=None) \n ------- \n")
            pass
        else:
            print(f"\nVENCRYPTION module --> HOME: \n ------- \nYou just used the command: help(category:str=None)\nThe different categories are: \n ------- \n 1 ==> Crypt \n 2 ==> Decrypt \n 3 ==> Hach \n 4 ==> Key \n 0 ==> Exit \n ------- \n Made by V / Lou du Poitou - Vencryption (c) 2024 \n ------- \n")
            cat = str(input(">>> Which category do you want help with ? "))
            help(cat)
        return None
    except Exception as e:
        raise Exception(f"[v-encryption] - An error has occurred --> {e}")
## ##
# --- --- --- #

# --- --- --- #

def createKey(text:str) -> list:
    try:
        if len(text) < 16: text += "0000000000000000"
        key = [list(), list()]
        key[0][:0] = str(text[::len(text)//16])[:16]
        key[1][:0] = str(text[::-(len(text)//16)])[:16]
        result = [list(), list()]
        for i in range(0, 16):
            result[0].append((ord(key[0][i])+i^(len(text)%100))%10)
            result[1].append((ord(key[1][i])+i^(len(text)%100))%10)
        return result
    except Exception as e:
        raise Exception(f"[v-encryption] - An error has occurred --> {e}")

# --- --- --- #

def getHach(text:str) -> str:
    try:
        if len(text) < 16: text += "0000000000000000"
        e = createKey(text)
        result = str()
        for i in range(0, 16):
            result += str(e[0][i])
            result += str(e[1][i])
        return result
    except Exception as e:
        raise Exception(f"[v-encryption] - An error has occurred --> {e}")

# --- --- --- #
# --- --- --- #

def crypt(text:bytes, key:str) -> bytes:
    try:
        key = createKey(key)
        result = list()
        for i in range(0, len(text)):
            result.append(text[i]^(key[0][i%16]+key[1][i%16]+i%10))
        return bytes(result)
    except Exception as e:
        raise Exception(f"[v-encryption] - An error has occurred --> {e}")

# --- --- --- #

def decrypt(text:bytes, key:str) -> bytes:
    try:
        key = createKey(key)
        result = list()
        for i in range(0, len(text)):
            result.append(text[i]^(key[0][i%16]+key[1][i%16]+i%10))
        return bytes(result)
    except Exception as e:
        raise Exception(f"[v-encryption] - An error has occurred --> {e}")

# --- --- --- #

## Vencryption (c) 2024 - Made by V / Lou du Poitou ##
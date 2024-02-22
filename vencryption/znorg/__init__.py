# (dé)cryptage (c) 2023 -- V / Lou du Poitou -- https://encryption.nexcord.pro/ #

try:
    import requests
except Exception as e:
    raise Exception(f"[v-encryption] - An error has occurred --> {e}")

url = "https://encryption.nexcord.pro"

def help(category:str=None):
    try:
        if category == None:
            print(f"\nENCRYPTION module --> HOME: \n ------- \nYou just used the command: help(category:str=None)\nThe different categories are: \n ------- \n 1 ==> Crypt \n 2 ==> Decrypt \n 0 ==> Exit \n ------- \n Link of the software : \n {url}/ \n ------- \n")
            cat = str(input(">>> Which category do you want help with ? "))
            help(cat)
        elif category == "1" or category.lower().strip() == "crypt":
            print("\nENCRYPTION module --> CRYPT: \n ------- \nEncrypts a string based on different keys.\nSyntax :\n ------- \n crypt(phrase:str, key1:int, key2:int, text:str = None)\n\n sentence: Character string between 0 and 500\n key1: Number between 1 and 9\n key2: Number between 1 and 9\n text: Character string between 0 and 80 \n ------- \n")
            cat = str(input(">>> Which category do you want help with ? "))
            help(cat)
        elif category == "2" or category.lower().strip() == "decrypt":
            print("\nENCRYPTION module --> DECRYPT: \n ------- \nAllows you to decrypt a string based on different keys.\nSyntax :\n ------- \n decrypt(phrase:str, key1:int, key2:int, text:str = None)\n\n sentence: Character string between 0 and 2000\n key1: Number between 1 and 9\n key2: Number between 1 and 9\n text: Character string between 0 and 80\n ------- \n")
            cat = str(input(">>> Which category do you want help with ? "))
            help(cat)
        elif category == "0" or category.lower().strip() == "exit":
            print("\nENCRYPTION module --> EXIT: \n ------- \nYou just left the help command\n Going back ?\n ------- \n ==> help(category:str=None) \n ------- \n")
            pass
        else:
            print(f"\nENCRYPTION module --> HOME: \n ------- \nYou just used the command: help(category:str=None)\nThe different categories are: \n ------- \n 1 ==> Crypt \n 2 ==> Decrypt \n 0 ==> Exit \n ------- \n Link of the software : \n {url}/ \n ------- \n")
            cat = str(input(">>> Which category do you want help with ? "))
            help(cat)
    except Exception as e:
        raise Exception(f"[v-encryption] - An error has occurred --> {e}")

def crypt(phrase:str, key1:int, key2:int, text:str = None):
    try:
        if int(key1) > 9 or int(key1) < 0 or int(key2) > 9 or int(key2) < 0: raise Exception("Invalid key(s) !")
        elif phrase == None or len(phrase) > 500: raise Exception("Invalid sentence !")
        elif text:
            if len(text) > 80: raise Exception("Invalid text !")

        data = {
            "phrase": phrase,
            "key1": key1,
            "key2": key2,
            "text": text
        }

        headers = {
            'Content-Type': 'application/json'
        }

        try:
            r = requests.post(f"{url}/api/crypt", json=data, headers=headers)
            response = r.json()["response"]
        except:
            response = None
        return response
    except Exception as e:
        raise Exception(f"[v-encryption] - An error has occurred --> {e}")

def decrypt(phrase:str, key1:int, key2:int, text:str = None):
    try:
        if int(key1) > 9 or int(key1) < 0 or int(key2) > 9 or int(key2) < 0: raise Exception("Invalid key(s) !")
        elif phrase == None or len(phrase) > 2000: raise Exception("Invalid sentence !")
        elif text: 
            if len(text) > 80: raise Exception("Invalid text !")

        data = {
            "phrase": phrase,
            "key1": key1,
            "key2": key2,
            "text": text
        }

        headers = {
            'Content-Type': 'application/json'
        }

        try:
            r = requests.post(f"{url}/api/decrypt", json=data, headers=headers)
            response = r.json()["response"]
        except:
            response = None
        return response
    except Exception as e:
        raise Exception(f"[v-encryption] - An error has occurred --> {e}")
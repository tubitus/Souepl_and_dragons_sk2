#----------KÓD PRO ŠIFRU----------
 
def caesar(text, posun_pro_caesar):
    result = ""
 
    for char in text:
        if char.lower() in abeceda:
            is_upper = char.isupper()
            idx = abeceda.index(char.lower())
            new_idx = (idx + posun_pro_caesar) % len(abeceda)
            new_char = abeceda[new_idx]
            result += new_char.upper() if is_upper else new_char
        else:
            result += char
    return result
 
def text_to_hex(text):
    hex_output = ' '.join(format(ord(c), 'x') for c in text)
    return hex_output

def mission_print(počet):
    global i
    if i<len(sifra_list):
        print(str(i+1) + ". část šifry je " + sifra_list[počet])  # Převod `i` na string
        i = i + 1  # Zvýšení hodnoty `i`
    else:
        print("NEMAM")

 
#----------CUSTOM INPUT PRO ŠIFRU----------
final_text_šifry = input("Zadejte šifru: ")
posun_pro_caesar = len(final_text_šifry)
#------------------------------------------
 
abeceda = "aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyýzž"
caesar_šifra = caesar(final_text_šifry, posun_pro_caesar)
hex = text_to_hex(final_text_šifry)
special = text_to_hex(caesar_šifra)
i = 0
 
 
print(f"Původní text: {final_text_šifry}")
print(f"Caesarova šifra (posun_pro_caesar {posun_pro_caesar}): {caesar_šifra}")
print(f"Hex: {hex}")
print(f"komplet: {special}")
 
#---------VÝPIS ZNAKŮ POSTUPNĚ Z ŠIFRY-----  
sifra_list = []
sifra_list = special.split()
print(sifra_list)
print(sifra_list[0])
print(len(sifra_list))
#------------------------------------------
mission_print(i)
mission_print(i)
mission_print(i)
mission_print(i)
mission_print(i)
mission_print(i)
mission_print(i)
txt_to_defypher=input("Zadej text šifry: ")
posun_po_ceasar_user=input("Zadej posun o kolik: ")
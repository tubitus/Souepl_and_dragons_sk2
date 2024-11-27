#----------KÓD PRO ŠIFRU----------
 
def caesar(text, posun_pro_caesar):
    abeceda = "aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyýzž"
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
 
#----------CUSTOM INPUT PRO ŠIFRU----------
final_text_šifry = input("Zadejte šifru: ")
posun_pro_caesar = len(final_text_šifry)
#------------------------------------------
 
caesar_šifra = caesar(final_text_šifry, posun_pro_caesar)
hex = text_to_hex(final_text_šifry)
special = text_to_hex(caesar_šifra)
 
 
print(f"Původní text: {final_text_šifry}")
print(f"Caesarova šifra (posun_pro_caesar {posun_pro_caesar}): {caesar_šifra}")
print(f"Hex: {hex}")
print(f"komplet: {special}")
 
#---------VÝPIS ZNAKŮ POSTUPNĚ Z ŠIFRY-----  
sifra_list = []
sifra_list = special.split()
print(sifra_list)
print(sifra_list[0])
#------------------------------------------
 
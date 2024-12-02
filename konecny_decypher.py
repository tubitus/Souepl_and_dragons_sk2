def caesar_zpet_na_text():
    result = ""
    for char in txt_to_defypher:
        if char.lower() in abeceda:
            is_upper = char.isupper()
            idx = abeceda.index(char.lower())
            new_idx = (idx - posun_po_ceasar_user) % len(abeceda)
            new_char = abeceda[new_idx]
            result += new_char.upper() if is_upper else new_char
        else:
            result += char  # Nezměněné znaky, které nejsou v abecedě
    return result

# Vstupní data
abeceda = "aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyýzž"
decypher = "šimon"

# Posunutí textu
txt_to_defypher = input("Zadej text šifry: ")
posun_po_ceasar_user = int(input("Zadej posun o kolik: "))  # Převod na int
posunuty_text = caesar_zpet_na_text()
print(f"Text po posunu o {posun_po_ceasar_user} zpátky: {posunuty_text}")
if decypher==posunuty_text:
    print("Správně si rozšifroval tajomnou")
else:
    print("Tvé rozluštění šifry bylo nezprávné, zkus to znovu.")

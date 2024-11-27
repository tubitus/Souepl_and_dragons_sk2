import random
 
# Seznam postav
characters = [
    "Jakub Kovařík (Cyclop + Kentaur)",
    "Daniel Šedivec (Ošklivý Ork)",
    "Šimík (Malý elf)",
    "Engineer (Mechanický Golem)"
]
 
# Seznam misí
missions = [
    "Zjisti, kdo rozbil okno v laboratoři!",
    "Objev tajemství učitelova sešitu!",
    "Zjisti, proč učitel matematiky nechce vynášet známky!",
    "Pomoz Šimikovi sehnat med!",
    "Získání starých knih o kouzlech v knihovně!",
    "Zlom tajnou šifru ve škole!",
    "Získej odpovědi na testy z deníku!"
]
 
# Seznam situací
situations = [
    "Potkáš Jakuba Kovaříka, který tě vyzve k odpovědím na jeho otázky.",
    "Zanesený ředitel má tajemství, které tě zavede k deníku.",
    "Daniel Šedivec tě přistihne a musíš se schovat!",
    "Šimík ti pomůže, pokud najdeš med!",
    "Engineer tě zablokuje a musíte najít způsob, jak ho porazit."
]
 
# Funkce pro generování náhodné mise
def generate_mission():
    mission = random.choice(missions)
    character = random.choice(characters)
    situation = random.choice(situations)
    print(f"Vaše mise: {mission}")
    print(f"Postava, kterou potkáte: {character}")
    print(f"Situace: {situation}")
 
# Vygenerování mise
generate_mission()
import random
 
# Definice otázek a odpovědí
quiz_questions = [
    {
        "question": "Kolik let je této škole?",
        "options": ["a) 69 let", "b) 81 let", "c) 73 let", "d) 56 let"],
        "answer": "c"
    },
    {
        "question": "Jaký předmět učí Jakub Kovařík, nebo-li Cyclop a Kentaur?",
        "options": ["a) Matematika", "b) Webovky", "c) Programování", "d) Tělocvik"],
        "answer": "c"
    },
    {
        "question": "Co musíš najít, aby ti Šimík, malý elf, pomohl?",
        "options": ["a) Klíč", "b) Med", "c) Kouzelnou hůlku", "d) Mlíko od táty"],
        "answer": "b"
    },
    {
        "question": "Kde se ukrývá tajemný deník podle pověstí?",
        "options": ["a) V ředitelně", "b) Ve staré knihovně", "c) V tajném podzemí školy", "d) V laboratoři chemie"],
        "answer": "c"
    },
    {
        "question": "Kolik tajných chodeb se údajně nachází v této škole?",
        "options": ["a) 3", "b) 5", "c) 7", "d) 10"],
        "answer": "c"
    },
    {
        "question": "Šifra: V laboratoři chemie najdeš následující zápis: H2O + ? = H2O2. Co musíš přidat?",
        "options": ["a) Kyslík", "b) Vodík", "c) Dusík", "d) Uhlík"],
        "answer": "a"
    },
    {
        "question": "Proč se Dáša obrátila k temné magii?",
        "options": ["a) Aby získala moc na ochranu svých přátel.", "b) Kvůli touze ovládnout školu a ostatní mágy.",
                    "c) Z pomsty vůči škole za její vyloučení.", "d) Trauma z sexuálního zneužití."],
        "answer": "a"
    },
    {
        "question": "Proč Ježíš tak pevně věří ve staré zákony školy?",
        "options": ["a) Je ze staré školy.", "b) Je línej věřit v jiné.",
                    "c) Bojí se změn a odmítá moderní způsoby.", "d) Závazal se přísahou, kterou nemůže porušit."],
        "answer": "b"
    }
]
 
# Hlavní třída hry
class TajemnaSkola:
    def __init__(self):
        self.health = 100
        self.inventory = []
        self.current_mission = 0
        self.remaining_questions = quiz_questions.copy()
        self.mission_items = [
            {"item": "Med"},
            {"item": "Elixír klidu"},
            {"item": "Kouzelná hůlka"},
            {"item": "Tajemný deník"},
            {"item": "Klíč k trezoru"},
            {"item": "Mapa podzemí"},
            {"item": "Starožitný amulet"},
            {"item": "Rukopis staré knihy"}
        ]
 
    def start(self):
        print("Vítejte v 'Tajemné škole a Deníku Rebelů'!")
        print("Vaším cílem je dokončit mise a získat tajemný deník.\n")
        while self.current_mission < 8 and self.health > 0:
            self.main_menu()
        if self.health > 0:
            self.end_game()
        else:
            print("\nBohužel jste zemřeli během hledání deníku. Konec hry.")
 
    def main_menu(self):
        print("\n--- Hlavní menu ---")
        print(f"Mise: {self.current_mission + 1}/8 | Zdraví: {self.health}")
        print("1. Prozkoumat nové místo (spustit misi)")
        print("2. Zkontrolovat inventář")
        print("3. Ukončit hru")
        choice = input("> ")
        if choice == "1":
            self.explore()
        elif choice == "2":
            self.check_inventory()
        elif choice == "3":
            print("Ukončili jste hru. Díky za hraní!")
            exit()
        else:
            print("Neplatná volba, zkuste to znovu.")
 
    def explore(self):
        if self.current_mission >= 8:
            print("Dokončili jste všechny mise!")
            return
 
        mission = self.mission_items[self.current_mission]
        question = self.remaining_questions.pop(random.randint(0, len(self.remaining_questions) - 1))
 
        print(f"\nMise {self.current_mission + 1} začíná!")
        if self.ask_question(question, mission["item"]):
            self.current_mission += 1
        else:
            print("Nepodařilo se dokončit misi. Zkusíte to znovu!")
 
    def ask_question(self, question, item):
        print("\n" + question["question"])
        for option in question["options"]:
            print(option)
        answer = input("Zadej svou odpověď (a/b/c/d): ").strip().lower()
        if answer == question["answer"]:
            print("Správně! Získáváš část kódu pro další postup.")
            if item:
                print(f"Získali jste předmět: {item}")
                self.inventory.append(item)
            return True
        else:
            print("Špatně! Ztrácíte 20 zdraví.")
            self.health -= 20
            return False
 
    def check_inventory(self):
        print("\n--- Inventář ---")
        if self.inventory:
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("Inventář je prázdný.")
 
    def end_game(self):
        print("\nGratulujeme! Našli jste Deník Rebelů.")
        print("Co chcete udělat?")
        print("1. Zničit deník a zlomit kletbu školy.")
        print("2. Použít deník k ovládnutí školy.")
        print("3. Vrátit deník na původní místo.")
        choice = input("> ")
        if choice == "1":
            print("Zničili jste deník a škola se vrací k normálu.")
        elif choice == "2":
            print("Stali jste se vládcem školy, ale zaplatili jste vysokou cenu.")
        elif choice == "3":
            print("Vrácením deníku obnovujete rovnováhu školy.")
        else:
            print("Neplatná volba. Deník zmizel neznámo kam.")
        print("Konec hry. Děkujeme za hraní!")
 
# Spuštění hry
game = TajemnaSkola()
game.start()
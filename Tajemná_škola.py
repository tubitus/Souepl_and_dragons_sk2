import random

class TajemnaSkola:
    def __init__(self):
        self.health = 100
        self.max_health = 100
        self.inventory = []
        self.journal_collected = False
        self.events = [
            "Jakub Kovařík", "Daniel Šedivec", "Šimík", "Ivan Gemela",
            "Temná Dáša", "Engineer", "Ježíš Breit", "Tlustý Malicherný Bok",
            "Mise: Získání medu", "Mise: Získání Elixíru klidu",
            "Vítek Fikrle", "Tereza Lékařská", "Vědma Uzdravka"
        ]
        self.completed_events = set()
        self.current_mission = 0

    def start(self):
        print("Vítejte v 'Tajemné škole a Deníku Rebelů'!")
        print("Vaším cílem je získat tajemný deník a odhalit pravdu o škole.")
        print("Hra končí po 10 misích. Hodně štěstí!\n")
        while not self.journal_collected and self.health > 0 and self.current_mission < 10:
            self.main_menu()
        if self.journal_collected:
            self.end_game()
        elif self.current_mission >= 10:
            print("\nDosáhli jste desáté mise, ale deník jste nezískali.")
            print("Škola zůstává zahalená tajemstvím. Konec hry.")
        else:
            print("\nBohužel jste zemřeli během hledání deníku. Konec hry.")
    
    def main_menu(self):
        print("\n--- Hlavní menu ---")
        print(f"Mise: {self.current_mission + 1}/10 | Zdraví: {self.health}")
        print("1. Prozkoumat nové místo")
        print("2. Zkontrolovat inventář")
        print("3. Použít předmět z inventáře")
        print("4. Ukončit hru")
        choice = input("> ")
        
        if choice == "1":
            self.explore()
        elif choice == "2":
            self.check_inventory()
        elif choice == "3":
            self.use_item()
        elif choice == "4":
            print("Ukončili jste hru. Díky za hraní!")
            exit()
        else:
            print("Neplatná volba, zkuste to znovu.")
    
    def explore(self):
        available_events = [e for e in self.events if e not in self.completed_events]
        if not available_events:
            print("Prozkoumali jste všechny dostupné lokace.")
            return
        event = random.choice(available_events)
        self.completed_events.add(event)
        self.current_mission += 1
        print(f"\nNa své cestě narazíte na: {event}")
        
        if event == "Jakub Kovařík":
            self.jakub_event()
        elif event == "Daniel Šedivec":
            self.daniel_event()
        elif event == "Šimík":
            self.simik_event()
        elif event == "Ivan Gemela":
            self.ivan_event()
        elif event == "Temná Dáša":
            self.dasa_event()
        elif event == "Engineer":
            self.engineer_event()
        elif event == "Ježíš Breit":
            self.breit_event()
        elif event == "Tlustý Malicherný Bok":
            self.bok_event()
        elif event == "Mise: Získání medu":
            self.get_honey_mission()
        elif event == "Mise: Získání Elixíru klidu":
            self.get_elixir_mission()
        elif event == "Vítek Fikrle":
            self.vitek_event()  # Opraveno přidáním metody pro Vítka Fikrle
        elif event == "Tereza Lékařská":
            self.tereza_event()
        elif event == "Vědma Uzdravka":
            self.uzdravka_event()
    
    def jakub_event(self):
        print("Potkali jste Jakuba Kovaříka. Musíte odpovědět na jeho hádanku.")
        question = "Kolik je 5 + 7?"
        answer = "12"
        user_answer = input(f"{question} > ")
        if user_answer == answer:
            print("Správně! Můžete pokračovat.")
        else:
            print("Špatně! Jakub vás zasáhne. Ztrácíte 20 zdraví.")
            self.health -= 20
    
    def daniel_event(self):
        print("Potkali jste Daniela Šedivce. Je velmi nebezpečný!")
        print("Daniel se pokusí vás zneškodnit svou pánvičkou.")
        if random.random() < 0.5:
            print("Podařilo se vám vyhnout jeho útoku!")
        else:
            print("Daniel vás zasáhl. Ztrácíte 30 zdraví.")
            self.health -= 30
    
    def simik_event(self):
        print("Potkali jste malého elfa Šimíka. Může vám pomoci.")
        print("Šimík vám nabídne léčivou magii.")
        heal = random.randint(10, 30)
        self.health = min(self.health + heal, self.max_health)
        print(f"Šimík vám přidal {heal} zdraví. Máte nyní {self.health} zdraví.")
    
    def ivan_event(self):
        print("Potkali jste Ivana Gemelu, ztraceného alchymistu.")
        print("Ivan vám nabídne alchymistický elixír.")
        if random.random() < 0.5:
            heal = random.randint(20, 40)
            self.health = min(self.health + heal, self.max_health)
            print(f"Ivan vám přidal {heal} zdraví. Máte nyní {self.health} zdraví.")
        else:
            print("Elixír selhal. Ztrácíte 10 zdraví.")
            self.health -= 10
    
    def dasa_event(self):
        print("Potkali jste Temnou Dášu, která se pokusí ovládnout vaši mysl.")
        print("Dáša použije svou temnou magii!")
        if random.random() < 0.3:
            print("Podařilo se vám odolat její magii!")
        else:
            print("Dáša vás zcela ovládla. Ztrácíte 40 zdraví.")
            self.health -= 40
    
    def engineer_event(self):
        print("Potkali jste Mechanického Golema – Engineer.")
        print("Engineer má silné mechanické útoky.")
        if random.random() < 0.5:
            print("Podařilo se vám vyhnout jeho útokům!")
        else:
            print("Engineer vás zranil. Ztrácíte 50 zdraví.")
            self.health -= 50
    
    def breit_event(self):
        print("Potkali jste Ježíše Breita, Bílého Rytíře.")
        print("Ježíš vám může nabídnout ochranu.")
        if random.random() < 0.7:
            print("Ježíš vám poskytl silnou ochranu. Získáváte 20 zdraví a obranu.")
            self.health = min(self.health + 20, self.max_health)
            self.inventory.append("Ochranný štít")
        else:
            print("Ježíš vás nezachránil a odmítl vaši pomoc.")
    
    def bok_event(self):
        print("Potkali jste Tlustého Malicherného Boka.")
        print("Tlustý Bok se snaží vás zneškodnit svou tlustou rukou.")
        if random.random() < 0.6:
            print("Ubránili jste se a unikli jeho útoku!")
        else:
            print("Tlustý Bok vás zasáhl. Ztrácíte 20 zdraví.")
            self.health -= 20
    
    def get_honey_mission(self):
        print("Získali jste med od včelího úlu!")
        self.inventory.append("Med")
        print("Med byl přidán do vašeho inventáře.")
    
    def get_elixir_mission(self):
        print("Našli jste Elixír klidu.")
        self.inventory.append("Elixír klidu")
        print("Elixír klidu byl přidán do vašeho inventáře.")
    
    def vitek_event(self):
        print("Potkali jste Vítka Fikrle, který vám nabízí léčbu.")
        print("Automaticky získáváte 10 zdraví.")
        self.health = min(self.health + 10, self.max_health)
        while True:
            gamble = input("Chcete zkusit zdvojnásobit své zdraví? (ano/ne) > ").lower()
            if gamble == "ano":
                if random.random() < 0.5:
                    heal = self.health
                    self.health = min(self.health + heal, self.max_health)
                    print(f"Podařilo se! Máte nyní {self.health} zdraví.")
                    if self.health == self.max_health:
                        print("Dosáhli jste maximálního zdraví. Mise končí.")
                        break
                else:
                    print("Smůla! Vítek ukončuje léčbu.")
                    break
            elif gamble == "ne":
                print("Rozhodli jste se neriskovat. Mise končí.")
                break
            else:
                print("Neplatná volba.")
    
    def tereza_event(self):
        print("Potkali jste Terezu Lékařskou, která nabízí léčivé lektvary.")
        if "Zlatý pohár" in self.inventory:
            print("Používáte Zlatý pohár a získáváte plné zdraví!")
            self.health = self.max_health
        else:
            heal = random.randint(15, 25)
            self.health = min(self.health + heal, self.max_health)
            print(f"Tereza vám přidala {heal} zdraví. Máte nyní {self.health} zdraví.")
    
    def uzdravka_event(self):
        print("Narazili jste na Vědmu Uzdravku.")
        if "Magický krystal" in self.inventory:
            print("Vědma použila váš Magický krystal na silné léčení!")
            self.health = min(self.health + 40, self.max_health)
            self.inventory.remove("Magický krystal")
        else:
            print("Vědma nemá čím léčit. Mise končí.")
    
    def use_item(self):
        if not self.inventory:
            print("Nemáte žádné předměty k použití.")
            return
        print("\n--- Použít předmět ---")
        for i, item in enumerate(self.inventory):
            print(f"{i + 1}. {item}")
        choice = input("> ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.inventory):
            item = self.inventory.pop(int(choice) - 1)
            print(f"Používáte: {item}")
        else:
            print("Neplatná volba.")
    
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

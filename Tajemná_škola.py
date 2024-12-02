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
            "Vítek Fikrle", "Tereza Lékařská", "Vědma Uzdravka", "Gabriel"
        ]
        self.completed_events = set()
        self.current_mission = 0
        self.starting_health()

    def starting_health(self):
        print("Začínáte dobrodružství...")
        if random.random() < 0.35:
            self.health = 50  # Snížení zdraví na 50 kvůli špatnému spánku
            print("Zaspali jste! Probouzíte se s únavou a máte jen 50 zdraví.")
        else:
            print("Probudili jste se čerství a zdraví.")
    
    def start(self):
        print("Vítejte v 'Tajemné škole a Deníku Rebelů'!")
        print("Vaším cílem je získat tajemný deník a odhalit pravdu o škole.")
        print("Hra končí po 15 misích. Hodně štěstí!\n")
        while not self.journal_collected and self.health > 0 and self.current_mission < 15:
            self.main_menu()
        if self.journal_collected:
            self.end_game()
        elif self.current_mission >= 15:
            print("\nDosáhli jste patnácté mise, ale deník jste nezískali.")
            print("Škola zůstává zahalená tajemstvím. Konec hry.")
        else:
            print("\nBohužel jste zemřeli během hledání deníku. Konec hry.")
    
    def main_menu(self):
        print("\n--- Hlavní menu ---")
        print(f"Mise: {self.current_mission + 1}/15 | Zdraví: {self.health}")
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
            self.vitek_event()
        elif event == "Tereza Lékařská":
            self.tereza_event()
        elif event == "Vědma Uzdravka":
            self.uzdravka_event()
        elif event == "Gabriel":
            self.gabriel_event()
    
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
        print("Potkali jste Daniela Šedivec, je velmi nebezpečný!")
        print("Daniel se pokusí vás zneškodnit svou pánvičkou.")
        
        if "Elixír klidu" in self.inventory:
            use_elixir = input("Máte Elixír klidu. Chcete ho použít? (y/n) > ")
            if use_elixir.lower() == "y":
                print("Používáte Elixír klidu a Daniel vás neudrží!")
                self.inventory.remove("Elixír klidu")
                print("Daniel vás nezasáhl, můžete pokračovat.")
                return  # Pokud použijete elixír, neútočí na vás okamžitě
            else:
                print("Nechali jste si elixír pro jinou příležitost.")
        
        print("Daniel vás zasáhl! Ztrácíte 30 zdraví.")
        self.health -= 30
    
    def gabriel_event(self):
        print("Gabriel se pokusí ukrást jeden z vašich předmětů.")
        if self.inventory:
            stolen_item = random.choice(self.inventory)
            self.inventory.remove(stolen_item)
            print(f"Gabriel ukradl: {stolen_item}")
        else:
            print("Gabriel nemá co ukrást! Rozzlobí se a udeří vás za 20 damage.")
            self.health -= 20
    
    def simik_event(self):
        print("Potkali jste malého elfa Šimíka. Může vám pomoci.")
        print("Šimík vám nabídne léčivou magii.")
        heal = random.randint(10, 30)
        self.health = min(self.health + heal, self.max_health)
        print(f"Šimík vám přidal {heal} zdraví. Máte nyní {self.health} zdraví.")
    
    def ivan_event(self):
        print("Potkali jste Ivana Gemelu, ztraceného alchymistu.")
        print("Ivan vám nabídne alchymistický elixír.")
        if random.random() < 0.6:
            heal = random.randint(20, 40)
            self.health = min(self.health + heal, self.max_health)
            print(f"Ivan vám přidal {heal} zdraví. Máte nyní {self.health} zdraví.")
        else:
            print("Elixír selhal. Ztrácíte 10 zdraví.")
            self.health -= 10
    
    def dasa_event(self):
        print("Potkali jste Temnou Dášu, která se pokusí ovládnout vaši mysl.")
        print("Dáša použije svou temnou magii!")
        if random.random() < 0.3:  # Zvýšená šance na poškození
            print("Podařilo se vám odolat její magii!")
        else:
            print("Dáša vás zcela ovládla. Ztrácíte 40 zdraví.")
            self.health -= 40
    
    def engineer_event(self):
        print("Potkali jste Mechanického Golema – Engineer.")
        print("Engineer má silné mechanické útoky.")
        if random.random() < 0.1:  # Zvýšená šance na poškození
            print("Podařilo se vám vyhnout jeho útokům!")
        else:
            print("Engineer vás zranil. Ztrácíte 50 zdraví.")
            self.health -= 50
    
    def breit_event(self):
        print("Potkali jste Ježíše Breita, znepřáteleného profesora.")
        print("Profesor se pokusí vás zasáhnout svou magií.")
        if random.random() < 0.5:  # Polovina šance na útok
            print("Zasáhl vás! Ztrácíte 20 zdraví.")
            self.health -= 20
    
    def bok_event(self):
        print("Potkali jste Tlustého Malicherného Boka, který vás nechce pustit.")
        print("Musíte se s ním utkat!")
        if random.random() < 0.2:  # Snížená šance na poškození
            print("Podařilo se vám vyhnout jeho útoku.")
        else:
            print("Bok vás zasáhl! Ztrácíte 30 zdraví.")
            self.health -= 30
    
    def get_honey_mission(self):
        print("Podařilo se vám najít med.")
        self.inventory.append("Med")
    
    def get_elixir_mission(self):
        print("Podařilo se vám najít Elixír klidu.")
        self.inventory.append("Elixír klidu")
    
    def check_inventory(self):
        print("\n--- Inventář ---")
        if not self.inventory:
            print("Váš inventář je prázdný.")
        else:
            for item in self.inventory:
                print(f"- {item}")
    
    def use_item(self):
        print("Jaký předmět chcete použít?")
        if not self.inventory:
            print("Váš inventář je prázdný.")
        else:
            for idx, item in enumerate(self.inventory):
                print(f"{idx + 1}. {item}")
            choice = input("> ")
            try:
                item_choice = int(choice) - 1
                item = self.inventory[item_choice]
                if item == "Med":
                    heal = random.randint(10, 30)
                    self.health = min(self.health + heal, self.max_health)
                    print(f"Použili jste med a získali {heal} zdraví.")
                    self.inventory.remove("Med")
                elif item == "Elixír klidu":
                    heal = random.randint(15, 35)
                    self.health = min(self.health + heal, self.max_health)
                    print(f"Použili jste elixír klidu a získali {heal} zdraví.")
                    self.inventory.remove("Elixír klidu")
                else:
                    print("Neznámý předmět.")
            except (ValueError, IndexError):
                print("Neplatná volba.")
    
    def vitek_event(self):
        print("Vítek Fikrle je starý student, který vás může naučit silné kouzlo.")
        print("Chcete přijmout jeho nabídku na trénink?")
        answer = input("y/n > ")
        if answer.lower() == 'y':
            self.health += 10
            print("Vítek vás posílil! Získali jste 10 zdraví.")
        else:
            print("Odmítli jste trénink. Pokračujete bez posílení.")

    def tereza_event(self):
        print("Tereza Lékařská je známá léčitelka ve škole.")
        print("Pokud máte nějaké zranění, nabídne vám pomoc.")
        if self.health < 30:
            heal = 30 - self.health
            self.health += heal
            print(f"Tereza vás uzdravila. Získali jste {heal} zdraví.")
        else:
            print("Tereza vás neposílí, protože máte dost zdraví.")
    
    def uzdravka_event(self):
        print("Potkali jste Vědmu Uzdravku.")
        print("Chce vám pomoci se zraněním, ale její pomoc je nebezpečná.")
        if random.random() < 0.5:
            self.health += 20
            print("Vědma Uzdravka vás uzdravila. Získali jste 20 zdraví.")
        else:
            print("Vědma vás zradila a poškodil jste se. Ztrácíte 15 zdraví.")
            self.health -= 15

    def end_game(self):
        print("\nGratulujeme! Našli jste Deník Rebelů.")
        if random.random() < 0.5:  # 50% šance na nalezení deníku
            print("Deník se vám podařilo najít!")
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
        else:
            print("Deník se vám nepodařilo najít.")
        print("Konec hry. Děkujeme za hraní!")
        
# Spuštění hry
game = TajemnaSkola()
game.start()

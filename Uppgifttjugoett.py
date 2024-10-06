import random

class tjugoett:
    def __init__(self):
        self.player: list[int] = []  # spelarens kort
        self.computer: list[int] = []  # datorns kort

    def dealer(self) -> int:
        return random.randint(2, 14)  # rturnera ett random kort mellan 2 och 14

    def ace_value(self, totala: int) -> int:
        # man får välja värdet av ett ess beroende på totala summan
        # om + 14 > 21, returnera 1, annars låt spelaren välja
        return 1 if totala + 14 > 21 else int(input("u har ett ess, Välj 1 eller 14: "))

    def score_calculate(self, cards: list[int]) -> int:
        # beräknar poängen som man har
        score = sum(cards)
        aces = cards.count(14)
        # om totala summan överstiger 21 med ess så ändras värdet till 1
        while score > 21 and aces:
            score -= 13
            aces -= 1
        return score

    def compare(self, user_score: int, computer_score: int) -> str:
        # jämför och returnerar resultatet av spelare och datorn
        if user_score > 21:
            return "du förlorar, du fick över 21"
        if computer_score > 21:
            return "du vinner, din motståndare fick över 21"
        if user_score == computer_score:
            return "det är oavgjort"
        if computer_score == 21 and len(self.computer) == 2:
            return "du förlorar, din motståndare har tjugoett"
        if user_score == 21 and len(self.player) == 2:
            return "du vinner, det är en Tjugoett"
        return "du vinner!" if user_score > computer_score else "Du förlorar"

    def reset(self):
        #Om ny spelrunda så återställer den spelarens händer
        self.player = []
        self.computer = []

    def round(self):
        # en spelrunda genomförs
        self.reset()
        game_finish: bool = False

        # här delas två kort till spelaren
        for _ in range(2):
            self.player.append(self.dealer())
            self.computer.append(self.dealer())

        while not game_finish:
            # visar både datorns och spelarens första kort.
            print(f"\ndina kort: {self.player}")
            print(f"datorns första kort: {self.computer[0]}\n")

            totala = sum(self.player)
            # om spelaren har ett ess i handen så hanteras den
            if 14 in self.player:
                ace_index = self.player.index(14)
                self.player[ace_index] = self.ace_value(totala)
                print(f"Dina uppdaterade kort: {self.player}\n")

            # beräknas poängen då för både spelaren och datorn
            user_score: int = self.score_calculate(self.player)
            computer_score: int = self.score_calculate(self.computer)
            
            print(f"Din nuvarande poäng: {user_score}\n")

            # här kontrolleras det om spelet ska avslutas
            if user_score == 21 or computer_score == 21 or user_score > 21:
                game_finish = True
            else:
                # här frågar det spelaren om den vill ha ett till kort
                user_should_deal = input("Skriv 'j' för att få ett till kort, 'n' för att stanna: ")
                if user_should_deal.lower() == "j":
                    new_card = self.dealer()
                    self.player.append(new_card)
                    # hanterar nya ess kortet
                    if new_card == 14:
                        totala = sum(self.player)
                        self.player[-1] = self.ace_value(totala)
                else:
                    game_finish = True

        # datorn drar kort till minst 17 eller mer
        while self.score_calculate(self.computer) < 17:
            self.computer.append(self.dealer())

        # beräknar slutpoängen
        user_score = self.score_calculate(self.player)
        computer_score = self.score_calculate(self.computer)
        
        # visar slutresultatet
        print(f"\nDin slutliga hand: {self.player}, slutpoäng: {user_score}")
        print(f"Datorns slutliga hand: {self.computer}, slutpoäng: {computer_score}\n")
        print(self.compare(user_score, computer_score))

if __name__ == "__main__":
    game = tjugoett()
    play_again = True
    
    while play_again:
        game.round()
        # vid avslut frågar spelare om den vill spela igen annars printar den ett avslut
        play_again = input("\nVill du spela igen? Skriv 'j' för ja eller 'n' för nej: ").lower() == 'j'

    print("\nTack för att du spelade!\n")
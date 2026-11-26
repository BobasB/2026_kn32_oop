import random

class GameCharacter:
    def __init__(self, name):
        self.name = name
        self.init_attack_power()
        self.init_health()

    def init_health(self, health: int = 100):
        self.health = health
        """Ініціалізує або скидає до значення за замовчуванням атрибут health"""
        self.health = health

    def init_attack_power(self, attack: int = 10):
        """Ініціалізує або скидає до значення за замовчуванням атрибут attack"""
        self.attack_power = attack

    @property
    def character_status(self):
        """Повертає рядок із статусом персонажа"""
        return f"""
        \tПерсонаж: {self.name} 
        \tЗдоров'я: {self.health} 
        \tАтака: {self.attack_power}"""

    def attack(self, other_character):
        """Здійснює атаку на іншого персонажа"""
        damage = random.randint(8, self.attack_power + 2)
        other_character.health -= damage
        if other_character.health < 0:
            other_character.health = 0

    def heal(self):
        """Відновлює здоров'я персонажа на певну кількість"""
        heal_amount = random.randint(5, 15)
        self.health += heal_amount
        if self.health > 100:
            self.init_health()

def main():
    name = str(input("Введіть ім'я вашого персонажа: "))
    player = GameCharacter(name)
    mob = GameCharacter("Моб")

    for n in range(5):
        print(f"\nРаунд {n + 1}")
        choice = input("Виберіть дію (1 - Атакувати, 2 - Вилікуватися): ")
        if choice == "1":
            player.attack(mob)
            print(f"Ви атакували {mob.name}. Його здоров'я: {mob.health}")
        elif choice == "2":
            player.heal()
            print(f"Ви відновили здоров'я. Ваше здоров'я: {player.health}")
        else:
            print("Невірний вибір. Пропущено хід.")
            continue
        mod_choce = random.choice(["attack", "heal"])
        if mod_choce == "attack":
            mob.attack(player)
            print(f"{mob.name} атакував вас. Ваше здоров'я: {player.health}")
        else:
            mob.heal()
            print(f"{mob.name} відновив здоров'я. Його здоров'я: {mob.health}")
        print("+++++ Статус персонажів +++++")
        print(mob.character_status)
        print(player.character_status)

if __name__ == "__main__":
    main()

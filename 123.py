import pickle

class Attributes:
    def __init__(self, health=100, energy=100, experience=0, level=1):
        self.health = health
        self.energy = energy
        self.experience = experience
        self.level = level

    def display(self):
        print(f"Здоров'я: {self.health}, Енергія: {self.energy}, Досвід: {self.experience}, Рівень: {self.level}")

    def reduce_health(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def increase_experience(self, amount):
        self.experience += amount
        print(f"Отримано досвіду: {amount}")
        if self.experience >= self.level * 100:
            self.experience = 0
            self.level += 1
            print(f"Вітаємо! {self.level} рівень досягнуто!")

    def reduce_energy(self, amount):
        self.energy -= amount
        if self.energy < 0:
            self.energy = 0

    def rest(self):
        self.energy += 30
        self.health += 5
        if self.health > 100:
            self.health = 100
        if self.energy > 100:
            self.energy = 100


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Додано до інвентаря: {item}")

    def show_inventory(self):
        print("Інвентар:", ", ".join(self.items) if self.items else "Порожній")


class Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.math = 0
        self.lang = 0 
        self.diz = 0 
        self.lead = 0
        self.attributes = Attributes()
        self.inventory = Inventory()

    def set_skills(self, math, lang, diz, lead):
        self.math = math
        self.lang = lang
        self.diz = diz
        self.lead = lead

    def get(self):
        print(f"Персонаж {self.name}, в віці {self.age}")
        print(f"Математичні скіли: {self.math}, Англійська: {self.lang}, Дизайн: {self.diz}, Лідерські якості: {self.lead}")
        self.attributes.display()
        self.inventory.show_inventory()

    def skill_high(self, math_high, lang_high, diz_high, lead_high):
        if math_high != 0:
            self.math += math_high
            print(f"Математичні навички підвищено на: {math_high}")
        if lang_high != 0:
            self.lang += lang_high
            print(f"Лінгвістичні навички підвищено на: {lang_high}")
        if diz_high != 0:
            self.diz += diz_high
            print(f"Дизайнерські навички підвищено на: {diz_high}")
        if lead_high != 0:
            self.lead += lead_high
            print(f"Лідерські якості покращено на: {lead_high}")

    def save_state(self, filename='character_state.pkl'):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print("Стан гри збережено.")

    @staticmethod
    def load_state(filename='character_state.pkl'):
        with open(filename, 'rb') as file:
            character = pickle.load(file)
        print("Стан гри завантажено.")
        return character


class Work:
    def __init__(self, work_type, math_reward=0, lang_reward=0, diz_reward=0, lead_reward=0, exp_reward=0, energy_cost=10):
        self.work_type = work_type
        self.math_reward = math_reward
        self.lang_reward = lang_reward
        self.diz_reward = diz_reward
        self.lead_reward = lead_reward
        self.exp_reward = exp_reward
        self.energy_cost = energy_cost

    def complete_work(self, character):
        print(f"Виконується завдання типу: {self.work_type}")
        
        if character.attributes.energy >= self.energy_cost:
            character.attributes.reduce_energy(self.energy_cost)
            character.skill_high(self.math_reward, self.lang_reward, self.diz_reward, self.lead_reward)
            character.attributes.increase_experience(self.exp_reward)
        else:
            print("Недостатньо енергії для виконання завдання.")
            character.attributes.reduce_health(10)
            print("Здоров'я зменшено через низьку енергію!")


ann = Character('Ann', 20)
ann.set_skills(0.2, 0.1, 0.2, 0.0)
ann.inventory.add_item("Енергетичний напій")

task1 = Work("Розробка дизайну", math_reward=0.1, lang_reward=0.2, diz_reward=0.3, lead_reward=0, exp_reward=50, energy_cost=20)

ann.get()
task1.complete_work(ann)
ann.get()

ann.save_state()
loaded_ann = Character.load_state()
loaded_ann.get()
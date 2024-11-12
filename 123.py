import pickle

# Клас для атрибутів персонажа: здоров'я, енергія, досвід та рівень
class Attributes:
    def __init__(self, health=100, energy=100, experience=0, level=1):
        self.health = health      # Здоров'я персонажа
        self.energy = energy      # Енергія персонажа
        self.experience = experience  # Досвід персонажа
        self.level = level        # Поточний рівень персонажа

    # Метод для виведення поточних атрибутів персонажа
    def display(self):
        print(f"Здоров'я: {self.health}, Енергія: {self.energy}, Досвід: {self.experience}, Рівень: {self.level}")

    # Зменшує здоров'я на задану кількість, не допускаючи значень нижче 0
    def reduce_health(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    # Збільшує досвід персонажа, підвищуючи рівень, коли досвід досягає порогу
    def increase_experience(self, amount):
        self.experience += amount
        print(f"Отримано досвіду: {amount}")
        # Перевірка для підвищення рівня
        if self.experience >= self.level * 100:
            self.experience = 0    # Обнулення досвіду після підвищення рівня
            self.level += 1
            print(f"Вітаємо! {self.level} рівень досягнуто!")

    # Зменшує енергію на задану кількість, не допускаючи значень нижче 0
    def reduce_energy(self, amount):
        self.energy -= amount
        if self.energy < 0:
            self.energy = 0

    # Відпочинок для відновлення енергії та здоров'я
    def rest(self):
        self.energy += 30
        self.health += 5
        if self.health > 100:
            self.health = 100
        if self.energy > 100:
            self.energy = 100


# Клас інвентаря для зберігання предметів персонажа
class Inventory:
    def __init__(self):
        self.items = []  # Список предметів в інвентарі

    # Додає новий предмет до інвентаря
    def add_item(self, item):
        self.items.append(item)
        print(f"Додано до інвентаря: {item}")

    # Виводить вміст інвентаря
    def show_inventory(self):
        print("Інвентар:", ", ".join(self.items) if self.items else "Порожній")


# Основний клас персонажа
class Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.math = 0  # Навички з математики
        self.lang = 0  # Навички з англійської мови
        self.diz = 0   # Дизайнерські навички
        self.lead = 0  # Лідерські якості
        self.attributes = Attributes()  # Об'єкт атрибутів (здоров'я, енергія, досвід)
        self.inventory = Inventory()    # Об'єкт інвентаря

    # Метод для встановлення початкових навичок
    def set_skills(self, math, lang, diz, lead):
        self.math = math
        self.lang = lang
        self.diz = diz
        self.lead = lead

    # Метод для виведення інформації про персонажа, включаючи навички, атрибути та інвентар
    def get(self):
        print(f"Персонаж {self.name}, в віці {self.age}")
        print(f"Математичні скіли: {self.math}, Англійська: {self.lang}, Дизайн: {self.diz}, Лідерські якості: {self.lead}")
        self.attributes.display()
        self.inventory.show_inventory()

    # Метод для підвищення навичок після виконання завдання
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

    # Метод для збереження стану персонажа у файл
    def save_state(self, filename='character_state.pkl'):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print("Стан гри збережено.")

    # Метод для завантаження стану персонажа з файлу
    @staticmethod
    def load_state(filename='character_state.pkl'):
        with open(filename, 'rb') as file:
            character = pickle.load(file)
        print("Стан гри завантажено.")
        return character


# Клас завдань для виконання, яке дає винагороду і витрачає енергію
class Work:
    def __init__(self, work_type, math_reward=0, lang_reward=0, diz_reward=0, lead_reward=0, exp_reward=0, energy_cost=10):
        self.work_type = work_type        # Тип завдання
        self.math_reward = math_reward    # Бонус до математики за виконання
        self.lang_reward = lang_reward    # Бонус до англійської
        self.diz_reward = diz_reward      # Бонус до дизайну
        self.lead_reward = lead_reward    # Бонус до лідерських якостей
        self.exp_reward = exp_reward      # Кількість досвіду, що надається
        self.energy_cost = energy_cost    # Витрати енергії

    # Метод для виконання завдання персонажем
    def complete_work(self, character):
        print(f"Виконується завдання типу: {self.work_type}")
        
        # Перевірка, чи достатньо енергії для виконання завдання
        if character.attributes.energy >= self.energy_cost:
            character.attributes.reduce_energy(self.energy_cost)
            character.skill_high(self.math_reward, self.lang_reward, self.diz_reward, self.lead_reward)
            character.attributes.increase_experience(self.exp_reward)
        else:
            # Якщо енергії недостатньо, здоров'я персонажа знижується
            print("Недостатньо енергії для виконання завдання.")
            character.attributes.reduce_health(10)
            print("Здоров'я зменшено через низьку енергію!")


# Створення персонажів
ann = Character('Ann', 20)
ann.set_skills(0.2, 0.1, 0.2, 0.0)  # Початкові навички персонажа
ann.inventory.add_item("Енергетичний напій")  # Додавання предмету в інвентар

# Створення завдання
task1 = Work("Розробка дизайну", math_reward=0.1, lang_reward=0.2, diz_reward=0.3, lead_reward=0, exp_reward=50, energy_cost=20)

# Виконання завдання та оновлення атрибутів
ann.get()
task1.complete_work(ann)
ann.get()

# Збереження стану персонажа у файл та його завантаження
ann.save_state()
loaded_ann = Character.load_state()
loaded_ann.get()

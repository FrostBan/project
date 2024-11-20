import json  

# Клас для опису персонажа
class Character:
    def __init__(self, name, age):
        self.name = name  # Ім'я персонажа
        self.age = age  # Вік персонажа
        self.math = 0  # Навички: Математика
        self.lang = 0  # Навички: Мова
        self.diz = 0  # Навички: Дизайн
        self.lead = 0  # Навички: Лідерство

    # Метод для встановлення початкових навичок
    def set_skills(self, math, lang, diz, lead):
        self.math = math
        self.lang = lang
        self.diz = diz
        self.lead = lead

    # Метод для отримання інформації про персонажа
    def get(self):
        print(f"Персонаж {self.name}, вік: {self.age}")
        print(f"Навички -> Математика: {self.math}, Мова: {self.lang}, Дизайн: {self.diz}, Лідерство: {self.lead}")

    # Метод для покращення навичок персонажа
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


# Клас для опису статусу персонажа (здоров'я, енергія, досвід)
class Status:
    def __init__(self):
        self.health = 100  # Здоров'я персонажа
        self.energy = 100  # Енергія персонажа
        self.experience = 0  # Досвід персонажа

    # Метод для отримання поточного статусу
    def get_status(self):
        return {"health": self.health, "energy": self.energy, "experience": self.experience}

    # Метод для зміни статусу
    def change_status(self, health_change=0, energy_change=0, experience_change=0):
        self.health += health_change
        self.energy += energy_change
        self.experience += experience_change


# Клас для збереження та завантаження гри
class GameSave:
    @staticmethod
    def save_game(character, status, filename="save.json"):
        # Підготовка даних для збереження
        data = {
            "character": {
                "name": character.name,
                "age": character.age,
                "skills": {
                    "math": character.math,
                    "lang": character.lang,
                    "diz": character.diz,
                    "lead": character.lead,
                },
            },
            "status": status.get_status(),
        }

        # Збереження у файл JSON
        with open(filename, "w") as save_file:
            json.dump(data, save_file, indent=4)
        print(f"Гра збережена у файл {filename}.")

    @staticmethod
    def load_game(filename="save.json"):
        try:
            # Завантаження даних із файлу JSON
            with open(filename, "r") as save_file:
                data = json.load(save_file)

            # Створення об'єктів Character і Status із завантажених даних
            character = Character(data["character"]["name"], data["character"]["age"])
            character.set_skills(
                data["character"]["skills"]["math"],
                data["character"]["skills"]["lang"],
                data["character"]["skills"]["diz"],
                data["character"]["skills"]["lead"],
            )

            status = Status()
            status.health = data["status"]["health"]
            status.energy = data["status"]["energy"]
            status.experience = data["status"]["experience"]

            print("Гра завантажена успішно.")
            return character, status
        except FileNotFoundError:
            print("Файл збереження не знайдено.")
            return None, None


# Приклад використання
Ann = Character("Ann", 20)
Ann.set_skills(0.2, 0.1, 0.2, 0.0)

status = Status()

# Збереження гри
GameSave.save_game(Ann, status)

# Завантаження гри
loaded_character, loaded_status = GameSave.load_game()

if loaded_character:
    loaded_character.get()
    print("Статус після завантаження:", loaded_status.get_status())
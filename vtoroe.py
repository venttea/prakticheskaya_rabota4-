class Employee:
    def __init__(self, name, position, experience_years):
        self.name = name
        self.position = position
        self.experience_years = experience_years

    def get_experience_bonus(self):
        if self.experience_years < 5:
            return 0.05
        elif 5 <= self.experience_years < 10:
            return 0.10
        else:
            return 0.15

# Пример использования
employee1 = Employee("Алиса", "Разработчик", 3)
employee2 = Employee("Петр", "Управляющий", 7)
employee3 = Employee("Мария", "Директор", 12)
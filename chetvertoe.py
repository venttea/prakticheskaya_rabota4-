from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def rest(self):
        pass

class Programmer(Worker):
    def work(self):
        return "Пишет код"

    def rest(self):
        return "Пьет кофеек"

class Designer(Worker):
    def work(self):
        return "Делает дизайники"

    def rest(self):
        return "Рисует за чашечкой чая"

programmer = Programmer()
designer = Designer()

print("Programmer:")
print(programmer.work())
print(programmer.rest())

print()

print("Designer:")
print(designer.work())
print(designer.rest())
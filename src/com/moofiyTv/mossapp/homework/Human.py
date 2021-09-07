# lab work
# This Class violates all SOLID Principles, fix it in a Logical way ;
import abc
import Needs


class Human(Needs):
    def __init__(self, name: str, nickname: str, salary: int, hobbies: []):
        self.name = name
        self.nickname = nickname
        self.salary = salary
        self.hobbies = hobbies

    def say_hello(self, lang: str):
        if lang == 'Arabic':
            return 'مرحبا'
        return 'Hello'

    def calculate_tax(self, percentage: int):
        salary = self.salary * percentage

    def add_hobby(self, hobby: str) -> int:
        self.hobbies.append(hobby)
        return len(self.hobbies)

    def create_nickName(self, post_fix: str):
        self.nickname = self.name + post_fix

    @abc.abstractmethod
    def pray(self):
        pass

    @abc.abstractmethod
    def play_sports(self):
        pass

    @abc.abstractmethod
    def get_married(self):
        pass

    @abc.abstractmethod
    def own_company(self):
        pass

    @abc.abstractmethod
    def become_employee(self):
        pass


human = Human()
human.say_hello('Arabic')

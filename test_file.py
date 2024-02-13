import random

class User:
    def __init__(self, name, surname, ID, languages, sex, age):
        self.name=name
        self.surname=surname
        self.ID=ID
        self.languages=languages
        self.sex=sex
        self.age=age
    def description(self):
        print(f'{self.name, self.surname} is our student!')

class Teacher:
    def __init__(self, name, surname, T_ID, languages, sex, age):
        self.name=name
        self.surname=surname
        self.T_ID=T_ID
        self.languages=languages
        self.sex=sex
        self.age=age

User1=['Nika', 'Kuznetsova', 1, ["english",'french'], 'Female', 31]
User2=['Kolya', 'Veselov', 2, ['german'], 'Male', 22]

def rename(user):
    global name, surname
    user.name=str(input())
    user.surname=str(input())
    
Teacher1=['Alla', 'Makarovna', 1, ["russian", 'english'], 'Female', 51]

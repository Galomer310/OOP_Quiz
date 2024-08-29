# Part 1 : Quizz :
# Answer the following questions

# What is a class? ,
# it's a blueprint for creating objects , a class defines the properties and behaviors that the objects created from it will have

# What is an instance?,
# it's an individual object created from a class that can operate independently from other instances of the same class

# What is encapsulation? ,
# it's a way to restrict the direct access to some components of an object, This prevents external interference and misuse of the data, ensuring that an object’s internal state is protected from unintended changes.

# What is abstraction?
# avstraction refers to the concept of hiding the complex implementation details and exposing only the necessary functionality. It helps in reducing complexity by allowing users to interact with an object at a higher level, without needing to understand its internal workings.

# What is inheritance?
# it's a feature of OOP that allows a class to inherit attributes and methods from another class ,

# What is multiple inheritance?
# A class inherits from a class that is already a child of another class.

# What is polymorphism?
# give the ability to present the same interface for different data types or objects of different classes to be treatad as objects of common superclass

# What is method resolution order or MRO?
# It is the order in which Python looks for a method or attribute in a class hierarchy. It defines the sequence in which Python searches for the methods or attributes when they are called on an instance of a class.

# Part 2 Create A Deck Of Cards Class

import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']
                                        for value in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if self.cards:
            return self.cards.pop()
        else:
            return "No cards left in the deck"

deck = Deck()
deck.shuffle()
card = deck.deal()
card2 = deck.deal()

print(f"Dealt card: {card}")
print(f"and {card2}")
print(f"Remaining cards: {len(deck.cards)}")
















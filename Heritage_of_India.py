import random

class CulturalDestination:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.programming = []
        self.public_art = []

    def add_programming(self, event):
        self.programming.append(event)

    def add_public_art(self, art):
        self.public_art.append(art)

    def display_programming(self):
        print(f"Upcoming Programming at {self.name}:")
        for event in self.programming:
            print(f"{event['title']} on {event['date']} at {event['time']}")

    def display_public_art(self):
        print(f"Public Art at {self.name}:")
        for art in self.public_art:
            print(f"{art['title']} by {art['artist']}")

class Event:
    def __init__(self, title, date, time, description):
        self.title = title
        self.date = date
        self.time = time
        self.description = description

class PublicArt:
    def __init__(self, title, artist, description, location):
        self.title = title
        self.artist = artist
        self.description = description
        self.location = location

class EmergingTalent:
    def __init__(self, name, age, discipline):
        self.name = name
        self.age = age
        self.discipline = discipline

class ArtCommunity:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def generate_income(self):
        income = random.randint(10000, 100000)
        print(f"{self.name} generated {income} from collaborations, aggregators, and accelerators investments.")

# Example usage
destination = CulturalDestination("Heritage of India", "Delhi")
event1 = Event("Theater Showcase", "2023-04-15", "18:00", "A showcase of the best regional theater in India")
event2 = Event("Dance Performance", "2023-04-20", "19:00", "A celebration of Indian dance styles")
destination.add_programming(event1.__dict__)
destination.add_programming(event2.__dict__)

art1 = PublicArt("Taj Mahal", "Shah Jahan", "A masterpiece of Mughal architecture", "Agra")
art2 = PublicArt("Gateway of India", "George Wittet", "A symbolic monument of Mumbai", "Mumbai")
destination.add_public_art(art1.__dict__)
destination.add_public_art(art2.__dict__)

talent1 = EmergingTalent("Rahul Singh", 22, "Musician")
talent2 = EmergingTalent("Priya Patel", 25, "Visual Artist")
community = ArtCommunity("Indian Art Association", "Mumbai")
community.add_member(talent1.__dict__)
community.add_member(talent2.__dict__)
community.generate_income()

destination.display_programming()
destination.display_public_art()

# Added integration testing code in the same program. 

import unittest

class TestCulturalDestination(unittest.TestCase):
    def setUp(self):
        self.destination = CulturalDestination("Heritage of India", "Delhi")
        self.event1 = Event("Theater Showcase", "2023-04-15", "18:00", "A showcase of the best regional theater in India")
        self.event2 = Event("Dance Performance", "2023-04-20", "19:00", "A celebration of Indian dance styles")
        self.art1 = PublicArt("Taj Mahal", "Shah Jahan", "A masterpiece of Mughal architecture", "Agra")
        self.art2 = PublicArt("Gateway of India", "George Wittet", "A symbolic monument of Mumbai", "Mumbai")
        self.talent1 = EmergingTalent("Rahul Singh", 22, "Musician")
        self.talent2 = EmergingTalent("Priya Patel", 25, "Visual Artist")
        self.community = ArtCommunity("Indian Art Association", "Mumbai")
        self.community.add_member(self.talent1.__dict__)
        self.community.add_member(self.talent2.__dict__)

    def test_add_programming(self):
        self.destination.add_programming(self.event1.__dict__)
        self.destination.add_programming(self.event2.__dict__)
        self.assertEqual(len(self.destination.programming), 2)

    def test_add_public_art(self):
        self.destination.add_public_art(self.art1.__dict__)
        self.destination.add_public_art(self.art2.__dict__)
        self.assertEqual(len(self.destination.public_art), 2)

    def test_generate_income(self):
        self.assertEqual(self.community.generate_income(), None)

if __name__ == '__main__':
    unittest.main()


# Regression Testing code
import requests;

class CulturalDestination:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.programming = []
        self.public_art = []

    def add_programming(self, event):
        self.programming.append(event)

    def add_public_art(self, art):
        self.public_art.append(art)

    def get_programming(self):
        url = "https://example.com/api/programming"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_public_art(self):
        url = "https://example.com/api/public_art"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

class Event:
    def __init__(self, name, date, time, description):
        self.name = name
        self.date = date
        self.time = time
        self.description = description

class PublicArt:
    def __init__(self, name, artist, description, location):
        self.name = name
        self.artist = artist
        self.description = description
        self.location = location

if __name__ == '__main__':
    destination = CulturalDestination("Heritage of India", "Delhi")

    # Get programming data from API
    programming_data = destination.get_programming()
    if programming_data:
        for event_data in programming_data:
            event = Event(event_data['name'], event_data['date'], event_data['time'], event_data['description'])
            destination.add_programming(event.__dict__)

    # Get public art data from API
    public_art_data = destination.get_public_art()
    if public_art_data:
        for art_data in public_art_data:
            art = PublicArt(art_data['name'], art_data['artist'], art_data['description'], art_data['location'])
            destination.add_public_art(art.__dict__)

    print(destination.programming)
    print(destination.public_art)


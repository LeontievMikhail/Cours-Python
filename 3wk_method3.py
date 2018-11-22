def extract_description(user_string):
    return "Открытие чемпионата мира по футболу"

def extract_date(user_string):
    return date(2018, 6,14)

class Event:
    def __init__(self, desctiption, event_date):
        self.description = desctiption
        self.date = event_date

    def __str__(self):
        return f"Event \"{self.description}\" at {self.date}"

    @classmethod
    def from_string(cls, user_input):
        description=extract_description(user_input)
        date = extract_date(user_input)
        return cls(desctiption, date)

event=Event.from_string("добавить в мой календарь открытие чемпионата мира по футболу на 14 июня 2018 года")
print(event)
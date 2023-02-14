from datetime import datetime

users = [
         {"name": "Volodymyr", "birthday": datetime(1990, 2, 6)},
         {"name":  "Maryna", "birthday": datetime(1983, 2, 13)},
         {"name": "Dmytro", "birthday": datetime(1982, 2, 14)},
         {"name": "Natallya", "birthday": datetime(1995, 2, 19)},
         {"name": "Olena", "birthday": datetime(1963, 2, 21)},
         {"name": "Tetyana", "birthday": datetime(1997, 2, 22)},
         {"name": "Mykola", "birthday": datetime(1987, 2, 19)},
         {"name": "Olga", "birthday": datetime(1985, 4, 29)}]
monday = []
next_monday =[]
tuesday = []
wednesday = []
thursday = []
friday = []

def get_birthdays_per_week(users):

    today = datetime.today()
    for user in users:
        name = user.get("name")
        birthday = user.get("birthday").replace(year=today.year)
        if today.day <= birthday.day <= today.day + 6:
            if birthday.weekday() == 0:
                monday.append(name)
            if birthday.weekday() == 1:
                tuesday.append(name)
            if birthday.weekday() == 2:
                wednesday.append(name)
            if birthday.weekday() == 3:
                thursday.append(name)
            if birthday.weekday() == 4:
                friday.append(name)
            if birthday.weekday() == 5 or birthday.weekday() == 6:
                next_monday.append(name)
            else:
                continue
    if monday:
        print(f"Monday: {', '.join(monday)}")
    if tuesday:
        print(f"Tuesday: {', '.join(tuesday)}")
    if wednesday:
        print(f"Wednesday : {', '.join(wednesday)}")
    if thursday:
        print(f"Thursday: {', '.join(thursday)}")
    if friday:
        print(f"Friday: {', '.join(friday)}")
    if next_monday:
        print(f"Next week Monday: {', '.join(next_monday)}")


get_birthdays_per_week(users)
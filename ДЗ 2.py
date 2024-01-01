from datetime import date, datetime, timedelta 

def get_birthdays_per_week(users): 
    today = date.today() 
    current_weekday = today.weekday() 

    birthdays_per_week = {} 
    for i in range(7):
        current_day = (current_weekday + i) % 7 
        current_date = today + timedelta(days=i) 
        current_weekday_name = current_date.strftime('%A') 

        birthdays_per_week[current_weekday_name] = [] 


        for user in users: 
            user_birthday = user['birthday'].replace(year=today.year) 

            if user_birthday < today: 
                user_birthday = user_birthday.replace(year=today.year + 1) 

            if user_birthday.weekday() == current_day: 
                birthdays_per_week[current_weekday_name].append(user['name']) 

    return birthdays_per_week



users = [
        {
            "name": "Bill", 
            "birthday": datetime(1955, 10, 28).date()
        },
        {
            "name": "Roma", 
            "birthday": datetime(1994, 1, 1).date()
        },
        {
            "name": "Vika", 
            "birthday": datetime(2001, 1, 3).date()
        },
        {
            "name": "Marynka", 
            "birthday": datetime(2002, 1, 3).date()
        },
]

# assert get_birthdays_per_week(users) == {
#     'Monday': ['Roma'], 
#     'Wednesday': ['Vika', "Marynka"]
# }

print(get_birthdays_per_week(users))

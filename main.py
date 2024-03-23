from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def get_day_of_week(birthdate):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_index = birthdate.weekday()
    return days_of_week[day_index]

def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def main():
    people = []
    
    while True:
        name = input("Enter person's name (or 'done' to finish): ")
        if name.lower() == "done":
            break
        
        birthdate_str = input("Enter person's birthdate (YYYY-MM-DD): ")
        if not validate_date(birthdate_str):
            print("Invalid date format. Please enter a valid date in YYYY-MM-DD format.")
            continue
        
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
        age = calculate_age(birthdate)
        day_of_week = get_day_of_week(birthdate)
        
        people.append((name, age, day_of_week))
    
    if not people:
        print("No data entered.")
        return
    
    oldest_person = max(people, key=lambda x: x[1])
    youngest_person = min(people, key=lambda x: x[1])
    
    total_people = len(people)
    
    print("\nResults:")
    print("Oldest person:", oldest_person[0], "with age:", oldest_person[1], "born on a", oldest_person[2])
    print("Youngest person:", youngest_person[0], "with age:", youngest_person[1], "born on a", youngest_person[2])
    print("Total people:", total_people)
    

if __name__ == "__main__":
    main()

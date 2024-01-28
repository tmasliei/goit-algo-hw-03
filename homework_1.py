def get_days_from_today(user_input): 
    try: 
        user_date = datetime.strptime(user_input, "%Y-%m-%d") 
        current_date = datetime.today() 
        x = current_date - user_date 
        return int(x.days) 
    except ValueError: 
        print(f"ERROR. Time data {user_input} does not match format '%Y-%m-%d'") 
        return None 
 
 
if name == '__main__': 
    user_input_ = input("Enter the date in the format YYYY-MM-DD: ") 
    print(get_days_from_today(user_input_))
from datetime import datetime as dtdt
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

def get_upcoming_birthdays(users=None):
    tdate=dtdt.today().date() # беремо сьогоднішню дату
    tdate.toordinal() # в дні з початку часу
    birthdays=[] # створюємо список для результатів
    for user in users: # перебираємо користувачів
        bdate=user["birthday"] # отрумуємо дату народження людини у вигляді рядка
        bdate=str(tdate.year)+bdate[4:] # Замінюємо рік на поточний
        bdate=dtdt.strptime(bdate, "%Y.%m.%d").date() # перетворюємо дату народження в об’єкт date
        week_day=bdate.isoweekday() # Отримуємо день тижня (1-7)
        bdo=bdate.toordinal() #в дні з початку часу
        days_between=bdo-tdate.toordinal() # рахуємо різницю між зараз і днем народження цьогоріч у днях
        if 0<=days_between<7: # якщо день народження протягом 7 днів від сьогодні
            if week_day<6: #  якщо пн-пт
                birthdays.append({'name':user['name'], 'birthday':bdate.isoformat().replace('-','.')[:10]}) 
                # Додаємо запис у список. Isoformat дає дату у вигляді yyyy-mm-dd, тому треба замінити - на .
            else:
                if dtdt.fromordinal(bdo+1).weekday()==0:# якщо неділя
                    birthdays.append({'name':user['name'], 'birthday':dtdt.fromordinal(bdo+1).isoformat().replace('-','.')[:10]})
                    #Переносимо на понеділок. Додаємо запис у список. Isoformat дає дату у вигляді yyyy-mm-dd, тому треба замінити - на .
                elif dtdt.fromordinal(bdo+2).weekday()==0: #якщо субота
                    birthdays.append({'name':user['name'], 'birthday':dtdt.fromordinal(bdo+2).isoformat().replace('-','.')[:10]})
                    #Переносимо на понеділок. Додаємо запис у список. Isoformat дає дату у вигляді yyyy-mm-dd, тому треба замінити - на .
    return birthdays


    #return {"name":name, "congratulation_date":cdate}

print(get_upcoming_birthdays(users))
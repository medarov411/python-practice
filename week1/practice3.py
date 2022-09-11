#1
true = True
false = False
def is_alive(health):
    if health <= 0:
        print(false)
    else:
        print(true)
is_alive(int(input("amount of HP: ")))

#2
def season_events(number_of_month):
    if number_of_month == 12 or 1 or 2:
        season = 'winter'
        print("Season is",season," White snow fell outside the window")
    elif number_of_month == 3 or 4 or 5:
        season = 'spring'
        print("Season is",season," Birds sang beautiful songs")
    elif number_of_month == 6 or 7 or 8:
        season = 'summer'
        print("Season is",season," The sun shone brighter than ever")
    elif number_of_month  == 9 or 10 or 11:
        season = 'autumn'
        print("Season is",season," The harvest was incredible")
    else:
        print("enter the correct value")

season_events(input("Enter the month: "))
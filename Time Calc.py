import math
import string


def round_to_5(x):
    z = math.floor(x)
    y = z % 5
    if y == 0:
        return z
    if y <= 2:
        return z - y
    if y >= 3:
        return z + (5-y)


print("Tristan's Time Calculator V1")
print("Choose addition type")
print("1: Adding decimal hours")
print("2: Adding Hours and Minutes")

choice = input()
user_input = ""
while choice != "3":
    time_sum = 0
    if choice == "1":
        print("Please enter your following times in this format: 1 hour and 40 minutes = 1.66")
        print("After entering all times, enter 'sum' for result")
        while user_input != "sum":
            user_input = input("Enter time: ")
            added_time = 0
            try:
                added_time = float(user_input)
            except ValueError:
                print("Please enter a postive decimal value")
            if added_time > 0:
                
                time_sum += round(added_time,2)
                print(time_sum)
        
        print(f"\nYour total sum in decimal hours is: {time_sum}")
        decimal = time_sum % 1
        d2m = (time_sum % 1) * 60
        minutes = round_to_5(d2m)
        hours = time_sum - decimal
        print(f"\nYour total time in hours and minutes is: {math.floor(hours)}h {minutes}m")

        print("\nTo add another set of times, enter 1 or 2")
        print("To finish, enter 3")
        user_input = ""
        choice = input()


    elif choice == "2":
        print("Please enter your following times in this format: 1 hour and 40 minutes = 1:40")
        print("After entering all times, enter 'sum' for result")
        hour_sum = 0
        minute_sum = 0
        while user_input != "sum":
            user_input = input("Enter time: ")
            #time_split = []
            try:
                time_split = user_input.split(":")
            except ValueError:
                print("Please enter time in correct format")
            if len(time_split) == 2:
                hour_sum += int(time_split[0])
                minute_sum += int(time_split[1])
                if minute_sum >  60:
                    hour_sum += 1
                    minute_sum = minute_sum % 60
                print(f"{hour_sum}:{minute_sum}")

        print(f"\nYour total time in hours and minutes is: {hour_sum}h {minute_sum}m")
        m2d = minute_sum / 60
        time_sum = round(hour_sum + m2d,2)
        print(f"\nYour total sum in decimal hours is: {time_sum}")

        print("\nTo add another set of times, enter 1 or 2")
        print("To finish, enter 3")
        user_input = ""
        choice = input()

    else:
        print("Please select a valid option")
        choice = input()

            

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannnot be 0.")
    return dividend/divisor


grades = []

print("Welcome to the average grades program.")

if len(grades) == 0:
    print("You don't have grades yet.")

try:
    average  = divide(sum(grades), len(grades))
    # putting this in else for different way of doing things
    # print(f"The average grade is {average}.")
    
except ZeroDivisionError as e:
    print(e)
    print("There are no grades yet in your list")
else:
    print(f"The average grade is {average}.")
finally:
    print("Thank you.")
    

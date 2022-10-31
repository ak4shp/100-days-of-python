def is_leap(year):
    """ It checks whether a year is leap year or not. Returns Boolean."""
    """ The Above line is the 'docstring' for this function. It appears when you hover the function name.""" 
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(a_year, a_month):
    '''It returns how many days are in that month. Takes YEAR and MONTH as parameter.'''
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if is_leap(a_year) and a_month == 2:
        return 29
    else:
        return month_days[a_month-1]
  
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)








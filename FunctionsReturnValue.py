def is_leap(year):
    """Take an Year as input and returns true if it is leap year, false if it is not"""
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
def days_of_month(Year,Month):
    if Month > 12 or Month < 1:
        return "Invalid Month input"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(Year) and Month == 2:
        return 29
    else:
        return month_days[Month-1]
Year = int(input('Enter the Year ?'))
Month = int(input('Enter the Month ?'))
days = days_of_month(Year,Month)  
print(days)
def is_leap(year: int)-> bool:

  if(year % 4== 0 and year % 100 != 0) or (year % 400 == 0):
    return True
  else:
      return False

year =int(input("Enter the year: "))
print(is_leap(year))

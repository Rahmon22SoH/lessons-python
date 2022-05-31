persons_age = int(input("Ввидите свой возраст "))

def determine_age(age, max_age = 100):
  age = abs(age)
  max_age = abs(max_age)
  if max_age >= 100:
    raise ValueError ('больше 100')
  if age >= 0 and age <= 5:
    return age
  elif age >= 6 and age <= 17:
    return age
  elif age >= 18 and age <= 23:
    return age
  elif age >= 24 and age <= 65:
    return age 

definition = determine_age(persons_age)
print(definition)
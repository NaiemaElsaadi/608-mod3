# File 1 - bult-in-min-max.py (Sections 4.1, 4.2, 4.3) " Naiema Elsaadi!!"

def maximum(value1, value2, value3):
    """Return the maximum of three values."""
    
    max_value = value1

    if  value2 > max_value:
         max_value = value2

         if value3 > max_value:
         
          max_value = value3
                 
         return max_value


max(22,17,40)
print('The maximum using the built-in max function is', max(22,17,40))
min(12, 5, 30)
print('The minimum using the built-in min function is', min(12, 5, 30))


def minimum(value1, value2, value3, value4):
  """Return the minimum of three values."""
  min_value = value1
  if value2 < min_value:
    min_value = value2
  if value3 < min_value:
    min_value = value3
  if value4 < min_value:
    min_value = value4
  return min_value
minimum(10, 20, 30, 40)
print('The minimum using a def function is', minimum(10, 20, 30, 40))
print('My name is Naiema Elsaadi')
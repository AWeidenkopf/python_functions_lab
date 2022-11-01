# Challenge 1 

def sum_to(n):
  i = 0
  sum = 0
  while i <= n:
    sum += i
    i+= 1
  return sum

# print(sum_to(6)

# --------------------------------------------------------------------------- #

# Challenge 2 

def largest(list):
  sorted_list =sorted(list)
  return sorted_list[-1]


# print(largest([1221,5,31,6,8,76,1,3]))
# print(largest([1, 2, 3, 4, 0]))

# --------------------------------------------------------------------------- #

# Challenge 3

def occurences(str1, str2):
  return str1.count(str2)

# print(occurences('hellolollohelo', 'lo'))

# --------------------------------------------------------------------------- #

# Challenge 4

def product(*args):
  result = 1 
  for arg in args:
    result = result * arg
  return result

print(product(4, 0.5, 5))







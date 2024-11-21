from fake_math import divide as divide_fake
from true_math import divide as divide_true

result1 = divide_fake(36, 3)
result2 = divide_fake(8,0)
result3 = divide_true(66,6)
result4 = divide_true(12,0)
print(result1)
print(result2)
print(result3)
print(result4)
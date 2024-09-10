from fake_math import divide as div_fake
from true_math import divide as div_true

print(div_fake(300, 0))
print(div_true(300, 0))

print(div_fake(300, 4))
print(div_true(300, 4))
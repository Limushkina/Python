# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
import random
x = random.randint(1, 100)
print(x)
y = random.randint(1, 100)
print(y)
z = random.randint(1, 100)
print(z)
if not(x or y or z) == -x and -y and -z:
    print(True)
else:
    print(False)
import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize production", pulp.LpMaximize)


# Визначення змінних
lemonade = pulp.LpVariable('lemonade', lowBound=0, cat='Integer')  # Кількість продукту лимонаду
fruit_juice = pulp.LpVariable('fruit_juice', lowBound=0,  cat='Integer')  # Кількість продукту фруктового соку

# Функція цілі (Максимізація виробництва)
model += lemonade + fruit_juice, "Total Production"

# Додавання обмежень
model += 2 * lemonade + 1 * fruit_juice <= 100  # Обмеження для води
model += 1 * lemonade + 0 * fruit_juice <= 50  # Обмеження для цукру
model += 1 * lemonade + 0 * fruit_juice <= 30
model += 0 * lemonade + 2 * fruit_juice <= 40

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробництво лимонаду:", lemonade.varValue)
print("Виробництво соку:", fruit_juice.varValue)
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x**2

# Межі інтегрування
a = 0  # нижня межа
b = 2  # верхня межа

# Метод Монте-Карло для обчислення інтеграла
N = 10000  # Кількість випадкових точок
random_x = np.random.uniform(a, b, N)
integral_monte_carlo = (b - a) * np.mean(f(random_x))

print("Обчислене значення інтеграла методом Монте-Карло:", integral_monte_carlo)

# Аналітичне обчислення інтеграла за допомогою scipy.quad
result_quad, error_quad = spi.quad(f, a, b)
print("Інтеграл (аналітичне обчислення):", result_quad)
print("Похибка аналітичного обчислення:", error_quad)

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Додавання випадкових точок
ax.scatter(random_x, f(random_x), color='blue', s=1, alpha=0.5)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()


print("\nВисновки:")
print(f"Метод Монте-Карло дав результат: {integral_monte_carlo}")
print(f"Аналітичний метод (quad) дав результат: {result_quad} з похибкою {error_quad:.2e}")
print(f"Різниця між результатами: {abs(integral_monte_carlo - result_quad):.6f}")


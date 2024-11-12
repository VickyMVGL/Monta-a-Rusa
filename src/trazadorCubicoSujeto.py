import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt


# Datos de los puntos de control
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([0.5, 0.8, 1.0, 0.9, 1.2, 0.7])

# Condiciones de frontera para el trazador cúbico sujeto (segunda derivada en los extremos)
bc_type = ((2, 0.0), (2, 0.0))  # Aquí hemos fijado la segunda derivada en 0 en ambos extremos

# Crear el trazador cúbico
cs = CubicSpline(x_data, y_data, bc_type=bc_type)
cs_clamped = CubicSpline(x_data, y_data, bc_type=((1, 0), (1, 0)))


# Graficar los resultados
x_fine = np.linspace(x_data.min(), x_data.max(), 100)
y_fine = cs(x_fine)
y_clamped = cs_clamped(x_fine)

plt.plot(x_data, y_data, 'o', label='Puntos de control')
plt.plot(x_fine, y_fine, '-', label='Interpolación cúbica, segunda derivada')
plt.plot(x_fine, y_clamped, label='Interpolación cúbica, primera derivada')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolación de trazador cúbico sujeto')
plt.show()
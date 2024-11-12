import numpy as np
import matplotlib.pyplot as plt

# Datos
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([1.2, 2.3, 3.7, 3.1, 5.0, 7.4])
grado = 2 

# Ajustar el polinomio de mínimos cuadrados
coeficientes = np.polyfit(x_data, y_data, grado)

# Crear el polinomio
p = np.poly1d(coeficientes)

# Puntos para graficar
x_fine = np.linspace(min(x_data), max(x_data), 100)
y_fine = p(x_fine)

print("Coeficientes del polinomio ajustado:", coeficientes)

# Graficar los puntos experimentales y el polinomio ajustado
plt.scatter(x_data, y_data, color='red', label='Datos experimentales')
plt.plot(x_fine, y_fine, color='blue', label=f'Ajuste polinómico (grado {grado})')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Ajuste de Polinomio de Mínimos Cuadrados')
plt.show()



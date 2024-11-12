import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt

# Definimos la matriz de coeficientes A y el vector de términos independientes b
import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt

def generar_sistema_aleatorio():
    
    # Genera una matriz A de tamaño n x n con valores enteros aleatorios entre -10 y 10
    A = np.random.randint(-5, 5, (3, 3))
    
    # Genera un vector b de tamaño n con valores enteros aleatorios entre -10 y 10
    b = np.random.randint(-5, 5, 3)
    
    # Verifica que la matriz sea invertible; si no lo es, vuelve a generarla
    while np.linalg.det(A) == 0:
        A = np.random.randint(-5, 5, (3, 3))
    
    return A, b

# Generar un sistema aleatorio de 3 ecuaciones (puedes cambiar el tamaño)
A, b = generar_sistema_aleatorio()


# Resolvemos el sistema de ecuaciones
x = solve(A, b)

print("Las fuerzas en los puntos críticos son:", x)

# Visualización (ejemplo simplificado, asumiendo un sistema 1D)
# Ajusta esta parte según tu problema específico
plt.plot(range(len(x)), x, 'o-')
plt.xlabel('Punto crítico')
plt.ylabel('Fuerza')
plt.title('Distribución de fuerzas en los puntos críticos')
plt.grid(True)
plt.show()
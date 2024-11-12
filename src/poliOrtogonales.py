import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre, chebyt

# Parámetros
orden = 5  # Orden máximo del polinomio
intervalo = np.linspace(-1, 1, 100)  # Intervalo para graficar los polinomios

# Crear figura para los polinomios de Legendre y Chebyshev
fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# Graficar Polinomios de Legendre
for n in range(orden + 1):
    Pn = legendre(n)  # Polinomio de Legendre de orden n
    axs[0].plot(intervalo, Pn(intervalo), label=f'P_{n}(x)')

axs[0].set_title('Polinomios de Legendre')
axs[0].set_xlabel('x')
axs[0].set_ylabel('Pn(x)')
axs[0].legend()
axs[0].grid(True)

# Graficar Polinomios de Chebyshev
for n in range(orden + 1):
    Tn = chebyt(n)  # Polinomio de Chebyshev de primer tipo de orden n
    axs[1].plot(intervalo, Tn(intervalo), label=f'T_{n}(x)')

axs[1].set_title('Polinomios de Chebyshev')
axs[1].set_xlabel('x')
axs[1].set_ylabel('Tn(x)')
axs[1].legend()
axs[1].grid(True)

# Mostrar gráficos
plt.tight_layout()
plt.show()
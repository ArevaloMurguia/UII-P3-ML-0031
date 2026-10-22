print("--- Arevalo Rafael NC:0031 Fecha:22/10/26 ---")
import numpy as np
print("=== 1. Indexacion de un arreglo de una dimension ===")
n0031 = np.array([10, 20, 30, 40, 50])
print(n0031)
print(n0031[0])
print(n0031[3])
print(n0031[-1])
print(n0031[-2])
print("-" * 40)
print("=== 2. Indexacion de un arreglo de dos dimensiones (2D) ===")
n0031 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(n0031)
print(n0031[0, 0])
print(n0031[1, 2])
print(n0031[-1, -1])
print(n0031[-2, -2])
print("-" * 40)
print("=== 3. Indexacion de un arreglo de tres dimensiones (3D) ===")
n0031 = np.array([
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])
print(n0031)
print(n0031[0, 0, 0])
print(n0031[1, 1, 2])
print(n0031[-1, -1, -2])
print("--- Arevalo Rafael NC:0031 Fecha:22/10/26 ---")
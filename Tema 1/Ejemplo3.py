# Determinar el número más pequeño que la computadora puede distinguir
epsilon = 1.0
while (1.0 + epsilon) > 1.0:
    epsilon = epsilon / 2.0

epsilon = epsilon * 2.0
print(f"El Épsilon de esta máquina es: {epsilon}")
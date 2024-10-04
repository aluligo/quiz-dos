#  calcular la liquidación
def calcular_liquidacion(salario, dias_laborados):
    prima = salario * dias_laborados / 360
    cesantias = salario * dias_laborados / 360
    intereses_cesantias = (cesantias * 0.12)/dias_laborados
    vacaciones = salario * dias_laborados / 720
    # sacar la  liquidación Total
    total_liquidacion = prima + cesantias + intereses_cesantias + vacaciones
    return prima, cesantias, intereses_cesantias, vacaciones, total_liquidacion
# ingresar Datos
nombre = input("Ingrese el nombre: ")
dias_laborados = int(input("Ingrese el número de días laborados: "))
salario = float(input("Ingrese el salario del empleado: "))

# invocar la funcion
prima, cesantias, intereses_cesantias, vacaciones, total_liquidacion = calcular_liquidacion(salario, dias_laborados)
# resultado
print("\n--- LIQUIDACION DEL EMPLEADO ---")
print(f"\nSeñor {nombre} para los {dias_laborados}  dias laborados y salario ${salario}, su liquidacion se compone asi :")
print(f"Prima: ${prima:.2f}")
print(f"Cesantías: ${cesantias:.2f}")
print(f"Intereses sobre cesantías: ${intereses_cesantias:.2f}")
print(f"Vacaciones: ${vacaciones:.2f}")
print(f"Total liquidación: ${total_liquidacion:.2f}")
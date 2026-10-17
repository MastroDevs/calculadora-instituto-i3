# script.py - Lógica de cálculo de notas para Instituto i3

def calcular_promedio(n1, n2, n3):
    """Calcula el promedio aritmético de tres notas."""
    return round((n1 + n2 + n3) / 3, 2)

def evaluar_estado(promedio):
    """Determina si el estudiante aprueba (nota mínima 3.0)."""
    if promedio >= 3.0:
        return "APROBADO"
    else:
        return "REPROBADO"

if __name__ == "__main__":
    print("=== Calculadora Instituto i3 ===")
    nombre = input("Ingrese nombre del estudiante: ")
    try:
        n1 = float(input("Ingrese nota 1 (0 a 5): "))
        n2 = float(input("Ingrese nota 2 (0 a 5): "))
        n3 = float(input("Ingrese nota 3 (0 a 5): "))
        
        if all(0 <= n <= 5 for n in [n1, n2, n3]):
            prom = calcular_promedio(n1, n2, n3)
            estado = evaluar_estado(prom)
            print(f"\nEstudiante: {nombre}")
            print(f"Promedio: {prom} - Estado: {estado}")
        else:
            print("Error: Las notas deben estar en el rango de 0 a 5.")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.") 
        

 
    

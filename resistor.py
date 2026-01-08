def conversor_resistencias():
    # Diccionarios de datos técnicos
    valores = {
        "negro": 0, "marron": 1, "rojo": 2, "naranja": 3, "amarillo": 4,
        "verde": 5, "azul": 6, "violeta": 7, "gris": 8, "blanco": 9
    }
    
    multiplicadores = {
        "negro": 1, "marron": 10, "rojo": 100, "naranja": 1000,
        "amarillo": 10000, "verde": 100000, "azul": 1000000,
        "oro": 0.1, "plata": 0.01
    }

    print("\n==============================================")
    print("   CONVERSOR DE CÓDIGO DE COLORES (4 BANDAS)")
    print("==============================================")

    while True:
        try:
            print("\nIntroduce los colores de las bandas (o escribe 'salir'):")
            
            b1 = input("Banda 1: ").strip().lower()
            if b1 == 'salir': break
            
            b2 = input("Banda 2: ").strip().lower()
            b3 = input("Banda 3 (Multiplicador): ").strip().lower()

            # Validación de existencia en el diccionario
            if b1 in valores and b2 in valores and b3 in multiplicadores:
                # Fórmula técnica: (Dígito1 Dígito2) * Multiplicador
                resultado_ohms = (valores[b1] * 10 + valores[b2]) * multiplicadores[b3]
                
                # Mejora: Formateo de unidades para mayor legibilidad
                if resultado_ohms >= 1000000:
                    print(f"--> Valor: {resultado_ohms / 1000000:.2f} MΩ")
                elif resultado_ohms >= 1000:
                    print(f"--> Valor: {resultado_ohms / 1000:.2f} KΩ")
                else:
                    print(f"--> Valor: {resultado_ohms:.2f} Ω")
            else:
                print("❌ Error: Uno o más colores no son válidos. Intenta de nuevo.")

        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

        # Preguntar si desea continuar
        opcion = input("\n¿Consultar otra resistencia? (s/n): ").lower()
        if opcion != 's':
            print("Cerrando el sistema de consulta. ¡Hasta luego!")
            break

if __name__ == "__main__":
    conversor_resistencias()

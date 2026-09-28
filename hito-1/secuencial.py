"""
secuencial.py — Hito 1
Suma secuencial de un vector grande. Baseline de referencia.
"""
import sys
import time
import array

# TODO (Integrante 1):
# 1. Definir la función suma_secuencial(data) que acumule todos los elementos.
# 2. Manejar memoria contigua de 32-bit floats usando array.array('f').
# 3. Medir el tiempo con time.perf_counter() e imprimir: N, suma y tiempo_ms.

def suma_secuencial(data: array.array) -> float:
    # TODO: Implementar acumulador secuencial
    return 0.0

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else (1 << 24)
    print(f"[ESQUELETO] secuencial.py pendiente de implementación por Integrante 1 (N={n})")

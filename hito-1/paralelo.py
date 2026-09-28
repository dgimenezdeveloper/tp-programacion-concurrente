"""
paralelo.py — Hito 1
Esqueleto multi-hilo con despacho dinámico por bloques.
"""
import sys
import time
import array
import threading

# Primitiva de sincronización de memoria compartida
lock_proximo = threading.Lock()
proximo = 0
BLOQUE = 1 << 16  # 65536 elementos

def worker(data: array.array, n: int, tid: int, parciales: list):
    global proximo
    acc = 0.0
    while True:
        # TODO (Integrante 2): Tomar un rango [lo, hi) de forma exclusiva:
        # 1. Adquirir lock_proximo (Protocolo de Entrada a la Sección Crítica).
        # 2. Si proximo >= n, salir del bucle (no hay más trabajo).
        # 3. lo = proximo; proximo = min(proximo + BLOQUE, n); hi = proximo.
        # 4. Liberar lock_proximo (Protocolo de Salida).
        # 5. El bucle for que suma data[lo:hi] debe quedar FUERA del lock para no serializar.
        break # Placeholder

    parciales[tid] = acc

def suma_paralela(data: array.array, n: int, t: int) -> float:
    # TODO (Integrante 2): Crear hilos, arrancarlos (.start()), esperar (.join())
    # y reducir el arreglo parciales en el hilo principal.
    return 0.0

if __name__ == "__main__":
    print("[ESQUELETO] paralelo.py pendiente de implementación por Integrante 2")

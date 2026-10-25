
"""
secuencial.py — Hito 1
Baseline secuencial para la suma de un vector de floats de 32 bits.

TODO resuelto:
- Suma secuencial mediante un acumulador local.
- Vector contiguo con array.array('f').
- Medición con time.perf_counter(), excluyendo la inicialización.
- Tamaño N configurable por línea de comandos.
"""

import array
import sys
import time


N_DEFAULT = 1 << 24


def suma_secuencial(data: array.array) -> float:
    """Devuelve la suma de todos los elementos del vector."""
    acumulador = 0.0

    for valor in data:
        acumulador += valor

    return acumulador


def main() -> None:
    """Inicializa los datos, mide la suma y muestra el resultado."""
    try:
        n = int(sys.argv[1]) if len(sys.argv) > 1 else N_DEFAULT
        if n < 1:
            raise ValueError("N debe ser mayor o igual a 1.")
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)

    data = array.array("f", [1.0]) * n

    inicio = time.perf_counter()
    suma = suma_secuencial(data)
    tiempo_ms = (time.perf_counter() - inicio) * 1000

    print(f"N={n} | suma={suma:.1f} | tiempo_ms={tiempo_ms:.3f} ms")


if __name__ == "__main__":
    main()


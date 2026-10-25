
"""
secuencial.py — Hito 1

Baseline secuencial para la suma de un vector de floats de 32 bits.

Características:
- Suma secuencial mediante un acumulador local.
- Vector contiguo con array.array('f').
- Medición con time.perf_counter(), excluyendo la inicialización.
- Tamaño N configurable por línea de comandos.
- Comprobación automática del error relativo.
- Validación controlada de entradas inválidas.
"""

import array
import math
import sys
import time


N_DEFAULT = 1 << 24
TOLERANCIA_RELATIVA = 1e-12


def suma_secuencial(data: array.array) -> float:
    """Devuelve la suma de todos los elementos del vector."""
    acumulador = 0.0

    for valor in data:
        acumulador += valor

    return acumulador


def obtener_tamano() -> int:
    """Obtiene y valida el tamaño del vector desde la línea de comandos."""
    if len(sys.argv) > 2:
        raise ValueError("Se permite como máximo un argumento: N.")

    if len(sys.argv) == 1:
        return N_DEFAULT

    try:
        n = int(sys.argv[1])
    except ValueError as error:
        raise ValueError("N debe ser un número entero válido.") from error

    if n < 1:
        raise ValueError("N debe ser mayor o igual a 1.")

    return n


def main() -> None:
    """Inicializa los datos, mide la suma y verifica su precisión."""
    try:
        n = obtener_tamano()
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)

    # Inicialización fuera del intervalo medido.
    data = array.array("f", [1.0]) * n

    inicio = time.perf_counter()
    suma = suma_secuencial(data)
    tiempo_ms = (time.perf_counter() - inicio) * 1000

    # Como todos los elementos valen 1.0, la suma esperada es N.
    suma_esperada = float(n)
    error_relativo = abs(suma - suma_esperada) / abs(suma_esperada)

    precision_correcta = (
        math.isfinite(suma)
        and error_relativo <= TOLERANCIA_RELATIVA
    )

    print(
        f"N={n} | "
        f"suma={suma:.1f} | "
        f"esperada={suma_esperada:.1f} | "
        f"error_relativo={error_relativo:.3e} | "
        f"tiempo_ms={tiempo_ms:.3f} ms"
    )

    if not precision_correcta:
        print(
            f"Error: la suma no cumple la tolerancia relativa "
            f"de {TOLERANCIA_RELATIVA:.1e}.",
            file=sys.stderr,
        )
        sys.exit(1)

    print("Verificación de precisión: OK")


if __name__ == "__main__":
    main()

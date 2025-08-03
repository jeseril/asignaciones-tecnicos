import heapq
from typing import List, Dict

def optimizar_asignacion(
    asistencias: List[dict],
    tecnicos: List[str]
) -> Dict[str, List[int]]:
    """
    Recibe una lista de asistencias (cada dict con 'id', 'tipo', 'zona')
    y una lista de nombres de técnicos.
    Asigna hasta 2 asistencias por técnico de forma equilibrada.
    Devuelve dict {tecnico: [id1, id2, ...]}.
    Complejidad: O(n·log k).
    """
    # 1) Prepara resultado
    asignaciones = {t: [] for t in tecnicos}
    # 2) Min-heap (carga, índice, nombre)
    heap = [(0, i, nombre) for i, nombre in enumerate(tecnicos)]
    heapq.heapify(heap)
    # 3) Asigna cada asistencia
    for a in asistencias:
        if not heap:
            break
        carga, idx, nombre = heapq.heappop(heap)
        if carga >= 2:
            break
        asignaciones[nombre].append(a["id"])
        heapq.heappush(heap, (carga + 1, idx, nombre))
    return asignaciones

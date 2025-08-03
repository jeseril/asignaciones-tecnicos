import pytest
from asignacion import optimizar_asignacion

def test_asignacion_equilibrada():
    asist = [{"id": i, "tipo":"t", "zona":"z"} for i in range(1,7)]
    tecn = ["A","B","C"]
    out = optimizar_asignacion(asist, tecn)
    print("Asignación resultante:", out)
    assert all(len(v)==2 for v in out.values())
    assert sorted(sum(out.values(), [])) == [1,2,3,4,5,6]

def test_menos_asistencias_que_capacidad():
    asist = [{"id": 1, "tipo":"x", "zona":"y"}]
    tecn = ["X","Y"]
    out = optimizar_asignacion(asist, tecn)
    print("Asignación resultante:", out)
    assert out["X"] == [1]
    assert out["Y"] == []

def test_mas_asistencias_que_capacidad():
    asist = [{"id": i, "tipo":"t", "zona":"z"} for i in range(1,8)]
    tecn = ["T1","T2","T3"]
    out = optimizar_asignacion(asist, tecn)
    print("Asignación resultante:", out)
    all_ids = sum(out.values(), [])
    assert len(all_ids) == 6
    assert 7 not in all_ids

def test_sin_asistencias():
    # Caso: no hay asistencias → todos los técnicos deben quedar con lista vacía
    asist = []
    tecn  = ["A","B","C"]
    out   = optimizar_asignacion(asist, tecn)
    # Cada técnico existe en el dict, pero con lista vacía
    assert set(out.keys()) == set(tecn)
    assert all(v == [] for v in out.values())
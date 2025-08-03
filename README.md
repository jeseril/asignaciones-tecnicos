# Optimizador de Asignación de Asistencias

## Contexto
Repartimos asistencias (id, tipo, zona) entre técnicos, max. 2 por técnico, buscando balance.

Internamente utilizamos un min-heap (montículo) para asignar siempre la siguiente asistencia al técnico con menos carga.


## Por qué usamos un min-heap

Elegimos un **min-heap** porque nos permite, en cada paso, extraer rápidamente al técnico con la menor carga (es decir, con menos asignaciones hasta el momento). De este modo:

1. Garantizamos balance de tareas, evitando sobrecargar a un mismo técnico. 
2. El heap garantiza en cada paso que siempre se seleccione el técnico con menos tareas, sin tener que reevaluar toda la lista.

## EJEMPLO
Con 1.000 asistencias y 100 técnicos:

**Búsqueda lineal:** hasta 1.000·100 = 100.000 comparaciones.

**Heap:** 
log 2 (1000)≈9,97 ⟶ 10 pasos,

1.000·10 = 7.000 comparaciones.

## Instalación
```bash
git clone https://github.com/jeseril/asignaciones-tecnicos.git
cd asignaciones-tecnicos
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
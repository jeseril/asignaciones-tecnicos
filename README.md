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
```

## Video de funcionamiento (test)

[▶️ Ver demostración en YouTube](https://youtu.be/X-B9eTv3drM)

## Referencias

- 📘 Documentación oficial de `heapq`:\
  [https://docs.python.org/3/library/heapq.html](https://docs.python.org/3/library/heapq.html)

- 📚 Complejidad `n log n`:\
  [https://www.educative.io/answers/nlogn-sorting-algorithms](https://www.educative.io/answers/nlogn-sorting-algorithms)

- 🎥 Explicación visual de heapsort:\
  [https://www.youtube.com/watch?v=wGSQ486Y4sc](https://www.youtube.com/watch?v=wGSQ486Y4sc)

- 📄 Artículo en GeeksforGeeks sobre Heap Sort:\
  [https://www.geeksforgeeks.org/dsa/heap-sort/](https://www.geeksforgeeks.org/dsa/heap-sort/)

- 🧠 Big-O notation en Python:\
  [https://medium.com/@limeira.felipe94/understanding-big-o-notation-o-n-and-o-log-n-in-python-3bb13f55ad7b](https://medium.com/@limeira.felipe94/understanding-big-o-notation-o-n-and-o-log-n-in-python-3bb13f55ad7b)


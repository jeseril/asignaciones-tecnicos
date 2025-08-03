# Optimizador de Asignación de Asistencias

## Contexto
Repartimos asistencias (id, tipo, zona) entre técnicos, max. 2 por técnico, buscando balance.

## Instalación
```bash
git clone <repo>
cd asignaciones-tecnicos
python3 -m venv venv
source venv/bin/activate   # o venv\\Scripts\\activate en Windows
pip install -r requirements.txt
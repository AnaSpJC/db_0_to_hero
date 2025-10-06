## 🧼 Fase 2 y 🧪 Fase 3 – Limpieza y derivación

Se aplicaron funciones con logging para limpiar y validar:

- `Nombre`: se eliminaron espacios, se capitalizó y se validó si era texto alfabético.
- `Edad`: se convirtió a entero y se validó que fuera mayor a 0.

Se generaron columnas derivadas:

- `Edad_valida`: indica si la edad es válida.
- `Mayor`: indica si la persona es mayor de edad (>18).
- `Rango etario`: clasifica en "Adolescente", "Jóven", "Adulto", "Mayor".

Se documentó trazabilidad en:

- `Log_nombre`: estado, original y resultado de cada nombre.
- `Log_edad`: estado, original y resultado de cada edad.

🔍 El archivo `personas_limpias.xlsx` contiene todas las columnas limpias y derivadas, con errores detectados y segmentación aplicada.

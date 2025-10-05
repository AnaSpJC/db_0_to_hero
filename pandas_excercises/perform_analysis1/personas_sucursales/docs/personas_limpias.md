# Documentación registros/valores descartados

##  Filtrado curatorial
Durante el proceso de limpieza, se detectaron registros con errores en los campos `Nombre` y `Edad`. Estos registros fueron excluidos del archivo final para garantizar la calidad del análisis.

### Criterios de exclusión:
- Nombre con caracteres no alfabéticos (por ejemplo: "123")
- Nombres vacíos
- Edad no convertible (por ejemplo: texto como "veinte")
- Edades negativas o nulas

### Registros descartados
Estos registros fueron documentados en las columnas `Log_nombre` y `Log_edad` para trazabilidad técnica.
Se conservaron en un archivo técnico (`personas_descartadas.xlsx`) para trazabilidad interna. No forman parte del archivo entregado `personas_limpias.xlsx`.

### Ejemplos de registros excluidos:

| Nombre original | Edad original | Motivo de descarte |
|------------------|----------------|---------------------|
| peDro            | veinte         | Edad no convertible |
| 123              | 40             | Nombre no alfabético |
| MARIA            | -5             | Edad negativa |
| mara             | (vacío)        | Edad nula |
| Laura            | (vacío)        | Edad nula |

🔍 Estos registros fueron excluidos del archivo `personas_limpias.xlsx` pero se conservan en `registros_descartados_cliente.xlsx` como parte del informe curatorial.







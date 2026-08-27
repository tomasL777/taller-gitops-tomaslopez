def calcular_estadisticas_notas(notas):
  
    if not notas:
        return {
            "total": 0,
            "promedio": 0.0,
            "aprobados": 0,
            "reprobados": 0,
            "nota_maxima": 0.0,
            "nota_minima": 0.0
        }

    total = len(notas)
    promedio = round(sum(notas) / total, 2)
    aprobados = sum(1 for nota in notas if nota >= 3.0)
    reprobados = sum(1 for nota in notas if nota < 3.0)
    nota_maxima = max(notas)
    nota_minima = min(notas)

    return {
        "total": total,
        "promedio": promedio,
        "aprobados": aprobados,
        "reprobados": reprobados,
        "nota_maxima": nota_maxima,
        "nota_minima": nota_minima
    }
        
 
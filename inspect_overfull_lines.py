import re

def show_lines(fname, start, end):
    lines = open(fname, encoding='utf-8').read().split('\n')
    print(f"=== {fname} ({start} to {end}) ===")
    for i in range(start-1, min(end, len(lines))):
        print(f"{i+1}: {lines[i]}")

show_lines("Fase_2/2.4_Diseno_de_Base_de_Datos_Relacional.tex", 205, 260)
show_lines("Fase_2/2.6_Arquitectura_Contenedores_Docker_Locales.tex", 200, 245)
show_lines("Fase_3/3.10_Reglas_Negocio_Validation_Gates_Middlewares_Express_v5.tex", 195, 225)
show_lines("Fase_3/3.11_Integracion_MinIO_S3_Evidencias_URLs_Prefirmadas.tex", 220, 240)
show_lines("Fase_3/3.15_Motor_Exportacion_Oficial_PDF_y_Word.tex", 215, 240)
show_lines("Fase_3/3.7_Endpoints_Persistencia_Secciones_y_Documentos.tex", 200, 225)
show_lines("Fase_4/4.1_Pruebas_Unitarias_en_Backend.tex", 335, 360)

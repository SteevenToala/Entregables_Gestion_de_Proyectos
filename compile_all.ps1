<#
.SYNOPSIS
    Compila todos los documentos LaTeX (.tex) del proyecto en sus respectivos PDFs.
.DESCRIPTION
    Recorre recursivamente las carpetas (Semana_1, Semana_2, etc.), ejecuta pdflatex
    en el directorio correspondiente para resolver imágenes y referencias, y limpia
    los archivos auxiliares si se indica.
.PARAMETER Clean
    Elimina archivos auxiliares (.aux, .log, .out, .synctex.gz, etc.) tras compilar.
#>
param (
    [switch]$Clean = $true
)

$rootDir = $PSScriptRoot
if (-not $rootDir) { $rootDir = Get-Location }

Write-Host "=====================================================" -ForegroundColor Cyan
Write-Host "  COMPILADOR AUTOMÁTICO DE ENTREGABLES LATEX (FISEI) " -ForegroundColor Cyan
Write-Host "=====================================================" -ForegroundColor Cyan

$texFiles = Get-ChildItem -Path $rootDir -Filter "*.tex" -Recurse | Where-Object { $_.FullName -notmatch '\\(\.git|\.aux|build)\\' }
$total = $texFiles.Count

if ($total -eq 0) {
    Write-Host "No se encontraron archivos .tex para compilar." -ForegroundColor Yellow
    exit 0
}

Write-Host "Se encontraron $total documentos .tex para procesar.`n" -ForegroundColor Gray

$success = 0
$failed = 0
$index = 1

foreach ($file in $texFiles) {
    $relativePath = $file.FullName.Substring($rootDir.Length).TrimStart('\', '/')
    Write-Host "[$index/$total] Compilando: $relativePath..." -ForegroundColor Yellow -NoNewline
    
    $fileDir = $file.DirectoryName
    $fileName = $file.Name
    $baseName = [System.IO.Path]::GetFileNameWithoutExtension($fileName)

    # Ejecutar pdflatex dos veces para resolver referencias cruzadas y numeración de páginas (LastPage)
    Push-Location $fileDir
    try {
        $out1 = pdflatex -interaction=nonstopmode -synctex=1 $fileName 2>&1
        $out2 = pdflatex -interaction=nonstopmode -synctex=1 $fileName 2>&1
        
        $pdfPath = Join-Path $fileDir "$baseName.pdf"
        if (Test-Path $pdfPath) {
            Write-Host " [OK]" -ForegroundColor Green
            $success++
        } else {
            Write-Host " [ERROR]" -ForegroundColor Red
            $failed++
        }

        # Limpiar auxiliares si $Clean está activo
        if ($Clean) {
            Get-ChildItem -Path $fileDir -Filter "$baseName.*" | Where-Object {
                $_.Extension -in @(".aux", ".log", ".out", ".toc", ".synctex.gz", ".fls", ".fdb_latexmk")
            } | Remove-Item -Force -ErrorAction SilentlyContinue
        }
    }
    catch {
        Write-Host " [FALLO]: $_" -ForegroundColor Red
        $failed++
    }
    finally {
        Pop-Location
    }

    $index++
}

Write-Host "`n-----------------------------------------------------" -ForegroundColor Cyan
Write-Host "Resumen de compilación:" -ForegroundColor White
Write-Host "  Exitosos: $success" -ForegroundColor Green
if ($failed -gt 0) {
    Write-Host "  Fallidos: $failed" -ForegroundColor Red
} else {
    Write-Host "  Fallidos: 0" -ForegroundColor Gray
}
Write-Host "-----------------------------------------------------" -ForegroundColor Cyan

# Build the Dogx technical report with XeLaTeX + Biber (no Perl / latexmk).
$ErrorActionPreference = "Stop"
Set-Location -Path $PSScriptRoot
$doc = "dogx_report"
xelatex -interaction=nonstopmode -halt-on-error "$doc.tex"
biber $doc
xelatex -interaction=nonstopmode -halt-on-error "$doc.tex"
xelatex -interaction=nonstopmode -halt-on-error "$doc.tex"
Write-Output "Built $doc.pdf"

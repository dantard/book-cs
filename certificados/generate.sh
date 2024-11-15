#!/bin/bash
rm latex/*pdf latex/*aux latex/*log
python genera_files.py
cd latex
for i in *.tex; do
    pdflatex $i
    echo $i
done
pdfunite *.pdf ../certificados.pdf

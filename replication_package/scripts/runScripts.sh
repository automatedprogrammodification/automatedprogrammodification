#!/bin/bash

# dependencies: Python3, matplotlib, numpy, pandas, treelib

mkdir ../graphs
mkdir ../graphs/space
mkdir ../graphs/delete
mkdir ../graphs/sample
mkdir ../graphs/sample_total
mkdir ../graphs/edits

echo 'basic data'
python3 processData.py delete
python3 processData.py sample
echo 'tests'
python3 processTests.py delete
python3 processTests.py sample
echo 'types'
python3 processTypeData.py sample
echo 'overlaps'
python3 processOverlaps.py 

python3 searchSpace.py
python3 drawGraphs.py delete
python3 drawGraphs.py sample project
python3 drawGraphs.py sample total
python3 drawTestGraphs.py delete
python3 drawTestGraphs.py sample
python3 drawTypeGraphs.py sample
python3 drawOverlapsGraphs.py edits

python3 createWebsite.py -> graphs.md

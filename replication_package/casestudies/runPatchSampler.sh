#!/bin/bash
rm lineData
rm statementData

array=( "arthas" "disruptor" "druid" "gson" "jcodec" "junit4" "mybatis-3" "opennlp" "spark" "spatial4j" )
for i in {0..9} 
do
    echo ${array[i]}
    cd ${array[i]}
        java -cp ../gin/build/gin.jar gin.util.PatchSampler -p ${array[i]} -d . -m ${array[i]}/${array[i]}.Profiler_output.csv -si -et LINE >> ../lineData
        java -cp ../gin/build/gin.jar gin.util.PatchSampler -p ${array[i]} -d . -m ${array[i]}/${array[i]}.Profiler_output.csv -si -et STATEMENT >> ../statementData
    cd ../
done

grep 'LINE edits for project' lineData > outLine
grep 'LINE deletions for project' lineData > outDelLine
grep 'STATEMENT edits for project' statementData > outStats
grep 'STATEMENT deletions for project' statementData > outDelStats

for i in {0..9} 
do
    awk '((NR-1) == "'"$i"'") {print "'"${array[i]}"'" ",allEdits," "LINE," $12;}' outLine >> out
    awk '((NR-1) == "'"$i"'") {print "'"${array[i]}"'" ",deleteEdits," "LINE," $12;}' outDelLine >> out
    awk '((NR-1) == "'"$i"'") {print "'"${array[i]}"'" ",allEdits," "STATEMENT," $12;}' outStats >> out
    awk '((NR-1) == "'"$i"'") {print "'"${array[i]}"'" ",deleteEdits," "STATEMENT," $12;}' outDelStats >> out
done

awk 'NR%2{printf "%s,",$0;next;}1' out >> out1
awk -F "\"*,\"*" '{print $1","$3","$4","$8;}' out1 > out2

echo 'Project,EditType,AllSingleEdits,SingleDeletes' > space.csv
cat out2 >> space.csv

rm out
rm out1
rm out2
rm outLine
rm outDelLine
rm outStats
rm outDelStats

mkdir ../data/
mv space.csv ../data/

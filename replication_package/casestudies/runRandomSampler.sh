#!/bin/bash
array=( "arthas" "disruptor" "druid" "gson" "jcodec" "junit4" "mybatis-3" "opennlp" "spark" "spatial4j" )
for i in {0..9} 
do
  cd ${array[i]}
  java -cp ../gin/build/gin.jar gin.RandomSampler -p ${array[i]} -d . -mavenHome $1 -o ${array[i]}.RandomSampler_j_STATEMENT_patchSize1_patchNumber10000_output.csv -j -m ${array[i]}.Profiler_output.csv -editType STATEMENT -patchNumber 10000 -patchSize 1
  java -cp ../gin/build/gin.jar gin.RandomSampler -p ${array[i]} -d . -mavenHome $1 -o ${array[i]}.RandomSampler_j_STATEMENT_patchSize2_patchNumber10000_output.csv -j -m ${array[i]}.Profiler_output.csv -editType STATEMENT -patchNumber 10000 -patchSize 2
  java -cp ../gin/build/gin.jar gin.RandomSampler -p ${array[i]} -d . -mavenHome $1 -o ${array[i]}.RandomSampler_j_STATEMENT_patchSize3_patchNumber10000_output.csv -j -m ${array[i]}.Profiler_output.csv -editType STATEMENT -patchNumber 10000 -patchSize 3
  java -cp ../gin/build/gin.jar gin.RandomSampler -p ${array[i]} -d . -mavenHome $1 -o ${array[i]}.RandomSampler_j_STATEMENT_patchSize4_patchNumber10000_output.csv -j -m ${array[i]}.Profiler_output.csv -editType STATEMENT -patchNumber 10000 -patchSize 4
  java -cp ../gin/build/gin.jar gin.RandomSampler -p ${array[i]} -d . -mavenHome $1 -o ${array[i]}.RandomSampler_j_STATEMENT_patchSize5_patchNumber10000_output.csv -j -m ${array[i]}.Profiler_output.csv -editType STATEMENT -patchNumber 10000 -patchSize 5
  java -cp ../gin/build/gin.jar gin.RandomSampler -p ${array[i]} -d . -mavenHome $1 -o ${array[i]}.RandomSampler_j_LINE_patchSize1_patchNumber10000_output.csv -j -m ${array[i]}.Profiler_output.csv -editType LINE -patchNumber 10000 -patchSize 1
  java -cp ../gin/build/gin.jar gin.RandomSampler -p ${array[i]} -d . -mavenHome $1 -o ${array[i]}.RandomSampler_j_LINE_patchSize2_patchNumber10000_output.csv -j -m ${array[i]}.Profiler_output.csv -editType LINE -patchNumber 10000 -patchSize 2
  java -cp ../gin/build/gin.jar gin.RandomSampler -p ${array[i]} -d . -mavenHome $1 -o ${array[i]}.RandomSampler_j_LINE_patchSize3_patchNumber10000_output.csv -j -m ${array[i]}.Profiler_output.csv -editType LINE -patchNumber 10000 -patchSize 3
  java -cp ../gin/build/gin.jar gin.RandomSampler -p ${array[i]} -d . -mavenHome $1 -o ${array[i]}.RandomSampler_j_LINE_patchSize4_patchNumber10000_output.csv -j -m ${array[i]}.Profiler_output.csv -editType LINE -patchNumber 10000 -patchSize 4
  java -cp ../gin/build/gin.jar gin.RandomSampler -p ${array[i]} -d . -mavenHome $1 -o ${array[i]}.RandomSampler_j_LINE_patchSize5_patchNumber10000_output.csv -j -m ${array[i]}.Profiler_output.csv -editType LINE -patchNumber 10000 -patchSize 5
  cd -
done

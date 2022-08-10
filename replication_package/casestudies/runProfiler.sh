#!/bin/bash
array=( "arthas" "disruptor" "druid" "gson" "jcodec" "junit4" "mybatis-3" "opennlp" "spark" "spatial4j" )
for i in {0..9} 
do
  cd ${array[i]}
  java -cp ../gin/build/gin.jar gin.Profiler -p ${array[i]} -d . -mavenHome $1 -o ${array[i]}.Profiler_output.csv
  cd -
done

array=( "arthas" "disruptor" "druid" "gson" "jcodec" "junit4" "mybatis-3" "opennlp" "spark" "spatial4j" )
for i in {0..9} 
do
  echo ${array[i]}
  cd ../casestudies/${array[i]}
  java -cp ../gin/build/gin.jar gin.util.PatchTester -patchFile ../data/edit_overlaps_all.csv -d . -m ${array[i]}.Profiler_output.csv -p ${array[i]} > ${array[i]}_self-repairs.csv
  cd -
done

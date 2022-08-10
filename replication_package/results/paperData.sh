sums () {
  awk -F ',' 'BEGIN{s=0}($2=="'$1'"){s=s+$'$2'}END{print s;}' $3 
}
sums_extra () {
  awk -F ',' 'BEGIN{s=0}($2=="'$1'" && $3=="'$3'"){s=s+$'$2'}END{print s;}' $4 
}

min_max () {
  awk -F ',' 'BEGIN{smin=100;smax=0;}($2=="'$1'" && $'$2'/$'$3'<smin){smin=$'$2'/$'$3';}($2=="'$1'" && $'$2'/$'$3'>smax){smax=$'$2'/$'$3';}END{print smin*100, smax*100;}' $4 
}
min_max_extra () {
  awk -F ',' 'BEGIN{smin=100;smax=0;}($3=="'$4'" && $2=="'$1'" && $'$2'/$'$3'<smin){smin=$'$2'/$'$3';}($3=="'$4'" && $2=="'$1'" && $'$2'/$'$3'>smax){smax=$'$2'/$'$3';}END{print smin*100, smax*100;}' $5
}

reasons () {
  awk -F ',' '($2=="'$1'"){a[$4] += $5}END{for (i in a) print i, a[i]}' $2 > out
  sort -n -k2 out > out2
  tail -6 out2
  rm out
  rm out2
}

for j in "STATEMENT" "LINE"
do 
  echo ""$j" pass rates for unique single edits"
  min_max_extra "$j" 6 7 1 "data/sample_data.csv"
  echo "number of test-suite adequate unique patches at "$j" level"
  sums "$j" 6 "data/sample_data.csv"
  echo "pass rates for "$j" edits per project and edit sequence length"
  min_max "$j" 6 7 "data/sample_data.csv"
  echo "netural variant rates for "$j" edits per project and edit sequence length"
  min_max "$j" 6 5 "data/sample_data.csv"
  echo "netural variant rates for single "$j" edits per project"
  min_max_extra "$j" 6 5 1 "data/sample_data.csv"
  # all: 218118 = 92244+25538+9539+41365+35379+14053
  # passing: (25538+35379)/218118. = 0.27928460741433536
  # compiling: (92244+41365)/218118.= 0.6125537553067606 
  echo "top 3 reasons for test failures for single "$j" deletes"
  reasons $j data/delete_test_data.csv
  echo "top 3 reasons for test failures for random "$j" edits"
  reasons $j data/sample_test_data.csv
  echo "netural variant rates for single "$j" deletes per project"
  min_max_extra "$j" 6 5 1 "data/delete_data.csv"
  echo "number of test-suite adequate unique single deletes at "$j" level"
  sums "$j" 7 "data/delete_data.csv"
  echo "compilation rates for single "$j" deletes per project"
  min_max_extra "$j" 5 7 1 "data/delete_data.csv"
  echo "pass rates for single "$j" deletes per project"
  min_max_extra "$j" 6 7 1 "data/delete_data.csv"
  echo "number of unique patches at "$j" level"
  for i in {1..5}
  do
    echo "edits:" $i
    sums_extra "$j" 7 $i "data/sample_data.csv"
  done
  echo "number of all single deletes at "$j" level"
  sums "$j" 11 "data/delete_data.csv"
  echo "number of unique patches at "$j" level"
  sums "$j" 7 "data/sample_data.csv"
  echo ""$j" compilation rates for unique single edits"
  min_max_extra "$j" 5 7 1 "data/sample_data.csv"
  echo "for section 6.1, compiled, all"
  echo $j
  awk -F ',' 'BEGIN{a=0;b=0;}($3==1 && $2=="'$j'"){a=a+$5;b=b+$7;}END{print a" "b;}' data/sample_data.csv
  echo $j "single-edit compilable test failures"
  awk -F ',' 'BEGIN{a=0;}($2=="'$j'" && $3==1 && $4!="TestPassed" && $4!="TestFailed" && $4!="PatchCompileError"){a=a+1;}END{print a;}' data/sample_test_data.csv 
  echo $j "java.lang.Assertion.Error"
  awk -F ',' 'BEGIN{a=0;}($2=="'$j'" && $3==1 && $4=="java.lang.AssertionError"){a=a+1;}END{print a;}' data/sample_test_data.csv 
  echo $j "java.lang.NullPointerException"
  awk -F ',' 'BEGIN{a=0;}($2=="'$j'" && $3==1 && $4=="java.lang.NullPointerException"){a=a+1;}END{print a;}' data/sample_test_data.csv 
  echo $j "TestPassed"
  awk -F ',' 'BEGIN{a=0;}($2=="'$j'" && $3==1 && $4=="TestPassed"){a=a+$5;}END{print a;}' data/sample_test_data.csv 
  echo $j "TestFailed"
  awk -F ',' 'BEGIN{a=0;}($2=="'$j'" && $3==1 && $4=="TestFailed"){a=a+$5;}END{print a;}' data/sample_test_data.csv 
  echo $j "PatchCompileError"
  awk -F ',' 'BEGIN{a=0;}($2=="'$j'" && $3==1 && $4=="PatchCompileError"){a=a+$5;}END{print a;}' data/sample_test_data.csv 
  ## outputs all test failure types into a file
  # awk -F ',' '($2=="'$j'" && $3==1 && $4!="TestPassed" && $4!="TestFailed" && $4!="PatchCompileError"){print $4;}' data/sample_test_data.csv > out$j
done

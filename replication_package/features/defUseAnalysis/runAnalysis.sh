#!/bin/bash

# runs the def-use analysis on all the case studies

# prerequisites:
# Assumes that you have run ../../casestudies/runProfiler.sh
# and assumes that you have run ../../casestudies/cloneRepos.sh
# will output def-use chains for each of the packages to stdout

./runTests.sh profiler/arthas.Profiler_output.csv  ../../casestudies/arthas/core/target/classes/  ../../casestudies/arthas/core/target/classes/:../../casestudies/arthas/core/target/arthas-core-jar-with-dependencies.jar

./runTests.sh profiler/disruptor.Profiler_output.csv ../../casestudies/disruptor/build_tmp/main/classes ../../casestudies/disruptor/build_tmp/main/classes

./runTests.sh profiler/gson.Profiler_output.csv  ../../casestudies/gson/gson/target/classes/  ../../casestudies/gson/gson/target/classes/ 

./runTests.sh profiler/disruptor.Profiler_output.csv ../../casestudies/disruptor/build/classes/java/main/ ../../casestudies/disruptor/build/classes/java/main/

./runTests.sh profiler/spark.Profiler_output.csv ../../casestudies/spark/target/classes/  ../../casestudies/spark/target/classes/:../../casestudies/spark/target/spark-core-2.9.2.jar:../../casestudies/spark/target/jetty-all-9.4.30.v20200611-uber.jar:../../casestudies/spark/target/slf4j-api-1.7.9.jar

./runTests.sh profiler/opennlp.Profiler_output.csv ../../casestudies/opennlp/opennlp-tools/target/classes/   ../../casestudies/opennlp/opennlp-tools/target/classes/

./runTests.sh profiler/druid.Profiler_output.csv  ../../druid/target/classes/  ../../casestudies/druid/target/classes/

./runTests.sh profiler/junit4.Profiler_output.csv  ../../casestudies/junit4/target/classes/  ../../casestudies/junit4/target/classes/:../../casestudies/junit4/lib/hamcrest-core-1.3.jar

./runTests.sh profiler/mybatis-3.Profiler_output.csv  ../../casestudies/mybatis-3/target/classes/  ../../casestudies/mybatis-3/target/classes/:../../casestudies/mybatis-3/target/javassist.jar

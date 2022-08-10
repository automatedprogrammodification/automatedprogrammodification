#!/bin/bash
git clone https://github.com/alibaba/arthas.git arthas
cd arthas
git checkout tags/arthas-all-3.0.5
mvn clean compile
mvn test
cd -
git clone https://github.com/LMAX-Exchange/disruptor.git disruptor
cd disruptor
git checkout tags/3.4.2
./gradlew build
./gradlew clean test
cd -
git clone https://github.com/alibaba/druid.git druid
cd druid
git checkout tags/1.1.11
mvn compile
mvn clean test
cd -
git clone https://github.com/google/gson.git gson
cd gson
git checkout tags/gson-parent-2.8.5
mvn compile
mvn clean test
cd -
git clone https://github.com/jcodec/jcodec.git
cd jcodec
git checkout tags/v0.2.3
mvn compile
mvn test
cd -
git clone https://github.com/junit-team/junit4.git junit4
cd junit4
git checkout tags/r4.13-beta-2
mvn compile
mvn test
cd -
git clone https://github.com/mybatis/mybatis-3.git mybatis-3
cd mybatis-3
git checkout tags/mybatis-3.4.6
./mvnw compile
./mvnw test
cd -
git clone https://github.com/apache/opennlp.git opennlp
cd opennlp
git checkout tags/opennlp-1.7.0
mvn install
mvn test
cd -
git clone https://github.com/perwendel/spark.git spark
cd spark
git checkout tags/2.7.2
./mvnw compile
./mvnw test
cd -
git clone https://github.com/locationtech/spatial4j.git spatial4j
cd spatial4j
git checkout tags/spatial4j-0.7
mvn compile
mvn test
cd -

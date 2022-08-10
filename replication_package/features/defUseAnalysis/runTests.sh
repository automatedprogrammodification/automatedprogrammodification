#!/bin/bash

#echo $1
#echo $2
classPath=$3
echo $classPath
cat $1 | tail -n +2 |(
    while read a; do
	ind=`echo $a | cut -d',' -f2 | cut -d'"' -f2`
	echo $ind
	ln=`echo $a | cut -d',' -f3 | cut -c 2- | cut -d'(' -f1`;
	ln1=`echo $a | cut -d',' -f3- | cut -d'"' -f2- | rev | cut -d')' -f2- | rev`;
	
	ln1=`echo $ln1")"`  # add bracket back in for signature
	fullMethodName=`echo $ln1 | rev | cut -d'.' -f1 | rev`
	# echo full method name $fullMethodName
	methodName=`echo $ln | rev | cut -d'.' -f1 | rev`
	fileName=`echo $ln | rev | cut -d'.' -f2- | tr . / | rev`
	fullClassName=`echo $ln | rev | cut -d'.' -f2- | rev`
	className=`echo $ln | rev | cut -d'.' -f2 | tr . / | rev`
	echo $ln
	echo $className
        echo $methodName
	#echo $fileName
	fileArg=`echo $2$fileName.class`
	#echo `ls -l $fileArg`
	#java -cp ../sootclasses-trunk-jar-with-dependencies.jar:. DefUse $className  $methodName
        # uncomment below
	echo "java -cp ../sootclasses-trunk-jar-with-dependencies.jar:.: DefUse $fullClassName  $methodName $classPath $ind $fullMethodName "
	java -cp ../sootclasses-trunk-jar-with-dependencies.jar:. DefUse $fullClassName  $methodName $classPath $ind $fullMethodName
	
    done)
    

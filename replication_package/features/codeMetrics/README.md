


CodeMetrics Analysis Code
====================
This directory contains the tools and instructions to run the code metrics analysis described in the related paper. This analysis uses the CheckStyle program to record the Cyclomatic Complexity, NCSS and NPATH measures for the target methods used in the paper's gin experiment.

Contents
--------

- **AddCyclomaticComplexity.java**:  a Java program for running the analysis the hot methods in each on each of the packages in the case-studies directory
- **checkstyle-8.36.2-all.jar**: the checkstyle program used to compute the metrics, released under the [LGPL](https://checkstyle.org/licenses.html#LGPL-2.1.2B)
- **checks.xml** config for checkstyle
- **AllMethods2.txt** a file containing the method names for all the hot methods for convenience

Running the Analysis
------------

The shell commands in the ../../casestudies directory should be run first.

The specific Checkstyle library release we used can be [found here](https://github.com/checkstyle/checkstyle/releases/tag/checkstyle-8.36.2) and is documented [here](https://checkstyle.sourceforge.io)

Compile the Java code: javac -cp checkstyle-8.36.2-all.jar:./pathToGin/build/gin.jar AddCyclomaticComplexity.java
Run the Java code: java -cp checkstyle-8.36.2-all.jar:./pathToGin/build/gin.jar:. AddCyclomaticComplexity

You will get a CSV file StatsFromCheckstyle2.csv listing the methods and the three metrics for each.

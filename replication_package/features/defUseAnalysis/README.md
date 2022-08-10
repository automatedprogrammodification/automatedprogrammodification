


DefUse Analysis Code
====================
This directory contains the tools and instructions to run the defUse analysis described in the related paper. The DefUse analysis uses the Soot program analysis library to record each intra and interline dependency in the target methods used in the paper's gin experiment.

Contents
--------

- **runTest.sh**:  a script for running defUse analysis the hot methods in each on each of the packages in the case-studies directory
- [sootclasses-trunk-jar-with-dependencies.jar](https://github.com/soot-oss/soot)  : the Soot libraries used in the defUse analyis
-**DefUse.java** the source file for the def-use analysis - outputs a sequence of line numbers for def-use pairs
- **runAnalysis.sh** a file containing the commands to run the analysis for each package. Each of these will send a set of def-use pairs to standard output. Note that the 

Running the Analysis
------------

The shell commands in the ../../casestudies directory should be run first.
Check that directory for instructions on additional jar files required to run the analysis on the methods labelled by the profiler.
The Soot library can be [found here](https://github.com/soot-oss/soot)

The jar file used for the libraries used in this experiment can be found in the directory above.

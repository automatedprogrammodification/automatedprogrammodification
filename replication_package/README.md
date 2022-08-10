# Program Transformation Landscapes for Automated Program Modification Using Gin

This is an artefact to accompany the "Program Transformation Landscapes for Automated Program Modification Using Gin" paper, submitted to the Empirical Software Engineering Journal.

## Repository Contents

All the data and graphs used in the paper are in the [results](results/) folder. 
Data in our paper is based on the experimental outputs contained in the [results/casestudies](results/casestudies) folder.

Scripts used to process our data are in the [scripts](scripts/) directory. It also contains the [PatchSampler.java](scripts/src/main/java/gin/util/PatchSampler.java) class that has been used to calculate the single-edit search space for our 10 subject programs, and the [PatchTester.java](scripts/src/main/java/gin/util/PatchTester.java) class that has been used to calculate self-repairs via recoveries to previous software version.

We have separated the final analysis connecting code plasticity to code complexity features into a separate [features](features/) folder. The metrics we computed for each of the hot methods in the study, and a Python script to categorise these methods as predictably/unpredictably amenable to APM (i.e., plastic), can be found in the [features](features/) folder. More detailed instructions are contained in a separate README in that folder.

## Replication Instructions

In order to replicate the work in the submission, please follow the steps outlined below. The steps should work on any Unix-based system. Same pre-requisites as those for [Gin](https://github.com/gintool/gin) are required, including JDK 1.8.x, Gradle 4.6 or above and Maven. All scripts aimed at automating this process were written in bash.

Please note that due to the undeterministic nature of our experiments you might get different results. 

### Clone the Repository

```
git clone https://github.com/automatedprogrammodification/automatedprogrammodification ginSearchSpace
cd ginSearchSpace
```

### Gin

Please download and build Gin (note the dependencies on [Gin's website](https://github.com/gintool/gin).

```
git clone https://github.com/gintool/gin.git 
cd gin
git checkout e897ad3487eaf21511e740a6828c6c20b168a278
./gradlew build 
cd -
```

### Subject Programs

We used 10 large real-world Java programs. Please run the [cloneRepos.sh](casestudies/cloneRepos.sh) script within that directory to download, compile the projects, and run their test suites. Please note that arthas has one test case that is time-zone dependent. In case mvn test fails, please amend it. A diff example is shown below:

```
--- a/core/src/test/java/com/taobao/arthas/core/view/ObjectViewTest.java
+++ b/core/src/test/java/com/taobao/arthas/core/view/ObjectViewTest.java
@@ -191,7 +191,7 @@ public class ObjectViewTest {
 
     @Test
     public void testDate() {
-        Date d = new Date(1531204354961L - TimeZone.getDefault().getRawOffset()
+        Date d = new Date(1531204354961L - TimeZone.getTimeZone("GMT+1").getRawOffset()
```

Assuming all tests passed, you can move to the next step.

### Run Profiler

For each project run Gin's Profiler within each repository. This is also automated in the [runProfiler.sh](casestudies/runProfiler.sh) script. Note that the script requires a path to your maven home repository (it's usually "/usr/local/", but could vary). Please note this step took us 2 days to complete.

### Run DeleteEnumerator

For each project run Gin's DeleteEnumerator within each repository. This is also automated in the [runDeleteEnumerator.sh](casestudies/runDeleteEnumerator.sh) script. Note that the script requires a path to your maven home repository (it's usually "/usr/local/", but could vary). Please note this step took us 2 days to complete.

### Run RandomSampler

For each project run Gin's RandomSampler within each repository. This is also automated in the [runRandomSampler.sh](casestudies/runRandomSampler.sh) script. Note that the script requires a path to your maven home repository (it's usually "/usr/local/", but could vary). Please note this step took us 8 days to complete.

### Run PatchSampler

Run Gin's PatchSampler within the [casestudies](casestudies) repository. This is also automated in the [runPatchSampler.sh](casestudies/runPatchSampler.sh) script. Note that the output is saved  to the (newly created) "data" folder.

### Data Analysis and Graph Generation

Make sure you have the following installed: Python3, and the following modules: matplotlib, numpy, pandas, treelib.

Assuming the following directory structure for each project (example of arthas below):

```
casestudies/arthas/arthas.Profiler_output.csv
casestudies/arthas/arthas.DeleteEnumerator_output.csv
casestudies/arthas/arthas.RandomSampler_j_STATEMENT_patchSize1_patchNumber10000_output.csv
casestudies/arthas/arthas.RandomSampler_j_STATEMENT_patchSize2_patchNumber10000_output.csv
casestudies/arthas/arthas.RandomSampler_j_STATEMENT_patchSize3_patchNumber10000_output.csv
casestudies/arthas/arthas.RandomSampler_j_STATEMENT_patchSize4_patchNumber10000_output.csv
casestudies/arthas/arthas.RandomSampler_j_STATEMENT_patchSize5_patchNumber10000_output.csv
```

and [space.csv](data/space.csv) file in the "data" folder, you can run the [runScripts.sh](scripts/runScripts.sh) script from within the 'scripts' folder to analyse all the data and generate graphs. By the end of the run graphs will be saved in the '../graphs' folder. A Markdown file will also be created with descriptions of the graphs in the 'scripts' folder, similar to the one in the top level directory [../graphs.md](../graphs.md).
This step took about 20min to complete.

## Help

If you have any problems replicating the results, please feel free to get in touch with [Justyna Petke](mailto:j.petke@ucl.ac.uk).

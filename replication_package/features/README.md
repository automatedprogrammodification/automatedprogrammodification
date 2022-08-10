Feature Analysis
==========

This directory contains the resources for feature analysis including scripts for the collation of summary statistics and code for performing def-use analysis on hot procedures. The code in this directory assumes that the packages have been downloaded and the package download and profiler scripts in the `../casestudies` directory  have been run.

Manifest
-------

- **defUseAnalysis**: directory containing the resources to find def-use chains on the target methods identified by the profiler
- **codeMetrics**: directory containing the resources to calculate cyclomatic complexity, NCSS and NPATH metrics on the target methods identified by the profiler
- **merged_stats_features.csv** data file collated from running the def-use and other features identified by the target methods run by the profiler
- **DisplayUseDefCorrels.ipynb** interactive python notebook for collating the methods identified as predictably/unpredictably plastic (or otherwise)
- **predictably_bad.csv** the non-plastic *upstanding citizen* methods listed in the paper
- **predictably_good.csv** the plastic *upstanding citizen* methods listed in the paper
- **unpredictably_bad.csv** the non-plastic *rogues' gallery* methods listed in the paper
- **unpredictably_good.csv** the plastic *rogues' gallery* methods listed in the paper
- **upstanding_citizens_and_rogues_links** direct links to the plastic *upstanding citizen* and *rogues' gallery* methods at their relevant projects' repositories

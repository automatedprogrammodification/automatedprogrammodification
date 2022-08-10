## Program Transformation Landscapes for Automated Program Modification Using Gin
These graphs visualise various information about the program variants obtained by applying patches generated in our experiments. This is additional material, presenting more detailed information than what is found in the paper.

###Search Space

These graphs show the numbers of syntactically valid edits for the identified hot methods. Data is aggregated per project. AllEdits include single DELETE, COPY, REPLACE, and SWAP operations. We also compare with the numbers of single DELETE operations only to emphasize their contribution to the search space of edits.

<table>
<tr>
<td>
<img src="replication_package/results/graphs/space/space_AllSingleEdits.png" alt="space_AllSingleEdits.png" width=450>
</td>
<td>
<img src="replication_package/results/graphs/space/space_LINE.png" alt="space_LINE.png" width=450>
</td>
</tr>
<tr>
<td>
<img src="replication_package/results/graphs/space/space_STATEMENT.png" alt="space_STATEMENT.png" width=450>
</td>
<td>
<img src="replication_package/results/graphs/space/space_SingleDeletes.png" alt="space_SingleDeletes.png" width=450>
</td>
</tr>
<tr>
<td>
<img src="replication_package/results/graphs/space/space_deletes.png" alt="space_deletes.png" width=450>
</td>
<td></td></tr>
</table>

###RandomSampler

These graphs visualise the results of the Random Sampling experiment per project. We show the compilation, test pass, and neutral variant rates for edit sequences of varying sizes, from 1 to 5. We also show the most commonly occuring types of failures. Additionally, we show the number of syntactically valid COPY, DELETE, REPLACE, and SWAP edit operations generated, and effective single edit operations, that is, those that pass the given test suite. Edits were restricted to hot methods. Data is aggregated per project.

<table>
<tr>
<td>
<img src="replication_package/results/graphs/sample/Compiled_LINE.png" alt="Compiled_LINE.png" width=450>
</td>
<td>
<img src="replication_package/results/graphs/sample/Compiled_STATEMENT.png" alt="Compiled_STATEMENT.png" width=450>
</td>
</tr>
<tr>
<td>
<img src="replication_package/results/graphs/sample/Neutral_Variant_Rate_LINE.png" alt="Neutral_Variant_Rate_LINE.png" width=450>
</td>
<td>
<img src="replication_package/results/graphs/sample/Neutral_Variant_Rate_STATEMENT.png" alt="Neutral_Variant_Rate_STATEMENT.png" width=450>
</td>
</tr>
<tr>
<td>
<img src="replication_package/results/graphs/sample/Passed_LINE.png" alt="Passed_LINE.png" width=450>
</td>
<td>
<img src="replication_package/results/graphs/sample/Passed_STATEMENT.png" alt="Passed_STATEMENT.png" width=450>
</td>
</tr>
<tr>
<td>
<img src="replication_package/results/graphs/sample/TestEdits_All_LINE.png" alt="TestEdits_All_LINE.png" width=450>
</td>
<td>
<img src="replication_package/results/graphs/sample/TestEdits_All_STATEMENT.png" alt="TestEdits_All_STATEMENT.png" width=450>
</td>
</tr>
<tr>
<td>
<img src="replication_package/results/graphs/sample/TestEdits_LINE.png" alt="TestEdits_LINE.png" width=450>
</td>
<td>
<img src="replication_package/results/graphs/sample/TestEdits_STATEMENT.png" alt="TestEdits_STATEMENT.png" width=450>
</td>
</tr>
<tr>
<td>
<img src="replication_package/results/graphs/sample/TypeSingleEdits_LINE.png" alt="TypeSingleEdits_LINE.png" width=450>
</td>
<td>
<img src="replication_package/results/graphs/sample/TypeSingleEdits_STATEMENT.png" alt="TypeSingleEdits_STATEMENT.png" width=450>
</td>
</tr>
<tr>
<td>
<img src="replication_package/results/graphs/sample/TypeSingleEffectiveEdits_LINE.png" alt="TypeSingleEffectiveEdits_LINE.png" width=450>
</td>
<td>
<img src="replication_package/results/graphs/sample/TypeSingleEffectiveEdits_STATEMENT.png" alt="TypeSingleEffectiveEdits_STATEMENT.png" width=450>
</td>
</tr>
</table>

###RandomSampler (aggregated)

These graphs visualise the results of the Random Sampling experiment. We show the compilation, test pass, and neutral variant rates for edit sequences of varying sizes, from 1 to 5.

<table>
<tr>
<td>
<img src="replication_package/results/graphs/sample_total/Compiled.png" alt="Compiled.png" width=450>
</td>
<td>
<img src="replication_package/results/graphs/sample_total/Neutral_Variant_Rate.png" alt="Neutral_Variant_Rate.png" width=450>
</td>
</tr>
<tr>
<td>
<img src="replication_package/results/graphs/sample_total/Passed.png" alt="Passed.png" width=450>
</td>
<td></td></tr>
</table>

###Overlapping edits from RandomSampler

These graphs visualise the results of the Random Sampling experiment. We analysed those edit sequences of size 2 and above for which we had data for each subset of the edit sequence. C represents successful compilation, P represents successful test pass, while F represents compilation failure. For instance, FCP means that in the edit sequence of 3 edits after application of the first edit the program variant did not compile, after application of the second edit, the program variant compiled, while application of all three edits in this edit sequence led to a program variant that compiled and passed all the associated tests.

<table>
<tr>
<td>
<img src="replication_package/results/graphs/edits/Overlaps_of_size_2.png" alt="Overlaps_of_size_2.png" width=450>
</td>
<td>
<img src="replication_package/results/graphs/edits/Overlaps_of_size_3.png" alt="Overlaps_of_size_3.png" width=450>
</td>
</tr>
<tr>
<td>
<img src="replication_package/results/graphs/edits/Overlaps_of_size_4.png" alt="Overlaps_of_size_4.png" width=450>
</td>
<td>
<img src="replication_package/results/graphs/edits/Overlaps_of_size_5.png" alt="Overlaps_of_size_5.png" width=450>
</td>
</tr>
<tr>
<td>
<img src="replication_package/results/graphs/edits/Overlaps_without_all_passing_of_size_2.png" alt="Overlaps_without_all_passing_of_size_2.png" width=450>
</td>
<td>
<img src="replication_package/results/graphs/edits/Overlaps_without_all_passing_of_size_3.png" alt="Overlaps_without_all_passing_of_size_3.png" width=450>
</td>
</tr>
<tr>
<td>
<img src="replication_package/results/graphs/edits/Overlaps_without_all_passing_of_size_4.png" alt="Overlaps_without_all_passing_of_size_4.png" width=450>
</td>
<td>
<img src="replication_package/results/graphs/edits/Overlaps_without_all_passing_of_size_5.png" alt="Overlaps_without_all_passing_of_size_5.png" width=450>
</td>
</tr>
</table>

###DeleteEnumerator

These graphs visualise the results of the Delete Enumeration experiment per project. We show the compilation, test pass, and neutral variant rates for single deletes. We also show the most commonly occuring types of failures.

<table>
<tr>
<td>
<img src="replication_package/results/graphs/delete/SingleDeleteEdits_Compiled.png" alt="SingleDeleteEdits_Compiled.png" width=450>
</td>
<td>
<img src="replication_package/results/graphs/delete/SingleDeleteEdits_Neutral_Variant_Rate.png" alt="SingleDeleteEdits_Neutral_Variant_Rate.png" width=450>
</td>
</tr>
<tr>
<td>
<img src="replication_package/results/graphs/delete/SingleDeleteEdits_Passed.png" alt="SingleDeleteEdits_Passed.png" width=450>
</td>
<td>
<img src="replication_package/results/graphs/delete/TestSingledeletes_All_LINE.png" alt="TestSingledeletes_All_LINE.png" width=450>
</td>
</tr>
<tr>
<td>
<img src="replication_package/results/graphs/delete/TestSingledeletes_All_STATEMENT.png" alt="TestSingledeletes_All_STATEMENT.png" width=450>
</td>
<td>
<img src="replication_package/results/graphs/delete/TestSingledeletes_LINE.png" alt="TestSingledeletes_LINE.png" width=450>
</td>
</tr>
<tr>
<td>
<img src="replication_package/results/graphs/delete/TestSingledeletes_STATEMENT.png" alt="TestSingledeletes_STATEMENT.png" width=450>
</td>
<td></td></tr>
</table>

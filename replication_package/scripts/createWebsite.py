import os
from globalVars import graphsDir

title = 'Program Transformation Landscapes for Automated Program Modification Using Gin'
intro = 'These graphs visualise various information about the program variants obtained by applying patches generated in our experiments. This is additional material, presenting more detailed information than what is found in the paper.'
header = '## ' + title + '\n' + intro

def section(x):
    print('\n###' + x + '\n')

def image(imgDir, title, s):
    print('<img src="' + os.path.join(imgDir, title) + '" alt="' + title + '" width=450>')

print(header)

headers = {'delete':'DeleteEnumerator', 'sample': 'RandomSampler', 'space': 'Search Space', 'sample_total': 'RandomSampler (aggregated)', 'edits': 'Overlapping edits from RandomSampler'}

descriptions = {
'space' : 'These graphs show the numbers of syntactically valid edits for the identified hot methods. Data is aggregated per project. AllEdits include single DELETE, COPY, REPLACE, and SWAP operations. We also compare with the numbers of single DELETE operations only to emphasize their contribution to the search space of edits.',
'sample' : 'These graphs visualise the results of the Random Sampling experiment per project. We show the compilation, test pass, and neutral variant rates for edit sequences of varying sizes, from 1 to 5. We also show the most commonly occuring types of failures. Additionally, we show the number of syntactically valid COPY, DELETE, REPLACE, and SWAP edit operations generated, and effective single edit operations, that is, those that pass the given test suite. Edits were restricted to hot methods. Data is aggregated per project.',
'sample_total' : 'These graphs visualise the results of the Random Sampling experiment. We show the compilation, test pass, and neutral variant rates for edit sequences of varying sizes, from 1 to 5.', 
'edits' : 'These graphs visualise the results of the Random Sampling experiment. We analysed those edit sequences of size 2 and above for which we had data for each subset of the edit sequence. C represents successful compilation, P represents successful test pass, while F represents compilation failure. For instance, FCP means that in the edit sequence of 3 edits after application of the first edit the program variant did not compile, after application of the second edit, the program variant compiled, while application of all three edits in this edit sequence led to a program variant that compiled and passed all the associated tests.',
'delete' : 'These graphs visualise the results of the Delete Enumeration experiment per project. We show the compilation, test pass, and neutral variant rates for single deletes. We also show the most commonly occuring types of failures.'
}

for s in ['space', 'sample', 'sample_total', 'edits', 'delete']:
    imgDir = os.path.join(graphsDir, s)
    section(headers.get(s))
    print(descriptions.get(s)+'\n')
    filenames = os.listdir(imgDir)
    filenames.sort()
    print('<table>')
    for f in range(len(filenames)):
        if not f % 2:  print('<tr>')
        print('<td>')
        image(imgDir, filenames[f], s)
        print('</td>')
        if f % 2:  print('</tr>')
    if not f % 2:  print('<td></td></tr>')
    print('</table>')

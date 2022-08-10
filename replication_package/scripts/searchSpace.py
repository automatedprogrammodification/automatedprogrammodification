import os, numpy, matplotlib
import pandas as pd
from globalVars import graphsDir, editTypes, calculate_perc, searchSpaceData

data = pd.read_csv(searchSpaceData)
data.drop(data.index[data['EditType'] == 'MATCHED_STATEMENT'], inplace = True)

def drawBarplot(barplot, ylabel, graphname, title, ymin, ymax):
    barplot.set_ylabel(ylabel)
    barplot.set_xlabel('')
    barplot.set_title(title)
    barplot.set_ylim(ymin, ymax)
    barplot.get_figure().tight_layout()
    barplot.get_figure().savefig(os.path.join(graphsDir, 'space', graphname))

for i in editTypes:
    df = data[data.EditType==i]
    df.set_index('Project')
    barplot = df.plot.bar(rot=45, x='Project')
    barplot.set_yscale('log')
    drawBarplot(barplot,'Number of Possible Edits','space_' + i +'.png', 'Search space size for single ' + i + ' edits', 1, max(data['AllSingleEdits'])*2)

df = data.pivot(index='Project',columns='EditType',values='AllSingleEdits')
barplot = df.plot.bar(rot=45)
barplot.set_yscale('log')
drawBarplot(barplot,'Number of Possible Edits','space_' + 'AllSingleEdits' +'.png', 'Search space size for ' + 'AllSingleEdits', 1, max(data['AllSingleEdits'])*100)

df = data.pivot(index='Project',columns='EditType',values='SingleDeletes')
barplot = df.plot.bar(rot=45)
drawBarplot(barplot,'Number of Possible Edits','space_' + 'SingleDeletes' +'.png', 'Search space size for ' + 'SingleDeletes', 0, max(data['SingleDeletes'])*1.1)

data['Delete Edits %'] = data.apply(calculate_perc, axis=1, args=['SingleDeletes', 'AllSingleEdits'])
df = data.pivot(index='Project',columns='EditType',values='Delete Edits %')
barplot = df.plot.bar(rot=45)
barplot.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter())
drawBarplot(barplot, '', 'space_deletes.png', '% of single deletes among all possible edits of given type', 0, max(data['Delete Edits %'])*1.2)

import os, sys, numpy, matplotlib
import pandas as pd
from globalVars import editTypes, dataDir, graphsDir, results, calculate_perc, checkValidInput

exp = checkValidInput()
df = pd.read_csv(os.path.join(dataDir, exp + '_data.csv'))
df.drop(df.index[df['EditType'] == 'MATCHED_STATEMENT'], inplace = True)

###### Calculate required percentages ######

df2 = df.copy()

if len(sys.argv)>2 and sys.argv[2]=='total':
    df2.set_index(['EditType','PatchSize'],inplace=True)
    df2 = df2.groupby(level=['EditType','PatchSize']).sum()

for i in ['Compiled', 'Passed']:
    df2[i] = df2.apply(calculate_perc, axis=1, args=['Unique'+i, 'UniquePatches'])
df2['Neutral_Variant_Rate'] = df2.apply(calculate_perc, axis=1, args=['UniquePassed', 'UniqueCompiled'])
df2 = df2.filter(results, axis=1)

###### Draw required graphs ######

def drawBarplot(barplot, title, graphname, cp, rename):
    barplot.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter())
    barplot.set_title(title)
    barplot.set_ylabel(cp)
    barplot.set_xlabel('')
    barplot.set_ylim(0,100)
    if rename: barplot.legend(title='EditCount')
    fig = barplot.get_figure()
    fig.tight_layout()
    fig.savefig(os.path.join(graphsDir, exp, graphname + '.png'))

if exp=='delete':

     for cp in results[3:]:
          barplot = df2.pivot(index='Project',columns='EditType',values=cp).plot.bar(rot=45)
          drawBarplot(barplot, 'Single Delete Edits per Project ', 'SingleDeleteEdits_' + cp, cp, False)

elif exp=='sample' and sys.argv[2]=='project':

    for cp in results[3:]:
            for et in editTypes:
                barplot = df2[df2.EditType==et].pivot(index='Project',columns='PatchSize',values=cp).plot.bar(rot=45)
                drawBarplot(barplot, et + '-level Patches', cp + '_' + et, cp, True)
    
elif exp=='sample' and sys.argv[2]=='total':

    df2.reset_index(inplace=True)
    exp = 'sample_total'

    for cp in results[3:]:
        barplot = df2.pivot(index='EditType',columns='PatchSize',values=cp).plot.bar(rot=0)
        barplot.set_xlabel('')
        drawBarplot(barplot, 'Patches For All Projects', cp, cp, True)

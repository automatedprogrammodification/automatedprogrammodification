import os, sys, numpy, matplotlib
import pandas as pd
from globalVars import editTypes, dataDir, graphsDir, calculate_perc, mutations, checkValidInput

exp = checkValidInput()
df = pd.read_csv(os.path.join(dataDir, exp + '_type_data.csv'))
df.drop(df.index[df['EditType'] == 'MATCHED_STATEMENT'], inplace = True)

if exp=='delete':
        print('Information not interesting. No graph produced.')

elif exp=='sample':

        df.drop('PatchSize',axis=1, inplace=True)
        muts = [x.capitalize() for x in mutations.keys()]
        for i in muts:
            df['Test-passing ' + i] = df.apply(calculate_perc, axis=1, args=[i, i + 'All'])
        for et in editTypes:
            df2 = df.loc[df.EditType==et].copy()
            df2.drop('EditType',axis=1, inplace=True)
            for i in muts:
                df2.drop(i,axis=1, inplace=True)
                df2.drop(i+'All',axis=1, inplace=True)
                df2.drop(i+'Compiled',axis=1, inplace=True)
            barplot = df2.plot.bar(x='Project', rot=45)
            barplot.set_title('Single test-passing edit type distribution for operators: '+ et)
            barplot.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter())
            barplot.set_ylim(0,100)
            barplot.set_xlabel('')
            barplot.get_figure().tight_layout()
            barplot.get_figure().savefig(os.path.join(graphsDir, exp, 'TypeSingleEffectiveEdits_' + et + '.png'))

            df2 = df.loc[df.EditType==et].copy()
            df2.drop('EditType',axis=1, inplace=True)
            for i in muts:
                df2.drop(i, axis=1, inplace=True)
                df2.drop('Test-passing '+i,axis=1, inplace=True)
            barplot = df2.plot.bar(x='Project', rot=45)
            barplot.set_title('Single edit type distribution for operators: '+ et)
            barplot.set_ylim(0,3500)
            barplot.get_figure().tight_layout()
            barplot.get_figure().savefig(os.path.join(graphsDir, exp, 'TypeSingleEdits_' + et + '.png'))

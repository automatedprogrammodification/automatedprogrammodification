import os, sys, numpy, matplotlib
import pandas as pd
from globalVars import editTypes, dataDir, graphsDir, checkValidInput, outTestColumns, projects

exp = checkValidInput()
df = pd.read_csv(os.path.join(dataDir, exp + '_test_data.csv'))
df.drop(df.index[df['EditType'] == 'MATCHED_STATEMENT'], inplace = True)
failureOccurrence = 1000

def drawBarplot(df, et, title, graphname, yscale, ymin, ymax, moveLegend):
    df.drop('PatchSize', axis=1)
    barplot = df.loc[df.EditType==et].pivot(index='Project',columns='TestExceptionType',values='TestsFailed').plot.bar(rot=45)
    barplot.set_title(title +' : '+ et)
    barplot.set_yscale(yscale)
    barplot.set_xlabel('')
    barplot.set_ylim(ymin, ymax)
    if moveLegend:
        barplot.legend(loc="upper left", bbox_to_anchor=[1, 1], ncol=1, fancybox=True, title='TestExceptionType')
    fig = barplot.get_figure()
    if moveLegend:
        fig.set_size_inches(9.6,4.8)
    fig.tight_layout()
    fig.savefig(os.path.join(graphsDir, exp, graphname))

def drawPlots(df, etNo, title, ymax1, ymax2, moveLegend):

    name = title.capitalize().replace(' ','')
    df2 = df.loc[df.TestExceptionType.isin(['TestFailed','PatchCompileError','TestPassed'])]
    for et in editTypes[:etNo]:
        drawBarplot(df2, et, 'Test results for '+title, 'Test'+name+'_All_' + et + '.png', 'linear', 0, ymax1, False)
    df2 = df.loc[~df.TestExceptionType.isin(['TestFailed','PatchCompileError','TestPassed'])]
    res = pd.DataFrame(columns = outTestColumns)
    for p in projects:
        for et in editTypes:
            df3 = df2.loc[(df2.Project==p) & (df2.EditType==et)]
            newDf = df3.loc[df3.TestsFailed > failureOccurrence].copy()
            newRow = {'Project': p, 'EditType' : et, 'TestExceptionType': 'Other', 'PatchSize': 1, 'TestsFailed': df3.loc[~df3.TestExceptionType.isin(newDf.TestExceptionType), 'TestsFailed'].sum()}
            newDf.loc[len(newDf)] = newRow
            res = pd.concat([res, newDf], ignore_index=True, sort=True)
    for et in editTypes[:etNo]:
        drawBarplot(res, et, 'Test failures (type shown if occurs > '+str(failureOccurrence)+' times in a project)\n for '+title, 'Test'+name+'_' + et + '.png', 'linear', 0, ymax2, moveLegend)

if exp=='delete':

    drawPlots(df, 2, 'single deletes', 21000, 3300, False)

elif exp=='sample':

    df.set_index(['Project','EditType','TestExceptionType'],inplace=True)
    df = df.groupby(level=['Project','EditType','TestExceptionType']).sum()
    df.reset_index(inplace=True) 
    drawPlots(df, 3, 'edits', 250000, 11000, True)

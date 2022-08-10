import os
import sys
import numpy
import matplotlib
import pandas as pd

from globalVars import editTypes, dataDir, graphsDir, maxps

###### Check valid input ######

exp = sys.argv[1]
if exp!='edits':
    print('Please specify the currently supported experiment type: "edits".')
    sys.exit()

df = pd.read_csv(os.path.join(dataDir, exp + '_overlaps.csv'))
df.drop(df.index[df['EditType'] == 'MATCHED_STATEMENT'], inplace = True)

###### Draw required graphs ######

df.set_index(['EditType','PatchSize','EditCompiled'],inplace=True)
df = df.groupby(level=['EditType','PatchSize','EditCompiled']).sum()

df.reset_index(inplace=True)

def draw(df2, ymax, title, ps):

    barplot = df2.pivot(index='EditType', columns='EditCompiled', values='Frequency').plot.bar(rot=0)
    barplot.set_title(title)
    barplot.set_ylim(0,ymax)
    barplot.set_xlabel('')
    if ps == 5:
      barplot.legend(loc="upper left", bbox_to_anchor=[1, 1], ncol=3, fancybox=True, title='Edit Sequence')
    else:
      barplot.legend(loc="upper right", bbox_to_anchor=[1, 1], ncol=2, fancybox=True, title='Edit Sequence')
    fig = barplot.get_figure()
    if ps == 5: fig.set_size_inches(9.6,4.8)
    fig.tight_layout()
    fig.savefig(os.path.join(graphsDir, exp,  title + '.png'))

for ps in range(2,maxps+1):
    df2 = df.loc[df['PatchSize']==ps]
    draw(df2, 3500, 'Overlaps_of_size_' + str(ps), ps)
    excl = 'P'
    for i in range(ps-1):
        excl += 'P'
    df2 = df.loc[df.PatchSize == ps]
    df2 = df2.loc[df2.EditCompiled !=  excl]
    draw(df2, 300, 'Overlaps_without_all_passing_of_size_' + str(ps), ps)

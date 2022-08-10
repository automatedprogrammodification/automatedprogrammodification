import os, numpy, matplotlib
import pandas as pd
from globalVars import projects, editTypes, dataDir, inputDir, projectsDir, checkValidInput
from globalVars import outTypeColumns, mutations

exp = checkValidInput()
df = pd.DataFrame(columns = outTypeColumns)
print('Note that only patches of size 1 are currently supported.')
maxps = 1

###### Extract required data ######

def getData(data, p, et, ps):

    idx = editTypes.index(et)
    res = {'copy': [0,0,0], 'delete': [0,0,0], 'replace': [0,0,0], 'swap': [0,0,0]}
    for k in mutations.keys():
        typePatches = data.loc[data.Patch.str.contains(mutations[k][idx])]
        compiled = typePatches.loc[typePatches.PatchCompiled==True]
        failedNo = len(compiled.loc[compiled.TestPassed==False].groupby(['Patch']).groups.keys())
        compiledNo = len(compiled.groupby(['Patch']).groups.keys())
        passed = compiledNo - failedNo
        res[k] = [passed, len(typePatches.groupby(['Patch']).groups.keys()), compiledNo]

    df.loc[len(df)] = [p, et, ps,
                        res.get('copy')[0], res.get('delete')[0], res.get('replace')[0], res.get('swap')[0],
                        res.get('copy')[1], res.get('delete')[1], res.get('replace')[1], res.get('swap')[1],
                        res.get('copy')[2], res.get('delete')[2], res.get('replace')[2], res.get('swap')[2]]

###### Process input files ######

for p in projects:

    if exp=='delete':

        filename = os.path.join(projectsDir, p, p + ".DeleteEnumerator_output.csv")
        print(filename)
        data = pd.read_csv(filename)

        # drop NoOps
        data.drop(data.index[data['NoOp'] == True], inplace = True)

        lineData = data.loc[data['Patch'].str.contains("gin.edit.line.DeleteLine")]
        stmtData = data.loc[data['Patch'].str.contains("gin.edit.statement.DeleteStatement")]
        getData(lineData, p, 'LINE', maxps)
        getData(stmtData, p, 'STATEMENT', maxps)

    elif exp=='sample':

        for et in editTypes:

            filename = os.path.join(projectsDir, p, p + '.RandomSampler_j_' + et + '_patchSize' + str(maxps) + '_patchNumber10000_output.csv')
            print(filename)
            data = pd.read_csv(filename)

            # drop NoOps
            data.drop(data.index[data['NoOp'] == True], inplace = True)

            getData(data, p, et, maxps)

df.to_csv(os.path.join(dataDir, exp + '_type_data.csv'),index=False)

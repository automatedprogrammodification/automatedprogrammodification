import os, numpy, matplotlib, globalVars
import pandas as pd
from globalVars import projects, editTypes, dataDir, inputDir, projectsDir, checkValidInput
from globalVars import outColumns

exp = checkValidInput()
maxps = globalVars.maxps
df = pd.DataFrame(columns = outColumns)

###### Extract required data ######

def getData(data, p, et, ps):

    patchesUnique = len(data.groupby(['Patch']).groups.keys())
    allPatches = len(data.groupby(['PatchIndex']).groups.keys())

    validPatches = data.loc[data.PatchValid==True]
    validUnique = len(validPatches.groupby(['Patch']).groups.keys())
    valid = len(validPatches.groupby(['PatchIndex']).groups.keys())
    
    compiledPatches = data.loc[data.PatchCompiled==True] 
    compiledUnique = len(compiledPatches.groupby(['Patch']).groups.keys())
    compiled = len(compiledPatches.groupby(['PatchIndex']).groups.keys())

    failedUnique = len(compiledPatches[compiledPatches.TestPassed==False].groupby(['Patch']).groups.keys())
    failed = len(compiledPatches[compiledPatches.TestPassed==False].groupby(['PatchIndex']).groups.keys())
    passedUnique = compiledUnique - failedUnique
    passed = compiled - failed

    df.loc[len(df)] = [p, et, ps, validUnique, compiledUnique, passedUnique, patchesUnique, valid, compiled, passed, allPatches]

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
            for ps in range(1,maxps+1):

                filename = os.path.join(projectsDir, p, p + '.RandomSampler_j_' + et + '_patchSize' + str(ps) + '_patchNumber10000_output.csv')
                print(filename)
                data = pd.read_csv(filename)

                # drop NoOps
                data.drop(data.index[data['NoOp'] == True], inplace = True)

                getData(data, p, et, ps)

df.to_csv(os.path.join(dataDir, exp + '_data.csv'),index=False)

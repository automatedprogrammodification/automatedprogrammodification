import os, numpy, matplotlib, globalVars
import pandas as pd
from globalVars import projects, editTypes, dataDir, inputDir, projectsDir, checkValidInput
from globalVars import outTestColumns

exp = checkValidInput()
maxps = globalVars.maxps
df = pd.DataFrame(columns = outTestColumns)

###### Extract required data ######

def getData(data, p, et, ps):

    other = 0
    check = 0
    for exception in data['TestExceptionType'].unique():
        if not pd.isnull(exception):
            excNo = len(data.loc[data.TestExceptionType==exception])
            other += excNo
            df.loc[len(df)] = [p, et, ps, exception, excNo]
        else:
            tmpData = data.loc[data['PatchCompiled']==True]
            excNo = tmpData['TestExceptionType'].isnull().sum() 
            df.loc[len(df)] = [p, et, ps, 'TestPassed', excNo]
            check += excNo
            tmpData = data.loc[data['PatchCompiled']==False]
            excNo = tmpData['TestExceptionType'].isnull().sum() 
            df.loc[len(df)] = [p, et, ps, 'PatchCompileError', excNo]
            check += excNo
    df.loc[len(df)] = [p, et, ps, 'TestFailed', other]
    check += other
    assert(check==len(data))

###### Process input files ######

for p in projects:

    if exp=='delete':

        filename = os.path.join(projectsDir, p, p + ".DeleteEnumerator_output.csv")
        print(filename)
        data = pd.read_csv(filename)

        # drop NoOps
        data.drop(data.index[data['NoOp'] == True], inplace = True)

        data.sort_values(['Patch','UnitTest'], inplace=True)
        data.drop_duplicates(subset=['Patch','UnitTest'], inplace=True)
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

                data.sort_values(['Patch','UnitTest'], inplace=True)
                data.drop_duplicates(subset=['Patch','UnitTest'], inplace=True)
                getData(data, p, et, ps)

df.to_csv(os.path.join(dataDir, exp + '_test_data.csv'),index=False)

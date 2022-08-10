import os, sys

inputDir = '..' # assumes scripts are run from the scripts directory

projects = ['arthas','disruptor', 'druid', 'gson', 'jcodec', 'junit4', 'mybatis-3', 'opennlp', 'spark', 'spatial4j']

projectsDir = os.path.join(inputDir, 'casestudies')
dataDir = os.path.join(inputDir,'data') 
graphsDir = os.path.join(inputDir,'graphs') 
searchSpaceData = os.path.join(dataDir,'space.csv') # extracted data from the output of PatchSampler runs

editTypes = ['LINE', 'STATEMENT'] #, 'MATCHED_STATEMENT']

mutations = {
    'copy':    ['gin.edit.line.CopyLine', 'gin.edit.statement.CopyStatement', 'gin.edit.matched.MatchedCopyStatement'],
    'delete':  ['gin.edit.line.DeleteLine', 'gin.edit.statement.DeleteStatement', 'gin.edit.matched.MatchedDeleteStatement'],
    'replace': ['gin.edit.line.ReplaceLine', 'gin.edit.statement.ReplaceStatement', 'gin.edit.matched.MatchedReplaceStatement'],
    'swap':    ['gin.edit.line.SwapLine', 'gin.edit.statement.SwapStatement', 'gin.edit.matched.MatchedSwapStatement']
}

maxps = 5

samplerColumns = ['PatchIndex','PatchSize','Patch','MethodIndex','TestIndex','UnitTest','RepNumber','PatchValid','PatchCompiled','TestPassed','TestExecutionTime(ns)','TestCPUTime(ns)','TestTimedOut','TestExceptionType','TestExceptionMessage','AssertionExpectedValue','AssertionActualValue','NoOp','EditsValid']

outColumns = ['Project', 'EditType', 'PatchSize', 'UniqueValid', 'UniqueCompiled', 'UniquePassed', 'UniquePatches', 'Valid', 'Compiled', 'Passed', 'AllPatches']
results = ['Project', 'EditType', 'PatchSize', 'Compiled', 'Passed', 'Neutral_Variant_Rate'] # gathers unique patches for drawing

outTestColumns = ['Project', 'EditType', 'PatchSize', 'TestExceptionType', 'TestsFailed']

outTypeColumns = ['Project', 'EditType', 'PatchSize', 'Copy', 'Delete', 'Replace', 'Swap', 'CopyAll', 'DeleteAll', 'ReplaceAll', 'SwapAll', 'CopyCompiled', 'DeleteCompiled', 'ReplaceCompiled', 'SwapCompiled']

def calculate_perc(row, nom, denom):
    return row[nom] / float(row[denom]) * 100

def checkValidInput():
    exp = sys.argv[1]
    if exp=='delete':
        global maxps
        maxps = 1
    elif exp!='sample':
        print('Please specify the experiment type: "delete" or "sample".')
        sys.exit()
    return exp

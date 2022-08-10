import csv, os, numpy, matplotlib, sys
import pandas as pd
from globalVars import graphsDir, editTypes, projects, maxps, dataDir, projectsDir, samplerColumns
from treelib import Tree, Node

exp = 'edits'

dataBig = pd.DataFrame(columns=['Project', 'EditType', 'MethodIndex', 'Patch', 'PatchSize', 'EditCompiled'])

def compiled(comp, passed):
    if passed:
        return 'P'
    if comp:
        return 'C'
    return 'F'

def findLongestPassed(subsets, node):

    if node.tag[2].endswith('P'):
        return node
    else:
        return findLongestPassed(subsets, subsets.parent(node.identifier))

def processSubsets(subsets, p, et):

    df = pd.DataFrame(columns=['Project', 'EditType', 'MethodIndex', 'Patch', 'PatchSize', 'EditCompiled'])
    for child in subsets.leaves():
        if 'P' in child.tag[2]:
            node = findLongestPassed(subsets, child)
            if node.tag[0] not in df.Patch.values:
                df.loc[len(df)] = [p, et, node.tag[3], node.tag[0], node.tag[1], node.tag[2]]
    return df

for p in projects:

    for et in editTypes:

        data = pd.DataFrame()

        for ps in range(1,maxps+1):

            filename = os.path.join(projectsDir, p, p + ".RandomSampler_j_" + et + "_patchSize" + str(ps) + "_patchNumber10000_output.csv")
            print(filename)

            df = pd.DataFrame(columns = samplerColumns)
            df = pd.read_csv(filename)

            # drop NoOps
            df.drop(df.index[df['NoOp'] == True], inplace = True)

            df.sort_values(['Patch','TestPassed'],inplace=True, ascending=[True,True])
            df.drop_duplicates(subset = 'Patch', inplace = True) 
            data = pd.concat([data, df], ignore_index=True)
            
        data.sort_values(['Patch','TestPassed'],inplace=True, ascending=[True,True])
        data.drop_duplicates(subset = 'Patch', inplace = True) 

        subsets = Tree()
        first = ''

        for index, row in data.iterrows():
       
            patch = row['Patch'] 
            check = len(patch.split('|')) - 2
            if check == 1: # path of size 1 found
                if first:
                    df = processSubsets(subsets, p, et)
                    dataBig = pd.concat([dataBig, df], ignore_index=True, sort=False)
                subsets = Tree()
                first = patch
                subsets.create_node([first, check, compiled(row['PatchCompiled'], row['TestPassed']), row['MethodIndex']],first)
            elif first:
                if check == 2 and patch.startswith(first):        
                    subsets.create_node([patch, check, subsets.get_node(first).tag[2] + compiled(row['PatchCompiled'], row['TestPassed']), row['MethodIndex']],patch, parent=first)
                elif check == 3:        
                    for child in subsets.children(first):
                        if patch.startswith(child.tag[0]):
                            subsets.create_node([patch, check, child.tag[2] + compiled(row['PatchCompiled'], row['TestPassed']), row['MethodIndex']], patch, parent=child.identifier)
                            break
                elif check == 4:        
                    for child in subsets.children(first):
                        for child2nd in subsets.children(child.identifier):
                            if patch.startswith(child.tag[0]):
                                subsets.create_node([patch, check, child2nd.tag[2] + compiled(row['PatchCompiled'], row['TestPassed']), row['MethodIndex']], patch, parent=child2nd.identifier)
                                break
                        else:
                            continue
                        break
                elif check == 5:        
                    for child in subsets.children(first):
                        for child2nd in subsets.children(child.identifier):
                            for child3rd in subsets.children(child2nd.identifier):
                                if patch.startswith(child.tag[0]):
                                    subsets.create_node([patch, check, child3rd.tag[2] + compiled(row['PatchCompiled'], row['TestPassed']), row['MethodIndex']], patch, parent=child3rd.identifier)
                                    break
                            else:
                                continue
                            break
                        else:
                            continue
                        break
                elif check > 5:
                     print('Patch length greater than 5 encountered, exiting..')
                     sys.exit()

dataBig.to_csv(os.path.join(dataDir, exp + '_overlaps_all.csv'), index=False)
dataBig.drop(columns=['Patch'], inplace=True)
dataBig.drop(columns=['MethodIndex'], inplace=True)
dataBig['Frequency'] = dataBig.groupby(['Project','EditType','PatchSize','EditCompiled'])['EditCompiled'].transform('count')
dataBig.drop_duplicates(inplace = True) 
dataBig.to_csv(os.path.join(dataDir, exp + '_overlaps.csv'), index=False)

import os
import json

jpacmanLocation = 'E:\Github_Desktop\ETS\jpac'
currentDir = os.getcwd()

#stream = os.popen(currentDir + '\\..\\RefactoringMiner-2.2.0\\bin\\RefactoringMiner -bc ' + jpacmanLocation + ' '
#                  '1185f2b770024ce65ec19b8258faaed057acdde5 0c10fb29dab401f33f8563bccdf272f168c69a8b -json '
#                  + currentDir + '\\..\\RefactoringMiner-2.2.0\\bin\\data.json')
#output = stream.read()


f = open(currentDir + '\\..\\RefactoringMiner-2.2.0\\bin\\data.json')
data = json.load(f)

typesOfRefactor = dict();
for commit in data['commits']:
    refactors = commit['refactorings']
    if refactors:
        #print(commit)
        for refactor in refactors:
            #print(f'\t{refactor}')
            refactorType = refactor['type']
            typesOfRefactor[refactorType] = typesOfRefactor.get(refactorType, 0) + 1
typesOfRefactor = dict(sorted(typesOfRefactor.items(), key=lambda item: item[1]))
for refactorType, count in typesOfRefactor.items():
    print(f'{refactorType}: {count}')

filesRefactored = dict();
for commit in data['commits']:
    refactors = commit['refactorings']
    if refactors:
        for refactor in refactors:
            for leftSideLocations in refactor['leftSideLocations']:
                file = leftSideLocations['filePath']
                filesRefactored[file] = filesRefactored.get(file, 0) + 1
            for rightSideLocations in refactor['rightSideLocations']:
                file = rightSideLocations['filePath']
                filesRefactored[file] = filesRefactored.get(file, 0) + 1
filesRefactored = dict(sorted(filesRefactored.items(), key=lambda item: item[1]))
for file, count in filesRefactored.items():
    print(f'{file}: {count}')



# Closing file
f.close()
import json
from pip._vendor import requests
import csv
import numpy as np
import matplotlib.pyplot as plt

repo = 'scottyab/rootbeer'
lstTokens = ['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']

gitUrl = 'https://api.github.com/repos/' + repo + '/commits?path='
headers = {'Authorization': 'token ' + lstTokens[0]}
files = []


with open('E:\\Github_Desktop\\ETS\\log530\\somecsv\\Rootbeer.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        elif row:
            filePath = row[0]
            print(f'processing {filePath},{row[1]}.')

            content = requests.get(gitUrl + filePath, headers=headers)
            details = json.loads(content.content)
            fileObj = {'fileName': filePath, 'commits': []}
            for line in details:
                commit = line['commit']
                date = commit['author']['date']
                name = commit['author']['name']
                email = commit['author']['email']
                fileObj['commits'].append({'email': email, 'date': date})
                #print(f'\t{name}({email}) modified on {date}.')
            files.append(fileObj)
            line_count += 1
    line_count = line_count - 1
    print(f'Processed {line_count} lines.')

    x = []
    y = []
    email = []
    number = 0
    for file in files:
        fileName = file['fileName']
        fileName = fileName.split('/')
        fileName = fileName[len(fileName)-1]
        print(fileName)
        for row in file['commits']:
            print(f"\t{row['email']} modified {row['date']}")
            x.append(fileName)
            y.append(row['date'])
            number = number +1
            email.append(number)
    y.sort()
    plt.scatter(x, y, c=email, cmap='nipy_spectral')
    plt.grid(True)
    plt.show()
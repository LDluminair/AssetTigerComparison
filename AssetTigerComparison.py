import csv
import subprocess

adNamesAndEmailDictionary = {}
updatedAssetNames = {}
foundCount = 0
csv_columns = ['Name', 'Email']


#getAdNamesScript = subprocess.call([r'powershell.exe', r'C:\Users\bgerdes\source\repos\LDluminair\AssetTigerComparison\getAdNames.ps1'])

targetAdNamesFile = r'C:\Users\bgerdes\Desktop\adDisplayNames.csv' 
targetAssetNamesFile = r'C:\Users\bgerdes\Desktop\persons.csv' 



with open(targetAdNamesFile) as adNamesList:
    reader = csv.DictReader(adNamesList)
    for row in reader:
        displayName = row['displayName']
        email = row['mail']
        adNamesAndEmailDictionary[displayName] = email

with open(targetAssetNamesFile) as assetNamesList:
    reader = csv.DictReader(assetNamesList)
    for row in reader:
        email = row['Email']
        for displayName, mail in adNamesAndEmailDictionary.items():
            if mail == '':
                continue
            elif mail == email:
                foundCount += 1
                updatedAssetNames[displayName] = mail
              
with open(r'c:\users\bgerdes\desktop\updateAssetNames.csv', 'w', newline='', encoding='utf-8') as updatedAssetNamescsv:
    write = csv.writer(updatedAssetNamescsv)
    write.writerow(csv_columns)
    for value, key in updatedAssetNames.items():
        write.writerow([value, key])


          
print(str(foundCount) + " names were found.")

#with open(targetAssetNamesFile) as assetNamesList:
#    reader = csv.DictReader(assetNamesList)
#    for row in reader:



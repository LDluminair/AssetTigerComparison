$OUs = 
"OU=Employees,DC=nampa,DC=nnu",
"OU=Partners,DC=nampa,DC=nnu",
"OU=Students,DC=nampa,DC=nnu"

$displayNameList

Foreach($OU in $OUs){
    $displayNameList += Get-ADUser -Filter * -Properties * -SearchBase $OU | select displayName,employeeID,mail | sort displayName}
    $displayNameList | export-csv C:\Users\bgerdes\Desktop\ADDisplayNames.csv -NoTypeInformation
# skript pro prihlaseni k Exchange online, je potreba znat login pro Admina

# Vyzadani jmena a hesla
$UserCredential = Get-Credential
#Spojeni se serverem
$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://outlook.office365.com/powershell-liveid/ -Credential $UserCredential -Authentication Basic -AllowRedirection
# Import exchange online funkci
Import-PSSession $Session
# Overeni funkcnosti
Get-Mailbox -ResultSize unlimited


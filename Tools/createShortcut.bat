@echo off

echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo sLinkFile = "%UserProfile%\Desktop\CODEXIS Green.lnk" >> CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
echo oLink.TargetPath = "https://app.codexis.cz" >> CreateShortcut.vbs
REM echo oLink.TargetPath = "C:\Program Files\Google\Chrome\Application\chrome.exe" >> CreateShortcut.vbs
REM echo oLink.Arguments = "https://app.codexis.cz" >> CreateShortcut.vbs
REM echo oLink.IconLocation = "\\sibadnb2\SHARE\CODEXIS_GREEN.ico" >> CreateShortcut.vbs
echo oLink.IconLocation = "http://storage.update.atlascloud.cz/vip/CODEXIS_GREEN.ico" >> CreateShortcut.vbs
echo oLink.WindowStyle = "3" >> CreateShortcut.vbs
echo oLink.Save >> CreateShortcut.vbs

cscript /nologo CreateShortcut.vbs
del CreateShortcut.vbs
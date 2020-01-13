# Creates shortcut on users desktop for URL app.codexis.cz
# sets icon from specifited location

$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$Home\Desktop\CODEXIS Green.lnk")
$Shortcut.TargetPath = "http:\\app.codexis.cz"
# $Shortcut.IconLocation = "\\sibadnb2\SHARE\CODEXIS_GREEN.ico"
$Shortcut.IconLocation = "http://storage.update.atlascloud.cz/vip/CODEXIS_GREEN.ico"
$Shortcut.Save()
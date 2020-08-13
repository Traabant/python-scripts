# Projde zadanou slozku, najde v ni soubory, ktere maji urcenou priponu a spocita jejich pocet a celekovou velikost
# Uzivateli do konzole vypise pocet nalezenych souboru a celkovou spocitanou velikost

# Pripony, pro filtr vyhledanych souboru
$extension_list = "*.maf","*.mpt","*.xltx","*.pptm","*.ott","*.ots","*.otp","*.txt","*.pptx","*.mat","*.mar","*.maq","*.oti","*.otf","*.otg","*.otc","*.vdx","*.ppt","*.vssm","*.xlsm","*.xls","*.vsdx","*.xlt","*.xts","*.xlsx","*.rtf","*.ppl","*.doc","*.mam","*.vsdm","*.oft","*.slk","*.ppsm","*.xps","*.vtx","*.odb","*.dif","*.docm","*.onetoc","*.xsn","*.adn","*.docx","*.xltm","*.one","*.pot","*.thmx","*.vsd","*.oth","*.vsl","*.vsw","*.vst","*.vss","*.vsx","*.adp","*.accdr","*.accdt","*.odf","*.accdb","*.accde","*.ppam","*.potm","*.odm","*.odi","*.dot","*.odg","*.sldm","*.dotm","*.odc","*.msg","*.vssx","*.dotx","*.odt","*.ods","*.odp","*.sldx","*.mdt","*.mdw","*.vstm","*.onetoc2","*.pub","*.mde","*.mdf","*.vstx","*.mda","*.mdb","*.potx","*.pdf","*.html","*.htm","*.jpeg","*.psp","*.tiff","*.tga","*.cr2","*.CR2","*.PSD","*.ico","*.sct","*.pxr","*.pct","*.pic","*.raw","*.jpe","*.tif","*.png","*.bmp","*.jpg","*.gif"

# Vyzvani uzivatle k zaddini slozky pro pocitani souboru
$path = Read-Host "Path to folder"

$full_size = 0;
$file_count = 0;

Get-ChildItem -Path $path -Include $extension_list -Recurse -Force | ForEach-Object {
    $full_size += $_.Length;
    $file_count += 1;
}
Write-Host("celkem nalezeno vyhovujicich souboru: " + $file_count + " Velikost: " +  $full_size/1MB + "MB")

# Create folders
$Names = "names"
$Ages = "ages"
$Numbers = "numbers"

# Check if these folder names exist
if (Test-Path -Path $Names){
Write-Output "This file already exists"
} else { New-Item -Path $Names -ItemType Directory 
         Write-Output "Folder with the name $Names has been created" 
}

if (Test-Path -Path $Ages){
Write-Output "This file already exists"
} else { New-Item -Path $Ages -ItemType Directory 
         Write-Output "Folder with the name $Ages has been created" 
}

if (Test-Path -Path $Numbers){
Write-Output "This file already exists"
} else { New-Item -Path $Numbers -ItemType Directory 
         Write-Output "Folder with the name $Numbers has been created" 
}
$Race = "race"
$Country = "country"
$Car = "car"

Set-Location -Path $Names
New-Item -Name $Race -ItemType Directory
New-Item -Name $Country -ItemType Directory
New-Item -Name $Car -ItemType Directory
Remove-Item $Race -Recurse -Force
Remove-Item $Country -Recurse -Force







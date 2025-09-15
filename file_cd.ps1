# Create folders
$folder_1 = 
$folder_2 = new_folder2
$folder_3 = new_folder3

# Check if these folder names exist
if (Test-Path -Path $folder_1){
Write-Output "This file already exixts"
} else { New-Item -Path $folder_1 -ItemType Directory 
         Write-Output "Folder with the name $folder_1 has been created" 
}

if (Test-Path -Path $folder_2){
Write-Output "This file already exixts"
} else { New-Item -Path $folder_2 -ItemType Directory 
         Write-Output "Folder with the name $folder_2 has been created" 
}

if (Test-Path -Path $folder_3){
Write-Output "This file already exixts"
} else { New-Item -Path $folder_3 -ItemType Directory 
         Write-Output "Folder with the name $folder_3 has been created" 
}







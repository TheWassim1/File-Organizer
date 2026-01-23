from pathlib import Path

path_inputted = str(input("Write the exact path of the messy folder you want to organize :  "))
path = Path(path_inputted)
nbfile=0
if not path.is_dir():
    print("Soryy, that's not a valid path! ")
    exit()

for file in path.iterdir():
    target_folder = ""
    if file.is_dir():
        target_folder ="Folders"
    match file.suffix.lower() : 
        case  ".exe" :
            target_folder="Applications"
        case ".jpg" | ".jpeg" | ".png" | ".gif" | ".webp" :
            target_folder="Pictures"
        case  ".txt" | ".pdf" | ".docx" | ".xlsx": 
            target_folder="Documents"
        case ".mp4" :
            target_folder="Videos"
        case ".zip" |".rar" :
            target_folder="Compressed"
        case ".mp3" :
            target_folder="Music"
        case ".iso" : 
            target_folder="ISO-files"
        
        
    if target_folder : 
        dest = path / target_folder
        dest.mkdir(parents=True , exist_ok=True)
        counter = 1 
        while (dest / file.name).exists():          
            newfilename=f"{file.stem}_{counter}{file.suffix}"
            file.replace(dest / newfilename)
            counter+=1
        file.replace(dest / file.name)
        print(f"Moved {file.name} ---> {target_folder}/") 
        nbfile+=1
print("*********************************************************")
if nbfile == 0 : 
    print(f"I can't recognize any files in  {path_inputted}")
else:
    print(f"[Success] organizing {nbfile} from {path_inputted} ")
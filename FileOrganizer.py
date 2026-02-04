from pathlib import Path

def organize_folder(path_inputted):
    path = Path(path_inputted)
    nbfile = 0

    # 1. Validation Checks
    if not path.exists():
        return "Error: Path does not exist!"
    if not path.is_dir():
        return "Error: Input is not a folder!"
    files = [f for f in path.iterdir() if f.is_file()]

    for file in files:
        target_folder = ""   
        match file.suffix.lower():
            case ".exe": target_folder = "Applications"
            case ".jpg" | ".jpeg" | ".png" | ".gif" | ".webp": target_folder = "Pictures"
            case ".txt" | ".pdf" | ".docx" | ".xlsx": target_folder = "Documents"
            case ".mp4" | ".avi" | ".mkv": target_folder = "Videos"
            case ".zip" | ".rar": target_folder = "Compressed"
            case ".mp3" | ".wav": target_folder = "Music"
            case ".iso": target_folder = "ISO-files"

        if target_folder:
            dest_dir = path / target_folder
            dest_dir.mkdir(parents=True, exist_ok=True)
            final_path = dest_dir / file.name
            counter = 1
            while final_path.exists():
                new_name = f"{file.stem}_{counter}{file.suffix}"
                final_path = dest_dir / new_name
                counter += 1
            try:
                file.replace(final_path)
                print(f"Moved {file.name} ---> {target_folder}/")
                nbfile += 1
            except PermissionError:
                print(f"Skipped {file.name} (Permission Denied)")

    # Return result string to the GUI
    if nbfile == 0:
        return f"No recognizable files found in {path.name}"
    else:
        return f"Success! Organized {nbfile} files."
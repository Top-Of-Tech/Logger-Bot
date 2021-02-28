from zipfile import ZipFile
import zipfile, os, shutil
from datetime import datetime

def zip_logs():
    if not os.path.exists('Backups/'): os.makedirs('Backups/')
    generate_back_up_name = datetime.now().strftime("%A %B %d %Y-%I_%M_%S%p")
    directories = ['Data']
    file_paths = []
    for directory in directories:
        file_paths += get_all_file_paths(directory)
    with ZipFile(f'Backups/Backup - {generate_back_up_name}.zip', 'w', compression=zipfile.ZIP_DEFLATED) as zip:
        for file in file_paths:
            zip.write(file)
    clear_folders(['Data'])

def get_all_file_paths(directory):
    file_paths = []
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths

def clear_folders(folders):
    for folder in folders:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path): os.unlink(file_path)
                elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

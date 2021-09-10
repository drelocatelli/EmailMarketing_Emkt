import os, subprocess
from shutil import make_archive

folder = str(subprocess.getoutput(f'basename {os.getcwd()}'))

def create_file(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    os.system(f'cp complete.html {folder}')
    os.chdir(f'{folder}')
    if not os.path.exists(folder):
        os.makedirs('assets')
    os.chdir(f'..')
    os.system(f'cp assets/* {folder}/assets')

    make_archive(folder, 'zip', root_dir=folder)

create_file(folder)

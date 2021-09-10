import os, subprocess
from shutil import make_archive

folder = str(subprocess.getoutput(f'basename {os.getcwd()}'))

def create_file(folder):
    os.system(f'mkdir -p {folder}')
    os.system(f'cp complete.html -t {folder}')
    os.chdir(f'{folder}')
    os.system(f'mkdir -p assets')
    os.chdir(f'..')
    os.system(f'cp assets/* {folder}/assets')

    make_archive(folder, 'zip', root_dir=folder)

    os.system(f'mkdir -p {folder}')
    os.system(f'cp complete.html -t {folder}')
    os.chdir(f'{folder}')
    os.system(f'mkdir -p assets')
    os.chdir(f'..')
    os.system(f'cp assets/* {folder}/assets')

create_file(folder)

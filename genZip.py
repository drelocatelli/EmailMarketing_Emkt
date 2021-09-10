import os, subprocess
from shutil import make_archive
from bs4 import BeautifulSoup
# import re

# text = ''

# with open('complete.html', 'r+') as file:
#     text += re.sub(r'<script.+?</script>', '', file.read(), flags=re.DOTALL)

# os.system('rm complete.html')

# with open('complete.html', 'w') as file:
#     file.write(text)

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

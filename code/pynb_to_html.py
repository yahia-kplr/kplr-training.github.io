import os

ALL_REPOS_PATH='/home/ubuntu/ALL_REPOS/'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(ALL_REPOS_PATH):
    for file in f:
        if file.endswith('.ipynb'):
            files.append(os.path.join(r, file))

for file in files:   
    if file.endswith('.ipynb'):
        print(file)
        os.system("jupyter nbconvert --to html '"+file+"'")
        
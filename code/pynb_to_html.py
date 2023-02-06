import os

ALL_REPOS_PATH='/Users/saxen/Documents/GitHub/kplr-training'
GH_PAGES_PATH='/Users/saxen/Documents/GitHub/kplr-training.github.io/notebooks'
files = []

# iterate over all local repos to collect pynb file names and paths
# r=root, d=directories, f = files
for r, d, f in os.walk(ALL_REPOS_PATH):
    for file in f:
        if file.endswith('.ipynb'):
            files.append(os.path.join(r, file))

# iterate over pynb files and convert to html into github pages local repo
# remember to push to git after completion
for file in files:   
    out_path = GH_PAGES_PATH+os.path.dirname(file).replace(ALL_REPOS_PATH,'')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    os.system("jupyter nbconvert  --output-dir='{}' --to html '{}'".format(out_path, file))
    print("Done")
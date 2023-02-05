import os

def rename_folders(repo_local):
    for dirpath, dirnames, filenames in os.walk(repo_local):
        for name in filenames + dirnames:            
            old_path = os.path.join(dirpath, name)
            new_path=''
            if (' ' in old_path):
                count+=1                
                if os.path.isdir(old_path):
                    print(old_path)
                    new_path = os.path.join(dirpath, name.replace('. ', '.').replace(' - ', '-').replace(' ', '-'))
                    os.rename(old_path, new_path)                            
                    print(new_path)
                    print()

def rename_files(repo_local):
    for dirpath, dirnames, filenames in os.walk(repo_local):
        for name in filenames + dirnames:            
            old_path = os.path.join(dirpath, name)
            new_path=''
            if (' ' in old_path):             
                if not os.path.isdir(old_path):
                    print(old_path)
                    new_path = os.path.join(dirpath, name.replace('. ', '.').replace(' ', '_'))
                    os.rename(old_path, new_path)
                    print(new_path)
                    print()

def rename_files_underscore(repo_local):
    for dirpath, dirnames, filenames in os.walk(repo_local):
        for name in filenames + dirnames:            
            old_path = os.path.join(dirpath, name)
            new_path=''
            if ('_.' in old_path):                             
                if not os.path.isdir(old_path):
                    print(old_path)
                    new_path = os.path.join(dirpath, name.replace('_.html', '.html'))
                    os.rename(old_path, new_path)
                    print(new_path)
                    print()

#repo_local = '/Users/saxen/Documents/GitHub/kplr-training'
repo_local = '/Users/saxen/Documents/GitHub/kplr-training.github.io'
#print(repo_local)
#rename_folders(repo_local)
rename_files_underscore(repo_local)
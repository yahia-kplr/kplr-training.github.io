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
        for name in filenames + dirnames:            #
            old_path = os.path.join(dirpath, name)
            new_path=''
            if ('_-_' in old_path):             
                if not os.path.isdir(old_path):
                    print(old_path)
                    new_path = os.path.join(dirpath, name.replace('. ', '.').replace(' ', '_').replace('_-_', '-'))
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
                    new_path = os.path.join(dirpath, name.replace('_.', '.'))
                    os.rename(old_path, new_path)
                    print(new_path)
                    print()

def replace_substring(input_string, _start, _end):
    character_index = input_string.find('%20')
    start_index = input_string.find(_start)
    end_index = input_string.find(_end)
    if character_index != -1:
        if start_index != -1 and end_index != -1 and end_index > start_index:
            _in = input_string[:start_index] + input_string[start_index:end_index+3]
            out = _in.replace('%20', '-') + input_string[end_index+3:]
            print(_in)
            print(out)
            return out
    else:
        return input_string
    
def replace_webspaces(repo_local):
    _start = "https://colab.research.google.com/github/kplr-training"
    _end = "colab-badge.svg"

    for dirpath, dirnames, filenames in os.walk(repo_local):
        for name in filenames + dirnames:
            path = os.path.join(dirpath, name)            
            if not os.path.isdir(path):
                if path.endswith(".html"):
                    print(path) 
                    with open(path, 'r') as file:                
                        input_strings = file.readlines()
                        output_strings = [replace_substring(input_string, _start, _end) for input_string in input_strings]
                    #with open(output_file, 'w') as file:
                        #file.writelines(output_strings)         #file.writelines(output_strings)
                        #break        

repo_local = '/Users/saxen/Documents/GitHub/kplr-training'
#repo_local = '/Users/saxen/Documents/GitHub/kplr-training.github.io/notebooks'
#print(repo_local)
#rename_folders(repo_local)
#replace_webspaces(repo_local)
rename_files(repo_local)
#replace_webspaces(repo_local)
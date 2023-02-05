import os
#from dotenv import load_dotenv

from github import Github

import re
import json


# except_bs64=[]
# except_bs64_path=[]

def list_files(repo, path):
    for file in repo.get_contents(path):
        if file.type == "dir":
            list_files(repo, file.path)
        else:
            print(file.path,file.html_url)
            
            
def add_link_colab(html_link):
    colab={
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\""+html_link+"\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    }
    return colab

def add_link_colab_local(html_link):
    colab={
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/"+html_link+"\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    }
    return colab    


def remove_colab(js_file):
    cpt=0
    if "metadata" in js_file:
        if 'colab' in js_file['metadata']:
            del js_file['metadata']['colab']
    for cell in js_file['cells']:
        if "colab_type" in cell['metadata']:
            js_file['cells'].remove(cell)
            
            
def make_dir_file_ipynb(lien_except):
    return [{"url":i,"path":'./'+"".join(i.replace('https://colab.research.google.com/github/kplr-training/','').split('blob/main/'))} for i in lien_except]
def make_dir_file(lien_except):
    return [i.update({"file":'/'.join(i['path'].split('/')[:-1]),'ipynb':'./'+i['path'].split('/')[-1]}) for i in lien_except]

def all_job(repo, path):
    # global except_bs64
    # global except_bs64_path
    for file in repo.get_contents(path):
        try :
            if file.type == "dir":
                all_job(repo, file.path)
            elif file.path.endswith(".ipynb"):
                html_test=file.html_url.replace('https://',"https://colab.research.google.com/")
                html_test=html_test.replace('github.com',"github")
                file_content = repo.get_contents(file.path).decoded_content.decode(encoding='UTF-8',errors='strict')
                json_object = json.loads(file_content)
                
                remove_colab(json_object)

                json_object['cells'].insert(0,add_link_colab(html_test))
                
                print(file.html_url)

                # pour update le repo github documente cette ligne
                repo.update_file(file.path, "auto-commit",json.dumps(json_object) , file.sha)

        except :
            # print("except :",file.html_url)
            # except_bs64.append(html_test)
            # except_bs64_path.append(file.path)
            pass


def main():
    #load_dotenv()

    g = Github('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')
    user = g.get_user()

    repos = [i.full_name for i in g.get_user().get_repos() if i.full_name.startswith('kplr-training')]
    
    for repo in repos:        
        repo = g.get_repo(repo)           
        all_job(repo, "")


if __name__ == "__main__":
    main()
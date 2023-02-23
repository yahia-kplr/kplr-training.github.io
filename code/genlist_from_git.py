
import os
from github import Github
TOKEN='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'

# Initialize a Github instance with your API token
g = Github(TOKEN)

# Get the authenticated user
user = g.get_user()

repo = g.get_repo("kplr-training/kplr-training.github.io")

def list_files(repo, path='',indent=0):
    html = ""
    html += " " * indent + "<ul>\n"
    for file in repo.get_contents(path):
        #if file.path.startswith('notebooks'):
        if file.type == "dir":
            html += " " * indent + "<li>" + file.name + "\n"
            html += list_files(repo, file.path, indent + 2)
            html +=  " " * indent + "</li>" + "\n"
            print(file.path)
        else:
            if (file.name.endswith('.html')):
                print(file.path,file.html_url)
                html += " " * indent + "<li><a href='" + file.path + "'>"+file.name+"</a></li>\n"
    html += " " * indent + "</ul>\n"
    return html

html = list_files(repo, 'notebooks')

# This in an ugly hack to insert a blank pixel in order to align the list to compensate a bug in LIQUID
html = html[:5] + "<li><a href='https://upload.wikimedia.org/wikipedia/commons/d/d2/Blank.png'></a></li>\n" + html[5:]
# the generated list.html files is included in the jekyll site and referenced in the index.html file
list_file = './_includes/list.html'
os.makedirs(os.path.dirname(list_file), exist_ok=True)
with open(list_file, 'w') as f:
    f.write(html)
from github import Github
import requests
from pprint import pprint
from pygithub3 import Github

# First create a Github instance:

token = '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'

g = Github(token)
for u in g.get_user().get_repo(name='Spur').get_collaborators():
    print(u)


print("repo")
for repo in g.get_user().get_repos():
    print(repo)

if __name__ == '__main__':
    print('PyCharm')
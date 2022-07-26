from config import *

def generate_url_repo_list():
    '''Generating URL for Listing Repo'''
    url = BASE_URL + SEARCH + REPO_QUERY
    return url

def generate_repo_commits_url(repo_full_name):
    '''Getting the commit datas using the repo name'''
    url = BASE_URL + REPOS + "/" + repo_full_name + COMMITS
    return url
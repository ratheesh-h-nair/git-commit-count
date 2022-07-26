import json
import requests
from services import *

def make_response(status,payload,message):
    '''default response standard definition'''
    return {
        'status':status,
        'payload':payload,
        'message':message
    }

def failed_response(message):
    '''default failed response standard definition'''
    return {
        'status':False,
        'payload':[],
        'message':message
    }

def get_repo_list(n,m):
    '''Listing the repos and getting the commit data'''
    repo_list = []
    url = generate_url_repo_list()
    response = requests.get(url) # Github API Calling
    if(response.status_code == 200):
        repo_response_payload = json.loads(response.text)
        count = 0
        for item in repo_response_payload['items']:
            if(count <= n):
                repo_list.append(
                    {
                        'name':item['name'],
                        'full_name':item['full_name'],
                        'git_url':item['git_url']
                    }
                ) # Appending to the list as object as it satisfied the condition
                count +=1
    else:
        return failed_response(response.text) # returns the response while it failed to get data from Github API
    if(len(repo_list)>=1):
        for item in repo_list:
            commit_count = []
            url = generate_repo_commits_url(item['full_name'])
            response = requests.get(url,headers=headers) # API Requests for commit records
            if(response.status_code == 200):
                commit_response_payload = json.loads(response.text)
                user_count = []
                for itm in commit_response_payload:
                    try:
                        list_of_all_values = [value for elem in user_count for value in elem.values()]
                        if(str(itm['author']['login']) in list_of_all_values):
                            for user in user_count:
                                if(user['username'] == str(itm['author']['login'])):
                                    user['commit_count'] = int(user['commit_count']) + 1
                        else:
                            user_count.append(
                                {
                                    'username':str(itm['author']['login']),
                                    'commit_count':1
                                }
                            )
                    except:
                        '''In case of any error happened on the response of any particular repo. That repo can be excluded from the listing'''
                        pass
                item['commit_count'] = user_count[:m:-1]
            else:
                ''' In case of repo listing API having any error. The error msg will be returned as response'''
                return failed_response(response.text)
    return repo_list

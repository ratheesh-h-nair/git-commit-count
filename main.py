from flask import Flask
from flask import Flask,jsonify,request
from helper import *

app = Flask(__name__)

@app.route('/')
def index():
    '''Main Function that returns the required respose as expected'''
    try:
        n = request.args.get('repo-count',default = 1,type=int)
        m = request.args.get('commit-count',default = 1,type=int)
        repo_list = get_repo_list(n,m)
        return jsonify(make_response(True,repo_list,LIST_OF_REPOS))
    except Exception as e:
        import sys
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("Linne Number : {0} , Error Type = {1}".format(exc_tb.tb_lineno,exc_type))
        return jsonify(failed_response(str(e)))

app.run(debug=True)

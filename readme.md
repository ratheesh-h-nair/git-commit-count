# Commit count on most popular repos in github
## The App providews the most commit count on most popular repos in github

The App is basically an API provides the most popular Repos and it commit count based on user wise in descending order

The App is developed on latest Python version 3.10.

## Tech

App uses a number of open source libraries to work properly:

- Flask -> Python web framework 
- Requests -> Requests will allow you to send HTTP/1.1 requests using Python

## Installation

Commit Count App requires [Python](https://www.python.org/) v3.10 to run.

Install the dependencies and devDependencies and start the server.

Clone the repository from
```sh
git clone https://github.com/ratheesh-h-nair/git-commit-count
```
Run the below command to install the dependency library

For Windows Users
```sh
pip install -r requirements.txt (Python 3)
```
For Linux / Ubuntu Users
```sh
pip3 install -r requirements.txt (Python 3)
```

After installing Run through the command below
For Windows
```sh
python main.py
```

For Linux / Ubuntu
```sh
python3 main.py(Ubuntu/Linux)
```

As mentioned it is a API based Application you need Postman to access the API
You can download the Postman App from https://www.postman.com/

Verify the development serever by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:5000
```

Also can access via online deployed cloud server from below link
```sh
http://ratheeshhnair.pythonanywhere.com?commit-count=2&repo-count=2
```

# The Parameter passing with URL is 
- commit-count -> Number of commits on the repository need to be displayed
- repo-count-> Number of repository need to be considered

**Free to hear! Thank You!**

# Flask User/Bootstrap Template
Flask template using flask-login and flask-bootstrap.

# Template Download and Setup
1. Create new repository on GitHub for your project.
2. Run following commands in terminal.
- git clone git@github.com:coreypizzle/user-bootstrap-template.git 'directory-name'
- cd 'directory-name'
- git remote rm origin
- git remote add origin 'new-repository-ssh'
- git push -u origin master
3. Rename appname.py to the name of your app.
4. Update /app/.flaskenv to reflect new appname.py name.
5. If on Windows, create Virtual Environment and install requirements.
- python -m virtualenv venv
- .\venv\Scripts\activate
- pip install -r requirements.txt
6. If on Linux, use existing Virtual Environment.
- source /venv/bin/activate

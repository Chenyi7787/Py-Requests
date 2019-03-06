Add Remote Repository:

1. mkdir Py-Requests(local)

2. git init(local)

3. github -> new repository Py-Requests(github)

4. sshkey -> id_rsa.pub(local) add to github(github)

5. git remote add origin git@github.com:Chenyi7787/Py-Requests.git(local)

6. vim readme.txt/git add readme.txt/git commit -m "add readme.txt"(local)

7. git push -u origin master(local first time to start push need to add "-u": asocciate local with remote repository master branch)

8. git push origin master(local no need to add "-u")


Create virtualenv:


1. pip3 install virtualenv

2. mkdir virtual-python3.6-local

3. virtualenv -p /usr/bin/python3.6 --no-site-packages virtualenv-python3.6-local

4. source virtualenv-python3.6-local/bin/activate

5. deactive


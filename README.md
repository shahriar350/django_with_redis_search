After installing the django, please installed required packages <br/>
`pip install -r requirements.txt`

First, you have to install `redis-stack-server` because only redis `redis-stack-server` can perform json and search. 
To install `redis-stack-server`, read the docs https://redis.io/docs/getting-started/install-stack/linux/

For windows, you have to install wsl (ubuntu) first. After installing WSL, open ubuntu shell and write same command as Linux user.

For linux, do check before install the following command if your linux distro and version is supported by redis or not from the previous redis installation website:
```shell
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
sudo chmod 644 /usr/share/keyrings/redis-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
sudo apt-get update
sudo apt-get install redis-stack-server
```

After installing the prior command, start the server by writing following command
```shell
sudo service redis-stack-server start
```
you can also perform `start` `stop` `restart`

After that please run
```pycon
python manage.py migrate
python manage.py runserver
```
Now, you have to create a account, you can create a superuser 
``python manage.py createsuperuser``
<br/><br/>
After creating the superuser, goto `/api/v1/categories` to create some category first.
<br/><br/>
**REDIS SEARCH RESULT** <br/>
Now, create some employees from `/api/v1/employees`. Try to use same name to get the search results.
<br/>
**The data you can see from `/api/v1/employees` is come from the redis server.**
<br/>
If you wanna search, `/api/v1/employees?search=saif` where `saif` is the searching data what you will search.
<br/>

GOTO `redisio/users/services` to read the redis search implementation.
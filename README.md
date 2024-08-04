# flask-basic-workshop
A simple flask webapp with signup, login, posting and commenting capability.

MysqlDB container creation command:
```terminal
docker run -d --name mysql-container -e MYSQL_ROOT_PASSWORD=my-secret-pw -e MYSQL_DATABASE=mydatabase -e MYSQL_USER=myuser -e MYSQL_PASSWORD=mypassword -p 3310:3306 mysql:latest
```

Dependency Installation commands:
```terminal
pip install Flask mysql-connector-python

pip install flask flask-sqlalchemy flask-wtf pymysql

```

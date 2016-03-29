sudo service mysql start
mysql -uroot -e "create database qa"
mysql -uroot -e "create user 'box'@'localhost' IDENTIFIED BY '1234'"
mysql -uroot -e "GRANT ALL PRIVILEGES ON qa.* TO 'box'@'localhost'"

python ./manage.py syncdb
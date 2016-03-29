sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -f /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo gunicorn -b 0.0.0.0:8080 hello:app -D

sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo rm -f /etc/gunicorn/sites-enabled/default
sudo /etc/init.d/gunicorn restart 

#sudo gunicorn -c /home/box/web/etc/gunicorn.conf ask.wsgi -D
#ask>sudo gunicorn --bind 0.0.0.0:8000 ask.wsgi:application

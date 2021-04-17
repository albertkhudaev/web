sudo apt update
sudo apt install python3.5 
sudo rm /usr/bin/python3   
sudo ln -s /usr/bin/python3.5 /usr/bin/python3 
sudo pip3 install gunicorn 
sudo pip3 install django==2.1  
sudo unlink /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
cd ../ask
gunicorn --bind='0.0.0.0:8000' ask.wsgi:application

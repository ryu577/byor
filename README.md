To get setup with the frameworks and libraries - 

pip install django
pip install django-bootstrap3
pip install django-datetime-widget
pip install django-jquery
pip install django-cuser
#Might not be needed: pip install mysql-client
pip install django-username-email --pre
pip install bcrypt

Go here - http://stackoverflow.com/questions/1972259/cannot-open-include-file-config-win-h-no-such-file-or-directory-while-inst and see comment on third answer.
This says - "To solve the issue I copied the directory C:\Program Files\MySQL\MySQL Connector C 6.0.2\ to C:\Program Files (x86)\MySQL\MySQL Connector C 6.0.2\. This solved the issue for me"

Then - 
pip install MySQL-python


On Ubuntu - 
All above pip commands (run as sudo)

sudo apt-get install mysql
sudo apt-get install python-mysqldb
pip install MySQL-python

Start MySQL:
sudo mysql -u root -p

Run command - 
GRANT ALL PRIVILEGES ON * . * TO 'byoradmin'@'localhost';



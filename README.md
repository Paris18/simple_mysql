# simple_mysql
simle project for login n register using django


step1 : create virtualenv in your system using command
        
        virtualenv 'env_name'   (virtual env should be installed)
step2 : run requirements.txt(inside project) file to create supporting environments
        
        pip install -r requirements.txt
step3 : create SIMPLE_DB mysql database in your system using shell
        
step4 :run project by
       
       python manage.py makemigrations (to find the changes to db)
       python manage.py migrate  (appy the changes to db)
       python manage.py runserver 

step 5 :checking output online

        --> http://127.0.0.1:8007/app1/register
        it will open the register page register the user first
        -->http://127.0.0.1:8007/app1/usrs
        it will print list of registered user 
        press on user name one who you want to find it will print deatails


in settings.py you need to change your db 'USERNAME' and 'PASSWORD'

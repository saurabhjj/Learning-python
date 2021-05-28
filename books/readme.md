Install Django :                                                    pip install Django
create a new django env :                                           python3 -m venv <environment name>
enter django virtual env:                                           source /<env name>/bin/activate
check django version :                                              django-admin --version
start a new project :                                               django-admin startproject <project name>
start python server :                                               python3 manage.py runserver
server on a different port:                                         python3 manage.py runserver <port number>
update changes to a table:                                          python3 manage.py makemigrations
push the updates on table:                                          python3 manage.py migrate 
Connect to pythin shell:                                            python3 manage.py shell
connect to a D from shell:                                          from books.models import Book ----- from <appname>.models import <table name>
get all objects from table:                                         Book.objects.all() --- <tablename>.objects.all()
insert data into table:                                             newbook=Book(title="My First Book")
                                                                    newbook.save()

get a single object from DB:                                        Book.objects.get(pk=1) ---- this based on primary key
get a single object based on where:                                 Book.objects.filter(<columnName>=<condition>) 
delete all the data from a table:                                   python3 manage.py flush
create super user:                                                  python3 manage.py createsuperuser
to override the default names in the DB:                            override the ___str__ function
print to console:                                                   print("Hello World")
for deployment, please look at deploy.md
to view the list of installed dependencies :                        pip freeze
to write the list of installed dependencies to a file:              pip freeze > <filename>

# machine-learning
- django usage
  - python
  - Pycharm project
  - django web based
    - sudo pip instal django
    - django-admin startproject test_server
    - python manage.py runserver 8080
      - generate app: python manage.py startapp myapp
      - add template and static folder
    - python manage.py makeimgrations
    - python manage.py mgrate
    
- movie recommend system
  - django-admin startproject server_movierecsys
  - python manage.py startapp books_recsys_app
  - python manage.py createsuperuser (admin/admin)
  - python manage.py runserver
  - apply model to database 
    - python manage.py makemigreations
    - python manage.py migrate
    
  - python manage.py get_plotsfromtitles --input=utilitymatrix.csv --outputplots=plots.csv --outputumatrix='umatrix.csv'
    - get movie description(plot) from http://www.omdbapi.com using movie title included utilitymatrix file, as getplotfromomdb function
    - using python module-requests
    - saved outputmatrix as utility matrix and csv file with outputplots

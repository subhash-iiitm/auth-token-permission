# DjangoRolePermissionTokenAuthorisation
Basic Role permission based token system authorisation for django.

##Installation
```pip install django-auth-token-permission```

or 

Download from https://pypi.python.org/pypi/django-auth-token-permission/0.1 and run ```python setup.py install```


##Usage
Six Tables are used to maintain this token based role permission authorisation system.

Run makemigrations to make the migration script and then migrate to create the desired tables.


##Endpoint
```/login```  ```POST -> username,password```
```/logout```   ```POST -> username,name,email,password```
```/register```   ```POST``` ```Header:{'x-csrf-token':token}```



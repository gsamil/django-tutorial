## 1. Install (Windows)

Create a virtual Python environment:
```
py -m venv django-env
.\django-env\Scripts\activate
pip install django==2.1.5
mkdir src
cd ./src
```

Create a project and start the server:

```
django-admin startproject best_django_project_ever .
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser
python manage.py startapp products
```

After adding an app to settings or changing the models.py file:
```
python manage.py makemigrations
python manage.py migrate
```

## 2. Run

Add product to database from shell

- start shell:
```
python manage.py shell
```

- add new product:

```python
from products.models import Product
Prodcut.objects.all()
Product.objects.create(title='t1',description='d1', price=2.33,summary='s1')
```

Change a field in the defined model:
- delete all files under migrations folder and db file 
- create the superuse again after modifications




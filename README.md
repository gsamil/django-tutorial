## 1. Install (Windows)

##### Create a virtual Python environment:
```
py -m venv django-env
.\django-env\Scripts\activate
pip install django==2.1.5
mkdir src
cd ./src
```

## 2. Run

##### Create a project and start the server:

```
django-admin startproject best_django_project_ever .
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser
```
##### Create new app
```
python manage.py startapp products
```
Add products to ``setting.py -> INSTALLED_APPS``

After adding an app to settings or changing the ``models.py`` file:
```
python manage.py makemigrations
python manage.py migrate
```

Add product to database from shell

- start shell wtih ``python manage.py shell``

- add new product:

```python
from products.models import Product
Prodcut.objects.all()
Product.objects.create(title='t1',description='d1', price=2.33,summary='s1')
```

## 3. Changing Model

Change a field in the defined model:
- delete all files under migrations folder and db file 
- create the superuser again after modifications

## Custom Homepage / URL Routing and Requests

- Create a app named pages.
- modify the ``views.py``
- Then go to ``url.py`` (it was set in ``settings.py -> ROOT_URLCONF``)

#### Modify page with Django template / inheritance

- render an html template, define it as a page. 
- Created a templates folder under src, define it under ``settings -> TEMPLATES``
- inheritance allows us to remove redundant code

#### Template Context and Conditions

see ``about.html`` and ``pages/views.py`` for template context example usage of  context and conditions

#### Template Tags and Filters

- [built-in tags](https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#built-in-tag-reference)
- [built-in filters](https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#built-in-filter-reference)
- generally we want to deal with this work in view.

#### Render data from Database

- start shell under src
```python
from produts.models import Product
obj = Product.objects.get(id=1)
dir(obj)
```

- see ``products/views.py -> product_detail_view``

#### Django Templates with Apps

- main templates folder overrides the templates folders under apps


## 4. Django Model Forms

- Create  ``forms.py`` file under ``products``

#### Raw HTML Form

- Data from POST method can be used in the backend as in ``products.view.product_create_view_raw_html()``

#### Pure Django Form

- [Django Form Fields](https://docs.djangoproject.com/en/3.1/ref/forms/fields/)
- Django forms do validations automatically.
- See ``products.forms.RawProductForm``

#### Form Widgets

- [Widgets](https://docs.djangoproject.com/en/3.1/ref/forms/widgets/)
- if you want a field not to be required : ``forms.CharField(required=False)`` (Default is ``True``.)
- Initial value ``forms.DecimaField(initial=5.4)``
- ``forms.CharField(label='')``
- See ``products -> forms.py`` for more.

#### Form Validation Methods

- See ``products.forms.ProductForm.clean_title()``

#### Initial Values for Forms

- See ``products.views.render_initial_data()``

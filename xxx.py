import os
import sys
import django

sys.path.append(r'D:\Python Code\CRM')

os.chdir(r'D:\Python Code\CRM')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CRM.settings")
django.setup()

from app03 import models

customer_obj_list = models.Customer.objects.all()
print('未完成')

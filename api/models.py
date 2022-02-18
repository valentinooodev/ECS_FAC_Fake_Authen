from django.db import models


class LoginModel(models.Model):
    user_id = models.CharField(max_length=4)
    user_name = models.CharField(max_length=50)
    token = models.CharField(max_length=200)

    class Meta:
        db_table = 'login_tbl'


from django.db import models

# if there is problem in 'migrate' command then , delete all the initial.py files except __inti__.py and then run 'makemigration' and 'migrate' this will solve the problem

class registration(models.Model):
    gender_choice = (
        # 'this will store in database' ,'this will shows to user'
        ('M','Male'),
        ('F','Female')
    )
    name = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    country = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    fi_password = models.CharField(max_length=15)
    se_password = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10,choices=gender_choice,default='M')
    is_tick = models.BooleanField("I Agree To The Terms and Conditions",default=False)

    def __str__(self):
        return self.name


class blog(models.Model):
    u_email = models.EmailField()
    blog_text = models.CharField(max_length=5000)

    def __str__(self):
        return self.u_email
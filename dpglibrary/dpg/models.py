from django.db import models

# Create your models here.
class Contact(models.Model):
    con_id = models.AutoField
    con_name = models.CharField(max_length=25)
    con_email = models.CharField(max_length=40)
    con_phone = models.IntegerField()
    con_message = models.CharField(max_length=500)

    def __str__(self):
        return self.con_name

class ml_list(models.Model):
    ml_sno = models.IntegerField(default=0)
    ml_title = models.CharField(max_length=60)
    ml_desc = models.CharField(max_length=500)
    ml_img = models.ImageField(upload_to = "dpg/images",default="")
    ml_link = models.CharField(max_length=600)

    def __str__(self):
        return self.ml_title
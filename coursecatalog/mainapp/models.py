from django.db import models

# Course


class Course(models.Model):
    title=models.CharField(max_length=255, verbose_name="Назва курса")
    datestart=models.DateTimeField(verbose_name="Дата старта курса")
    dateend = models.DateTimeField(verbose_name="Дата конца курса")
    amount=models.DecimalField(max_digits=3,decimal_places=0,default=1,verbose_name="Количество лекций")

    def __str__(self):
        return self.title #Admin

class Catalog(models.Model):
    course = models.ForeignKey("Course",verbose_name='Каталог курсов',on_delete=models.CASCADE)

    def __str__(self):
        return "Каталог курсов" #Admin
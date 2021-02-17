from django.db import models

# Create your models here.
class TypeOfMeasurment(models.Model):
    measurment = models.CharField(verbose_name='вид измерения', max_length=64, unique=True)

    def __str__(self):
        return f'{self.measurment}'

class MeasuringInstrument(models.Model):
    STATUS_CHOICES = (
        ('in repair', 'В ремонте'),
        ('in work', 'В работе'),
        ('in verification', 'На поверке'),
        ('in calibration', 'На калибровке'),
        ('in storage', 'На хранении'),
    )
    name = models.CharField(verbose_name='наименование', max_length=128)
    typeofmeasurment = models.ForeignKey(TypeOfMeasurment, verbose_name='тип измерений', on_delete=models.CASCADE)
    state_register_number = models.CharField(verbose_name='ГРСИ', max_length=16)
    year = models.CharField(verbose_name='год выпуска', max_length=4, default=0)
    invertarian_number = models.CharField(verbose_name='инвертарный номер', max_length=6, default=0000)
    factory_number = models.CharField(verbose_name='заводской номер', max_length=16)
    owner = models.CharField(verbose_name='владелец', max_length=128)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='in_storage')

    def __str__(self):
        return f'{self.name}'
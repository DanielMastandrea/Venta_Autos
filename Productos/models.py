from django.db import models

class Autos(models.Model):
    brand = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    year = models.IntegerField()
    price = models.FloatField()
    description = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)
    stock = models.IntegerField()

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural = 'Autos'

class Motos(models.Model):
    brand = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    year = models.IntegerField()
    engine_cc = models.IntegerField()
    horses_hp = models.IntegerField()
    price = models.FloatField()
    description = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)
    stock = models.IntegerField()

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'Moto'
        verbose_name_plural = 'Motos'

class Ceros(models.Model):
    brand = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)
    stock = models.IntegerField()

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'Cero'
        verbose_name_plural = 'Ceros'                
from django.db import models

class Diak(models.Model):
    nev = models.CharField(max_length=255)
    jelszo = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Diák'
        verbose_name_plural = 'Diákok'

    def __str__(self):
        """Unicode representation of Kerdes."""
        return f"{self.nev}"
    
class Feladat(models.Model):
    feladat = models.CharField(max_length=255,)
    kie = models.CharField(max_length=255,null=True, default = None)
    kiesz = models.CharField(max_length=255,null=True, default = None)
    
    class Meta:
        verbose_name = 'Feladat'
        verbose_name_plural = 'Feladatok'

    def __str__(self):
        """Unicode representation of Kerdes."""
        return f"{self.feladat}"
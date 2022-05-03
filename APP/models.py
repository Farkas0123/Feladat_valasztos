from django.db import models
    
class Feladat(models.Model):
    feladat = models.CharField(max_length=255,)
    kie = models.CharField(max_length=255,null=True, default = None, blank=True)
    kiesz = models.CharField(max_length=255,null=True, default = None, blank=True)
    egyezzik = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Feladat'
        verbose_name_plural = 'Feladatok'

    def __str__(self):
        """Unicode representation of Kerdes."""
        return f"{self.feladat}"
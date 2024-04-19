from django.db import models

class CoreModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Region(CoreModel):
    TYPE = (
        ('shahar', 'shahar'),
        ('viloyat', 'viloyat'),
    )

    name = models.CharField(max_length=255)
    turi = models.CharField(max_length=20, choices=TYPE)

    class Meta:
        verbose_name = 'Viloyat'
        verbose_name_plural = 'Viloyatlar'

    def __str__(self):
        return self.name


class District(CoreModel):
    TYPE = (
        ('city', 'city'),
        ('district', 'district'),
    )

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'District'
        verbose_name_plural = 'Districts'

    def __str__(self):
        return self.name


class Faculty(CoreModel):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'

    def __str__(self):
        return self.name

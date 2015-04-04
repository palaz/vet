from django.db import models

# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    is_section = models.BooleanField(default=False, verbose_name='Consigli Vet')
    slug = models.SlugField(max_length=50, default='categoria')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorie'


class Page(models.Model):
    category = models.ForeignKey(Category, verbose_name='Categoria')
    name = models.CharField(max_length=100, verbose_name='Titolo')
    text = models.TextField(verbose_name='Testo')
    slug = models.SlugField(max_length=100, default='pagina')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Pagina'
        verbose_name_plural = 'Pagine'
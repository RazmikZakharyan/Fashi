from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse

class Departments(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('department', args=[str(self.slug)])

    class Meta:
        verbose_name_plural = "Departments"
        ordering = ["title"]

class Collection(models.Model):
    title = models.CharField(max_length=10)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('collection', args=[str(self.slug)])

    class Meta:
        ordering = ["title"]


class Brand(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ["title"]


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('category', args=[str(self.slug)])

    class Meta:
        ordering = ["title"]

class Tag(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('tag', args=[str(self.slug)])

    class Meta:
        ordering = ["title"]

class Size(models.Model):
    title = models.CharField(max_length=1)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ["title"]


class Color(models.Model):
    title = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ["title"]


class Product(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    availability = models.PositiveIntegerField(blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.FileField(blank=True)
    created_at = models.TimeField(auto_now_add=True)
    update = models.TimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    color = models.ManyToManyField(Color)
    size = models.ManyToManyField(Size, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    departments = models.ForeignKey(Departments, null=True, blank=True, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, null=True, blank=True, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return '{}:{}'.format(self.category, self.title)

    def get_absolute_url(self):
        return reverse('product', args=[str(self.slug)])

    def get_img(self):
        if not self.image:
            return '-'
        return self.image.url


    def photo(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % self.get_img())

    class Meta:
        ordering = ["created_at"]


class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='Photos/%Y/%d')

    def __str__(self):
        return self.product.title
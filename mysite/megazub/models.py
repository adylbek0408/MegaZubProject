from django.db import models


class CarouselItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class CategoryService(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Service(models.Model):
    category_service = models.ForeignKey(CategoryService, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    guarantee = models.TextField()
    is_promotion = models.BooleanField(default=False, null=True, blank=True)
    end_promotion = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class ServicePhotos(models.Model):
    image = models.ImageField(upload_to='images/')

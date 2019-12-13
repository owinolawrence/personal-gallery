from django.db import models

class Category(models.Model):
    category=models.CharField(max_length=40)
    def __str__(self):
        return self.category
    
    def delete_category(self):
            self.delete()
    def save_category(self):
            self.save()

    @classmethod
    def update(cls,id,name):
        category=Category.objects.filter(id=id)
        category.update(category=name)
        return category

    @classmethod
    def search_by_category(cls,search_term):
        news = cls.objects.filter(category__icontains=search_term)
        return Category

class Location(models.Model):
    city=models.CharField(max_length=50)
    def __str__(self):
        return self.city
    def save_location(self):
        self.save()
    def delete_location(self):
        self.delete()
    @classmethod
    def update (cls,id,name):
        location = Location.objects.filter(id=id)
        location.update(city=name)
        return location

class Image(models.Model):
    image = models.ImageField(upload_to = 'pictures/')
    name = models.CharField(max_length =40)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category,db_column='category')
    def save_image(self):
        self.save()
    @classmethod
    def get_all(cls):
        images = cls.objects.all()
        return images
    @classmethod
    def search_by_category(cls,search_term):
        image = cls.objects.filter(category__category__contains=search_term)
        return image
    @classmethod
    def update(cls,id,name):
        image=Image.objects.filter(id=id)
        image.update(name=name)
        return image
    def delete_image(self):
        self.delete()
    @classmethod
    def get_image_by_id(cls,id):
        image = Image.objects.get(id=id)
        return image
    @classmethod
    def filter_location(cls,fil):
        location_image=Image.objects.filter(location__city__icointain=fil)
        return location_image




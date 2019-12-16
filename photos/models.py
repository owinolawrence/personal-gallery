from django.db import models



class Location(models.Model):
    country=models.CharField(max_length=50)
    def __str__(self):
        return self.country
    def save_location(self):
        self.save()
    def delete_location(self):
        self.delete()
    @classmethod
    def update (cls,id,name):
        location = Location.objects.filter(id=id)
        location.update(country=name)
        return location
class Category(models.Model):
    category=models.CharField(max_length=50)
    def __str__(self):
        return self.category
    def save_category(self):
        self.save()
    def delete_category(self):
        self.delete()
    @classmethod
    def update(cls,id,name):
        category=Category.objects.filter(id=id)
        category.update(category=name)
        return category

    
class Image(models.Model):
    image = models.ImageField(upload_to ='pictures/')
    name = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category_item = models.ForeignKey(Category)

    @classmethod
    def display_photo(cls):
        photo=cls.objects.all()
        return photo
    def save_image(self):
        self.save()
    @classmethod
    def get_all(cls):
        images = cls.objects.all()
        return images
    @classmethod
    def search_by_category(cls,search_term):
        image = cls.objects.filter(category_item__category__icontains=search_term)
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
        location_image=Image.objects.filter(location__country__icointain=fil)
        return location_image

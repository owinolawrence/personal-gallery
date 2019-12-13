from django.db import models


class Location(models.Model):


    def save_location(self):
            self.save()

    def delete_location(self):
            self.save()

class Category(models.Model):

    def delete_category(self):
            self.save()
    def save_gategory(self):
            self.save()

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return photos



class Images(models.Model):
    def save_images(self):
        self.save()

    def delete_images(self):
        self.save()
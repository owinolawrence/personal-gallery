from django.db import models


class Location(models.Model):


    def save_location(self):
            self.save()

    def delete_location(self):
            self.save()

class Gategory(models.Model):

    def delete_gategory(self):
            self.save()
    def save_gategory(self):
            self.save()



class Images(models.Model):
    def save_images(self):
        self.save()

    def delete_images(self):
        self.save()
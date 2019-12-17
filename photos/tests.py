from django.test import TestCase

from .models import Category, Location,Image


class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Location(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

        #Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Location))


    # Testing Save Method
    def test_save_method(self):
        self.james.save_location()
        location = Location.objects.all()
        self.assertTrue(len(editors) > 0)

    def test_delete_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
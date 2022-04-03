from django.test import TestCase
from .models import UserSample
from .forms import ClassAndUserTestForm


# Create your tests here.
class MyTest(TestCase):
    def setUp(self):
        UserSample.objects.create(name="testname", desc="desc test")

    def test_user_sample_model(self):
        test1 = UserSample.objects.get(name="testname")
        self.assertEqual(test1.desc, "desc test")

    def test_user_test_form(self):
        model_obj = UserSample.objects.create(name="testname2", desc="desc test2")
        dict_set = {
            "name": model_obj.name,
            "desc": model_obj.desc
        }
        form = ClassAndUserTestForm(data=dict_set)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data.get('name'), model_obj.name)
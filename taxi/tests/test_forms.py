from django.test import TestCase
from django.urls import reverse_lazy

from taxi.forms import DriverCreationForm


class FormTests(TestCase):
    def test_user_creation_form_with_valid_data(self):
        form_data = {
            "username": "test_user",
            "password1": "gfdfd53g",
            "password2": "gfdfd53g",
            "first_name": "Andrew",
            "last_name": "Smith",
            "license_number": "XYZ98765",
        }
        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], form_data["username"])
        self.assertEqual(
            form.cleaned_data["first_name"], form_data["first_name"]
        )
        self.assertEqual(
            form.cleaned_data["last_name"], form_data["last_name"]
        )
        self.assertEqual(
            form.cleaned_data["license_number"], form_data["license_number"]
        )

    def test_user_creation_form_with_invalid_passwords(self):
        form_data = {
            "username": "test_user",
            "password1": "gfdfd53g",
            "password2": "differentPass456",
            "first_name": "Andrew",
            "last_name": "Smith",
            "license_number": "XYZ98765",
        }
        form = DriverCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)


class SearchTests(TestCase):

    def test_driver_search(self):
        data = {
            "username": "Ivan",
            "page": 1,
        }
        response = self.client.get(
            reverse_lazy("taxi:driver-list"), data, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "username")
        self.assertContains(response, "page")

    def test_car_search(self):
        data = {
            "model": "Sedan",
            "page": 1,
        }
        response = self.client.get(
            reverse_lazy("taxi:car-list"), data, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "model")
        self.assertContains(response, "page")

    def test_manufacturer_search(self):
        data = {
            "name": "BMW",
            "page": 1,
        }
        response = self.client.get(
            reverse_lazy("taxi:manufacturer-list"), data, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "name")
        self.assertContains(response, "page")

from django.test import TestCase
from .models import User, Product
from .forms import UserForm, ProductForm

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(name='User1', password='1')
        Product.objects.create(name='Bananas', price=10.25, user_id=user.id)

    def test_first_name_min_length(self):
        product = Product.objects.get(id=1)
        self.assertTrue(len(product.name)>=2)
        self.assertTrue(product.price>=0)
        self.assertEquals(product.user_id, 1)

class ProductFormTest(TestCase):
    def test_input_values(self):
        form_data = {'name': 'a', 'price': 10.25}
        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())

        form_data = {'name': 'ab', 'price': -10.25}
        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())

        form_data = {'name': 'ab', 'price': 10.25}
        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid())




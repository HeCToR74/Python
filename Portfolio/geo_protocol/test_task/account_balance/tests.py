from django.test import TestCase
from .models import Customer, Action

class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(name="Customer A", balance=10)
        Customer.objects.create(name="Customer B", balance=20)

    def test_customeres(self):
        customeres = Customer.objects.get()
        self.assertEqual(customeres, {"customeres": [{"name": "Customer A", "balance": 10},
                                                     {"name": "Customer B", "balance": 20}
                                                     ]
                                      })



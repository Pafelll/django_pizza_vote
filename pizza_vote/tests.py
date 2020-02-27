from django.test import TestCase
from pizza_vote.models import Vote, Pizza, Topping


class ToppingTest(TestCase):
    def create_topping(self, name='Jalapeno'):
        return Topping.objects.create(name=name)

    def test_create_topping(self):
        t = self.create_topping()
        self.assertTrue(isinstance(t, Topping))
        self.assertEqual(t.__str__(), t.name)


from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import RealEstate

class RealEstateTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user1 = get_user_model().objects.create_user(username='testuser1', password='password') 
        test_user1.save()

        test_real_estate = RealEstate.objects.create(owner=test_user1, name='Real Estate 1', address='123 Main St', city='San Diego', state='CA', zip_code=92101, description='Test description', price=100000, bedrooms=2, bathrooms=2, garage=1, sqft=1000, lot_size=1.0, photo_main='static/real_estate_app/images/real_estate_default.jpg', photo_1='static/real_estate_app/images/real_estate_default.jpg', photo_2='static/real_estate_app/images/real_estate_default.jpg', photo_3='static/real_estate_app/images/real_estate_default.jpg', contact_info='+1 (123) 456-7890')

        test_real_estate.save()

    def test_real_estate_content(self):
        realestate = RealEstate.objects.get(id=1)
        actual_owner = str(realestate.owner)
        actual_name = str(realestate.name)
        actual_address = str(realestate.address)
        actual_city = str(realestate.city)
        actual_state = str(realestate.state)
        actual_zip_code = str(realestate.zip_code)
        actual_description = str(realestate.description)
        actual_price = str(realestate.price)
        actual_bedrooms = str(realestate.bedrooms)
        actual_bathrooms = str(realestate.bathrooms)
        actual_garage = str(realestate.garage)
        actual_sqft = str(realestate.sqft)
        actual_lot_size = str(realestate.lot_size)
        actual_photo_main = str(realestate.photo_main)
        actual_photo_1 = str(realestate.photo_1)
        actual_photo_2 = str(realestate.photo_2)
        actual_photo_3 = str(realestate.photo_3)
        actual_contact_info = str(realestate.contact_info)
        self.assertEqual(actual_owner, 'testuser1')
        self.assertEqual(actual_name, 'Real Estate 1')
        self.assertEqual(actual_address, '123 Main St')
        self.assertEqual(actual_city, 'San Diego')
        self.assertEqual(actual_state, 'CA')
        self.assertEqual(actual_zip_code, '92101')
        self.assertEqual(actual_description, 'Test description')
        self.assertEqual(actual_price, '100000')
        self.assertEqual(actual_bedrooms, '2')
        self.assertEqual(actual_bathrooms, '2')
        self.assertEqual(actual_garage, '1')
        self.assertEqual(actual_sqft, '1000')
        self.assertEqual(actual_lot_size, '1.0')
        self.assertEqual(actual_photo_main, 'static/real_estate_app/images/real_estate_default.jpg')
        self.assertEqual(actual_photo_1, 'static/real_estate_app/images/real_estate_default.jpg')
        self.assertEqual(actual_photo_2, 'static/real_estate_app/images/real_estate_default.jpg')
        self.assertEqual(actual_photo_3, 'static/real_estate_app/images/real_estate_default.jpg')
        self.assertEqual(actual_contact_info, '+1 (123) 456-7890')

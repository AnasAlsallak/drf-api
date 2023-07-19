from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import RealEstate
from django.urls import reverse
from rest_framework import status

class RealEstateTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        test_user1 = get_user_model().objects.create_user(username='testuser1', password='password') 
        test_user1.save()

        test_real_estate = RealEstate.objects.create(owner=test_user1, name='Real Estate 1', address='123 Main St', city='San Diego', state='CA', zip_code=92101, description='Test description', price=100000, bedrooms=2, bathrooms=2, garage=1, sqft=1000, lot_size=1.0, photo_main='static/real_estate_app/images/real_estate_default.jpg', photo_1='static/real_estate_app/images/real_estate_default.jpg', photo_2='static/real_estate_app/images/real_estate_default.jpg', photo_3='static/real_estate_app/images/real_estate_default.jpg', contact_info='+1 (123) 456-7890')

        test_real_estate.save()

    def setUp(self):
        self.client.login(username="testuser1", password="password")

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

    def test_get_realestate_list(self):
        url = reverse("realestate_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        RealEstate = response.data
        self.assertEqual(len(RealEstate), 1)
        self.assertEqual(RealEstate[0]["name"], "Real Estate 1")

    def test_get_RealEstate_by_id(self):
        url = reverse("realestate_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        RealEstate = response.data
        self.assertEqual(RealEstate["name"], "Real Estate 1")

    def test_create_RealEstate(self):
        url = reverse("realestate_list")
        data = {"owner": 1, "name": "Real Estate 2", "description": "amazing"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        realestates = RealEstate.objects.all()
        self.assertEqual(len(realestates), 2)
        self.assertEqual(RealEstate.objects.get(id=2).name, "Real Estate 2")

    def test_update_RealEstate(self):
        url = reverse("realestate_detail", args=(1,))
        data = {
            "owner": 1,
            "name": "Real Estate 1",
            "description": "very amazing",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        realestate = RealEstate.objects.get(id=1)
        self.assertEqual(realestate.name, data["name"])
        self.assertEqual(realestate.owner.id, data["owner"])
        self.assertEqual(realestate.description, data["description"])

    def test_delete_realestate(self):
        url = reverse("realestate_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        realestates = RealEstate.objects.all()
        self.assertEqual(len(realestates), 0)

    def test_authentication_required(self):
        self.client.logout()
        url = reverse("realestate_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

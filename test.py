from django.test import TestCase, Client

from myfirm.models import Info, Section


client = Client()

class FunctionalTests(TestCase):
  
    def setUp(self):
        super().setUp()
        Info.objects.create(
            firm_name="Ponies R Us",
            social_description="Ponies!",
            url="https://ponies-r-us.com",
            phone="+1.000.000.0000",
            logo="logo.jpg",
            active=True,
        )
        Section.objects.create(
            published=True,
            title="We are the pony people",
            body="We specialize in cryptography, cryptozoology, petty theft, and luxury real estate.",
            link_text="Ponies",
        )
        Section.objects.create(
            published=True,
            title="Careers",
            body="Seeking Unicorns.",
            link_text="Careers",
            image="unicorns.jpg",
        )

    def test_get(self):
        resp = client.get("/")
        self.assertEqual(resp.status_code, 200)
 
    def test_404_unknown_url(self):
        resp = client.get("not-valid/")
        self.assertEqual(resp.status_code, 404)

    def test_just_one_active_info(self):
        with self.assertRaises(Exception):
            Info.objects.create(
                firm_name="ZombieCrypt II, LLC",
                social_description="From Deep in the Abyss!",
                url="https://zombies-r-us-ii.com",
                phone="+1.000.000.0001",
                logo="logo.jpg",
                active=True,
            )
        
    def test_contact(self):
        payload = {
            "contact_email": "meee@here.com",
            "subject": "Can I have a pony?",
            "body": "I really want a pony, can I have one? I WANT ONE NOW!!!",
        }   
        resp = client.post(
            "/",
            body=payload,
        )
        self.assertEqual(resp.status_code, 200) 

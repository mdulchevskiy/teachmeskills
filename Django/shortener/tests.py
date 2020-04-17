from django.test import TestCase
from shortener.models import Shortener
from django.utils import timezone


class ShortenerTestCase(TestCase):
    def setUp(self):
        Shortener.objects.create(
            long_url='https://www.youtube.com/',
            short_url='4FguE2',
            date=timezone.now(),
        )

    def test_create_and_delete(self):
        shorten_object_created = Shortener.objects.filter(id=1).first()
        Shortener.objects.filter(id=1).delete()
        shorten_object_deleted = Shortener.objects.filter(id=1).first()
        self.assertNotEqual(shorten_object_created, None)
        self.assertEqual(shorten_object_deleted, None)

    def test_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        response = self.client.post('/', {
            'long_url': 'http://www.bitly.com',
            'shortening_method': 'manual',
            'manual_shortening': 'dev',
        })
        created_object = Shortener.objects.filter(id=2).first()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(created_object.long_url, 'http://www.bitly.com')
        self.assertEqual(created_object.short_url, 'dev')

    def test_redirect(self):
        shorten_link = Shortener.objects.get(id=1).short_url
        response = self.client.get(f'/{shorten_link}')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], 'https://www.youtube.com/')

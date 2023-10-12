from django.test import SimpleTestCase

# Create your tests here.
class SimpleTest(SimpleTestCase):
    def test_todo(self):
        response = self.client.get('/api')
        self.assertEqual(response.status_code, 301)

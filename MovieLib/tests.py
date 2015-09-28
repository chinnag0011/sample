from django.test import TestCase
from django.utils import timezone
from MovieLib.models import Movie
from django.utils import unittest
# Create your tests here.

import datetime
from django.test import TestCase

'''class MovieViewsTestCase(TestCase):
    movie_1=0 
    def test_index(self):
        movie_1 = Movie.objects.create(
            title='Django?',
            genre='lang',
            release_date=timezone.now(),
            price='12'
         )

       
        resp = self.client.get('/MovieLib/')
       # self.assertEqual(resp.status_code, movie_1)
        self.assertTrue('latest_movie_list' in resp.context)
        self.assertEqual([Movie.pk for movie in resp.context['latest_movie_list']], [1]) '''


class MovieTestCase(TestCase):
     
      def test_create_movie(self, title="", genre="", price="0.0"):
          return Movie.objects.create(title=title, genre=genre, release_date=timezone.now(), price=price)

      def test_movie_creation(self):
          m = self.test_create_movie()
          self.assertTrue(isinstance(m, Movie))
          #self.assertEqual(m.title, 'Ram')
          m.save()

'''
    def setUp(self):
        Movie.objects.create(title="bhahubali", genre="action", release_date=10/07/2015)
    def test_movie(self):
        bhahubali = Movie.objects.get(name="bhahubali")
        resp = self.client.get('/MovieLib/')

        self.assertEqual(bhahubali, 'The bhahubali release on "10/07/2015"')


    def tearDown(self):
        self.Movie.quit

if __name__ == '__main__':
    unittest.main()


'''

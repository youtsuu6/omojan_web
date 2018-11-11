import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status

import logging

from game.models import Word


class WordTests(TestCase):

    def test_get(self):
        logger = logging.getLogger(__name__)

        data = {
            'name': 'テスト単語1',
        }

        Word.objects.create(**data)

        url = reverse('word-list')
        logger.info(url)
        response = self.client.get(url)
        logger.info(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [{
            'id': 1,
            'name': data['name'],
        }])

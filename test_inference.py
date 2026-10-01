import unittest
from unittest.mock import Mock, patch
from PIL import Image
import requests
from inference import predict, InferenceError

class InferenceTests(unittest.TestCase):
    def setUp(self):
        self.image = Image.new('RGB', (8, 8))
    def response(self, body, status=200):
        return Mock(status_code=status, ok=status == 200, json=Mock(return_value=body))
    @patch('inference.requests.post')
    def test_highest_confidence_not_first(self, post):
        post.return_value = self.response({'predictions': [{'class':'giraffe','confidence':.2}, {'class':'dog','confidence':.9}]})
        self.assertEqual(predict(self.image, 'test')[0]['class'], 'dog')
        self.assertEqual(post.call_args.kwargs['timeout'], (10,45))
    @patch('inference.requests.post')
    def test_missing_key_makes_no_request(self, post):
        with self.assertRaises(InferenceError): predict(self.image, None)
        post.assert_not_called()
    @patch('inference.requests.post')
    def test_timeout(self, post):
        post.side_effect=requests.Timeout()
        with self.assertRaisesRegex(InferenceError, 'timed out'): predict(self.image, 'test')
    @patch('inference.requests.post')
    def test_empty_detection_is_valid(self, post):
        post.return_value=self.response({'predictions':[]})
        self.assertEqual(predict(self.image,'test'),[])
    @patch('inference.requests.post')
    def test_reject_service_error_and_invalid_confidence(self, post):
        for body,status in [({},403), ({},500), ({'predictions':[{'class':'dog','confidence':2}]},200), ({'predictions':'invalid'},200)]:
            post.return_value=self.response(body,status)
            with self.assertRaises(InferenceError): predict(self.image,'test')
if __name__ == '__main__': unittest.main()

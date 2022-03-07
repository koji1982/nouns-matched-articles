from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve
from articles.tests.test_views import *


class ScenarioTest(TestCase):

    def test_user_open_eval_apply_result(self):
        #urlを指定してページを開く
        view = resolve('/')
        self.assertEqual(view.func, article_response)

        request = HttpRequest()
        function_response = view.func(request)
        actual_html = function_response.content.decode('utf8')

        expected_template = render_to_string('app/frame.html')

        self.assertEqual(function_response.status_code, REQUEST_OK)
        self.assertEqual(actual_html, expected_template)
        #最初のページで上から1番目と3番目の記事にgoodの評価をする

        #カテゴリーを国際に切り替える

        #2番目と3番目の記事にuninterestedの評価をする

        #反映ボタンを押す

        #結果のページを開く
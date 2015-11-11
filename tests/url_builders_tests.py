import unittest
import url_builders


class UrlBuildersTests(unittest.TestCase):
    def test_build_gif_url_when_there_is_no_search_term(self):
        self.assertEqual(url_builders.build_gif_url(None),
                         'http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC')

    def test_build_gif_url_with_a_search_term(self):
        self.assertEqual(url_builders.build_gif_url("fun"),
                         'http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=fun')


if __name__ == '__main__':
    unittest.main()

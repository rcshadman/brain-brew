import pytest

from brain_brew.utils import find_media_in_field


class TestFindMedia:
    @pytest.mark.parametrize("field_value, expected_results", [
        (r'<img src="image.png">', ["image.png"]),
        (r'<img src="image.png" >', ["image.png"]),
        (r'< img src="image.png">', ["image.png"]),
        (r'<     img src="image.png">', ["image.png"]),
        (r'<img class="myamainzingclass" src="image.png" >', ["image.png"]),
        (r'<img class=noquotesclass src="image.png" >', ["image.png"]),
        (r'<img src="image.png" class=classattheendforsomereason>', ["image.png"]),
        (r'words in the field <img src="image.png" > end other stuff', ["image.png"]),
        (r'<img src="ug-map-saint_barthelemy.png" />', ["ug-map-saint_barthelemy.png"]),
        (r'<img src="ug-map-saint_barthelemy.png" /><img src="image.png">',
            ["ug-map-saint_barthelemy.png", "image.png"]),
        (r'[sound:test.mp3]', ["test.mp3"]),
        (r'[sound:test.mp3][sound:othersound.mp3]', ["test.mp3", "othersound.mp3"]),
        (r'[sound:test.mp3]                       [sound:othersound.mp3]', ["test.mp3", "othersound.mp3"]),
        (r'words in the field [sound:test.mp3] other stuff too [sound:othersound.mp3] end', ["test.mp3", "othersound.mp3"]),
    ])
    def test_find_media_in_field(self, field_value, expected_results):
        assert find_media_in_field(field_value) == expected_results
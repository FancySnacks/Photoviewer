import pytest

from photov.util import is_image_file
from .mock_imagebrowser import MockImageBrowser


@pytest.fixture
def mock_directory() -> list[str]:
    return ["image.jpg", "photo.png", "test.jpeg", "anim.gif", "article.txt"]


@pytest.fixture
def mock_browser(mock_directory):
    browser = MockImageBrowser()
    browser.dir = mock_directory
    return browser


def test_load_only_images_from_directory(mock_directory):
    dir = mock_directory
    images = list(filter(is_image_file, dir))
    assert all([is_image_file(f) for f in images]) is True


def test_get_image_at_target_index(mock_browser):
    img = mock_browser.get_image_at(0)
    assert img != ""


def test_get_image_index(mock_browser):
    expected = 1
    path = mock_browser.images[1]
    id = mock_browser.get_image_index(path)
    assert id == expected


def test_get_next_image(mock_browser):
    target_image = mock_browser.images[1]
    next_image = mock_browser.next_image()
    assert next_image == target_image


def test_get_previous_image(mock_browser):
    target_image = mock_browser.images[2]
    mock_browser.current_image = mock_browser._images[0]
    prev_image = mock_browser.prev_image()
    assert prev_image == target_image


def test_get_previous_image_when_at_beginning(mock_browser):
    target_image = mock_browser.images[-1]
    prev_image = mock_browser.prev_image()
    assert prev_image == target_image

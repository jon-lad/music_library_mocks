import pytest
from unittest.mock import Mock
from lib.music_library import MusicLibrary

'''
On initalisation track_list is empty
'''
def test_on_intialisation_track_list_is_empty():
    music_library = MusicLibrary()

    actual = music_library.track_list

    expected = []

    assert actual == expected

'''
when searching for a track when no tracks added
throws error
'''
def test_search_with_no_tracks():
    music_library = MusicLibrary()

    actual = music_library.search("test")
    expected = []

    assert actual == expected

'''
when searching for a track that matches keyword
returns an instance of that track
'''
def test_search_returns_matching_track():
    music_library = MusicLibrary()

    matching_track_1 = Mock()
    matching_track_1.matches.return_value = True

    music_library.add(matching_track_1)

    actual = music_library.search("test")

    expected = [matching_track_1]

    assert actual == expected


'''
Test with multiple matching tracks
returns first match
'''
def test_search_returns_matching_track_with_multiple_tracks():
    music_library = MusicLibrary()

    matching_track_1 = Mock()
    matching_track_1.matches.return_value = True

    not_matching_track_1 = Mock()
    not_matching_track_1.matches.return_value = False

    not_matching_track_2 = Mock()
    not_matching_track_2.matches.return_value = False


    music_library.add(not_matching_track_1)
    music_library.add(matching_track_1)
    music_library.add(not_matching_track_2)

    actual = music_library.search("test")

    expected = [matching_track_1]

    assert actual == expected

'''
Test with no matching tracks
throws an error
'''
def test_search_returns_matching_track_with_no_tracks():
    music_library = MusicLibrary()

    not_matching_track_1 = Mock()
    not_matching_track_1.matches.return_value = False

    not_matching_track_2 = Mock()
    not_matching_track_2.matches.return_value = False


    music_library.add(not_matching_track_1)
    music_library.add(not_matching_track_2)

    actual = music_library.search("test")

    expected = []

    assert actual == expected

    '''
when searching for a track that matches keyword and several tracks which dont
returns an instance of that track
'''
def test_search_returns_matching_track_with_multiple_matching():
    music_library = MusicLibrary()

    matching_track_1 = Mock()
    matching_track_1.matches.return_value = True

    matching_track_2 = Mock()
    matching_track_2.matches.return_value = True

    not_matching_track_1 = Mock()
    not_matching_track_1.matches.return_value = False

    not_matching_track_2 = Mock()
    not_matching_track_2.matches.return_value = False


    music_library.add(not_matching_track_1)
    music_library.add(matching_track_1)
    music_library.add(not_matching_track_2)
    music_library.add(matching_track_2)

    actual = music_library.search("test")

    expected = [matching_track_1, matching_track_2]

    assert actual == expected

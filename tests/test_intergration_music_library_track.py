from lib.music_library import MusicLibrary
from lib.track import Track
import pytest

'''
when searching for a track that matches keyword
returns an instance of that track
'''
def test_search_returns_matching_track():
    music_library = MusicLibrary()

    track_1 = Track("Title", "Artist")

    music_library.add(track_1)

    actual = music_library.search("Title")

    expected = [track_1]

    assert actual == expected


'''
Test with multiple matching tracks
returns first match
'''
def test_search_returns_matching_track_with_multiple_tracks():
    music_library = MusicLibrary()

    track_1 = Track("Title 1", "Artist 1")
    track_2 = Track("Title 2", "Artist 2")
    track_3 = Track("Title 3", "Artist 3")


    music_library.add(track_2)
    music_library.add(track_1)
    music_library.add(track_3)

    actual = music_library.search("Artist 1")

    expected = [track_1]

    assert actual == expected

'''
Test with no matching tracks
throws an error
'''
def test_search_returns_matching_track_with_no_tracks():
    music_library = MusicLibrary()

    track_2 = Track("Title 1", "Artist 1")
    track_2 = Track("Title 2", "Artist 2")


    music_library.add(track_2)
    music_library.add(track_2)

    actual = music_library.search("test")

    expected = []

    assert actual == expected

    '''
when searching for a track that matches keyword and several tracks which dont
returns an instance of that track
'''
def test_search_returns_matching_track_with_multiple_matching():
    music_library = MusicLibrary()

    track_1 = Track("Title 1", "Artist 1")
    track_2 = Track("Title 2", "Artist 1")
    track_3 = Track("Title 3", "Artist 3")



    music_library.add(track_2)
    music_library.add(track_1)
    music_library.add(track_3)

    actual = music_library.search("Artist 1")

    expected = [track_2, track_1]

    assert actual == expected

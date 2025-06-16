from lib.track import Track

'''
Test on initalise
title is added to track
'''
def test_title_is_set_on_intialise():
    track = Track("Title", "Artist")

    actual = track.title

    expected = "Title"

    assert actual == expected

'''
Test on initalise
artist is added to track
'''
def test_artist_is_set_on_intialise():
    track = Track("Title", "Artist")

    actual = track.artist

    expected = "Artist"

    assert actual == expected

'''
Keyword matches title
retturns true
'''
def test_keyword_matches_title():
    track = Track("Title", "Artist")

    actual = track.matches("Title")

    expected = True

    assert actual == expected

'''
Keyword matches artist
retturns true
'''
def test_keyword_matches_artist():
    track = Track("Title", "Artist")

    actual = track.matches("Artist")

    expected = True

    assert actual == expected

    '''
Keyword matches neither
retturns false
'''
def test_keyword_matches_artist():
    track = Track("Title", "Artist")

    actual = track.matches("hello")

    expected = False

    assert actual == expected
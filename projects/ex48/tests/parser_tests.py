from nose.tools import assert_equal, assert_raises
from ex48 import parser, lexicon

word_list = lexicon.scan('north south west')
word_list2 = lexicon.scan('kill the bear')
word_list3 = word_list2[:]
word_list4 = lexicon.scan('from the kill')
word_list5 = lexicon.scan('from the door')
sentence = lexicon.scan('princess go north')
verb_list = lexicon.scan('go the in')


def test_word_list():
    assert_equal(word_list, [('direction', 'north'), ('direction', 'south'), ('direction', 'west')])


def test_verb_list():
    assert_equal(verb_list, [('verb', 'go'), ('stop', 'the'), ('stop', 'in')])


def test_peek():
    assert_equal(parser.peek(word_list), 'direction')


def test_match():
    word1 = parser.match(word_list2, 'verb')
    assert_equal(word_list2, [('stop', 'the'), ('noun', 'bear')])
    assert_equal(word1, ('verb', 'kill'))
    word2 = parser.match(word_list2, 'noun')
    assert_equal(word_list2, [('noun', 'bear')])
    assert_equal(word2, None)


def test_skip():
    parser.skip(word_list3, 'verb')
    assert_equal(word_list3, [('stop', 'the'), ('noun', 'bear')])


def test_parse_verb():
    word = parser.parse_verb(word_list4)
    assert_equal(word, ('verb', 'kill'))
    assert_raises(parser.ParserError, parser.parse_verb, word_list5)


def test_parse_object():
    word = parser.parse_object(word_list5)
    assert_equal(word, ('noun', 'door'))
    assert_raises(parser.ParserError, parser.parse_object, word_list4)


def test_parse_subject():
    word = parser.parse_subject(verb_list)
    assert_equal(word, ('noun', 'player'))
    assert_raises(parser.ParserError, parser.parse_subject, word_list)


def test_parse_sentence():
    sentence1 = parser.parse_sentence(sentence)
    assert_equal(sentence1.subject, 'princess')
    assert_equal(sentence1.verb, 'go')
    assert_equal(sentence1.object, 'north')
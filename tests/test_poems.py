from norn_dh.poems import Poem, PoemCollection

# Test for Poem class
class TestPoem:
    def test_poem_initialization(self):
        poem = Poem(
            dhlabid="123", urn="urn:123", title="Test Poem", page_start=1, 
            page_end=2, overlapp="yes", digital_visning="url", comment="Sample comment"
        )
        assert poem.dhlabid == "123"
        assert poem.urn == "urn:123"
        assert poem.title == "Test Poem"
        assert poem.page_start == 1
        assert poem.page_end == 2
        assert poem.overlapp == "yes"
        assert poem.digital_visning == "url"
        assert poem.comment == "Sample comment"
        assert poem.pages is None

    def test_poem_default_values(self):
        poem = Poem(urn="urn:123", title="Test Poem", page_start=1, 
                    page_end=2, overlapp="yes", digital_visning="url", comment="Sample comment")
        assert poem.dhlabid is None
        assert poem.pages is None

# Test for PoemCollection class
class TestPoemCollection:
    def test_poem_collection_initialization(self):
        poems = [Poem(urn="urn:123", title="Poem 1", page_start=1, 
                      page_end=2, overlapp="yes", digital_visning="url", comment="Comment 1")]
        collection = PoemCollection(
            poems=poems, urn="urn:coll", author="Author", title="Collection Title",
            year=2020, publisher="Publisher", publisher_place="Place"
        )
        assert len(collection.poems) == 1
        assert collection.urn == "urn:coll"
        assert collection.author == "Author"
        assert collection.title == "Collection Title"
        assert collection.year == 2020
        assert collection.publisher == "Publisher"
        assert collection.publisher_place == "Place"
        
    def test_collection_with_multiple_poems(self):
        poem1 = Poem(urn="urn:123", title="Poem 1", page_start=1, 
                     page_end=2, overlapp="yes", digital_visning="url", comment="Comment 1")
        poem2 = Poem(urn="urn:124", title="Poem 2", page_start=3, 
                     page_end=4, overlapp="no", digital_visning="url2", comment="Comment 2")
        collection = PoemCollection(
            poems=[poem1, poem2], urn="urn:coll", author="Author", title="Collection Title",
            year=2020, publisher="Publisher", publisher_place="Place"
        )
        assert len(collection.poems) == 2


from app.src.data_cleaning.emoji_cleaner import remove_emojis

expected_text = "This is a test"

def test_when_inputTextContainsEmoji_expect_emojiIsRemovedFromText():
    #Arrange
    sample_text = u'This is a test\U0001f602'
    
    #Act
    cleaned_text = remove_emojis(sample_text)
    
    #Assert
    assert expected_text == cleaned_text
    
    
def test_when_inputTextContainsNoEmoji_expect_inputTextToBeReturned():
    #Arrange
    sample_text = 'This is a test'
    
    #Act
    cleaned_text = remove_emojis(sample_text)
    
    #Assert
    assert expected_text == cleaned_text
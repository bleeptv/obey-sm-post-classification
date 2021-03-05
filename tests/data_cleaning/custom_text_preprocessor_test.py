from app.src.data_cleaning.custom_text_preprocessor import lemmatize_stemming, preprocess


def test_when_inputTextContainsAnEAtTheEnd_expect_inputTextToBeLemmatized():
    #Arrange
    input_text = "iPhone"
    expected_lemmatized_text = "iPhone"
    
    #Act
    actual_lemmatized_text = lemmatize_stemming(input_text)
    
    #Assert
    assert expected_lemmatized_text == actual_lemmatized_text
    
    
def test_when_inputTextContainsAnNoEAtTheEnd_expect_inputTextToBeStemmed():
    #Arrange
    input_text = "wolves"
    expected_stemmed_text = "wolv"
    
    #Act
    actual_stemmed_text = lemmatize_stemming(input_text)
    
    #Assert
    assert expected_stemmed_text == actual_stemmed_text


def test_when_inputTextContainsAStopWord_expext_stopWordToBeRemovedFromPreProcessedList():
    #Arrange
    input_text = "the newest town"
    expected_preprocced_list = ["newest", "town"]
    
    #Act
    actual_preprocessed_list = preprocess(input_text)
    
    #Assert
    assert expected_preprocced_list == actual_preprocessed_list
    

def test_when_inputTextContainsPunctuation_expext_outputListToStripOutPunctuation():
    #Arrange
    input_text = "That's not cool my ai rap brother. It's Abraham's laptop, right?"
    expected_preprocced_list = ["cool", "ai", "rap", "brother", "abraham", "laptop", "right"]
    
    #Act
    actual_preprocessed_list = preprocess(input_text)
    
    #Assert
    assert expected_preprocced_list == actual_preprocessed_list
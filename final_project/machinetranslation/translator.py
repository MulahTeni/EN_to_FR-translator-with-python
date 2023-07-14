"""
    IBM French - English Translator Project
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
        English to French
    """
    return MyMemoryTranslator(source='en-GB', target='fr-FR').translate(english_text)

def french_to_english(french_text):
    """
        French to English
    """
    return MyMemoryTranslator(source='fr-FR', target='en-GB').translate(french_text)

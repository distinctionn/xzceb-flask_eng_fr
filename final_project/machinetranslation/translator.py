"""
Module for language translation using IBM Watson Language Translator
"""

import os
from ibm_watson import LanguageTranslatorV3
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(
    version='2018-05-01', authenticator=authenticator)
translator.set_service_url(url)


def english_to_french(english_text):
    """
    Translates English text to French
    :param english_text: English text to translate
    :type english_text: str
    :return: Translated French text
    :rtype: str
    """
    response = translator.translate(
        text=english_text, source='en', target='fr').get_result()
    french_text = response['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """
    Translates French text to English
    :param french_text: French text to translate
    :type french_text: str
    :return: Translated French text
    :rtype: str
    """
    response = translator.translate(
        text=french_text, source='fr', target='en').get_result()
    english_text = response['translations'][0]['translation']
    return english_text

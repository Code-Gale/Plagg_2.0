from googletrans import Translator

def translate_text(text, source_lang, target_lang):
    translator = Translator()
    translation = translator.translate(text, src=source_lang, dest=target_lang)
    translated_text = translation.text
    return translated_text

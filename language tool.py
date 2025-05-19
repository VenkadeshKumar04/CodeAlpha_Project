from googletrans import Translator

def translate_text(text, src_lang='auto', target_lang='en'):
    translator = Translator()
    try:
        translated = translator.translate(text, src=src_lang, dest=target_lang)
        return translated.text
    except Exception as e:
        return f"Error: {e}"

input_text = "Bonjour tout le monde"
translated_text = translate_text(input_text, src_lang='fr', target_lang='en')
print(f"Original: {input_text}")
print(f"Translated: {translated_text}")

from googletrans import Translator
translator = Translator()
text = 'enter the language you want to detect'
curlang=translator.detect(text)
print(curlang)
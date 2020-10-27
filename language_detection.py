# google trans
from googletrans import Translator
translator = Translator()
text = 'enter the language you want to detect'
curlang=translator.detect(text)
print(curlang)

# quickest lang detect library
import cld3
print(cld3.get_language(text))

# best accuracy with indic languages
import langid
print(langid.classify(text))

# reference: https://stackoverflow.com/a/57349132

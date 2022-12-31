from googletrans import Translator #pip install googletrans==3.1.0a0

# 1 - Translation

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line, dest='en') # it can translate to any language just change the token in dest = 'token' like dest = 'hi'
    data = result.text
    return data






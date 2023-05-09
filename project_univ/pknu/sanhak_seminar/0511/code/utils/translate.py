ERROR_MESSAGE = "GOOGLE ERROR MESSAGE"

def translate_text(text, translater, src='en', dest='de'):
    result = translater.translate(text, src=src, dest=dest)
    return result.text
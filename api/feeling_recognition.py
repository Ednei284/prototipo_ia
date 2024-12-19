from textblob import TextBlob

def feeling_analiser(texto):
    blob = TextBlob(texto)
    sentimento = blob.sentiment
    if sentimento.polarity < 0.0:
        return 'negativo'  
    if sentimento.polarity > 0.0:          
        return 'positivo'
    if sentimento.polarity == 0.0:
        return 'neutro'
    



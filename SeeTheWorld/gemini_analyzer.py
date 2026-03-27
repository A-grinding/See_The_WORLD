from textblob import TextBlob
from collections import Counter
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords



def inferDoc(input, output):
    stop_words = [ 'stop', 'the', 'to', 'and', 'a', 'in', 'it', 'is', 'I', 'that', 'had', 'on', 'for', 'were', 'was']
    df = pd.read_csv(input)
    results = []
    
    for text in df['full_text']:
        words = re.findall(r'\b\w+\b', str(text).lower())
        filtered_words = [word for word in words if word not in stop_words and len(word)>2]
        blob = TextBlob(str(text))
        choice = blob.sentiment.polarity
        
        if choice > 0:
            feeling = "Positive"
        elif choice < 0: 
            feeling = "Negative"
        else:
            feeling = "Neutral"
        
        freq_word = Counter(filtered_words)
        if freq_word:
            keyword = freq_word.most_common(1)[0][0]
        else:
            keyword = ""
            
        results.append({
            "tweet" : text,
            "keyword" : keyword,
            "intentions" : feeling
        })
        

    results_df = pd.DataFrame(results)
    results_df.to_csv(output, index=False)
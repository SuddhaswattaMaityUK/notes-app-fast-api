from app.repository.note_repo import NoteRepository
from fastapi import Depends
from textblob import TextBlob

class SentimentAnalysisService:
    def __init__(self):
        pass
    
    async def analyze_sentiment(self, content:str) -> dict:

        sentiment_dict= {
            'mood': 'Neutral',
            'opinion': 'Neutral',
            'text': 'Nothing to analyze'
        }

        if content is None:
            return sentiment_dict      
        
        sentiment_dict['text'] = content
        
        text = content
        testimonial = TextBlob(text)
        polarity, subjectivity = testimonial.sentiment

        print("Polarity:", polarity)
        print("Subjectivity:", subjectivity)

        if subjectivity < 0.5:
            sentiment_dict['opinion'] = "Factual"
        else:   
            sentiment_dict['opinion'] = "Personal Opinion"
        
        
        if polarity > 0:
            sentiment_dict['mood'] = "Positive"
        elif polarity < 0:
            sentiment_dict['mood'] = "Negative"

        
        
        return sentiment_dict

    
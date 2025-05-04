
import pytest
from app.service.ml_service import SentimentAnalysisService

@pytest.fixture
def ml_service():
    # Setup code for ML service
    service = SentimentAnalysisService()
    yield service
    # Teardown code if needed

@pytest.mark.asyncio
async def test_sentiment_analysis_service(ml_service):
    # Test sentiment analysis service
    text = "I love programming!"
    result = await ml_service.analyze_sentiment(text)
    assert result is not None
    assert isinstance(result, dict)
    assert result.get('mood') == "Positive"
   
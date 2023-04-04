pip install tensorflow
pip install -q transformers

from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis")
data = ["I love my boyfriend", "I hate people for gossip"]
sentiment_pipeline(data)
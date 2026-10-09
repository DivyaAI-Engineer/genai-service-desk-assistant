from app.classifier import TicketClassifier
from app.summarizer import IncidentSummarizer


classifier = TicketClassifier()

classifier.train(
    "data/incidents.csv"
)

summarizer = IncidentSummarizer()

ticket = """
Customer cannot connect to VPN.
Password was recently reset.
Investigation required.
"""

category = classifier.predict(ticket)

summary = summarizer.summarize(ticket)

print("\nIncident Analysis")
print("------------------")
print("Category:", category)
print("Summary:", summary)

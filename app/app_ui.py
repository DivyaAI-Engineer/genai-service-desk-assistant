import streamlit as st

from classifier import TicketClassifier


classifier = TicketClassifier()

classifier.train(
    "../data/incidents.csv"
)

st.title(
    "AI Incident Classifier"
)

ticket = st.text_area(
    "Enter Incident Description"
)

if st.button("Classify"):

    category = classifier.predict(ticket)

    st.success
  (
        f"Predicted Category: {category}"
    )

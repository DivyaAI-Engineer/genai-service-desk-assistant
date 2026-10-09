class IncidentSummarizer:

    def summarize(self, text):

        sentences = text.split(".")

        return ".".join(sentences[:2])

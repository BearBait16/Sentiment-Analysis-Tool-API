import json
import polars as pl
from lets_plot import *

LetsPlot.setup_html()   # correct object name

ids = []
sentiments = []

# Use raw string for Windows path
with open(r"Backend\hamburger_hut_reviews_sentiment.json", "r") as file:
    data = json.load(file)

    for review_id, results in data.items():
        y = results[0]["label"]
        x = review_id

        if x is not None and y is not None:
            ids.append(x)
            sentiments.append(y)

# Create dataframe
df = pl.DataFrame({
    "ID": ids,
    "Sentiments": sentiments
})

# Count occurrences
counts = df.group_by("Sentiments").len().rename({"len": "Counts"})

# Create plot
plot = (
    ggplot(counts, aes(x="Sentiments", y="Counts"))
    + geom_bar()
    + ggtitle("Sentiment Distribution")
)

# Save image
ggsave(plot, "Sentiments.png", scale=2)
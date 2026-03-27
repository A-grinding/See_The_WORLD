library(ggplot2)

data <- read.csv("analyzed_tweets.csv")

png("sentiment_distribution.png", width=800, height=500)

ggplot(data, aes(x = keyword, fill = intentions)) +
  geom_bar(stat = "count") +
  labs(
    title = "Sentiment Distribution by Keyword",
    x = "Keyword",
    y = "Count"
  ) +
  theme_minimal()

dev.off()
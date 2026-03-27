library(ggplot2)

data <- read.csv("analyzed_tweets.csv")

plot1 <- ggplot(data, aes(x = sentiment,)) + geom_bar() + ggtitle("Sentiment Analysis")

ggsave("sentiment_analysis_plot.png", plot = plot1)
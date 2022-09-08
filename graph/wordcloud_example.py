import random
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud, STOPWORDS


# Using custom colors
def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)


df = pd.read_csv(r"../assets/data/db_codigoml-400mil-21-12-22.csv", encoding="latin-1")
comment_words, stopwords = '', set(STOPWORDS)
stopwords_br = {'de', 'para', 'com', 'lampada'}

for val in df.description:
    val = str(val)  # Typecaste each val to string
    tokens = val.split()  # split the value

    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()  # Converts each token into lowercase

    comment_words += " ".join(tokens) + " "

# WordCloud for Python documentation: https://amueller.github.io/word_cloud/index.html
wc = WordCloud(width=800, height=800, background_color='white', stopwords=stopwords_br, min_font_size=10)
wc.generate(comment_words)
default_colors = wc.to_array()

# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)

# Using custom colors
plt.title("Custom colors")
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3), interpolation="bilinear")
wc.to_file("grey_color.png")
plt.axis("off")

# Using default colors
plt.title("Default colors")
plt.imshow(default_colors, interpolation="bilinear")
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()

from bnlp.corpus import stopwords
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



file = './data/train_generic_small.csv'
df = pd.read_csv(file, encoding='utf-8')
print(df.head(10))

# plot the log of label frequency of a dataframe
# df: dataframe
# label: label column name
# title: title of the plot
# save: save the plot to a file
def plot_log_label_frequency(df, label, title, save=False):
  plt.figure(figsize=(16, 5))
  ax = sns.countplot(x=label, data=df)
  # plt.yscale('log')
  ax.set(yscale="log")
  plt.title(title)
  # plt.show()
  if save: plt.savefig("eda/" + title + '.png')

plot_log_label_frequency(df, 'tag', 'Log Label Frequency', True)


# find top 15 most frequent words from df
# df: dataframe
# label: label column name
# title: title of the plot
# save: save the plot to a file
def plot_top_15_words(df, label, title, save=False):
  plt.figure(figsize=(16, 5))
  plt.rc('font', family='Nirmala UI')
  ax = sns.countplot(x=label, data=df, order=df[label].value_counts().iloc[:15].index)
  plt.title(title)
  # plt.show()
  if save: plt.savefig("eda/" + title + '.png')

plot_top_15_words(df, 'word', 'Top 15 Most Frequent Words', True)

# find top 15 most frequent words from df that are not in the stopword list
# df: dataframe
# label: label column name
# title: title of the plot
# save: save the plot to a file
def plot_top_15_words_without_stopwords(df, label, title, save=False):
  plt.figure(figsize=(16, 5))
  plt.rc('font', family='Nirmala UI')
  df = df[~df[label].isin(stopwords)]
  ax = sns.countplot(x=label, data=df, order=df[label].value_counts().iloc[:15].index)
  plt.title(title)
  # plt.show()
  if save: plt.savefig("eda/" + title + '.png')

plot_top_15_words_without_stopwords(df, 'word', 'Top 15 Most Frequent Words Without Stopwords', True)


# plot sentence length distribution from df where sentence id is given
# df: dataframe
# sentence_id: sentence id column name
# title: title of the plot
# save: save the plot to a file
def plot_sentence_length_distribution(df, sentence_id, title, save=False):
  plt.figure(figsize=(16, 5))
  df['sentence_len'] = df.groupby(sentence_id)[sentence_id].transform('count')
  ax = sns.countplot(x='sentence_len', data=df)
  plt.title(title)
  # plt.show()
  if save: plt.savefig("eda/" + title + '.png')

plot_sentence_length_distribution(df, 'sentence_id', 'Sentence Length Distribution By Word', True)


# plot the average word length distribution from df where word is given
# df: dataframe
# word: word column name
# title: title of the plot
# save: save the plot to a file
def plot_average_word_length_distribution(df, word, title, save=False):
  plt.figure(figsize=(16, 5))
  df['word_len'] = df[word].str.len()
  ax = sns.distplot(df['word_len'], kde_kws={'bw':1})
  plt.title(title)
  # plt.show()
  if save: plt.savefig("eda/" + title + '.png')

plot_average_word_length_distribution(df, 'word', 'Average Word Length Distribution', True)
  


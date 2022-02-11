import numpy as np
import pandas as pd
import seaborn as sns
from fitter import Fitter, get_common_distributions, get_distributions
import matplotlib.pyplot as plt

data_path = "../data/bug-fix-commit-message.csv"
col_list = [0]
dataset = pd.read_csv(data_path, usecols=col_list)
# dataset.head()
# dataset.info()
sns.set_style('white')
sns.set_context("paper", font_scale=2)
sns.displot(dataset, x="carat")
plt.show()

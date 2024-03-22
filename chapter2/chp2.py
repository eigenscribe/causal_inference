import numpy as np
from scipy import stats
from colors import bcolors as bc


from bookstore_associations import *
scm = BookSCM(random_seed=45) # instantiate SCM
  buy_book_a, buy_book_b = scm.sample(100) # sample 100 samples from SCM
  buy_book_a.shape, buy_book_b.shape # check whether the shapes are as expected

  proba_book_a_given_book_b = buy_book_a[buy_book_b].sum() / buy_book_a[buy_book_b].shape[0]
  print(f"Probability of buying book A given book B: {proba_book_a_given_book_b:0.3f}\n\n")

print(f"✨✨ Mean and Variance of B before vs. after Intervention on A ✨✨")
print()
from bookstore_interventions1 import *

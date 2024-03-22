import numpy as np
from scipy import stats
from colors import bcolors as bc


from bookstore_associations import *
scm = BookSCM(random_seed=45) # instantiate SCM
  buy_book_a, buy_book_b = scm.sample(100) # sample 100 samples from SCM
  buy_book_a.shape, buy_book_b.shape # check whether the shapes are as expected

  proba_book_a_given_book_b = buy_book_a[buy_book_b].sum() / buy_book_a[buy_book_b].shape[0]
  print(f"Probability of buying book A given book B: {proba_book_a_given_book_b:0.3f}\n\n")

#bookstore_interventions
print(f"✨✨ Mean and Variance of B before vs. after Intervention on A ✨✨")
SAMPLE_SIZE = 100
np.random.seed(45)

u_0 = np.random.randn(SAMPLE_SIZE)
u_1 = np.random.randn(SAMPLE_SIZE)

a = u_0
b = 5 * a + u_1

r, p = stats.pearsonr(a,b)
print(f"Mean of B before any intervention: {bc.PURPLE}{b.mean():0.3f}{bc.ENDC}")
print(f"Variance of B before any intervention: {bc.BLUE}{b.var():0.3f}{bc.ENDC}")
print(f"Correlation between A and B:\n{bc.OKCYAN}r = {r:0.3f}{bc.ENDC}; {bc.OKGREEN}p = {p:0.3f}{bc.ENDC}\n")

# Intervene on A by fixing its value to 1.5
a = np.array([1.5] * SAMPLE_SIZE)
b = 5 * a + u_1

print(f"Mean of B after intervention on A: {bc.PURPLE}{b.mean():0.3f}{bc.ENDC}")
print(f"Variance of B after intervention on A: {bc.BLUE}{b.var():03f}{bc.ENDC}\n")

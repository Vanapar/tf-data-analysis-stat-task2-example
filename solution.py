import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1028110554 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    a1 = pow((1 - p) / 2, 1 / x.size())
    a2 = pow((1 + p) / 2, 1 / x.size())
    max = x.max()
    return (max - 0.074) / a2 + 0.074, (max - 0.074) / a1 + 0.074

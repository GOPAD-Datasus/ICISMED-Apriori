import pandas as pd

from dev import preprocess, apply_apriori, postprocess


if __name__ == '__main__':
    pd.options.mode.copy_on_write = True

    n_cluster = preprocess()
    apply_apriori(n_cluster)
    postprocess(n_cluster)
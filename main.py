from dev import preprocess, apply_apriori, postprocess


if __name__ == "__main__":
    n_cluster = preprocess()
    apply_apriori(n_cluster)
    postprocess(n_cluster)

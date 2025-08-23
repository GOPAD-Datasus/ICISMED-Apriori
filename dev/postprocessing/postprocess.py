from .clear_rules import filter_redundant_rules, clear_str


def postprocess(n_cluster: int) -> None:
    list_inter = [f'data/intermediate/rules_{i}.csv'
                  for i in range(n_cluster)]

    for file, i in zip(list_inter, range(n_cluster)):
        df_filtered = filter_redundant_rules(file)

        df_filtered['antecedents'] = \
            df_filtered['antecedents'].apply(clear_str)
        df_filtered['consequents'] = \
            df_filtered['consequents'].apply(clear_str)

        final_path = f'data/final/frules_{i}.csv'
        df_filtered.to_csv(final_path, index=False)

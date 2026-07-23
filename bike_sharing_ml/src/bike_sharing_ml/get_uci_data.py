from ucimlrepo import fetch_ucirepo
import pandas as pd

def get_uci_data(id: int) -> pd.DataFrame:
    uci_df = fetch_ucirepo(id)

    return uci_df.data.original
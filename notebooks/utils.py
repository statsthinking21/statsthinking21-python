import pandas as pd
import numpy as np


def threshold_df_correlation(df, thresh=0.3, 
                             use_absolute_corr=True, show_corrs=True):
    """
    return correlations in a data frame that exceed a particular threshold
    """
    cc = df.corr()
    if use_absolute_corr:
        cc = np.abs(cc)
    cc_exceeds_thresh = np.where(cc > thresh)
    exceedence = pd.DataFrame()
    for variable_idx in range(len(cc_exceeds_thresh[0])):
        row = cc_exceeds_thresh[0][variable_idx]
        col = cc_exceeds_thresh[1][variable_idx]
        if row == col:
            continue
        exceedence.loc[variable_idx, 'rowvar'] = cc.index[row]
        exceedence.loc[variable_idx, 'colvar'] = cc.index[col]
        exceedence.loc[variable_idx, 'corr'] = cc.iloc[row, col]
    if show_corrs:
        with pd.option_context('display.max_rows', None):
            print(exceedence)

    return(exceedence)

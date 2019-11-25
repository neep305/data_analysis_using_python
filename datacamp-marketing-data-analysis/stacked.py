import numpy as np
import pandas as pd


def stacked():
    mul_index = pd.MultiIndex.from_tuples([('cust_1','2015'),('cust_1','2016'),('cust_2','2015'),('cust_2','2016')])

    data = pd.DataFrame(data=np.arange(16).reshape(4,4),
                        index=mul_index,
                        columns=['prd_1','prd_2','prd_3','prd_4'],
                        dtype='int')

    print('============<< multi-index >>===========')
    print(data)

    return data


if __name__ == '__main__':
    data = stacked()
    data_stacked = stacked().stack()
    print('\n============<< stacked data >>===========')
    print(data_stacked)

    # print(data_stack.index)

    print(data_stacked['cust_2']['2015'][['prd_1', 'prd_2']])

    # Nan to DataFrame
    data.loc['cust_2', 'prd_4'] = np.nan
    print(data)

    # stack with 'dropna=False'
    print('\n============<< data having NaN >>===========')
    print(data.stack(dropna=False))

    # stack with 'dropna=True'
    print('\n============<< data not having NaN >>===========')
    print(data.stack(dropna=True))

    print('\n============<< unstack level=-1 >>===========')
    print(data_stacked.unstack(level=-1))

    print('\n============<< unstack level=0 >>===========')
    print(data_stacked.unstack(level=0))

    print('\n============<< unstack level=1 >>===========')
    print(data_stacked.unstack(level=1))

    # converting Series to DataFrame
    data_stacked_unstacked = data_stacked.unstack(level=-1)
    print('\n============<< data_stacked.unstack >>===========')
    print(data_stacked_unstacked)

    # converting index to columns
    data_stacked_unstacked_df = data_stacked_unstacked.reset_index()
    print('\n============<< data_stacked_unstacked_df >>===========')
    print(data_stacked_unstacked_df)

    # changing columns' name
    print('\n============<< data_stacked_unstacked_df renaming columns >>===========')
    # data_stacked_unstacked_df = data_stacked_unstacked_df.rename(columns={'level_0': 'customer_id', 'level_1': 'year'}, inplace=True)
    print(data_stacked_unstacked_df.rename(columns={'prd_1': '상품'}))

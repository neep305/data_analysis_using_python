import numpy as np
import pandas as pd


def stacked():
    mul_index = pd.MultiIndex.from_tuples([('cust1','2015'),('cust1','2016'),('cust2','2015'),('cust2','2016')])

    data = pd.DataFrame(data=np.arange(16).reshape(4,4),
                        index=mul_index,
                        columns=['prd_1','prd_2','prd_3','prd_4'],
                        dtype='int')

    print('============<< multi-index >>===========')
    print(data)

    return data


if __name__ == '__main__':
    data_stack = stacked().stack()
    print('============<< stacked data >>===========')
    print(data_stack)

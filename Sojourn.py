
# coding: utf-8

# In[4]:

import pandas as pd

def addIncDecCum(timelist, incdec):
    global pd
    df = pd.DataFrame()
    df['time'] = timelist
    df = df.sort_values('time')
    df['incdec'] = incdec 
    df = pd.concat([pd.DataFrame({'time':[0], 'incdec':[0]}), df])
    df = df.reset_index()
    df = df.drop('index', axis=1)
    df['cum'] = df.index
    df = df.ix[:, ['time', 'incdec', 'cum']]
    return df

def addSNum(dfA, dfD):
    global pd
    # dfA と dfD を繋げる
    dfAD = pd.concat([dfA, dfD])
    dfAD = dfAD.sort_values('time')
    dfAD = dfAD.reset_index()
    dfAD = dfAD.drop(0)
    dfAD = dfAD.drop(['index', 'cum'], axis=1)
    dfAD = dfAD.reset_index()
    dfAD = dfAD.drop('index', axis=1)
    # s-num を追加
    snum = [0]
    for incdec in dfAD['incdec']:
        snum.append(snum[-1] + incdec)
    del snum[0]
    dfAD['s-num'] = snum
    
    return dfAD

def Sojourn(df):
    dfA = addIncDecCum(df['a-time'],  1)
    dfD = addIncDecCum(df['d-time'], -1)
    dfAD = addSNum(dfA, dfD)
    return dfA, dfD, dfAD


# In[ ]:




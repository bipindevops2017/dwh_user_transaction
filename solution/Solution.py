#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import json
import glob
# setting  the base location to read files
# base_location="/Users/btiwari/PycharmProjects/dwh-coding-challenge/data/"
base_location = "/usr/app/src/data/"

#reading and Parsing/Normalizing acccount records
accounts_location=base_location+'accounts/*.json'
l=[]
for filename in glob.glob(accounts_location):
    with open(filename) as data_file:
        data = json.load(data_file)
    l.append(pd.json_normalize(data))

# concating all df to after normalizing the data
account_df = pd.concat(l, axis=0) 
account_df.reset_index(drop=True, inplace=True)

#sorting the values to see in which form records was infused
adf = account_df.sort_values('ts')

#visualizing the Data
print("Normalized Account DF \n",adf)



### DeNormalizing acccount records or filtering useful records

##Updating the records to created one
adf['data.phone_number'].update(adf['set.phone_number'])
adf['data.address'].update(adf['set.address'])
adf['data.email'].update(adf['set.email'])

#removing unwanted columns 
adf=adf.drop(['set.phone_number','set.address','set.email','id','op','ts'], axis=1)

# replacing the None records
adf = adf.fillna(method="ffill")

#dropping records without card_details
adf = adf.dropna()

print(adf.columns)
print("DeNormalized Account DF \n",adf)

#renaming columns
adf.rename(columns = {'set.savings_account_id':'savings_account_id', 'set.card_id':'card_id',
                   'data.account_id':'account_id','data.name':'name','data.address':'address',
                    'data.phone_number':'phone_number','data.email':'email'}, inplace = True)

#visualizing the Data
print("DeNormalized Account DF \n",adf)
print(adf.columns)

#reading and Parsing/Normalizing acccount records
cards_location=base_location+'cards/*.json'
l=[]
for filename in glob.glob(cards_location):
    with open(filename) as data_file:
        data = json.load(data_file)
    l.append(pd.json_normalize(data))
    
# concating all df to after normalizing the data
cards_df = pd.concat(l, axis=0)
cards_df.reset_index(drop=True, inplace=True)

#sorting the values to see in which form records was infused
cdf=cards_df.sort_values('ts')

#visualizing the Data
print("Normalized cards DF \n",cdf)




### DeNormalizing acccount records or filtering useful records

##Updating the records to created one
cdf['data.status'].update(cdf['set.status'])
cdf['data.credit_used'].update(cdf['set.credit_used'])

#removing unwanted columns
cdf=cdf.drop(['set.status','set.credit_used','id','op'], axis=1)

# replacing the None records of credit_used to 0
cdf['data.credit_used'] = cdf['data.credit_used'].fillna(0)

#filling Nan Values
cdf = cdf.fillna(method="ffill")

#renaming columns
cdf.columns = ['ts','card_id', 'card_number','credit_used','monthly_limit','status']

#visualize the Data
print("DeNormalized cards DF \n",cdf)



#reading and Parsing/Normalizing acccount records
savings_accounts_location=base_location+'savings_accounts/*.json'
l=[]
for filename in glob.glob(savings_accounts_location):
    with open(filename) as data_file:
        data = json.load(data_file)
    l.append(pd.json_normalize(data))
    
# concating all df to after normalizing the data
savings_accounts_df = pd.concat(l, axis=0)
savings_accounts_df.reset_index(drop=True, inplace=True)

#sorting the values to see in which form records was infused
sdf=savings_accounts_df.sort_values('ts')

#visualizing the Data
print("Normalized Savings DF \n",sdf)





### DeNormalizing acccount records or filtering useful records

##Updating the records to created one
sdf['data.balance'].update(sdf['set.balance'])
sdf['data.interest_rate_percent'].update(sdf['set.interest_rate_percent'])

#removing unwanted columns
sdf=sdf.drop(['set.balance','set.interest_rate_percent','id','op'], axis=1)

# replacing the None records of balance to 0
sdf['data.balance']=sdf['data.balance'].fillna(0)

#filling Nan Values
sdf = sdf.fillna(method="ffill")

#renaming columns
sdf.columns = ['ts','savings_account_id', 'balance','interest_rate_percent','status']

#visualize the data
print("DeNormalized Savings DF \n",sdf)



# Selecting only required columns
adf = adf[['savings_account_id','card_id','account_id']]
cdf = cdf[['ts','card_id','credit_used']]
sdf = sdf[['ts','savings_account_id','balance']]


# Dropping rows where credit_used and balance  is < 0
cdf.drop(cdf[cdf.credit_used <=0 ].index, inplace=True)
sdf.drop(sdf[sdf.balance <=0 ].index, inplace=True)




#Applying Join the Tables 
acdf=cdf.merge(adf, how='left', on='card_id')
sacdf=sdf.merge(acdf, how='left', on='savings_account_id',suffixes=('_savings', '_cards'))




# savings account number of transaction w.r.t. time

savings_final_df = sacdf.groupby(['balance','ts_savings']).agg(
                                            balance=('balance', 'first'), 
                                            ts_savings=('ts_savings', 'first'),
                                            savings_account_id=('savings_account_id','first'))

print('savings account number of transaction w.r.t. time \n',savings_final_df)

# savings account total number of transactions
savings_transaction_count = (sacdf.groupby(['ts_savings','balance']).agg(savings_transaction_count=('balance', 'unique'))).count()
print('savings account total number of transactions \n',savings_transaction_count)



# credit card number of transaction w.r.t. time
cards_final_df = sacdf.groupby(['credit_used','ts_cards']).agg(credit_used=('credit_used', 'first'),
                                            ts_cards=('ts_cards', 'first'),
                                             card_id=('card_id','first'))
print('credit card number of transaction w.r.t. time \n',cards_final_df)

# credit card total number of transactions
cards_transaction_count = (sacdf.groupby(['credit_used','ts_cards']).agg(credit_transaction_count=('credit_used', 'unique'))).count()
print('credit card total number of transactions \n',cards_transaction_count)









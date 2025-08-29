
import pandas as pd, os
def build(infile='data/raw/synthetic_logs.csv', outfile='data/processed/features.csv'):
    df=pd.read_csv(infile, parse_dates=['timestamp'])
    df['hour']=df['timestamp'].dt.hour
    df['off_hours']=((df['hour']<8)|(df['hour']>18)).astype(int)
    os.makedirs(os.path.dirname(outfile), exist_ok=True)
    df.to_csv(outfile, index=False)
    print('Features saved ->', outfile)
if __name__=='__main__':
    build()

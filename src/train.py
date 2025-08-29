
import pandas as pd, joblib, os
from sklearn.ensemble import IsolationForest
def train(infile='data/processed/features.csv', model_out='models/iforest.pkl'):
    df=pd.read_csv(infile)
    X=df[['hour','bytes_sent','off_hours']]
    clf=IsolationForest(contamination=0.02, random_state=1)
    clf.fit(X)
    os.makedirs(os.path.dirname(model_out), exist_ok=True)
    joblib.dump(clf, model_out)
    print('Model saved ->', model_out)
if __name__=='__main__':
    train()

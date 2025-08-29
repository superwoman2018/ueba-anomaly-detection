
import pandas as pd, joblib, os
from sklearn.metrics import roc_auc_score, average_precision_score
import matplotlib.pyplot as plt
def evaluate(infile='data/processed/features.csv', model_in='models/iforest.pkl'):
    df=pd.read_csv(infile)
    X=df[['hour','bytes_sent','off_hours']]
    y=df.get('label', pd.Series([0]*len(df)))
    clf=joblib.load(model_in)
    scores=-clf.decision_function(X)
    auc=roc_auc_score(y,scores) if y.sum()>0 else 0.0
    ap=average_precision_score(y,scores) if y.sum()>0 else 0.0
    print(f'ROC-AUC={auc:.3f} AP={ap:.3f}')
    os.makedirs('reports/figures', exist_ok=True)
    plt.hist(scores,bins=50)
    plt.savefig('reports/figures/score_hist.png')
    print('Saved plot -> reports/figures/score_hist.png')
if __name__=='__main__':
    evaluate()


import csv, random, os
from datetime import datetime, timedelta
def synthesize(out='data/raw/synthetic_logs.csv'):
    random.seed(1)
    start = datetime.now() - timedelta(days=3)
    rows=[]
    for u in range(5):
        user=f'user_{u:03d}'
        for d in range(3):
            day = start + timedelta(days=d)
            for i in range(10):
                ts = day.replace(hour=random.choice([9,10,11,15]), minute=random.randint(0,59))
                rows.append([ts.isoformat(), user, 'login', random.randint(1000,200000), 'PK', 0])
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out,'w',newline='') as f:
        w=csv.writer(f)
        w.writerow(['timestamp','user','action','bytes_sent','geo','label'])
        for r in rows:
            w.writerow(r)
    print('Wrote', len(rows), 'events to', out)
if __name__=='__main__':
    synthesize()

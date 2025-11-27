import os, glob
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class Retriever:
    def __init__(self, docs_path='docs/'):
        self.docs = []
        self.ids = []
        
        for fp in glob.glob(os.path.join(docs_path, '*.md')):
            with open(fp, 'r', encoding='utf-8') as f:
                text = f.read()
            chunks = [c.strip() for c in text.split('\n\n') if c.strip()]
            for i, ch in enumerate(chunks):
                cid = f"{os.path.basename(fp)}::chunk{i}"
                self.ids.append(cid)
                self.docs.append(ch)
        
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
        if self.docs:
            self.tfidf = self.vectorizer.fit_transform(self.docs)
        else:
            self.tfidf = None

    def retrieve(self, query, k=5):
        if self.tfidf is None: 
            return []
        qv = self.vectorizer.transform([query])
        scores = (self.tfidf @ qv.T).toarray().squeeze()
        idxs = scores.argsort()[::-1][:k]
        results = [{"id": self.ids[i], "text": self.docs[i], "score": float(scores[i])} for i in idxs]
        return results

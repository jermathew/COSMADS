import yake
import glob
import json
import numpy as np

class DocumentManagerDB:

    def __init__(self):
        self.documents_dir = "documents"

        language = "en"
        max_ngram_size = 1
        deduplication_thresold = 0.9
        numOfKeywords = 20
        self.kw_extractor = yake.KeywordExtractor(lan=language, 
                                     n=max_ngram_size, 
                                     dedupLim=deduplication_thresold,
                                     top=numOfKeywords)
        
    def levenshteinDistanceDP(self, token1, token2):
        token1 = token1.lower()
        token2 = token2.lower()

        distances = np.zeros((len(token1) + 1, len(token2) + 1))

        for t1 in range(len(token1) + 1):
            distances[t1][0] = t1

        for t2 in range(len(token2) + 1):
            distances[0][t2] = t2
            
        a = 0
        b = 0
        c = 0
        
        for t1 in range(1, len(token1) + 1):
            for t2 in range(1, len(token2) + 1):
                if (token1[t1-1] == token2[t2-1]):
                    distances[t1][t2] = distances[t1 - 1][t2 - 1]
                else:
                    a = distances[t1][t2 - 1]
                    b = distances[t1 - 1][t2]
                    c = distances[t1 - 1][t2 - 1]
                    
                    if (a <= b and a <= c):
                        distances[t1][t2] = a + 1
                    elif (b <= a and b <= c):
                        distances[t1][t2] = b + 1
                    else:
                        distances[t1][t2] = c + 1

        return distances[len(token1)][len(token2)]
        
    def extract_document(self, query):
        query_keyword = self.kw_extractor.extract_keywords(query)
        #print(f"Query keywords: {query_keyword}")

        match_doc = {}
        documents_saved = glob.glob(f"{self.documents_dir}/*.txt")
        for document in documents_saved:
            with open(document, "r") as f:
                text = f.read()
                text_keyword = self.kw_extractor.extract_keywords(text)
                #print(f"Text keywords: {document} ----- {text_keyword}\n")

                new_txt_kw = []
                for txt_kw in text_keyword:
                    for q_kw in query_keyword:
                        # levenshtein distance
                        d_lev = self.levenshteinDistanceDP(txt_kw[0], q_kw[0])
                        if d_lev <= 2:
                            #print(f"Levenshtein distance: {d_lev}")
                            new_txt_kw.append(q_kw)
                        else:
                            new_txt_kw.append(txt_kw)
                text_keyword = new_txt_kw
                #print(text_keyword)
                #print(query_keyword)

                # jaccard similarity
                intersection = len(set(query_keyword).intersection(set(text_keyword)))
                #print(f"Intersection: {intersection}")

                union = len(set(query_keyword).union(set(text_keyword)))
                #print(f"Union: {union}")

                jaccard_similarity = intersection / union
                
                match_doc[document] = jaccard_similarity
        
        #print(f"Matched documents: {match_doc}")

        # reverse = True -> sort in descending order
        match_doc = dict(sorted(match_doc.items(), key=lambda item: item[1], reverse=True))

        best_match_file = list(match_doc.keys())[0]

        with open(best_match_file, "r") as f:
            best_match = f.read()

        return best_match
    
if __name__ == "__main__":
    doc_man = DocumentManagerDB()
    
    q = "q4"
    with open("queries_pipelines.json", "r") as f:
        queries = json.load(f)
    query = queries[q]["query"]

    best_match = doc_man.extract_document(query)
    print(f"Best match: {best_match}")

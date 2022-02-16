""" Reproduce the hybrid results in v1.1 """

import argparse
from collections import defaultdict

from tqdm import tqdm


lang2alpha = {'arabic': 0.77, 'bengali': 0.71, 'english': 1.0, 'finnish': 0.77, 'indonesian': 0.9, 'japanese': 0.99, 'korean': 1.0, 'russian': 0.93, 'swahili': 0.56, 'telugu': 0.73, 'thai': 0.84}


def load_runs(fn):
    runs = defaultdict(dict)
    with open(fn) as f:
        for line in f:
            qid, _, docid, _, score, _ = line.rstrip().split()
            runs[qid][docid] = float(score)
    return runs


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Interpolate runs')
    parser.add_argument('--dense', required=True, help='retrieval run1')
    parser.add_argument('--sparse', required=True, help='retrieval run2')
    parser.add_argument('--output', required=True)
    parser.add_argument('--alpha', type=float, default=None, help="The alpha weight on dense / sparse score. use the pre-defined (optimal) one if not given.")
    parser.add_argument('--lang', type=str, default=None, help="The language of the runfiles to compute hybrid on. Need to be set if alpha is not given.")
    parser.add_argument('--normalization', action='store_true')
    parser.add_argument('--weight-on-dense', action='store_true')

    args = parser.parse_args()
    runs_1 = load_runs(args.dense) 
    runs_2 = load_runs(args.sparse)

    hybrid_result = {}
    output_f = open(args.output, 'w')
    alpha = args.alpha
    if not alpha:
        if not args.lang:
            raise ValueError(f"Need to either set --alpha or --lang to compute hybrid.")
        alpha = lang2alpha.get(args.lang, None)
        if not args.lang:
            raise ValueError(f"Unrecognized lang, need to be one of {list(lang2alpha.keys())}.")

    for key in tqdm(list(set(runs_1.keys()).union(set(runs_2.keys())))):
        dense_hits = {docid: runs_1[key][docid] for docid in runs_1[key]} if key in runs_1 else {}
        sparse_hits = {docid: runs_2[key][docid] for docid in runs_2[key]} if key in runs_2 else {}

        hybrid_result = []
        min_dense_score = min(dense_hits.values()) if len(dense_hits) > 0 else 0
        max_dense_score = max(dense_hits.values()) if len(dense_hits) > 0 else 1
        min_sparse_score = min(sparse_hits.values()) if len(sparse_hits) > 0 else 0
        max_sparse_score = max(sparse_hits.values()) if len(sparse_hits) > 0 else 1
        for doc in set(dense_hits.keys()) | set(sparse_hits.keys()):
            if doc not in dense_hits:
                sparse_score = sparse_hits[doc]
                dense_score = min_dense_score
            elif doc not in sparse_hits:
                sparse_score = min_sparse_score
                dense_score = dense_hits[doc]
            else:
                sparse_score = sparse_hits[doc]
                dense_score = dense_hits[doc]

            if args.normalization:
                sparse_score = 0 if (max_sparse_score - min_sparse_score) == 0 else (
                    (sparse_score - (min_sparse_score + max_sparse_score) / 2) / (max_sparse_score - min_sparse_score))
                dense_score = 0 if (max_sparse_score - min_sparse_score) == 0 else (
                    (dense_score - (min_dense_score + max_dense_score) / 2) / (max_dense_score - min_dense_score))

            score = args.alpha * sparse_score + dense_score if not args.weight_on_dense else sparse_score + args.alpha * dense_score
            hybrid_result.append((doc, score))

        hybrid_result = sorted(hybrid_result, key=lambda x: x[1], reverse=True)
        for idx, item in enumerate(hybrid_result):
            output_f.write(f'{key} Q0 {item[0]} {idx+1} {item[1]} hybrid\n')
    output_f.close()
<p align="center">
    <br>
      <img src="https://user-images.githubusercontent.com/31640436/130242523-edc285f2-beda-4b10-ba2b-6ca5b5d9b6a8.png" width="27%">
    <br>
</p>

<h4 align="center">
    <p>
        <a href="#download">Download</a> |
        <a href="#baselines-and-evaluation">Baselines and Evaluation</a> |
        <a href="#results">Results</a> |
        <a href="https://arxiv.org/abs/2108.08787">Paper</a>
    <p>
</h4>

 
## Introduction
Mr. TyDi is a multi-lingual benchmark dataset built on [TyDi](https://arxiv.org/abs/2003.05002), covering eleven typologically diverse languages.
It is designed for mono-lingual retrieval, specifically to evaluate ranking with learned dense representations.
Mr. TyDi is licensed under the Apache License 2.0. 

## Download 

#### 1. Dataset (topic, qrels, folds, collections)

| Version | Dataset Link |
|------------|------------------------------------------------------------------------------------------|
|**Version 1.1**| [Arabic](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.1-arabic.tar.gz) \| [Bengali](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.1-bengali.tar.gz) \| [English](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.1-english.tar.gz) \| [Finnish](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.1-finnish.tar.gz) \| [Indonesian](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.1-indonesian.tar.gz) \| [Japanese](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.1-japanese.tar.gz) \| [Korean](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.1-korean.tar.gz) \| [Russian](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.1-russian.tar.gz) \| [Swahili](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.1-swahili.tar.gz) \| [Telugu](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.1-telugu.tar.gz) \| [Thai](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.1-thai.tar.gz) |
| **Version 1.0** | [Arabic](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-arabic.tar.gz) \| [Bengali](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-bengali.tar.gz) \| [English](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-english.tar.gz) \| [Finnish](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-finnish.tar.gz) \| [Indonesian](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-indonesian.tar.gz) \| [Japanese](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-japanese.tar.gz) \| [Korean](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-korean.tar.gz) \| [Russian](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-russian.tar.gz) \| [Swahili](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-swahili.tar.gz) \| [Telugu](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-telugu.tar.gz) \| [Thai](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-thai.tar.gz) |

The dataset (v1.1) is also available on HuggingFace Dataset:
- [castorini/mr-tydi](https://huggingface.co/datasets/castorini/mr-tydi)
- [castorini/mrtydi-corpus](https://huggingface.co/datasets/castorini/mr-tydi-corpus)

#### 2. Pre-build sparse index (for BM25)

| Version | Index Link |
|------------|------------------------------------------------------------------------------------------|
|**Version 1.1**|  [Arabic](https://vault.cs.uwaterloo.ca/s/7oDFnq8FmTazf2a/download) \| [Bengali](https://vault.cs.uwaterloo.ca/s/HaPaz2wFbRMP2LK/download) \| [English](https://vault.cs.uwaterloo.ca/s/w4ccMwH5BLnXQ3j/download) \| [Finnish](https://vault.cs.uwaterloo.ca/s/Pgd3mqjy77a6FR8/download) \| [Indonesian](https://vault.cs.uwaterloo.ca/s/tF8NE7pWZ2xGix7/download) \| [Japanese](https://vault.cs.uwaterloo.ca/s/ema8i83zqJr7n48/download) \| [Korean](https://vault.cs.uwaterloo.ca/s/igmEHCTjTwNi3de/download) \| [Russian](https://vault.cs.uwaterloo.ca/s/Pbi9xrD7jSYaxnX/download) \| [Swahili](https://vault.cs.uwaterloo.ca/s/SWqajDQgq8wppf6/download) \| [Telugu](https://vault.cs.uwaterloo.ca/s/DAB6ba5ZF98awH6/download) \| [Thai](https://vault.cs.uwaterloo.ca/s/2Ady6AwBwNbYLpg/download)
|**Version 1.0**| [Arabic](https://vault.cs.uwaterloo.ca/s/kKed9pzMGPdiHkm/download) \| [Bengali](https://vault.cs.uwaterloo.ca/s/QWsjtMgprLBx6gd/download) \| [English](https://vault.cs.uwaterloo.ca/s/RG3wTom3TBnYbyx/download) \| [Finnish](https://vault.cs.uwaterloo.ca/s/FwCbws5okxsjH5T/download) \| [Indonesian](https://vault.cs.uwaterloo.ca/s/FJLKPZwGKn2wCD5/download) \| [Japanese](https://vault.cs.uwaterloo.ca/s/mYj9g7pJZqGbZXM/download) \| [Korean](https://vault.cs.uwaterloo.ca/s/zKAFt5q8wLjokWq/download) \| [Russian](https://vault.cs.uwaterloo.ca/s/TBMEn2coT9Xoyk8/download) \| [Swahili](https://vault.cs.uwaterloo.ca/s/rpX6TbqrE73yoLp/download) \| [Telugu](https://vault.cs.uwaterloo.ca/s/eWN7ZYpfknRHZEM/download) \| [Thai](https://vault.cs.uwaterloo.ca/s/HnF36dN86SdZKx6/download)

#### 3. Pre-build dense index (for mDPR)
| Version | Index Link |
|------------|------------------------------------------------------------------------------------------|
|**Version 1.1**|  [Arabic](https://vault.cs.uwaterloo.ca/s/Jgj3rYjbyRrmJs8/download) \| [Bengali](https://vault.cs.uwaterloo.ca/s/4PpkzXAQtXFFJHR/download) \| [English](https://vault.cs.uwaterloo.ca/s/A7pjbwYeoT4Krnj/download) \| [Finnish](https://vault.cs.uwaterloo.ca/s/erNYkrYzRZxpecz/download) \| [Indonesian](https://vault.cs.uwaterloo.ca/s/BpR3MzT7KJ6edx7/download) \| [Japanese](https://vault.cs.uwaterloo.ca/s/k7bptHT8GwMJpnF/download) \| [Korean](https://vault.cs.uwaterloo.ca/s/TigfYMde94YWAoE/download) \| [Russian](https://vault.cs.uwaterloo.ca/s/eN7demnmnspqxjk/download) \| [Swahili](https://vault.cs.uwaterloo.ca/s/JgiX8PRftnqcPwy/download) \| [Telugu](https://vault.cs.uwaterloo.ca/s/dkm6RGdgRbnwiX2/download) \| [Thai](https://vault.cs.uwaterloo.ca/s/fFrRYefd3nWFR3J/download)
|**Version 1.0**|  [Arabic](https://vault.cs.uwaterloo.ca/s/JptH9xNcWsEJnto/download) \| [Bengali](https://vault.cs.uwaterloo.ca/s/Q2e8iRc6W2598RA/download) \| [English](https://vault.cs.uwaterloo.ca/s/YsJeS6EHA4XndHP/download) \| [Finnish](https://vault.cs.uwaterloo.ca/s/EkywkiRTkPHEcHF/download) \| [Indonesian](https://vault.cs.uwaterloo.ca/s/3RJBaDKjmFtEiXQ/download) \| [Japanese](https://vault.cs.uwaterloo.ca/s/iMdqFEatGGKWqJY/download) \| [Korean](https://vault.cs.uwaterloo.ca/s/DWjLygpryrrDmAg/download) \| [Russian](https://vault.cs.uwaterloo.ca/s/saJ9fwdE4Fxy6jD/download) \| [Swahili](https://vault.cs.uwaterloo.ca/s/P4zpSg3CHp4ckmZ/download) \| [Telugu](https://vault.cs.uwaterloo.ca/s/PrpzZTxgRwyP3EG/download) \| [Thai](https://vault.cs.uwaterloo.ca/s/wT8GSZqY6T8JRqC/download)


#### 4. Checkpoints
- [castorini/mdpr-question-nq](https://huggingface.co/castorini/mdpr-question-nq)
- [castorini/mdpr-passage-nq](https://huggingface.co/castorini/mdpr-passage-nq)


## Baselines and Evaluation
The one-command index and reproduce would require the recent dev version of Pyserini.
Please follow this [guidance](https://github.com/castorini/pyserini/#development-installation) to setup a dev installation for Pyserini.

This page only covers the scripts to reproduce *searching*.
The indexes are all handled within Pyserini. 
That is, you won't need to manually download the above indexes or models to run the following scripts.
For the scripts to reproduce the sparse and dense indexes,
please refer to the Pyserini documentations:

| Version | Model | Documentation Link |
|------------|-------|------------------------------------------------------------------------------------------|
|**Version 1.1**| Sparse Index |  [Arabic](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/lucene-index.mrtydi-v1.1-Arabic.20220108.6fcb89.README.md) \\| [Bengali](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/lucene-index.mrtydi-v1.1-Bengali.20220108.6fcb89.README.md) \\| [English](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/lucene-index.mrtydi-v1.1-English.20220108.6fcb89.README.md) \\| [Finnish](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/lucene-index.mrtydi-v1.1-Finnish.20220108.6fcb89.README.md) \\| [Indonesian](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/lucene-index.mrtydi-v1.1-Indonesian.20220108.6fcb89.README.md) \\| [Japanese](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/lucene-index.mrtydi-v1.1-Japanese.20220108.6fcb89.README.md) \\| [Korean](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/lucene-index.mrtydi-v1.1-Korean.20220108.6fcb89.README.md) \\| [Russian](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/lucene-index.mrtydi-v1.1-Russian.20220108.6fcb89.README.md) \\| [Swahili](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/lucene-index.mrtydi-v1.1-Swahili.20220108.6fcb89.README.md) \\| [Telugu](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/lucene-index.mrtydi-v1.1-Telugu.20220108.6fcb89.README.md) \\| [Thai](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/lucene-index.mrtydi-v1.1-Thai.20220108.6fcb89.README.md)
|**Version 1.1**| Dense Index |  [Arabic](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/faiss.mrtydi-v1.1-Arabic.20220207.5df364.README.md) \\| [Bengali](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/faiss.mrtydi-v1.1-Bengali.20220207.5df364.README.md) \\| [English](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/faiss.mrtydi-v1.1-English.20220207.5df364.README.md) \\| [Finnish](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/faiss.mrtydi-v1.1-Finnish.20220207.5df364.README.md) \\| [Indonesian](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/faiss.mrtydi-v1.1-Indonesian.20220207.5df364.README.md) \\| [Japanese](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/faiss.mrtydi-v1.1-Japanese.20220207.5df364.README.md) \\| [Korean](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/faiss.mrtydi-v1.1-Korean.20220207.5df364.README.md) \\| [Russian](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/faiss.mrtydi-v1.1-Russian.20220207.5df364.README.md) \\| [Swahili](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/faiss.mrtydi-v1.1-Swahili.20220207.5df364.README.md) \\| [Telugu](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/faiss.mrtydi-v1.1-Telugu.20220207.5df364.README.md) \\| [Thai](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/faiss.mrtydi-v1.1-Thai.20220207.5df364.README.md)
#### 1. BM25
Define variables based on language
```bash
lang=arabic     # one of {'arabic', 'bengali', 'english', 'finnish', 'indonesian', 'japanese', 'korean', 'russian', 'swahili', 'telugu', 'thai'}
lang_abbr=ar    # one of {'ar', 'bn', 'en', 'fi', 'id', 'ja', 'ko', 'ru', 'sw', 'te', 'th'}
set_name=test   # one of {'train', 'dev', 'test'}
runfile=runs/run.bm25.mrtydi-v1.1-${lang}.${set_name}.txt

python -m pyserini.search --bm25 \
    --language ${lang_abbr} \
    --topics mrtydi-v1.1-${lang}-${set_name} \
    --index mrtydi-v1.1-${lang} \
    --output ${runfile}
```

#### 2. mDPR
```bash
lang=arabic     # one of {'arabic', 'bengali', 'english', 'finnish', 'indonesian', 'japanese', 'korean', 'russian', 'swahili', 'telugu', 'thai'}
lang_abbr=ar    # one of {'ar', 'bn', 'en', 'fi', 'id', 'ja', 'ko', 'ru', 'sw', 'te', 'th'}
set_name=test   # one of {'train', 'dev', 'test'}
runfile=runs/run.mdpr.mrtydi-v1.1-$lang.${set_name}.txt

python -m pyserini.dsearch \
    --topics mrtydi-v1.1-${lang}-${set_name} \
    --index mrtydi-v1.1-${lang}-mdpr-nq \
    --encoder castorini/mdpr-question-nq \
    --batch-size 36 \
    --threads 12 \
    --output 
```

#### 3. BM25+mDPR hybrid
use the pre-set best alpha for each language:
```bash
lang=arabic     # one of {'arabic', 'bengali', 'english', 'finnish', 'indonesian', 'japanese', 'korean', 'russian', 'swahili', 'telugu', 'thai'}

python scripts/hybrid.py    --lang ${lang} \
                            --sparse ${bm25_runfile} \
                            --dense ${dense_runfile} \
                            --output ${runfile} \
                            --weight-on-dense \
                            --normalization
```
or to run hybrid with any `alpha`:
```bash
alpha=0.5
python scripts/hybrid.py    --alpha ${alpha} \
                            --sparse ${bm25_runfile} \
                            --dense ${dense_runfile} \
                            --output ${runfile} \
                            --weight-on-dense \
                            --normalization
```
where the `bm25_runfile` and `dense_runfile` are prepared from the previous two steps.

#### 4. Evaluate
```bash
python -m pyserini.eval.trec_eval -c -mrecip_rank -mrecall.100 ${qrels} ${runfile} 
```


## Results
Here we present the MRR@100 and Recall@100 scores after fixing a bug relavant to using multi-lingual models in Pyserini 0.13.0. The sparse scores are unaffected, whereas the mDPR and Hybrid scores are higher than the original reported ones to various degree.
We also put the updated figures under the [figures/](./figures) directory.
### MRR@100
|                |   Ar  |   Bn  |   En  |   Fi  |   In  |   Ja  |   Ko  |   Ru  |   Sw  |   Te  |   Th  |  avg  |
|----------------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| BM25 (default) | 0.368 | 0.418 | 0.140 | 0.284 | 0.376 | 0.211 | 0.285 | 0.313 | 0.389 | 0.343 | 0.401 | 0.321 |
|   BM25 (tuned) | 0.366 | 0.413 | 0.150 | 0.287 | 0.382 | 0.217 | 0.280 | 0.329 | 0.396 | 0.424 | 0.416 | 0.333 |
|      mDPR (NQ) | 0.291 | 0.291 | 0.291 | 0.206 | 0.271 | 0.213 | 0.235 | 0.283 | 0.189 | 0.111 | 0.172 | 0.226 |
|         Hybrid | 0.500 | 0.555 | 0.328 | 0.377 | 0.481 | 0.360 | 0.361 | 0.455 | 0.415 | 0.418 | 0.507 | 0.426 |

### Recall@100
|                |   Ar  |   Bn  |   En  |   Fi  |   In  |   Ja  |   Ko  |   Ru  |   Sw  |   Te  |   Th  |  avg  |
|----------------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| BM25 (default) | 0.793 | 0.869 | 0.537 | 0.719 | 0.843 | 0.645 | 0.619 | 0.648 | 0.764 | 0.758 | 0.853 | 0.732 |
|   BM25 (tuned) | 0.800 | 0.874 | 0.551 | 0.725 | 0.846 | 0.656 | 0.797 | 0.660 | 0.764 | 0.813 | 0.853 | 0.758 |
|      mDPR (NQ) | 0.650 | 0.779 | 0.678 | 0.568 | 0.685 | 0.584 | 0.533 | 0.647 | 0.528 | 0.366 | 0.515 | 0.594 |
|         Hybrid | 0.871 | 0.946 | 0.793 | 0.827 | 0.900 | 0.794 | 0.718 | 0.815 | 0.808 | 0.823 | 0.883 | 0.834 |

## Citation
If you find our paper useful or use the dataset in your work, please cite our paper and the TyDi paper:
```
@article{mrtydi,
      title={{Mr. TyDi}: A Multi-lingual Benchmark for Dense Retrieval}, 
      author={Xinyu Zhang and Xueguang Ma and Peng Shi and Jimmy Lin},
      year={2021},
      journal={arXiv:2108.08787},
}
```
```
@article{tydiqa,
    title={{TyDi QA}: A Benchmark for Information-Seeking Question Answering in Typologically Diverse Languages},
    author={Jonathan H. Clark and Eunsol Choi and Michael Collins and Dan Garrette and Tom Kwiatkowski and Vitaly Nikolaev and Jennimaria Palomaki}
    year={2020},
    journal={Transactions of the Association for Computational Linguistics}
}
```

## Contact us
If you have any question or suggestions regarding the dataset, code or publication, 
please contact Xinyu Zhang (x978zhan[at]uwaterloo.ca)

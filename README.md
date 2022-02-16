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

### Version 1.1

#### 1. Dataset (topic, qrels, folds, collections)
&nbsp;&nbsp;&nbsp;&nbsp; [Ar](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.1-arabic.tar.gz) \| [Bn](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.1-bengali.tar.gz) \| [En](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.1-english.tar.gz) \| [Fi](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.1-finnish.tar.gz) \| [Id](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.1-indonesian.tar.gz) \| [Ja](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.1-japanese.tar.gz) \| [Ko](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.1-korean.tar.gz) \| [Ru](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.1-russian.tar.gz) \| [Sw](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.1-swahili.tar.gz) \| [Te](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.1-telugu.tar.gz) \| [Th](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.1-thai.tar.gz) 

&nbsp;&nbsp;&nbsp;&nbsp;The dataset (v1.1) is also available on HuggingFace Dataset:
- [castorini/mr-tydi](https://huggingface.co/datasets/castorini/mr-tydi)
- [castorini/mrtydi-corpus](https://huggingface.co/datasets/castorini/mr-tydi-corpus)

#### 2. Pre-build sparse index (for BM25)
&nbsp;&nbsp;&nbsp;&nbsp; [Ar](https://vault.cs.uwaterloo.ca/s/7oDFnq8FmTazf2a/download) \| [Bn](https://vault.cs.uwaterloo.ca/s/HaPaz2wFbRMP2LK/download) \| [En](https://vault.cs.uwaterloo.ca/s/w4ccMwH5BLnXQ3j/download) \| [Fi](https://vault.cs.uwaterloo.ca/s/Pgd3mqjy77a6FR8/download) \| [Id](https://vault.cs.uwaterloo.ca/s/tF8NE7pWZ2xGix7/download) \| [Ja](https://vault.cs.uwaterloo.ca/s/ema8i83zqJr7n48/download) \| [Ko](https://vault.cs.uwaterloo.ca/s/igmEHCTjTwNi3de/download) \| [Ru](https://vault.cs.uwaterloo.ca/s/Pbi9xrD7jSYaxnX/download) \| [Sw](https://vault.cs.uwaterloo.ca/s/SWqajDQgq8wppf6/download) \| [Te](https://vault.cs.uwaterloo.ca/s/DAB6ba5ZF98awH6/download) \| [Th](https://vault.cs.uwaterloo.ca/s/2Ady6AwBwNbYLpg/download)

#### 3. Pre-build dense index (for mDPR)
&nbsp;&nbsp;&nbsp;&nbsp; [Ar](https://vault.cs.uwaterloo.ca/s/Jgj3rYjbyRrmJs8/download) \| [Bn](https://vault.cs.uwaterloo.ca/s/4PpkzXAQtXFFJHR/download) \| [En](https://vault.cs.uwaterloo.ca/s/A7pjbwYeoT4Krnj/download) \| [Fi](https://vault.cs.uwaterloo.ca/s/erNYkrYzRZxpecz/download) \| [Id](https://vault.cs.uwaterloo.ca/s/BpR3MzT7KJ6edx7/download) \| [Ja](https://vault.cs.uwaterloo.ca/s/k7bptHT8GwMJpnF/download) \| [Ko](https://vault.cs.uwaterloo.ca/s/TigfYMde94YWAoE/download) \| [Ru](https://vault.cs.uwaterloo.ca/s/eN7demnmnspqxjk/download) \| [Sw](https://vault.cs.uwaterloo.ca/s/JgiX8PRftnqcPwy/download) \| [Te](https://vault.cs.uwaterloo.ca/s/dkm6RGdgRbnwiX2/download) \| [Th](https://vault.cs.uwaterloo.ca/s/fFrRYefd3nWFR3J/download)

#### 4. Checkpoints
- [castorini/mdpr-question-nq](https://huggingface.co/castorini/mdpr-question-nq)
- [castorini/mdpr-passage-nq](https://huggingface.co/castorini/mdpr-passage-nq)


<details>
    <summary> <b> Previous Versions </b></summary>

### Version 1.0

#### 1. Dataset
&nbsp;&nbsp;&nbsp;&nbsp;  [Ar](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-arabic.tar.gz) \| [Bn](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-bengali.tar.gz) \| [En](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-english.tar.gz) \| [Fi](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-finnish.tar.gz) \| [Id](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-indonesian.tar.gz) \| [Ja](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-japanese.tar.gz) \| [Ko](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-korean.tar.gz) \| [Ru](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-russian.tar.gz) \| [Sw](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-swahili.tar.gz) \| [Te](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-telugu.tar.gz) \| [Th](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-thai.tar.gz)

#### 2. Pre-build sparse index (for BM25)
&nbsp;&nbsp;&nbsp;&nbsp; [Ar](https://vault.cs.uwaterloo.ca/s/kKed9pzMGPdiHkm/download) \| [Bn](https://vault.cs.uwaterloo.ca/s/QWsjtMgprLBx6gd/download) \| [En](https://vault.cs.uwaterloo.ca/s/RG3wTom3TBnYbyx/download) \| [Fi](https://vault.cs.uwaterloo.ca/s/FwCbws5okxsjH5T/download) \| [Id](https://vault.cs.uwaterloo.ca/s/FJLKPZwGKn2wCD5/download) \| [Ja](https://vault.cs.uwaterloo.ca/s/mYj9g7pJZqGbZXM/download) \| [Ko](https://vault.cs.uwaterloo.ca/s/zKAFt5q8wLjokWq/download) \| [Ru](https://vault.cs.uwaterloo.ca/s/TBMEn2coT9Xoyk8/download) \| [Sw](https://vault.cs.uwaterloo.ca/s/rpX6TbqrE73yoLp/download) \| [Te](https://vault.cs.uwaterloo.ca/s/eWN7ZYpfknRHZEM/download) \| [Th](https://vault.cs.uwaterloo.ca/s/HnF36dN86SdZKx6/download)

#### 3. Pre-build dense index (for mDPR)
&nbsp;&nbsp;&nbsp;&nbsp; [Ar](https://vault.cs.uwaterloo.ca/s/JptH9xNcWsEJnto/download) \| [Bn](https://vault.cs.uwaterloo.ca/s/Q2e8iRc6W2598RA/download) \| [En](https://vault.cs.uwaterloo.ca/s/YsJeS6EHA4XndHP/download) \| [Fi](https://vault.cs.uwaterloo.ca/s/EkywkiRTkPHEcHF/download) \| [Id](https://vault.cs.uwaterloo.ca/s/3RJBaDKjmFtEiXQ/download) \| [Ja](https://vault.cs.uwaterloo.ca/s/iMdqFEatGGKWqJY/download) \| [Ko](https://vault.cs.uwaterloo.ca/s/DWjLygpryrrDmAg/download) \| [Ru](https://vault.cs.uwaterloo.ca/s/saJ9fwdE4Fxy6jD/download) \| [Sw](https://vault.cs.uwaterloo.ca/s/P4zpSg3CHp4ckmZ/download) \| [Te](https://vault.cs.uwaterloo.ca/s/PrpzZTxgRwyP3EG/download) \| [Th](https://vault.cs.uwaterloo.ca/s/wT8GSZqY6T8JRqC/download)

</details>

## Baselines and Evaluation
The one-command reproduction (on v1.1) would require the recent dev version of Pyserini.
Please follow this [guidance](https://github.com/castorini/pyserini/#development-installation) to setup a dev installation for Pyserini.

This page only covers the scripts to reproduce *searching*.
The indexes are all handled within Pyserini. 
That is, you won't need to manually download the above indexes or models to run the following scripts.
For the scripts to reproduce the sparse and dense indexes,
please refer to the Pyserini documentations:

Model | Documentation Link |
|-------|------------------------------------------------------------------------------------------|
Sparse Index |  [Ar](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/lucene-index.mrtydi-v1.1-arabic.20220108.6fcb89.README.md) \\| [Bn](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/lucene-index.mrtydi-v1.1-bengali.20220108.6fcb89.README.md) \\| [En](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/lucene-index.mrtydi-v1.1-english.20220108.6fcb89.README.md) \\| [Fi](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/lucene-index.mrtydi-v1.1-finnish.20220108.6fcb89.README.md) \\| [Id](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/lucene-index.mrtydi-v1.1-indonesian.20220108.6fcb89.README.md) \\| [Ja](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/lucene-index.mrtydi-v1.1-japanese.20220108.6fcb89.README.md) \\| [Ko](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/lucene-index.mrtydi-v1.1-korean.20220108.6fcb89.README.md) \\| [Ru](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/lucene-index.mrtydi-v1.1-russian.20220108.6fcb89.README.md) \\| [Sw](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/lucene-index.mrtydi-v1.1-swahili.20220108.6fcb89.README.md) \\| [Te](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/lucene-index.mrtydi-v1.1-telugu.20220108.6fcb89.README.md) \\| [Th](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/lucene-index.mrtydi-v1.1-thai.20220108.6fcb89.README.md)
Dense Index |  [Ar](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/faiss.mrtydi-v1.1-arabic.20220207.5df364.README.md) \\| [Bn](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/faiss.mrtydi-v1.1-bengali.20220207.5df364.README.md) \\| [En](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/faiss.mrtydi-v1.1-english.20220207.5df364.README.md) \\| [Fi](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/faiss.mrtydi-v1.1-finnish.20220207.5df364.README.md) \\| [Id](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/faiss.mrtydi-v1.1-indonesian.20220207.5df364.README.md) \\| [Ja](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/faiss.mrtydi-v1.1-japanese.20220207.5df364.README.md) \\| [Ko](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/faiss.mrtydi-v1.1-korean.20220207.5df364.README.md) \\| [Ru](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/faiss.mrtydi-v1.1-russian.20220207.5df364.README.md) \\| [Sw](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/faiss.mrtydi-v1.1-swahili.20220207.5df364.README.md) \\| [Te](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/faiss.mrtydi-v1.1-telugu.20220207.5df364.README.md) \\| [Th](https://github.com/castorini/pyserini/blob/master/pyserini/resources/index-metadata/faiss.mrtydi-v1.1-thai.20220207.5df364.README.md)
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

<p align="center">
    <br>
      <img src="https://user-images.githubusercontent.com/31640436/130242523-edc285f2-beda-4b10-ba2b-6ca5b5d9b6a8.png" width="27%">
    <br>
</p>

<h4 align="center">
    <p>
        <a href="#download">Download</a> |
        <a href="#baselines-and-evaluation">Baselines and Evaluation</a> |
        <a href="https://arxiv.org/abs/2108.08787">Paper</a>
    <p>
</h4>

 
## Introduction
Mr. TyDi is a multi-lingual benchmark dataset built on [TyDi](https://arxiv.org/abs/2003.05002), covering eleven typologically diverse languages.
It is designed for mono-lingual retrieval, specifically to evaluate ranking with learned dense representations.

## Download 

#### 1. Dataset (topic, qrels, folds, collections)

&nbsp;&nbsp;&nbsp;&nbsp;[Arabic](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-arabic.tar.gz)
| [Bengali](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-bengali.tar.gz)
| [English](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-english.tar.gz)
| [Finnish](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-finnish.tar.gz)
| [Indonesian](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-indonesian.tar.gz)
| [Japanese](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-japanese.tar.gz)
| [Korean](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-korean.tar.gz)
| [Russian](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-russian.tar.gz)
| [Swahili](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-swahili.tar.gz)
| [Telugu](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-telugu.tar.gz)
| [Thai](https://git.uwaterloo.ca/jimmylin/mr.tydi/-/raw/master/data/mrtydi-v1.0-thai.tar.gz)

#### 2. Pre-build sparse index (for BM25)

&nbsp;&nbsp;&nbsp;&nbsp;[Arabic](https://vault.cs.uwaterloo.ca/s/kKed9pzMGPdiHkm/download)
| [Bengali](https://vault.cs.uwaterloo.ca/s/QWsjtMgprLBx6gd/download)
| [English](https://vault.cs.uwaterloo.ca/s/RG3wTom3TBnYbyx/download)
| [Finnish](https://vault.cs.uwaterloo.ca/s/FwCbws5okxsjH5T/download)
| [Indonesian](https://vault.cs.uwaterloo.ca/s/FJLKPZwGKn2wCD5/download)
| [Japanese](https://vault.cs.uwaterloo.ca/s/mYj9g7pJZqGbZXM/download)
| [Korean](https://vault.cs.uwaterloo.ca/s/zKAFt5q8wLjokWq/download)
| [Russian](https://vault.cs.uwaterloo.ca/s/TBMEn2coT9Xoyk8/download)
| [Kiswahili](https://vault.cs.uwaterloo.ca/s/rpX6TbqrE73yoLp/download)
| [Telugu](https://vault.cs.uwaterloo.ca/s/eWN7ZYpfknRHZEM/download)
| [Thai](https://vault.cs.uwaterloo.ca/s/HnF36dN86SdZKx6/download)

#### 3. Pre-build dense index (for mDPR)

&nbsp;&nbsp;&nbsp;&nbsp; [Arabic]()
| [Bengali]() 
| [English]() 
| [Finnish]()
| [Indonesian]()
| [Japanese]() 
| [Korean]()
| [Russian]() 
| [Kiswahili]()
| [Telugu]()
| [Thai]()

#### 4. Checkpoints
- [castorini/mdpr-question-nq]() 
- [castorini/mdpr-context-nq]()


## Baselines and Evaluation
#### 1. BM25
#### 2. mDPR


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

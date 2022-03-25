# IPM-Planner

[TOC]

- 03/20/2022: Initialization.

## 1 Structure

```
IPM-Planner
├── dt_model                    - Protection time: fitting curves
│   ├── coef_dv2maxdt.bin
│   ├── coef_mradian2maxdt.bin
│   └── dtmodel.py
├── mlp_model                   - Priority: Trained MLP
│   ├── ipmodel.ckpt
│   ├── ipmodel.pt
│   └── mlp_model.py
└── utils                       - bin file io
    └── bin_file_io.py
```


## 2 Introduction

This is the project page of the paper "**Real-Time Speed Planning for Autonomous Driving in Dynamic Environment with Interaction Point Model**".

[![Watch the video](./picts/cover-IPM-k.png)](https://youtu.be/n644Pj4Q9yo)



## 3 Complementary Videos

- Pairs of interactions from the INTERACTION dataset [1], where "**x**" denotes the interaction point.

![interaction_scenes](./picts/interaction_scenes.gif)


## Reference

[1] Zhan W, Sun L, Wang D, et al. Interaction dataset: An international, adversarial and cooperative motion dataset in interactive driving scenarios with semantic maps[J]. arXiv preprint arXiv:1910.03088, 2019.

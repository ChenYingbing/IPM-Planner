# IPM-Planner

- 2022/03/20: Initialization.
- 2022/09/04: Accepted by RA-L.

## Structure

```
IPM-Planner
├── dt_model                    - Protection time: fitting curves
│   └── dtmodel.py				- fitting coeffients C_{1-4}
├── mlp_model                   - Priority: trained MLP
│   ├── ipmodel.ckpt
│   ├── ipmodel.pt
│   └── mlp_model.py
└── utils                       - bin file io
    └── bin_file_io.py
```


## Introduction

This is the project page of the paper "**Efficient Speed Planning for Autonomous Driving in Dynamic Environment with Interaction Point Model**".

**Abstract**: Safely interacting with other traffic participants is one of the core requirements for autonomous driving, especially in intersections and occlusions. Most existing approaches are designed for particular scenarios and require significant human labor in parameter tuning to be applied to different situations. To solve this problem, we first propose a learning-based Interaction Point Model (IPM), which describes the interaction between agents with the *protection time* and *interaction priority* in a unified manner. We further integrate the proposed IPM into a novel planning framework, demonstrating its effectiveness and robustness through comprehensive simulations in highly dynamic environments.

[![Watch the video](./picts/cover-IPM-k.png)](https://youtu.be/n644Pj4Q9yo)



The preprint version of our paper presenting the IPM-based planner is now available on arXiv: https://arxiv.org/abs/2209.09013.



## CITATION

```
@article{chen2022efficient,
  title={Efficient Speed Planning for Autonomous Driving in Dynamic Environment with Interaction Point Model},
  author={Chen, Yingbing and Xin, Ren and Cheng, Jie and Zhang, Qingwen and Mei, Xiaodong and Liu, Ming and Wang, Lujia},
  journal={IEEE Robotics and Automation Letters},
  year={2022},
  publisher={IEEE}
}
```



## Supplementary Videos

- Pairs of interactions from the INTERACTION dataset [1], where "**x**" denotes the interaction point.

![interaction_scenes](./picts/interaction_scenes.gif)


## Reference

[1] Zhan W, Sun L, Wang D, et al. Interaction dataset: An international, adversarial and cooperative motion dataset in interactive driving scenarios with semantic maps[J]. arXiv preprint arXiv:1910.03088, 2019.

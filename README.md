## CV Benchmarks

Benchmarks for popular classification and object detection models on CPUs and GPUs.

Pretrained model parameters provided by [gluon-cv] model zoo

**Env Setup**

* CPU: Intel(R) Xeon(R) CPU E5-2683 v3 @ 2.00GHz
* GPU: NVIDIA TITAN XP
* RAM: 252G
* OS: Ubuntu 16.04
* CUDA: 8.0.61
* cuDNN: 5.1.5
* Python: 3.6.8
* MXNet: 1.4.0 w/o mkl
* TVM: 0.6.dev

**Classification**

| Network Arch       | Input Shape | CPU time(ms) | GPU time(ms) | VRAM(MB) | TVM CPU time(ms) | TVM GPU time(ms) | TVM VRAM(MB) | Citation |
| ------------------ | ----------- | -----------: | -----------: | -------: | ---------------: | ---------------: | -----------: | :------: |
| MobileNet (1.0)    | 1x3x224x224 |        48.00 |         4.55 |      477 |             3.10 |             0.92 |          403 | \[[1]\]  |
| MobileNet v2 (1.0) | 1x3x224x224 |        62.06 |         8.53 |      483 |             3.12 |             1.65 |          407 | \[[2]\]  |
| VGG16              | 1x3x224x224 |       420.59 |         5.74 |     1577 |            82.82 |             4.23 |         1053 | \[[7]\]  |
| ResNet50           | 1x3x224x224 |        93.07 |        10.81 |      701 |            18.38 |             3.90 |          529 | \[[3]\]  |

**Detection**

| Network Arch (Backbone)   | Input Shape | CPU time(ms) | GPU time(ms) | VRAM(MB) |    TVM CPU time(ms) |    TVM GPU time(ms) |        TVM VRAM(MB) | Citation |
| ------------------------- | ----------- | -----------: | -----------: | -------: | ------------------: | ------------------: | ------------------: | :------: |
| Faster RCNN (ResNet50)    | 1x3x800x800 |     15480.15 |       371.80 |     2945 | tvm not support yet | tvm not support yet | tvm not support yet | \[[4]\]  |
| SSD (MobileNet (1.0))     | 1x3x512x512 |       408.30 |        24.29 |      775 |              300.18 | tvm not support yet | tvm not support yet | \[[5]\]  |
| SSD (ResNet50)            | 1x3x512x512 |       678.04 |        33.02 |     1065 |              377.31 | tvm not support yet | tvm not support yet | \[[5]\]  |
| YOLO v3 (MobileNet (1.0)) | 1x3x416x416 |       479.82 |        17.72 |      771 |               61.70 | tvm not support yet | tvm not support yet | \[[6]\]  |
| YOLO v3 (DarkNet53)       | 1x3x416x416 |       843.06 |        27.55 |     1109 |              119.26 | tvm not support yet | tvm not support yet | \[[6]\]  |

---

**Env Setup**

* CPU: Intel(R) Core(TM) i7-7700K CPU @ 4.20GHz
* GPU: GeForce GTX 1080 Ti
* RAM: 31.3G
* OS: Ubuntu 16.04
* CUDA: 10.0.130
* cuDNN: 7.5.0
* Python: 3.6.8
* MXNet: 1.4.0 w/ mkl
* TVM: 0.6.dev

**Classification**

| Network Arch       | Input Shape | CPU time(ms) | GPU time(ms) | VRAM(MB) | TVM CPU time(ms) | TVM GPU time(ms) | TVM VRAM(MB) | Citation |
| ------------------ | ----------- | -----------: | -----------: | -------: | ---------------: | ---------------: | -----------: | :------: |
| MobileNet (1.0)    | 1x3x224x224 |         8.30 |         2.22 |      503 |             5.92 |             0.74 |          407 | \[[1]\]  |
| MobileNet v2 (1.0) | 1x3x224x224 |        18.85 |         3.98 |      505 |             4.29 |             0.89 |          409 | \[[2]\]  |
| VGG16              | 1x3x224x224 |        89.55 |         5.46 |     1605 |           178.67 |             4.21 |         1061 | \[[7]\]  |
| ResNet50           | 1x3x224x224 |        28.13 |         6.37 |      723 |            42.74 |             3.42 |          535 | \[[3]\]  |

**Detection**

| Network Arch (Backbone)   | Input Shape | CPU time(ms) | GPU time(ms) | VRAM(MB) |    TVM CPU time(ms) |    TVM GPU time(ms) |        TVM VRAM(MB) | Citation |
| ------------------------- | ----------- | -----------: | -----------: | -------: | ------------------: | ------------------: | ------------------: | :------: |
| Faster RCNN (ResNet50)    | 1x3x800x800 |      5565.82 |       326.32 |     2949 | tvm not support yet | tvm not support yet | tvm not support yet | \[[4]\]  |
| SSD (MobileNet (1.0))     | 1x3x512x512 |        95.28 |        15.93 |      777 |              726.48 | tvm not support yet | tvm not support yet | \[[5]\]  |
| SSD (ResNet50)            | 1x3x512x512 |       211.78 |        23.25 |     1069 |              941.38 | tvm not support yet | tvm not support yet | \[[5]\]  |
| YOLO v3 (MobileNet (1.0)) | 1x3x416x416 |       165.48 |        10.96 |      775 |              156.73 | tvm not support yet | tvm not support yet | \[[6]\]  |
| YOLO v3 (DarkNet53)       | 1x3x416x416 |       315.16 |        18.64 |     1105 |              359.61 | tvm not support yet | tvm not support yet | \[[6]\]  |

---

**Env Setup**

* CPU: Intel Core i7-6700HQ @ 2.60GHz
* GPU: None
* RAM: 16.0G
* OS: macOS 10.14
* CUDA: None
* cuDNN: None
* Python: 3.6.8
* MXNet: 1.4.0 w/o mkl
* TVM: 0.6.dev

**Classification**

| Network Arch       | Input Shape | CPU time(ms) | TVM CPU time(ms) | Citation |
| ------------------ | ----------- | -----------: | ---------------: | :------: |
| MobileNet (1.0)    | 1x3x224x224 |        34.05 |             8.71 | \[[1]\]  |
| MobileNet v2 (1.0) | 1x3x224x224 |        64.42 |             8.41 | \[[2]\]  |
| VGG16              | 1x3x224x224 |       261.23 |           212.48 | \[[7]\]  |
| ResNet50           | 1x3x224x224 |        80.02 |            67.62 | \[[3]\]  |

**Detection**

| Network Arch (Backbone)   | Input Shape | CPU time(ms) |    TVM CPU time(ms) | Citation |
| ------------------------- | ----------- | -----------: | ------------------: | :------: |
| Faster RCNN (ResNet50)    | 1x3x800x800 |     16197.89 | tvm not support yet | \[[4]\]  |
| SSD (MobileNet (1.0))     | 1x3x512x512 |       372.46 |             1111.51 | \[[5]\]  |
| SSD (ResNet50)            | 1x3x512x512 |       656.17 |             1350.06 | \[[5]\]  |
| YOLO v3 (MobileNet (1.0)) | 1x3x416x416 |       562.84 |              205.64 | \[[6]\]  |
| YOLO v3 (DarkNet53)       | 1x3x416x416 |       841.82 |              533.84 | \[[6]\]  |

---

**P.S. the `TVM CPU time` of SSD should be caused by some kind of bug or mistake, the result is really the case.**

---

[gluon-cv]:https://gluon-cv.mxnet.io
[1]:https://arxiv.org/abs/1704.04861
[2]:https://arxiv.org/abs/1801.04381
[3]:https://arxiv.org/abs/1512.03385
[4]:https://arxiv.org/abs/1506.01497
[5]:https://arxiv.org/abs/1512.02325
[6]:https://arxiv.org/abs/1804.02767
[7]:https://arxiv.org/abs/1409.1556
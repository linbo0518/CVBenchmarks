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

**Classification**

| Network Arch | Input Shape | CPU time(ms) | GPU time(ms) | VRAM(MB) | Citation | 
| --- | --- | ---: | ---: | ---: | :---: |
| MobileNet (1.0) | 1x3x224x224 | 47.39 | 4.99 | 485 | \[[1]\] |
| MobileNet v2 (1.0) | 1x3x224x224 | 69.97 | 7.87 | 491 | \[[2]\] |
| ResNet50 | 1x3x224x224 | 100.24 | 8.36 | 707 | \[[3]\] |

**Detection**

| Network Arch (Backbone) | Input Shape | CPU time(ms) | GPU time(ms) | VRAM(MB) | Citation | 
| --- | --- | ---: | ---: | ---: | :---: |
| Faster RCNN (ResNet50) | 1x3x800x800 | 15480.15 | 335.64 | 2955 | \[[4]\] |
| SSD (MobileNet (1.0)) | 1x3x512x512 | 468.88 | 24.21 | 783 | \[[5]\] |
| SSD (ResNet50) | 1x3x512x512 | 718.59 | 31.37 | 1075 | \[[5]\] |
| YOLO v3 (MobileNet (1.0)) | 1x3x416x416 | 500.80 | 19.32 | 779 | \[[6]\] |
| YOLO v3 (DarkNet53) | 1x3x416x416 | 865.41 | 24.96 | 1115 | \[[6]\] |

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

**Classification**

| Network Arch | Input Shape | CPU time(ms) | GPU time(ms) | VRAM(MB) | Citation | 
| --- | --- | ---: | ---: | ---: | :---: |
| MobileNet (1.0) | 1x3x224x224 | 8.23 | 2.19 | 511 | \[[1]\] |
| MobileNet v2 (1.0) | 1x3x224x224 | 8.15 | 3.91 | 513 | \[[2]\] |
| ResNet50 | 1x3x224x224 | 27.48 | 6.29 | 731 | \[[3]\] |

**Detection**

| Network Arch (Backbone) | Input Shape | CPU time(ms) | GPU time(ms) | VRAM(MB) | Citation | 
| --- | --- | ---: | ---: | ---: | :---: |
| Faster RCNN (ResNet50) | 1x3x800x800 | 5565.82 | 303.54 | 2957 | \[[4]\] |
| SSD (MobileNet (1.0)) | 1x3x512x512 | 90.14 | 13.79 | 785 | \[[5]\] |
| SSD (ResNet50) | 1x3x512x512 | 198.66 | 22.53 | 1077 | \[[5]\] |
| YOLO v3 (MobileNet (1.0)) | 1x3x416x416 | 155.25 | 9.80 | 783 | \[[6]\] |
| YOLO v3 (DarkNet53) | 1x3x416x416 | 296.47 | 17.73 | 1113 | \[[6]\] |

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

| Network Arch | Input Shape | CPU time(ms) | TVM CPU time(ms) | Citation | 
| --- | --- | ---: | ---: | :---: |
| MobileNet (1.0) | 1x3x224x224 | 34.05 | 8.71 | \[[1]\] |
| MobileNet v2 (1.0) | 1x3x224x224 | 64.42 | 8.41 | \[[2]\] |
| VGG16 | 1x3x224x224 | 261.23 | 212.48 | \[[7]\] |
| ResNet50 | 1x3x224x224 | 80.02 | 67.62 | \[[3]\] |

**Detection**

| Network Arch (Backbone) | Input Shape | CPU time(ms) | TVM CPU time(ms) | Citation | 
| --- | --- | ---: | ---: | :---: |
| Faster RCNN (ResNet50) | 1x3x800x800 | 16197.89 | tvm not support yet | \[[4]\] |
| SSD (MobileNet (1.0)) | 1x3x512x512 | 372.46 | 1111.51 | \[[5]\] |
| SSD (ResNet50) | 1x3x512x512 | 656.17 | 1350.06 | \[[5]\] |
| YOLO v3 (MobileNet (1.0)) | 1x3x416x416 | 562.84 | 205.64 | \[[6]\] |
| YOLO v3 (DarkNet53) | 1x3x416x416 | 841.82 | 533.84 | \[[6]\] |

**P.S.: the `TVM CPU time` of SSD should be caused by some kind of bug or mistake, the result on my MacBook Pro (15-inch, 2016) is really the case.**

---

[gluon-cv]:https://gluon-cv.mxnet.io
[1]:https://arxiv.org/abs/1704.04861
[2]:https://arxiv.org/abs/1801.04381
[3]:https://arxiv.org/abs/1512.03385
[4]:https://arxiv.org/abs/1506.01497
[5]:https://arxiv.org/abs/1512.02325
[6]:https://arxiv.org/abs/1804.02767
[7]:https://arxiv.org/abs/1409.1556
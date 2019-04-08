import sys
import numpy as np
import mxnet as mx
import gluoncv as gcv
import tvm
from tvm import relay
from tvm.contrib import graph_runtime
from tvm.contrib.download import download_testdata
from time import time


def get_input(input_shape):
    im_fname = download_testdata(
        'https://github.com/dmlc/web-data/blob/master/' +
        'gluoncv/detection/street_small.jpg?raw=true',
        'street_small.jpg',
        module='data')
    x, img = gcv.data.transforms.presets.ssd.load_test(im_fname,
                                                       short=input_shape[2])
    return x.asnumpy().astype('float32')


if __name__ == "__main__":
    net_name_list = [
        'mobilenet1.0',
        'mobilenetv2_1.0',
        'vgg16',
        'resnet50_v1',
        'ssd_512_mobilenet1.0_coco',
        'ssd_512_resnet50_v1_coco',
        'yolo3_mobilenet1.0_coco',
        'yolo3_darknet53_coco',
        'faster_rcnn_resnet50_v1b_coco',
    ]
    input_shape_list = [
        (1, 3, 224, 224),
        (1, 3, 224, 224),
        (1, 3, 224, 224),
        (1, 3, 224, 224),
        (1, 3, 512, 512),
        (1, 3, 512, 512),
        (1, 3, 416, 416),
        (1, 3, 416, 416),
        (1, 3, 800, 800),
    ]

    # mx_ctx = mx.cpu()
    mx_ctx = mx.gpu()

    idx = int(sys.argv[1])
    model_name = net_name_list[idx]
    input_shape = input_shape_list[idx]
    mx_result = list()

    # get input
    x = get_input(input_shape)
    mx_input = mx.nd.array(x, ctx=mx_ctx)

    # get model
    net = gcv.model_zoo.get_model(model_name, pretrained=True, ctx=mx_ctx)
    net.hybridize()

    print('start', model_name, 'speed benchmark')

    for idx in range(10):
        # warm up
        mx_out = net(mx_input)
        mx.nd.waitall()
        # speed benchmark
        start = time()
        for _ in range(100):
            mx_out = net(mx_input)
            mx.nd.waitall()
        mx_result.append(((time() - start) / 100) * 1000)
        print('mxnet:', idx, 'time', (((time() - start) / 100) * 1000))

    print('mxnet:', model_name, np.min(mx_result), np.mean(mx_result),
          np.max(mx_result))

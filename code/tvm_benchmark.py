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


def compile_model(net, input_shape, target):
    shape_dict = {'data': input_shape}
    tvm_net, tvm_params = relay.frontend.from_mxnet(net, shape_dict)
    with relay.build_config(opt_level=3):
        graph, lib, params = relay.build(tvm_net, target, params=tvm_params)
    return graph, lib, params


def run(graph, lib, params, x, ctx):
    m = graph_runtime.create(graph, lib, ctx)
    tvm_input = tvm.nd.array(x, ctx=ctx)
    m.set_input('data', tvm_input)
    m.set_input(**params)
    return m


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

    # target = tvm.target.create('llvm -mcpu=haswell')
    # tvm_ctx = tvm.cpu()
    target = tvm.target.cuda('1080ti')
    tvm_ctx = tvm.gpu()

    idx = int(sys.argv[1])
    model_name = net_name_list[idx]
    input_shape = input_shape_list[idx]
    tvm_result = list()

    # get input
    x = get_input(input_shape)

    # get model
    net = gcv.model_zoo.get_model(model_name, pretrained=True)

    # compile model
    graph, lib, params = compile_model(net, input_shape, target)
    m = run(graph, lib, params, x, tvm_ctx)

    print('start', model_name, 'speed benchmark')

    for idx in range(10):
        # warm up
        m.run()
        tvm_out = m.get_output(0)
        # speed benchmark
        start = time()
        for _ in range(100):
            m.run()
            tvm_out = m.get_output(0)
        tvm_result.append(((time() - start) / 100) * 1000)
        print(' tvm :', idx, 'time', (((time() - start) / 100) * 1000))

    print(' tvm :', model_name, np.min(tvm_result), np.mean(tvm_result),
          np.max(tvm_result))

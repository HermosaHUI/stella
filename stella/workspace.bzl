
def if_tf(if_true, if_false = []):
    return select({
        str(Label("//stella:with_tf_support")): if_true,
        "//conditions:default": if_false,
    })

def if_onnx(if_true, if_false = []):
    return select({
        str(Label("//stella:with_onnx_support")): if_true,
        "//conditions:default": if_false,
    })

def if_pytorch(if_true, if_false = []):
    return select({
        str(Label("//stella:with_pytorch_support")): if_true,
        "//conditions:default": if_false,
    })

import src.models as models

MODEL_DISPATCHER = {
    "alexnet": models.AlexNet,
    "vgg11": models.VGG11,
    "resnet34": models.ResNet34,
}

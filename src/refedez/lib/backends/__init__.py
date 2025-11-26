from refedez.lib.backends.numpy import FederatedNumpy
from refedez.lib.backends.torch import FederatedTorch
from refedez.lib.config import Backend


def get_backend_from_type(cls):
    if issubclass(cls, FederatedTorch):
        return Backend.PYTORCH
    elif issubclass(cls, FederatedNumpy):
        return Backend.NUMPY
    else:
        raise NotImplementedError(f"ReFedEz doesn't support {cls} types")

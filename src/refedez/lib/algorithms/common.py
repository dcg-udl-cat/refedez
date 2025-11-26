from abc import ABC
from enum import Enum

from nvflare.app_common.workflows.model_controller import ModelController


class FedAlgorithmBase(ABC):
    def get_controller(self) -> ModelController:
        pass


class FedAlgorithm(Enum):
    FED_AVG = "FED_AVG"
    FED_OPT = "FED_OPT"
    SCAFFOLD = "SCAFFOLD"

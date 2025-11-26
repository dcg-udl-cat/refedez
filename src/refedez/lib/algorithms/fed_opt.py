from dataclasses import dataclass

import torch
from nvflare.app_common.workflows.model_controller import ModelController
from nvflare.app_opt.pt.fedopt_ctl import FedOpt

from refedez.lib.algorithms.common import FedAlgorithmBase
from refedez.lib.config import JobConfiguration, Backend


@dataclass(frozen=True)
class FedOptAlgorithm(FedAlgorithmBase):
    source_model: torch.nn.Module

    def get_controller(self) -> ModelController:
        return FedOpt(source_model=self.source_model)

    @staticmethod
    def from_(config: JobConfiguration, persistor_id: str) -> "FedOptAlgorithm":
        if config.type != Backend.PYTORCH:
            raise ValueError("FedOpt is only valid if you're using pytorch")
        return FedOptAlgorithm(source_model=config.model_cls)

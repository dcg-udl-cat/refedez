from dataclasses import dataclass

from nvflare.app_common.workflows.fedavg import FedAvg
from nvflare.app_common.workflows.model_controller import ModelController

from refedez.lib.algorithms.common import FedAlgorithmBase

from refedez.lib.config import JobConfiguration


@dataclass(frozen=True)
class FedAvgAlgorithm(FedAlgorithmBase):
    num_clients: int
    num_rounds: int
    persistor_id: str

    def get_controller(self) -> ModelController:
        return FedAvg(
            num_clients=self.num_clients,
            num_rounds=self.num_rounds,
            persistor_id=self.persistor_id,
        )

    @staticmethod
    def from_(config: JobConfiguration, persistor_id: str) -> "FedAvgAlgorithm":
        return FedAvgAlgorithm(
            num_clients=config.num_clients,
            num_rounds=config.num_rounds,
            persistor_id=persistor_id,
        )

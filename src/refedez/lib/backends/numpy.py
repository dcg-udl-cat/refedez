import os
from abc import ABC
from typing import Any

from nvflare import FedJob
from nvflare.app_common.np.np_model_persistor import NPModelPersistor
from nvflare.client.config import ExchangeFormat
from nvflare.job_config.script_runner import ScriptRunner, FrameworkType

from refedez.lib.algorithms.factory import from_algorithm
from refedez.lib.config import JobConfiguration
from refedez.lib.constants import ENV_RUN_JOB_STAGE


class FederatedNumpy(ABC):
    """Abstract base class for federated learning models using NumPy.

    This class defines the interface for models that participate in federated learning
    workflows using NumPy arrays for weight representation.

    Subclasses must implement the abstract methods to define the model's forward pass,
    weight retrieval and setting, and training step logic.
    """

    def forward(self, x: Any):
        raise NotImplementedError()

    def get_weights(self) -> Any:
        raise NotImplementedError()

    def set_weights(self, new_weights: Any) -> None:
        raise NotImplementedError()

    def train_step(self, learning_rate=1.0) -> Any:
        raise NotImplementedError()


def __create_numpy_job(config: JobConfiguration, output_path: str):
    name = "fed_numpy"
    job = FedJob(name=name, min_clients=config.num_clients)

    persistor = NPModelPersistor(model_dir="/models", model_name="server.npy")
    persistor_id = job.to_server(persistor, config.server.name)

    controller = from_algorithm(config.algorithm, config, persistor_id).get_controller()
    job.to_server(controller, config.server.name)

    # Define script runner for clients
    train_script = config.to_execute_script_path
    script_runner = ScriptRunner(
        script=train_script,
        script_args=f"{ENV_RUN_JOB_STAGE}",
        launch_external_process=False,
        framework=FrameworkType.NUMPY,
        server_expected_format=ExchangeFormat.NUMPY,
        params_transfer_type="FULL",
    )

    # Assign to clients
    for client in config.clients:
        client_name = client.name
        job.to(script_runner, client_name, tasks=["train"])

    # Export job folder
    job.export_job(job_root=output_path)
    return os.path.join(output_path, name)


def __execute(model: FederatedNumpy):
    pass

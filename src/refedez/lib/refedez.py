import sys
from inspect import getfile
from typing import List

from refedez.lib.algorithms.common import FedAlgorithm
from refedez.lib.backends import Backend
from refedez.lib.backends.numpy import __execute as execute_numpy
from refedez.lib.backends.torch import __execute as execute_torch
from refedez.lib.backends.tensorflow import __execute as execute_tensorflow
from refedez.lib.config import JobConfiguration, Server, Client
from refedez.lib.constants import ENV_RUN_JOB_STAGE
from refedez.lib.job import execute_job_config


def Federated(
    server: Server,
    clients: List[Client],
    refedez_config: str,
    num_rounds=1,
    backend=Backend.PYTORCH,
    algorithm=FedAlgorithm.FED_AVG,
):
    """
     Runs a federated learning experiment using the specified backend and configuration.

    This function orchestrates the communication and training rounds between a central
    server and multiple clients according to the provided `refedez_config` file.
    The backend determines the machine learning framework used (e.g., PyTorch or NumPy).

    Args:
        server (Server): The federated server responsible for aggregating model updates
            and coordinating the training process.
        clients (List[Client]): A list of participating clients, each responsible for
            local model training and update submission.
        refedez_config (str): Path to the ReFedEz configuration file (YAML or JSON)
            that defines the experiment setup, data paths, and hyperparameters.
        num_rounds (int, optional): Number of federated training rounds to execute.
            Defaults to 1.
        backend (Backend, optional): Backend to use for computation. Can be one of the
            supported frameworks in `Backend` (e.g., `Backend.PYTORCH`, `Backend.NUMPY`).
            Defaults to `Backend.PYTORCH`.
        algorithm (FedAlgorithm, optional): Backend to use for computation. Can be one of the
            supported frameworks in `FedAlgorithm` (e.g., `FedAlgorithm.FED_AVG`, `FedAlgorithm.SCAFFOLD`).
            Defaults to `FedAlgorithm.FED_AVG`.

    Returns:
        None: This function does not return a value directly, but performs training,
        logging, and potentially saves model artifacts or metrics as side effects.

    Raises:
        ValueError: If the configuration file path is invalid or unreadable.
        RuntimeError: If the backend fails to initialize or training fails mid-process.
        ConnectionError: If communication with clients fails during aggregation rounds.

    Example:
    """

    def decorator(cls):
        # Only run the logic if this module is executed as __main__
        if cls.__module__ == "__main__":
            args = sys.argv
            should_execute = len(args) >= 2 and ENV_RUN_JOB_STAGE in args[1]

            if should_execute:
                if backend == Backend.PYTORCH:
                    execute_torch(cls())
                elif backend == Backend.NUMPY:
                    execute_numpy(cls())
                elif backend == Backend.TENSORFLOW:
                    execute_tensorflow(cls())
                else:
                    raise NotImplementedError(f"Unsupported backend {backend}")
            else:
                script_path = getfile(cls)
                job_config = JobConfiguration(
                    server=server,
                    clients=clients,
                    refedez_config=refedez_config,
                    to_execute_script_path=script_path,
                    num_rounds=num_rounds,
                    model_cls=cls,
                    type=backend,
                    algorithm=algorithm,
                )
                execute_job_config(job_config)
                sys.exit(0)
        return cls

    return decorator

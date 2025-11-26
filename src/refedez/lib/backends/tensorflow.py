import os

import nvflare.client as flare
from nvflare import FedJob
from nvflare.client.config import ExchangeFormat
from nvflare.job_config.script_runner import ScriptRunner, FrameworkType
import tensorflow as tf
from nvflare.app_opt.tf.model_persistor import TFModelPersistor
from refedez.lib.algorithms.factory import from_algorithm
from refedez.lib.config import JobConfiguration
from refedez.lib.constants import ENV_RUN_JOB_STAGE


class FederatedTensorFlow(tf.keras.Model):
    """Base class for federated learning models using TensorFlow (Keras).

    This class extends tf.keras.Model and provides an interface for models
    in federated learning scenarios. It handles initialization
    and defines abstract methods for weight management and local training.
    """

    def __init__(self):
        super(FederatedTensorFlow, self).__init__()

    def forward(self, inputs):
        pass

    def get_weights(self):
        pass

    def set_weights(self, new_weights):
        pass

    def train_step(self, learning_rate=1.0):
        pass


def __create_tf_job(config: JobConfiguration, output_path: str):
    name = "tf_job"
    job = FedJob(name=name, min_clients=config.num_clients)

    persistor = TFModelPersistor(
        model=config.model_cls(), save_name=config.server.save_model_path
    )
    persistor_id = job.to_server(persistor, config.server.name)

    controller = from_algorithm(config.algorithm, config, persistor_id).get_controller()
    job.to_server(controller, config.server.name)

    train_script = config.to_execute_script_path
    for client in config.clients:
        script_runner = ScriptRunner(
            script=train_script,
            script_args=f"{ENV_RUN_JOB_STAGE}",
            launch_external_process=False,
            framework=FrameworkType.TENSORFLOW,
            server_expected_format=ExchangeFormat.KERAS_LAYER_WEIGHTS,  # Use Keras weights format for exchange
            params_transfer_type="FULL",
        )
        job.to(script_runner, client.name, tasks=["train"])

    job.export_job(job_root=output_path)
    return os.path.join(output_path, name)


def __execute(model: FederatedTensorFlow):
    flare.init()
    sys_info = flare.system_info()
    client_name = sys_info["site_name"]
    print(f"Client {client_name} initialized")

    while flare.is_running():
        input_model = flare.receive()
        print(f"Client {client_name}, current_round = {input_model.current_round}")
        if input_model.params == {}:
            params = model.get_weights()
        else:
            params = input_model.params  # This could be a list or dict of weights
        model.set_weights(params)
        print(
            f"Client {client_name}: Loaded global weights (round {input_model.current_round})"
        )

        print(f"Client {client_name}: Starting local training...")
        _ = model.train_step(learning_rate=1.0)
        print(
            f"Client {client_name}: Finished training for round {input_model.current_round}"
        )

        updated_weights = model.get_weights()
        output_model = flare.FLModel(
            params=updated_weights,
            params_type="FULL",
            current_round=input_model.current_round,
        )
        print(
            f"Client {client_name}: Sending updated weights to server for aggregation."
        )
        flare.send(output_model)

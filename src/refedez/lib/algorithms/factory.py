from refedez.lib.algorithms.common import FedAlgorithm, FedAlgorithmBase
from refedez.lib.algorithms.fed_avg import FedAvgAlgorithm
from refedez.lib.algorithms.fed_opt import FedOptAlgorithm
from refedez.lib.algorithms.scaffold import ScaffoldAlgorithm
from refedez.lib.config import JobConfiguration


def from_algorithm(
    algorithm: FedAlgorithm,
    config: JobConfiguration,
    persistor_id: str,
) -> FedAlgorithmBase:
    if FedAlgorithm.FED_AVG == algorithm:
        return FedAvgAlgorithm.from_(config, persistor_id)
    elif FedAlgorithm.FED_OPT == algorithm:
        return FedOptAlgorithm.from_(config, persistor_id)
    elif FedAlgorithm.SCAFFOLD == algorithm:
        return ScaffoldAlgorithm.from_(config, persistor_id)
    else:
        raise ValueError(f"Not supported algorithm: {algorithm}")

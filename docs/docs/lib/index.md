# Library API

The ReFedEz library provides a high-level API for implementing federated learning algorithms. It abstracts away the complexities of distributed communication, allowing you to focus on your machine learning models and training logic.

## What the Library Does

The library enables you to write federated learning code that runs seamlessly across distributed machines. Instead of dealing with low-level networking, serialization, and coordination, you write standard ML code and the library handles:

- **Model Distribution**: Automatically sending model weights between server and clients
- **Aggregation**: Coordinating federated averaging and other aggregation strategies
- **Lifecycle Management**: Handling training rounds, validation, and synchronization
- **Framework Integration**: Supporting PyTorch and NumPy backends out of the box

## Where to Use It

Use the library in your `model.py` or training script files. This is where you define your federated learning algorithm. The library is designed for:

- **Research Prototyping**: Quickly test federated algorithms without infrastructure setup
- **Production ML Code**: Write clean, framework-agnostic federated training code
- **Algorithm Development**: Focus on the ML logic while the library handles distribution

## Basic Usage

1. **Choose a Backend**: Inherit from `FederatedTorch` for PyTorch models or `FederatedNumpy` for NumPy-based implementations.

2. **Use the @Federated Decorator**: Apply this decorator to your class to specify the server and client configurations. The decorator automatically reads from your `refedez.yaml` and connects to the running ReFedEz deployment.

3. **Implement Required Methods**:
   - `get_weights()`: Return current model parameters
   - `set_weights(weights)`: Load new model parameters
   - `train_step()`: Perform one round of local training
   - `validate(weights)`: Evaluate model performance

## Example

```python
from refedez.lib import Federated, Server, Client, FederatedTorch


@Federated(
    server=Server("server.localhost", save_model_path="/models/final_model.pt"),
    clients=[Client("site1"), Client("site2")],
    refedez_config="./refedez.yaml"
)
class MyFederatedModel(FederatedTorch):
    def __init__(self):
        super().__init__()
        # Your model initialization here

    def get_weights(self):
        # Return model weights
        pass

    def set_weights(self, weights):
        # Load model weights
        pass

    def train_step(self):
        # Local training logic
        pass

    def validate(self, weights):
        # Validation logic
        pass
```

When you run this script, the library automatically:
- Connects to the ReFedEz-deployed server and clients
- Coordinates federated training rounds
- Handles model synchronization and aggregation

---

## Library Definitions

::: refedez.lib
    handler: python
    options:
      members_order: source
      show_submodules: true

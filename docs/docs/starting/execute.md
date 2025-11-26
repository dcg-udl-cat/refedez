# Execute

Once your ReFedEz project is configured and started (as described in [Start](start.md)), you can execute federated learning jobs. This section uses the CIFAR-10 example to demonstrate the execution process.

## Prerequisites

Before running the example:

1. **Install Dependencies**: Ensure all required packages are installed. From the project directory:
   ```bash
   uv sync
   ```
   Or with pip:
   ```bash
   pip install -e .
   ```

2. **Prepare Directories**: Create the necessary directories for datasets and models:
   ```bash
   mkdir -p /ds
   mkdir -p /models
   ```

3. **Download Dataset**: Download the CIFAR-10 dataset to the expected location (on each client):
   ```bash
   # Using torchvision (will be done automatically by the script, but ensure it's available)
   python -c "import torchvision; torchvision.datasets.CIFAR10(root='/ds/cifar10', train=True, download=True)"
   python -c "import torchvision; torchvision.datasets.CIFAR10(root='/ds/cifar10', train=False, download=True)"
   ```

## Running the Federated Learning Job

The CIFAR-10 example uses a PyTorch-based federated learning implementation. The `model.py` file contains a `CIFAR10Federated` class decorated with `@Federated`, which automatically handles the distributed training across the configured server and clients.

To start the federated training:

```bash
python model.py
```

This command:
- Initializes the federated learning process using the configuration in `refedez.yaml`
- Loads the CIFAR-10 dataset from `/ds/cifar10`
- Trains a CNN model across the distributed clients (`site1` and `site2`) and server (`server.localhost`)
- Aggregates model updates using federated averaging
- Saves trained models to `/models/test.pl` on the server


## Expected Output

- **Models**: Trained model checkpoints saved to `/models/`

After completion, you can stop the deployment:

```bash
refedez stop
```

And clean up temporary files:

```bash
refedez clean
```

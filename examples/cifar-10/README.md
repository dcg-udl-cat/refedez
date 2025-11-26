# CIFAR-10 Model example

This example expects the following project structure:

```
/models     # directory where trained models will be saved
/ds         # directory where the dataset will be stored
```

Make sure both directories exist and are writable by whatever process runs your training script (e.g., your user, a container, or a service). If needed:

```
mkdir -p /models /ds
chmod u+rwx /models /ds
```

## Download the Dataset

Download the CIFAR-10 (Python version) archive:

https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz

## Prepare the Dataset

Move the downloaded file into the /ds directory and extract it:

```
cd ds
tar -xzf cifar-10-python.tar.gz
```
The extracted folder (e.g., cifar-10-batches-py) contains the dataset batches used by the example code.

## Execute ReFedEz

Now just `start` ReFedEz and execute `python model.py` (with the correct python env).

# Start

Once you have configured your project files (`project.yml` and `refedez.yaml`) as described in the [Configure](configure.md) section, you can deploy and start your federated learning setup.

## Starting the Project

Run the following command from your project directory:

```bash
refedez start
```

This command performs the following steps:

1. **Build Environments**: Creates reproducible environments for each client and server using Nix, ensuring all dependencies (Python, libraries, etc.) are consistent across machines.
2. **Deploy to Remote Machines**: If any machines are configured as `remote` in `refedez.yaml`, ReFedEz securely transfers the built environments via SSH.
3. **Launch NVIDIA FLARE Apps**: Starts the appropriate NVIDIA FLARE applications (server or client) on each machine, initializing the federated learning process.

The command will provide output showing the progress of building, deploying, and starting each component.

## Checking Status

After starting, you can check the status of your deployment and see where project files are stored on each machine:

```bash
refedez status
```

This command displays:
- The current state of each participant (running, stopped, etc.)
- The locations of project files and logs on local and remote machines
- Any errors or issues that may have occurred during startup

Use `refedez status` to verify that all components are running correctly before proceeding with your federated learning tasks.

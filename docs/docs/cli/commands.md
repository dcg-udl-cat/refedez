# Commands

ReFedEz provides a command-line interface (CLI) with four main commands to manage your federated learning deployments. All commands operate on the `refedez.yaml` configuration file in the current directory by default.

## start

Starts the federated learning deployment by building environments, provisioning NVIDIA FLARE, and launching services on all configured machines.

**Usage:**
```bash
refedez start
```

**What it does:**

- Builds reproducible environments using Nix for each machine
- Provisions Nvidia Flare configurations
- Patches provisioned files with the built environments
- Uploads and starts services on local and remote machines via SSH
- Updates project state to running

**Requirements:** Project must not already be running. Requires `refedez.yaml` and `project.yml` in the current directory.

## status

Displays the current status of the ReFedEz project, including running machines and their configurations.

**Usage:**
```bash
refedez status
```

**Output:**

- For running projects: A table showing machine names, types (local/remote), file folders, IPs, and users
- For clean projects: Confirmation that the project is clean
- For dirty projects: Warning about old builds and unnecessary files

**Requirements:** Valid `refedez.yaml` configuration file.

## stop

Stops all running federated learning services by signaling shutdown to each machine.

**Usage:**
```bash
refedez stop
```

**What it does:**

- Creates shutdown signal files on all machines (local and remote)
- NVIDIA FLARE services detect the shutdown file and terminate gracefully
- Updates project state to dirty (ready for cleanup)

**Requirements:** Project must be in a running state.

## clean

Removes temporary build files and cleans up the project workspace.

**Usage:**

```bash
refedez clean
```

**What it does:**

- Deletes the entire `.refedez` folder and all temporary files
- Resets the project to a clean state

**Requirements:** Project must be in a dirty state (after stopping). This command is destructive and cannot be undone.

# Configure

An ReFedEz project uses two main configuration files to define and deploy your federated learning setup:

## project.yml (NVIDIA FLARE Configuration)

This is the standard NVIDIA FLARE project configuration file that defines the federated learning participants, their roles, and communication settings. You don't need to deeply understand or modify this file manually – ReFedEz handles the integration. However, ensure that the participant names (servers, clients, and admins) in this file match exactly with those defined in your `refedez.yaml`.

For example, if `project.yml` defines participants named `server.localhost`, `site1`, and `site2`, your `refedez.yaml` must reference the same names.

## refedez.yaml (ReFedEz Configuration)

This file configures the machines and environments for each participant in your federated learning project. It tells ReFedEz how to deploy and run the services on different machines.

### Structure and Attributes

- **refedez** (object): Global ReFedEz settings.
  - `folder` (string): Directory where ReFedEz stores temporary files and build artifacts (e.g., `./.refedez`).
  - `capabilities` (string): Path to the `project.yml` file (e.g., `./project.yml`).

- **machines** (object): Defines each machine participating in the federation. Keys are participant names matching `project.yml`.
  - `type` (string): Connection type. Options: `"local"` (runs on the same machine) or `"remote"` (connects via SSH).
  - `ip` (string, optional): IP address or hostname for remote machines (required for `type: "remote"`).
  - `user` (string, optional): SSH username for remote machines (required for `type: "remote"`).

- **project** (object): Specifies the working directory for each participant.
  - `folder` (string): Path to the project directory on the target machine (e.g., `.` for current directory).

### Example Configurations

#### Local Setup (All on Same Machine)

```yaml
refedez:
  folder: ./.refedez
  capabilities: ./project.yml

machines:
  server.localhost:
    type: local
  site1:
    type: local
  site2:
    type: local

project:
  server.localhost:
    folder: .
  site1:
    folder: .
  site2:
    folder: .
```

#### Remote Setup (Distributed Machines)

```yaml
refedez:
  folder: ./.refedez
  capabilities: ./project.yml

machines:
  server.localhost:
    type: remote
    ip: server.example.com
    user: ubuntu
  site1:
    type: remote
    ip: 192.168.1.100
    user: researcher
  site2:
    type: remote
    ip: 192.168.1.101
    user: researcher

project:
  server.localhost:
    folder: /home/ubuntu/federated-project
  site1:
    folder: /home/researcher/federated-project
  site2:
    folder: /home/researcher/federated-project
```

In the remote example, ensure SSH keys are set up for passwordless authentication between your local machine and the remote hosts.

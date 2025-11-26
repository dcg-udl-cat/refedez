# CLI Reference

The ReFedEz CLI provides a simple interface to manage federated learning deployments. It handles building environments, deploying to machines, and controlling the lifecycle of your federated projects.

## Getting Started

The CLI workflow follows these steps:

- [Requirements](../starting/requirements.md): Ensure your network and machines are set up
- [Configure](../starting/configure.md): Set up `project.yml` and `refedez.yaml`
- [Start](../starting/start.md): Deploy and launch services
- [Execute](../starting/execute.md): Run your federated learning jobs

## Commands

See [Commands](commands.md) for detailed documentation of all available CLI commands:

- `refedez start` - Build and deploy federated services
- `refedez status` - Check deployment status
- `refedez stop` - Stop running services
- `refedez clean` - Clean up temporary files

## Project Structure

ReFedEz projects typically include:

- `project.yml` - NVIDIA FLARE configuration (participants, certificates, etc.)
- `refedez.yaml` - ReFedEz-specific settings (machines, environments)
- `model.py` - Your federated learning code
- `.refedez/` - Temporary folder created during deployment

## Configuration Files

### refedez.yaml

Defines machines and their connection details:

```yaml
refedez:
  folder: ./.refedez
  capabilties: ./project.yml

machines:
  server.localhost:
    type: local
  client1:
    type: remote
    ip: 192.168.1.100
    user: researcher

project:
  server.localhost:
    folder: .
  client1:
    folder: /home/researcher/project
```

### project.yml

NVIDIA FLARE configuration defining participants and their roles. ReFedEz uses this to provision the federated setup but you generally don't need to modify it manually.

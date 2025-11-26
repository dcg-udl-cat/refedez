# State Management

ReFedEz uses a state management strategy similar to [Terraform's state](https://developer.hashicorp.com/terraform/language/state) system. This approach tracks the current status of your federated learning deployment, including which machines are running, their configurations, and temporary file locations.

## How State Works

When you run `refedez start`, ReFedEz:

- Builds and deploys environments to your machines
- Records the deployment details in a local state file
- Updates the state to reflect that services are running

The state file is stored in the `.refedez` folder and contains information about:

- Running machines and their temporary directories
- Deployed file paths
- Connection details for remote machines

## Status vs. Reality

When you check `refedez status`, you're viewing the recorded state, not necessarily the current reality. Machines may have:

- Crashed or been restarted externally
- Lost network connectivity
- Been manually stopped

This is expected behavior and mirrors how Terraform handles infrastructure state. The state represents the "desired" or "last known" status, not a real-time health check.

## Stop and Clean Commands

### Stop Command

`refedez stop` gracefully shuts down services by creating shutdown signal files on each machine. If a machine has already stopped (e.g., crashed), the command completes successfully without errors. This ensures the stop operation is idempotent and safe to run multiple times.

### Clean Command

`refedez clean` removes all temporary files and the state information when the project is in a "dirty" state (after stopping). This is necessary because:

- Stopped machines may leave behind temporary directories
- State files can become stale if machines die unexpectedly
- Clean ensures a fresh start for the next deployment

Always run `refedez clean` after stopping to reset your project to a clean state.

## Best Practices

- Run `refedez status` to check recorded state before making changes
- Use `refedez stop` to gracefully shut down (safe even if already stopped)
- Run `refedez clean` after stopping to remove temporary files
- If machines die unexpectedly, the state may be outdated – clean and restart as needed

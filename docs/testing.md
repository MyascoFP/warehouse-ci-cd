
# Testing and CI/CD

## Automated tests

The project uses Pytest for unit testing.

Run tests locally:

    python -m pytest -v

## GitHub Actions

The CI pipeline is configured in:

    .github/workflows/main.yml

The pipeline performs:

1. Source code checkout.
2. Python environment setup.
3. Dependency installation.
4. Automated test execution.

## Branches

- `main` - stable version.
- `development` - development branch.
- `release` - release preparation.

## Releases

The first stable release is `v1.0.0`.

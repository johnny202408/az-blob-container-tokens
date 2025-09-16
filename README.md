# Azure Blob Storage with SAS Tokens Terraform Module

This Terraform configuration provisions an Azure Blob Storage environment including a storage account, a private blob container, and generates SAS tokens with specific permissions. The SAS tokens are saved as local files for secure use.

## Features

- Uses the AzureRM provider for resource provisioning.
- Creates or references an existing Resource Group.
- Creates a Storage Account with blob versioning and change feed enabled.
- Creates a private Blob Container within the Storage Account.
- Generates two SAS tokens for the Blob Container:
  - **Write SAS Token:** Allows add, create, and write permissions.
  - **Read/Delete SAS Token:** Allows read, list, and delete permissions.
- SAS tokens have configurable expiry duration.
- Saves SAS tokens to local text files for easy access.
- Outputs relevant resource names, keys, endpoints, and SAS tokens.

## Prerequisites

- Terraform version that supports required providers (azurerm ~> 3.0, time ~> 0.9).
- Azure account with sufficient permissions to create or manage resource groups and storage accounts.
- Optional: An existing Resource Group with the specified name or uncomment resource group creation block.

## Usage

1. Clone or download this Terraform configuration.
2. Adjust Terraform variables as needed (see below).
3. Initialize Terraform:


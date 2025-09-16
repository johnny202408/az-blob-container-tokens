#!/usr/bin/env python3
import unittest
import os
import time
from azure.storage.blob import BlobClient

class TestSASTokens(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # For demo: generate a unique blob name
        ts = int(time.time())
        cls.blob_name = f"test-{ts}.txt"

        # Read SAS tokens from files (Terraform created these)
        with open("write_sas_token.txt", "r") as f:
            write_sas = f.read().strip()
        with open("read_delete_sas_token.txt", "r") as f:
            read_delete_sas = f.read().strip()

        # Storage account + container info (hardcoded or from env)
        account_name = "stgblobabc0001"
        container_name = "blob-container-01"
        blob_base_url = f"https://{account_name}.blob.core.windows.net/{container_name}/{cls.blob_name}"

        # Build full SAS URLs
        cls.write_sas_url = blob_base_url + write_sas
        cls.read_delete_sas_url = blob_base_url + read_delete_sas

        print("\n=== SAS Token Test Setup ===")
        print(f"Blob name: {cls.blob_name}")
        print(f"Write SAS blob URL: {cls.write_sas_url}")
        print(f"Read/Delete SAS blob URL: {cls.read_delete_sas_url}")
        print("============================\n")

    def test_full_cycle(self):
        # Upload with write SAS
        blob_client = BlobClient.from_blob_url(self.write_sas_url)
        blob_client.upload_blob(b"Hello World", overwrite=True)

        # Read with read/delete SAS
        read_client = BlobClient.from_blob_url(self.read_delete_sas_url)
        content = read_client.download_blob().readall()
        self.assertEqual(content, b"Hello World")

        # Delete with read/delete SAS
        read_client.delete_blob()
        with self.assertRaises(Exception):  # Expect BlobNotFound
            read_client.download_blob().readall()


if __name__ == "__main__":
    unittest.main()

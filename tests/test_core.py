import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from file_manager import listar_imagens
from gemini_client import extrair_texto_da_imagem


class FileManagerTests(unittest.TestCase):
    def test_lists_only_supported_image_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            for name in ["page.png", "photo.JPG", "scan.jpeg", "notes.txt"]:
                Path(tmp, name).write_bytes(b"test")

            self.assertEqual(
                sorted(listar_imagens(tmp)),
                ["page.png", "photo.JPG", "scan.jpeg"],
            )


class GeminiConfigurationTests(unittest.TestCase):
    def test_missing_api_key_fails_before_network_request(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(RuntimeError, "GEMINI_API_KEY"):
                extrair_texto_da_imagem("does-not-matter.png")


if __name__ == "__main__":
    unittest.main()

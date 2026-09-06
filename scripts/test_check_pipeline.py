"""Deterministic mutation tests for `validate_mcp_config` in check_pipeline.py.

Stdlib-only (unittest), matching this repository's existing dependency-free
validation pattern — no new test framework. Run directly:

    python3 scripts/test_check_pipeline.py

Every case here exercises `validate_mcp_config` in isolation against a
temporary `.mcp.json`; none of it depends on the live prompts.chat service.
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_pipeline as cp  # noqa: E402

VALID_ENTRY = {"type": "http", "url": "https://prompts.chat/api/mcp"}


class ValidateMcpConfig(unittest.TestCase):
    def _check(self, content):
        """Write `content` (dict -> JSON, str -> raw text, None -> no file)
        to a temporary .mcp.json and return validate_mcp_config's issues."""
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / ".mcp.json"
            if content is not None:
                if isinstance(content, str):
                    path.write_text(content, encoding="utf-8")
                else:
                    path.write_text(json.dumps(content), encoding="utf-8")
            return cp.validate_mcp_config(path)

    # --- expected PASS ---

    def test_valid_exact_config(self):
        issues = self._check({"mcpServers": {"prompts-chat": dict(VALID_ENTRY)}})
        self.assertEqual(issues, [])

    def test_sibling_server_plus_valid_prompts_chat(self):
        issues = self._check({
            "mcpServers": {
                "some-other-server": {"anything": "goes", "even": ["a", "list"]},
                "prompts-chat": dict(VALID_ENTRY),
            }
        })
        self.assertEqual(issues, [])

    # --- expected controlled FAIL, no traceback ---

    def test_missing_file(self):
        issues = self._check(None)
        self.assertTrue(issues)

    def test_malformed_json(self):
        issues = self._check("{ not valid json")
        self.assertTrue(issues)

    def test_root_wrong_type(self):
        issues = self._check(["not", "an", "object"])
        self.assertTrue(issues)

    def test_mcp_servers_wrong_type(self):
        issues = self._check({"mcpServers": []})
        self.assertTrue(issues)

    def test_prompts_chat_wrong_type(self):
        issues = self._check({"mcpServers": {"prompts-chat": ["not", "an", "object"]}})
        self.assertTrue(issues)

    def test_prompts_chat_missing(self):
        issues = self._check({"mcpServers": {}})
        self.assertTrue(issues)

    def test_wrong_url(self):
        issues = self._check({
            "mcpServers": {"prompts-chat": {"type": "http", "url": "https://evil.example/api/mcp"}}
        })
        self.assertTrue(issues)

    def test_missing_type(self):
        issues = self._check({
            "mcpServers": {"prompts-chat": {"url": "https://prompts.chat/api/mcp"}}
        })
        self.assertTrue(issues)

    def test_wrong_type_value(self):
        issues = self._check({
            "mcpServers": {"prompts-chat": {"type": "sse", "url": "https://prompts.chat/api/mcp"}}
        })
        self.assertTrue(issues)

    def test_headers_key_rejected(self):
        issues = self._check({
            "mcpServers": {"prompts-chat": {**VALID_ENTRY, "headers": {"Authorization": "x"}}}
        })
        self.assertTrue(issues)

    def test_oauth_key_rejected(self):
        issues = self._check({"mcpServers": {"prompts-chat": {**VALID_ENTRY, "oauth": {}}}})
        self.assertTrue(issues)

    def test_headers_helper_key_rejected(self):
        issues = self._check({"mcpServers": {"prompts-chat": {**VALID_ENTRY, "headersHelper": "x"}}})
        self.assertTrue(issues)

    def test_unexpected_key_rejected(self):
        issues = self._check({"mcpServers": {"prompts-chat": {**VALID_ENTRY, "apiKey": "x"}}})
        self.assertTrue(issues)


if __name__ == "__main__":
    unittest.main()

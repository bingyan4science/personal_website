"""Runtime facts for Bing Yan's website helper."""

from pathlib import Path


def site_facts(_query: str) -> str:
    return Path(__file__).with_name("facts.md").read_text(encoding="utf-8")


CONTEXT_PROVIDERS = {"site_facts": site_facts}
CONTEXT_LABELS = {"site_facts": "Facts"}
RESOURCE_PROVIDERS = {}

"""Select relevant paragraphs from the public biography for each question."""

import re
import unicodedata
from collections import Counter
from pathlib import Path


def terms(text: str) -> set[str]:
    text = unicodedata.normalize("NFKC", text).casefold().replace("ph.d.", "phd")
    words = set(re.findall(r"[^\W_]+", text)).difference(
        "a an and are as at be bing by can did do does for from has have her how i in is it "
        "me my of on or s she that the to was what when where which who with yan you your".split()
    )
    # Prefixes let "teach" find "teaching". Full words distinguish project names.
    return words | {word[:5] for word in words if len(word) > 5}


def site_facts(query: str) -> str:
    text = Path(__file__).with_name("facts.md").read_text(encoding="utf-8")
    paragraphs = [line for line in text.splitlines() if line and not line.startswith("#")]
    # Keep citation URLs in the returned text, but match on their human-readable labels.
    vocabulary = [terms(re.sub(r"\]\(https?://[^)]+\)", "]", p)) for p in paragraphs]
    counts = Counter(word for words in vocabulary for word in words)
    question = terms(query)
    scores = [sum(1 / counts[w] for w in question & words) for words in vocabulary]
    ranked = sorted(range(len(paragraphs)), key=scores.__getitem__, reverse=True)
    selected = [paragraphs[i] for i in ranked[:3] if scores[i]]
    if selected:
        return "\n\n".join(selected)
    # Broad questions should still have access to the biography and research overview.
    overview = text.split("## Research\n\n", 1)[1].split("\n\n", 1)[0]
    return "\n\n".join([*paragraphs[:2], overview])


CONTEXT_PROVIDERS = {"site_facts": site_facts}
CONTEXT_LABELS = {"site_facts": "Facts"}
RESOURCE_PROVIDERS = {}

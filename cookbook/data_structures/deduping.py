"""
Removing duplicates from a sequence while maintaining order.

The advantage of doing it this way is that it preserves order.
"""
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe_hash(items, key=None):
    """Handles items that are hashes, takes a lambda function."""
    seen = set()
    for item in items:
        val = item if key is none else key(item)
        if val not in seen:
            yield item
            seen.add(val)

# === Stage 50: Add unit tests for import and export behavior ===
# Project: HealthLog
import json, os, tempfile
from pathlib import Path
from healthlog.core.storage import Storage

def test_import_export_roundtrip():
    with tempfile.TemporaryDirectory() as tmpdir:
        storage = Storage(tmpdir)
        entry = {"type": "habit", "name": "Drink Water", "data": {"count": 8}}
        storage.add_entry(entry)
        exported = json.loads(storage.export())
        assert len(exported["entries"]) == 1
        imported_storage = Storage(Path(tmpdir) / "import_test")
        imported_storage.import_data(json.dumps(exported))
        reloaded = imported_storage.get_entries()
        assert len(reloaded) == 1
        assert reloaded[0]["name"] == entry["name"]

def test_export_empty():
    with tempfile.TemporaryDirectory() as tmpdir:
        storage = Storage(tmpdir)
        exported = json.loads(storage.export())
        assert "entries" in exported and len(exported["entries"]) == 0

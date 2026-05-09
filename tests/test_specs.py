from pathlib import Path
from vega_forge.cli import load_spec

def test_load_spec():
    assert load_spec(Path('examples/specs/static-site.json'))['type'] == 'static-site'

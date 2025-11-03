import os
import sys

import pytest


skip_on_windows = pytest.mark.skipif(
    sys.platform.startswith("win"),
    reason="Ghostscript not installed in Windows test environment",
)

skip_pdftopng = pytest.mark.skip(
    reason="Ghostscript not installed in Windows test environment",
)


# Check if ghostscript module is available
def _is_ghostscript_installed():
    try:
        import ghostscript  # noqa: F401
        return True
    except ModuleNotFoundError:
        return False


skip_without_ghostscript = pytest.mark.skipif(
    not _is_ghostscript_installed(),
    reason="Ghostscript Python module not installed",
)


@pytest.fixture
def testdir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "files")


@pytest.fixture
def foo_pdf(testdir):
    return os.path.join(testdir, "foo.pdf")

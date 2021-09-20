import stactools.core

from stactools.noaa_c_cap.dataset import Dataset
from stactools.noaa_c_cap.metadata import Metadata

stactools.core.use_fsspec()


def register_plugin(registry):
    from stactools.noaa_c_cap import commands
    registry.register_subcommand(commands.create_noaa_c_cap_command)


__all__ = ['Metadata', 'Dataset']
__version__ = "0.1.0"

import stactools.core

from stactools.noaa_c_cap.stac import create_collection, create_item

__all__ = ['create_collection', 'create_item']

stactools.core.use_fsspec()


def register_plugin(registry):
    from stactools.noaa_c_cap import commands
    registry.register_subcommand(commands.create_noaa_c_cap_command)


__version__ = "0.1.0"

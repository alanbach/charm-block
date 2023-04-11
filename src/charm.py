#!/usr/bin/env python3
# Copyright 2023 Alan Baghumian
# See LICENSE file for licensing details.
#
# Learn more at: https://juju.is/docs/sdk

from cmath import e
import logging
from ops.charm import CharmBase
from ops.main import main
from ops.model import MaintenanceStatus, ActiveStatus, BlockedStatus

logger = logging.getLogger(__name__)

class BlockCharm(CharmBase):
    """Charm the service."""

    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.disk_storage_attached, self._on_disk_storage_attached)
        self.framework.observe(self.on.disk_storage_detaching, self._on_disk_storage_detaching)
        self.framework.observe(self.on.install, self._on_install)
        self.framework.observe(self.on.config_changed, self._on_config_changed)
        self.framework.observe(self.on.start, self._on_start)

    def _on_disk_storage_attached(self, event):
        logger.info("Storage Disk Attached.")
        self.unit.status = ActiveStatus("Active: Ready")

    def _on_disk_storage_detaching(self, event):
        logger.info("Storage Disk Detaching.")
        self.unit.status = ActiveStatus("Active: Ready")

    def _on_install(self, event):
        logger.info("Charm is installing.")
        self.unit.status = MaintenanceStatus("Installing")

    def _on_config_changed(self, event):
        logger.info("Charm Config Change.")
        self.unit.status = ActiveStatus("Active: Ready")

    def _on_start(self, event):
        logger.info("Charm Started.")
        self.unit.status = ActiveStatus("Active: Ready")


if __name__ == "__main__":
    main(BlockCharm)

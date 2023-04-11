# Overview

Block is a very simple charm that allocates and deploys storage disks to any juju deployed virtual machine.

## Usage

### A. Create storage pools (Required)

```
juju create-storage-pool ssd cinder volume-type="ssd"
juju create-storage-pool nvme cinder volume-type="nvme"
```
```
juju create-storage-pool ebsgp3 ebs volume-type="gp3"
```

### B. Deploy instance + block disk

```
juju deploy block --storage disk=ssd,100G,1 --constraints "mem=1G zones=az2"
```

### C. Add disks to existing instances

```
juju deploy block
juju add-unit block --to 0
juju add-storage block/0 disk=nvme,100G,1
```

### D. Validate storage

```
juju storage
Unit     Storage ID  Type   Pool  Size    Status    Message
block/0  disk/0      block  ssd  100GiB  attached  
block/1  disk/1      block  nvme 100GiB  attached  
```

## Other resources

- [Read more](https://charmhub.io/block)

- [Contributing](CONTRIBUTING.md) <!-- or link to other contribution documentation -->

- See the [Juju SDK documentation](https://juju.is/docs/sdk) for more information about developing and improving charms.

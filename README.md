# Get disk information from MAAS

Parse yaml output from MAAS cli and print information about machine disks

## Usage

```
maas tor3 machines read hostname=<hostname> | ./get_disks.py

<hostname>

  Bootdisk
    ssd             1600.3     /dev/disk/by-id/scsi-SNVMe_MO001600KXPTR_KSC2N4936ICE12R0L
  Devices
    ssd             1600.3     /dev/disk/by-id/scsi-SNVMe_MO001600KXPTR_KSC2N4936ICE12R0L
    ssd             1599.8     /dev/disk/by-id/wwn-0x600062b21f339fc02f5dfab3b4d7c603
```

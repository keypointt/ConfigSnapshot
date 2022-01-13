## Motivation
Manage config files for different sub-systems which are working together as a whole is a pain.

Since a single change in one sub-system's config will break the whole system.

When there is a need to switch between different version of the whole system, config of all sub-system should also be version controlled, something like version of versions.

### Use Case
For example, in my case, I'm working with AWS, Azure, Kubernetes, Docker, Git, SSH, and also some customized project specific value files.

I need to snapshot (aka version) of all the following config files:
```shell
# folders
~/.ssh/*
~/.aws/*
~/.docker/*
~/.kube/*
~/.git/*

# single files
~/.bashrc
~/.gitconfig
......and some files of interest
```

Use cases:
* create a snapshot of all the config files
* switch between different config files snapshot, eg. switch from dev-version of config files where I've made some variable value changes, to prod-version of config files where I need to do some adhoc debugging and fixing
* delete some snapshot which is expired

## How does it work

### Snapshot
```shell
chmod 744 snapshot_config.py

python3 snapshot_config.py  <custome_description> # default is empty description

# example
python3 snapshot_config.py awsLbWorking

ll ~/config_snapshot/
total 68
drwxrwxr-x 17 xin xin 4096 Jan 10 10:31 ./
drwxr-xr-x 34 xin xin 4096 Jan 10 10:22 ../
drwxrwxr-x  7 xin xin 4096 Jan 10 10:31 2022011010awsLbWorking/
```

### Restore
```shell
chmod 744 snapshot_config.py

python3 restore_snapshot_config.py <target_snapshot_path_to_be_restored>

# example
python3 restore_snapshot_config.py ~/config_snapshot/2022011010awsLbWorking

```

## Tested Environment
Ubuntu 20.04

## TODO
* back up option to cloud providers like AWS/Azure/GCP.

## Reference
* https://superuser.com/questions/180251/copy-list-of-files
* https://stackoverflow.com/questions/1868714/how-do-i-copy-an-entire-directory-of-files-into-an-existing-directory-using-pyth

# Disk Image Checker

A minimal CLI interface for the image format inspector embedded in
https://opendev.org/openstack/oslo.utils.

## Install it from PyPI

```bash
# SOON pip install diskimagechecker
```

## Usage

```bash
# python -m diskimagechecker -i /path/to/good-image
# echo $?
0
# python -m diskimagechecker -i /path/to/danger-image
# echo $?
1
```

By default, will not output anything, but will return exit code
`1` on any failure, including security check failure, and `0` on success.

If used with `-v`, we report all information found about the image:
```bash
# python -m diskimagechecker -v -i /path/to/good-image
SAFETY_CHECK_PASSED=True
VIRTUAL_SIZE=12345678
ACTUAL_SIZE=123456
IMAGE_FORMAT=qcow2
```

## Development

Just put up a PR, it's Apache 2.0 licensed.

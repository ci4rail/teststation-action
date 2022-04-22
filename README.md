# Github action to run tests on testfarm test stations

This Github action allows you to test software components on a testfarm test station.

Note: this action is used by [fw-esp-action](https://github.com/ci4rail/fw_esp-action).

## Usage

```yaml
on: push

jobs:
  test:
    runs-on: ubuntu-latest
    name: test on teststation
    steps:
      - uses: ci4rail/teststation-action@v1
        with:
          pipeline-name: "the-pipeline"
          # This name is resolved by tailscale magic DNS
          mqtt-broker-url: "lizard-rpi:1883"
          test-name: "iou01 all"
          artifact-override: |
            {
              \"desired_versions.iou01_1.name\": \"fw-iou01-default\",
              \"desired_versions.iou01_1.version\": \"3b92cdf\",
              \"desired_versions.iou01_1.source.type\": \"ci4rail-minio\",
              \"desired_versions.iou01_1.source.bucket\": \"esp-fw-testing\",
              \"desired_versions.iou01_1.source.filetype\": \"fwpkg\"
            }
          access-token: ${{ secrets.FW_CI_TOKEN }}
          # must be a reusable, emphemeral key!
          tailscale-key: ${{ secrets.YODA_TAILSCALE_AUTHKEY }}
```

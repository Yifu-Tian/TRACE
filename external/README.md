# External Repositories

This folder tracks external repositories used by TRACE. Keep third-party source
code outside the TRACE repository unless there is a strong reason to vendor it.

## HOT3D Toolkit

- Local path: `/home/yifu/hot3d`
- Upstream: `https://github.com/facebookresearch/hot3d.git`
- Purpose: download and read the HOT3D dataset for early TRACE prototyping

Recommended workflow:

- Use the official HOT3D repository for downloading and inspecting the dataset.
- Store downloaded HOT3D data under `/home/yifu/TRACE/data/hot3d` or another
  large-data directory.
- Implement TRACE-specific loaders in `/home/yifu/TRACE/src`, not inside the
  HOT3D repository.

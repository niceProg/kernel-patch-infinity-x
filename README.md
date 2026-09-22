# kernel-patch-infinity-x

Build kernel **InnOvaTioN** (bezkemods) untuk **POCO X6 5G (garnet)** di ROM Infinity-X 3.12,
diganti root-nya ke **KernelSU-Next v3.4 + SUSFS v2.3.0** supaya cocok dengan manager KSU Next v3.4.

Alur workflow (`.github/workflows/build.yml`):

1. Clone `bezkemods/android_kernel_xiaomi_sm7435-new` (branch `innovation`, commit di-pin).
2. Revert commit KSU Next lama + SUSFS v2.2.0 bawaan InnOvaTioN.
3. Pasang SUSFS sisi kernel dari `simonpunk/susfs4ksu` (`gki-android12-5.10`).
4. Pasang KernelSU-Next dari `pershoot/KernelSU-Next` branch `dev-susfs` (v3.4.0 + SUSFS).
5. Config = `/proc/config.gz` dari HP (`configs/`), LTO diganti ThinLTO.
6. Build `Image` dengan Android clang r563880c, bungkus AnyKernel3 garnet, terbitkan sebagai Release.

Patch tambahan: taruh di `patches/kernel/*.patch` (kernel) atau `patches/ksun/*.patch` (KernelSU-Next).

> Hasil build BELUM tentu aman. Tes dulu pakai `fastboot boot`, simpan backup `boot.img`.

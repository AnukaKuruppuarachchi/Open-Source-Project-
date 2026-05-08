# Building Hypersomnia on Windows (CTF Fork)

## Prerequisites

### Required Software

| Tool | Version | Notes |
|------|---------|-------|
| Visual Studio Build Tools 2022 | 17.x | Install "Desktop development with C++" workload |
| LLVM / clang-cl | 19.1.5 | Must be on PATH; provides `clang-cl.exe` and `lld-link.exe` |
| CMake | 4.3.1+ | Must be on PATH |
| Ninja | any recent | Bundled with VS Build Tools or install separately |
| Git | any | For submodule population |
| OpenSSL (Win64, static) | 3.x | See note below |

### OpenSSL Installation

Download and install the **Win64 OpenSSL** package from https://slproweb.com/products/Win32OpenSSL.html.
Install to `C:\OpenSSL-v32-Win64` (the path used in the CMake flags below).

Expected layout after install:
```
C:\OpenSSL-v32-Win64\
  include\
  lib\
    VC\
      x64\
        MT\
          libssl_static.lib
          libcrypto_static.lib
```

---

## 1. Clone and Populate Submodules

This fork does **not** have `.git` history for submodules. The recommended approach is to clone the upstream Hypersomnia repo alongside this one and copy the submodule content with robocopy.

```powershell
# Clone the CTF fork (no submodules in .git)
git clone https://github.com/AnukaKuruppuarachchi/Hypersomnia_CTF.git

# Clone upstream to get populated submodules
git clone --recurse-submodules https://github.com/TeamHypersomnia/Hypersomnia.git Hypersomnia-upstream

# Copy submodule content from upstream into the CTF fork
# (run from the parent folder containing both repos)
robocopy Hypersomnia-upstream\src\3rdparty "Open-Source-Project--daniel\src\3rdparty" /E /XD .git
```

The project has 11 submodules under `src/3rdparty/`.

---

## 2. Configure CMake

Open a **Developer PowerShell** or plain PowerShell — the build command below calls `vcvarsall.bat` manually, so no special shell is required.

```powershell
# From repo root:
$REPO = "D:\Downloads\Open-Source-Project--daniel2\Open-Source-Project--daniel"

cmd /c @"
call "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvarsall.bat" x64 >nul 2>&1
cmake -S "$REPO" -B "$REPO\build" ^
  -G Ninja ^
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 ^
  -DCMAKE_C_COMPILER=clang-cl ^
  -DCMAKE_CXX_COMPILER=clang-cl ^
  -DCMAKE_LINKER=lld-link ^
  -DARCHITECTURE=x64 ^
  -DOPENSSL_ROOT_DIR="C:\OpenSSL-v32-Win64" ^
  -DOPENSSL_USE_STATIC_LIBS=FALSE ^
  -DALSOFT_UPDATE_BUILD_VERSION=OFF
"@
```

### CMake Flag Explanations

| Flag | Reason |
|------|--------|
| `-G Ninja` | Use Ninja build system (fast, parallel) |
| `-DCMAKE_POLICY_VERSION_MINIMUM=3.5` | Suppresses CMake policy warnings from older 3rdparty CMakeLists |
| `-DCMAKE_C_COMPILER=clang-cl` | Use clang-cl (MSVC-compatible Clang frontend) |
| `-DCMAKE_CXX_COMPILER=clang-cl` | Same for C++ |
| `-DCMAKE_LINKER=lld-link` | Use LLVM linker (faster than MSVC link.exe) |
| `-DARCHITECTURE=x64` | Target 64-bit |
| `-DOPENSSL_ROOT_DIR=...` | Point CMake to the correct OpenSSL install path |
| `-DOPENSSL_USE_STATIC_LIBS=FALSE` | Use shared/import libs (avoids static lib path issues) |
| `-DALSOFT_UPDATE_BUILD_VERSION=OFF` | Prevents openal-soft from reading `.git/modules/.../index`, which doesn't exist because submodules were copied rather than cloned via git |

---

## 3. Build

```powershell
cmd /c "call `"C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvarsall.bat`" x64 >nul 2>&1 && cd /d D:\Downloads\Open-Source-Project--daniel2\Open-Source-Project--daniel\build && ninja 2>&1 && echo BUILD_SUCCESS || echo BUILD_FAILED"
```

A full build compiles **791 targets** and produces `build\Hypersomnia.exe`.
Incremental rebuilds only recompile changed translation units.

---

## 4. Run

```powershell
cmd /c "call `"C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvarsall.bat`" x64 >nul 2>&1 && cd /d D:\Downloads\Open-Source-Project--daniel2\Open-Source-Project--daniel\build && ninja run 2>&1"
```

The `ninja run` target changes directory to the build folder and launches `Hypersomnia.exe` with the correct working directory so it can find its assets.

---

## Troubleshooting

### openal-soft fails to find git index
**Error**: CMake error about `.git/modules/3rdparty/openal-soft/index` not found.  
**Fix**: Add `-DALSOFT_UPDATE_BUILD_VERSION=OFF` to the CMake configure command.

### OpenSSL not found
**Error**: `Could not find OpenSSL` during CMake configure.  
**Fix**: Ensure OpenSSL is installed at `C:\OpenSSL-v32-Win64` and the `-DOPENSSL_ROOT_DIR` flag points there.

### clang-cl not found
**Error**: `The C compiler ... is not able to compile a simple test program`.  
**Fix**: Install LLVM for Windows from https://releases.llvm.org/ and ensure `clang-cl.exe` is on your `PATH`.

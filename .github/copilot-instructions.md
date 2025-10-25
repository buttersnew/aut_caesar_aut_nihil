## Purpose
Short, actionable guidance for AI coding agents working on this repository (Mount & Blade: Warband mod).

## Big picture (what this repo is)
- This repo contains a Warband mod built using a Python-based module system (W.R.E.C.K.). There are two main areas:
  - `Aut_Caesar_Aut_Nihil/` — module data and assets (exported text files, shaders, music, textures, etc.). Examples: `troops.txt`, `items.txt`, `mb.fx`, `mb_src.fx`.
  - `module_system/` — the compiler and helpers: `compile.py`, `compiler.py`, `header_*.py`, `module_*.py`, and `process_*.py` scripts. This directory defines the game data and performs export.
  - `handbook/` — the official handbook of the mod as pdf document.
  - `data_sourcefiles/` — flora and skybox definitions.
  - `website/` — code for the official website of the mod.

## How to build / developer workflows (exact commands)
 - Environment requirements:
   - Python 3.x (the module system in this repo has been updated to be compatible with Python 3). Use a modern Python 3 interpreter (3.8+ recommended). If you previously used Python 2, update your virtual environment and tooling accordingly.
   - On Windows, `fxc` (HLSL compiler) is required for `compile_fx.bat` (shaders compilation).

- Common commands (run from repository root or the named folder):
  - Compile by executing `module_system\compile.bat` ([W.R.E.C.K version 1.14](https://forums.taleworlds.com/index.php?threads/warband-refined-enhanced-compiler-kit-v1-0-0-mar-01-2015.325102/post-9791153))
  - The compiler `module_system\build_module.bat` is deprecated.
  - Shader compile: go to `Aut_Caesar_Aut_Nihil` and run `compile_fx.bat` (requires `fxc` on PATH), it will compile the source file `mb_src.fx`.

## Key files to read first (where to look for authoritative behavior)
- `module_system/compile.py` — top-level compiler runner; prints helpful hints when parse/syntax errors occur (missing commas / bracket mismatches).
- `module_system/compiler.py` — the W.R.E.C.K. implementation: identifier handling, parsing rules and validation. Most logic that enforces conventions lives here.
- `module_system/module_*.py` — the mod data you edit (troops, items, scenes, dialogs, etc.).
- `module_system/header_*.py` — constants and opcode definitions referenced by the compiler.
- `module_system/IDs` — contains ID files, can be ignored, only relevant for compiler.
- `module_system/Process` — contains additional files for the compiler, can be ignored.
- `module_system/colorama` — contains additional files for the compiler, can be ignored.
- `module_system/strings_character_names` — contains character name strings.
- `module_system/strings_face_keys` — contains face key strings.
- `Aut_Caesar_Aut_Nihil/` — the output/export folder and shader source(s).

## Project-specific conventions (concrete, not generic)
- Identifier and naming rules:
  - The compiler normalizes identifiers: spaces -> underscores, and lowercases by default. Avoid capital letters unless you know the compile flag `cap` is used.
  - Quick-strings: prefix with `@` in data (compiler creates quick-string entries).
  - Global variables are referenced with a leading `$` (converted to WRECK globals).
  - Local variables are referenced with leading `:` (converted to `l.*` locals).
- Scripts that can fail must be named with `cf_` prefix (compiler warns when a script can fail but doesn't start with `cf_`).
- Many parse errors are caused by missing commas/parentheses — the runner prints a location hint (see `compile.py` / `compiler.py` output messages).

## Typical edit cycle (recommended)
1. Edit `module_system/module_*.py` that holds the entity you want to change (e.g., `module_items.py`, `module_troops.py`).
2. Run `module_system\build_module.bat` to re-run the processing scripts, or `module_system\compile.bat` to run the core W.R.E.C.K. compiler.
3. Fix any compiler output (missing comma, illegal identifier, unassigned local, missing required plugin) — compiler prints targeted hints with file/line tokens.
4. Re-run shader build (if editing FX): `Aut_Caesar_Aut_Nihil\compile_fx.bat` (requires `fxc`).

## Integration & dependency notes
- The shader pipeline depends on `fxc` (DirectX HLSL compiler). If shader compilation fails, ensure the Microsoft DirectX / Windows SDK toolchain is installed and `fxc.exe` is on PATH.
 - The module system has been updated for Python 3. Use a Python 3 virtual environment for builds.

## Deployment / CI (GitHub Actions)
- The repo contains two GitHub Actions workflows in `.github/workflows/` that automate releases and the website:
  - `create-release.yml` — triggered when `version.txt` changes on `develop`.
    - Reads `version.txt`, zips `Aut_Caesar_Aut_Nihil` into `ACAN-v${TAG}.zip`, creates a **pre-release** with tag `v${TAG}` and uploads:
      - `ACAN-v${TAG}.zip` (mod zip)
      - `handbook/aut_ceasar_aut_nihil_handbook.pdf` (PDF asset)
    - Trigger it by bumping `version.txt` and pushing to `develop`.
  - `static.yml` — deploys the `website/` folder to GitHub Pages.
    - Triggers: push to `develop` that touches `website/**`, manual dispatch, or runs after `Create Pre-Release` completes.
    - It generates `website/index.html` by querying releases (uses `gh` and `jq` on the runner), injects download blocks and deploys via the Pages actions.

Notes and tips:
- `GITHUB_TOKEN` (available in Actions) is used to create releases and upload assets; no extra secrets are required for the default flows.
- `static.yml` relies on the `gh` CLI and `jq` on the runner (these are available on the Ubuntu hosted runner used in the workflow).
- `version.txt` should contain the version string used for the release tag (example in repo: `1.0.0.7-beta`). Update that file to trigger the pre-release workflow.
- To deploy the website after a release, either push website changes to `develop` or let `static.yml` run automatically after the `Create Pre-Release` workflow completes.

Optional local/testing commands (developer convenience):
  - Create a pre-release from local (requires `gh` CLI authenticated):
    gh release create v1.2.3 --prerelease --title "Version 1.2.3 (Pre-release)" --notes "Automated pre-release"
  - Upload an asset to an existing release (gh CLI):
    gh release upload v1.2.3 ACAN-v1.2.3.zip aut_ceasar_aut_nihil_handbook.pdf

## Where AI agents should look for patterns/examples of MBScript code
- To learn data layout examples, open these files:
  - `module_system/module_items.py` (item tuples/lists)
  - `module_system/module_troops.py` (troop structures and upgrade patterns)
  - `module_system/module_dialogs.py` (dialog entries, states and voiceover fields)
  - `module_system/module_scripts.py` (script bodies, local variables usage)
  - `module_system/module_game_menus.py` (definitions of menus, which allow asimple display)
  - `module_system/module_presentations.py` (definitions of presentations, which allow advanced display)
- For constants and opcodes check header files: `module_system/header_operations.py`, `module_system/header_triggers.py`, `module_system/header_common.py`.

## Quick debugging tips for AI agents for compiler errors
- If compile fails with TypeError complaining about 'object is not callable' or 'indices must be integers', the compiler hints that a missing comma is the likely cause and prints the `module` and approximate code snippet near the offending line.
- Look at compiler warnings about `unassigned local` (l.x) or `local declared but never used` — these point to script-level variable handling.

## Tone / style to follow when changing code/data
- Keep data formats (lists/tuples) compatible with the existing `module_*.py` files. Follow the existing naming and casing conventions (underscores, lowercase identifiers).
- Avoid editing `header_*.py` unless you need to add constants: it affects the whole build and may break many processors.

## If anything is unclear or you need more detail
- Tell me which area you want expanded (e.g., "examples for adding a troop", "how to add a new shader pass", or "explain the script opcode set"). I can expand this guidance or synthesize quick examples.

## Syntax:
* Module data files should follow the module system's data syntax as before: the `module_*.py` files define tuples/lists representing game entities. The module system accepts the same tuple/list shapes used historically.
* All Python code (tools / processors / compile scripts) should be run with Python 3 in this repo (the module_system was updated for Python 3 compatibility).
* Adhere strictly to the Module System's syntax: (operation, <arg1>, <arg2>...).
* Tuples and lists are the primary data structures.
* All text strings must be enclosed in quotation marks.

## File Structure:
* Identify the correct file for the request (module_dialogs.py, module_scripts.py, module_game_menus.py, etc.).
* When adding new items, place them at the end of the relevant list, just before the closing bracket ].
* When creating new definitions (e.g., troops, items, quests), ensure a unique ID string with a fitting name.

## Scripting and Logic:
* Check file `module_system/header_common.py` to understand available commands and their meaning.
* Use global variables ($g_variable) for data that persists across scenes.
* Use local variables (:variable) for temporary data within a single script or trigger.
* Use reg0, reg1, etc., for displaying numbers in text. Load them with (assign, regX, ...) operation.
* Use s1, s2, s3 etc, as string registers for storing strings. Load the with (str_store_string, s1, ...) operation.
* Use bitwise operations (val_or, store_and) with powers of two (1, 2, 4, 8...) for managing flags.
* All conditional logic must be wrapped in (try_begin)...(else_try)...(try_end) blocks.

## Formatting and Best Practices:
* Provide complete, copy-pasteable code blocks.
* When improving text, only modify the string content, not the code structure.
* Assume all requests are for the base game's Module System unless a specific mod (like WSE2) is mentioned.
* Clearly label which file each code block belongs to.
* Keep text improvements immersive and consistent with the specified tone.
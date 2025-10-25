# Aut Caesar Aut Nihil

![Aut Caesar Aut Nihil](https://raw.githubusercontent.com/buttersnew/aut_caesar_aut_nihil/main/website/acan_logo_gold.png)
*Official Handbook Cover*

**Aut Caesar Aut Nihil** (Latin for "Either Caesar or Nothing") is a comprehensive modification for Mount & Blade: Warband set in the Roman Empire as of 68 A.D. This mod offers a deeply immersive experience, allowing players to navigate the intricate political, economic, and military landscape of the era.

Empires, like humans, are born, grow, and eventually die. But their ideas can survive. This mod explores the enduring legacy of the Roman Empire, a testament to the heights of civilization, governance, and order that continues to echo through time.

---

## Table of Contents
- [About the Mod](#about-the-mod)
- [Key Features](#key-features)
- [Installation](#installation)
- [Official Handbook](#official-handbook)
- [Official Website](#official-website)
- [For Developers](#for-developers)
  - [Repository Structure](#repository-structure)
  - [Build Process](#build-process)
  - [Typical Edit Cycle](#typical-edit-cycle)
  - [Continuous Integration (GitHub Actions)](#continuous-integration-github-actions)

---

## About the Mod

*Aut Caesar Aut Nihil* transforms the world of Calradia into the Roman Empire and its surrounding territories. Players can rise from a humble citizen to a powerful senator, a legionary commander, or even the Emperor himself. The mod focuses on historical detail and complex gameplay mechanics, offering a unique sandbox experience.

Engage in deep political intrigue within the Roman Senate, manage your own latifundia and estates, establish trade routes to India, and lead legions into battle with historical formations. The world is rich with unique quests, special locations, and hundreds of historical and original NPCs that bring the era to life.

## Key Features

*   **Roman Government:** Experience a detailed simulation of the Roman government, including the roles of Emperor, Governors, Legates, and the Senate.
*   **Deep Economy:** Manage imperial and personal budgets, engage in trade with far-off lands like India, lend money, rule settlements, and build workshops or vast *latifundia* (estates).
*   **Extensive Factions:** Interact with dozens of Major, Minor, and Rebel factions, from the mighty Parthian Empire to the tribal kingdoms of Germania and Britannia.
*   **Religion and Piety:** Convert to Christianity, Judaism, or various pagan pantheons. Your piety and religious choices have a tangible impact on gameplay.
*   **Dozends of new Quests:** Embark on the Roman main story, a linked series of quests, or discover dozens of special and generic quests that offer unique challenges and rewards.
*   **Hundreds of named NPCs:** Meet hundreds of unique, named NPCs, including historical figures, companions, faction leaders, and special characters who drive the narrative.
*   **Advanced Battle Mechanics:** Command your troops using formations like the *Shield Wall* and *Wedge*. Experience morale shocks, pre-battle actions, and challenging multi-ladder, multi-directional sieges.
*   **Special Locations:** Discover and explore dozens of unique locations, including Rome, Alexandria, the Pyramids, the Valley of the Kings, and hidden sacred places.

## Installation

1.  Navigate to the official website [Aut Caesar Aut Nihil](https://buttersnew.github.io/aut_caesar_aut_nihil/).
2.  Download the latest `ACAN-vX.X.X.X.zip` file (recommended to download the stable release).
3.  Extract the contents of the zip file.
4.  Move the resulting `Aut_Caesar_Aut_Nihil` folder into your Mount & Blade: Warband `Modules` directory (e.g., `C:\Program Files (x86)\Steam\steamapps\common\MountBlade Warband\Modules`).
5.  Launch Mount & Blade: Warband, and select "Aut Caesar Aut Nihil" from the module dropdown menu.

## Official Handbook

For a complete and detailed guide to every feature in the mod, please refer to the **[Official Handbook](./handbook/aut_ceasar_aut_nihil_handbook.pdf)**. This document covers everything from game concepts and politics to a full list of quests and special NPCs.

## Official Website

The official website of [Aut Caesar Aut Nihil](https://buttersnew.github.io/aut_caesar_aut_nihil/) contains the download links of the latest stable release and the latest development release. it is hosted with github-pages.

---

## For Developers

This section provides guidance for developers and contributors working on the repository. The mod is built using [W.R.E.C.K version 1.14](https://forums.taleworlds.com/index.php?threads/warband-refined-enhanced-compiler-kit-v1-0-0-mar-01-2015.325102/post-9791153), a Python-based enhancement of the native module system.

### Repository Structure

The repository is organized into several key directories:
-   `Aut_Caesar_Aut_Nihil/`: Contains the compiled module data and game assets (text files, textures, shaders, music, etc.). This is the output folder for the compiler.
-   `module_system/`: The heart of the mod's development. It contains the Python 3-compatible compiler scripts (`compile.py`, `compiler.py`), data definitions (`module_*.py`), and constants (`header_*.py`).
-   `handbook/`: Source for the official handbook PDF.
-   `data_sourcefiles/`: Definitions for flora and skyboxes.
-   `website/`: Source code for the official mod website.

### Build Process

**Environment Requirements:**
*   **Python 3.x:** The module system is compatible with Python 3. A modern version (3.8+) is recommended.
*   **fxc.exe:** On Windows, the DirectX HLSL compiler (`fxc.exe`) is required for compiling shaders. It is part of the Windows SDK. Ensure it is available in your system's PATH.

**Compiling the mod**
*   **Compile Module:** To compile the module system, run the following batch script from the repository root:
    ```sh
    module_system\compile.bat
    ```
*   **Compile Shaders:** To compile shaders, navigate to the module directory and run the script:
    ```sh
    cd Aut_Caesar_Aut_Nihil
    compile_fx.bat
    ```

### Typical Edit Cycle

1.  **Edit Data:** Modify the Python files in `module_system/` (e.g., `module_items.py`, `module_dialogs.py`).
2.  **Compile Module:** Run `module_system\compile.bat` to export your changes into the text files in `Aut_Caesar_Aut_Nihil/`.
3.  **Fix Errors:** Address any errors reported by the compiler. The output often provides helpful hints about file names and line numbers for issues like missing commas or parentheses.
4.  **Compile Shaders (if needed):** If you've edited `mb_src.fx`, run `Aut_Caesar_Aut_Nihil\compile_fx.bat`.
5.  **Test:** Launch the mod in Warband to test your changes.

### Continuous Integration (GitHub Actions)

This repository uses GitHub Actions to automate releases and website deployment.

*   **`create-pre-release.yml`:**
    *   **Trigger:** Pushing a change to `version.txt` on the `develop` branch.
    *   **Action:** Automatically creates a zipped archive of the `Aut_Caesar_Aut_Nihil` folder, drafts a new pre-release on GitHub, and uploads the mod zip and the handbook PDF as assets.

*   **`create-release.yml`:**
    *   **Trigger:** Pushing a change to `version.txt` on the `main` branch.
    *   **Action:** Automatically creates a zipped archive of the `Aut_Caesar_Aut_Nihil` folder, drafts a new stable release on GitHub, and uploads the mod zip and the handbook PDF as assets.

*   **`static.yml`:**
    *   **Trigger:** A push to the `website/` directory, the completion of the `create-release`/`create-pre-release` workflow, or manual dispatch.
    *   **Action:** Deploys the `website/` folder to GitHub Pages. It dynamically generates download links on the website based on the latest GitHub releases (one for pre-releases, one for stable releases).

# Capture the Flag (CTF) Game Mode for Hypersomnia

## Overview

This project implements a **Capture the Flag (CTF) game mode** for the open-source multiplayer game engine **Hypersomnia**.

The goal of the project is to extend the existing gameplay framework by introducing a structured team-based objective mode while maintaining compatibility with Hypersomnia’s existing multiplayer, physics, and gameplay systems.

The project is developed as part of an **Open Source Software module**.

---


### Group Members

- Anuka Kuruppuarachchi  
- Claudia O'Callaghan  
- Daniel Wagner  

### Project Repository
https://github.com/TeamHypersomnia/Hypersomnia

### Original Hypersomnia Repository
https://github.com/TeamHypersomnia/Hypersomnia

---

# Project Idea

Capture the Flag is a team-based multiplayer game mode where two teams compete to capture the opposing team's flag and return it to their base while defending their own flag.

This project introduces CTF mechanics to Hypersomnia while integrating cleanly with the existing architecture.

Key gameplay features include:

- Two opposing teams
- Team bases
- Capturable flags
- Score tracking
- Win condition logic
- Multiplayer synchronization

---

# Project Objectives

The main objectives of the project are:

- Design and implement a fully functional CTF game mode
- Introduce new gameplay entities such as flags and bases
- Ensure multiplayer synchronization of flag and scoring logic
- Integrate the game mode into the existing Hypersomnia architecture
- Extend the user interface to support CTF gameplay
- Follow open-source development best practices

### Stretch Goals

If time permits, additional features may include:

- Configurable rule sets (flag return timers, score limits)
- Bot compatibility
- Match statistics tracking for CTF matches

---

# Technologies Used

## Development

- **C++** – Core implementation language
- **Hypersomnia Engine** – Existing open-source multiplayer engine
- **GitHub** – Version control and collaboration
- **Visual Studio Code** – Development environment


# Testing

New features are tested through:

- Local builds
- Multiplayer gameplay testing
- Manual validation of game mechanics

Future improvements may include automated tests and continuous integration.

---

# Contributing

Contributions are welcome.

To contribute:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a pull request

Example workflow:

```
git checkout -b feature/new-ctf-feature
git commit -m "Add new CTF feature"
git push origin feature/new-ctf-feature
```

All pull requests will be reviewed before merging.

---

# Issue Reporting

Issues can be reported through the GitHub **Issues** section.

Please include:

- A clear description of the problem
- Steps to reproduce the issue
- Expected behaviour
- Screenshots or logs if applicable

---

# License

This project follows the same license as the original Hypersomnia project.

**License:** GNU Affero General Public License v3.0 (AGPL-3.0)

See the `LICENSE` file for full details.

---

# Acknowledgements

This project builds upon the open-source Hypersomnia engine and its contributors.

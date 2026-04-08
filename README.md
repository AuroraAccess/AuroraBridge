# Aurora Sovereign Bridge (v1.0)

Interactive Command Interface for **Aurora Access dOS**.

## Overview
AuroraBridge represents a decentralized interaction layer between the user and the kernel. Unlike traditional shells, the entire logic of "The Bridge" is implemented using the autonomous **A-Code** language ("Soldered Language"), ensuring absolute sovereignty and independence from external libraries.

## Architecture
1. **Core Link**: The kernel provides hardware-level access to UART via `sys.uart_getc` and `sys.uart_putc`.
2. **Logic Layer**: The shell manages user input, maintains command buffers, and handles real-time terminal output.

## Installation
This repository is designed to be used as a Git Submodule within the main `ARM64-core` project.

---
[RCF:PROTECTED] — This module is an integral part of the Aurora System.

# Changelog

All notable changes to Decorix will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- Added `Before`, `After`, and `Finally` hook classes.
- Added the `Decorex` class for decorator management.
- Added function validation through the `validate` decorator.
- Added custom exceptions for validation and hook management.

### Changed
- Refactored the project into a more modular structure.
- Organized hook-related classes into separate modules.
- Improved class inheritance and code organization.

### Fixed
- Fixed hook execution and registry management.
- Fixed decorator execution behavior.
- Preserved the original function return value when using the `Finally` hook.
- Improved synchronization when removing registered hooks.
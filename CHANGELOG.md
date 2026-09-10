# Changelog

## [In Development] - Unreleased

<!--
> [!NOTE]
>

> [!TIP]
>

> [!IMPORTANT]
>

> [!WARNING]
>

> [!CAUTION]
>

Section Order:

### Added
### Fixed
### Changed
### Removed
-->

<!-- Your changes go here -->

## [2.0.1] - 2026-09-10

### Added

- CODEOWNERS file to define code ownership.

### Changed

- pin `allianceauth` dependency to `>=5.2`
- pin `allianceauth-app-utils` dependency to `>=1.33`
- pin `python` dependency to `>=3.10,<3.15`
- Optimized Tests
- Enhance Makefile and configuration management
- Added pre-commit hooks management in pre-commit.mk with commands for installation, uninstallation, updates, and checks.
- Improved Redis command management in redis.mk with better echo messages.
- Updated tests.mk to enhance test running and coverage reporting.
- Modified .pre-commit-config.yaml to use regex for JSON file exclusion.
- Updated CHANGELOG.md to include a section for new changes.
- Enhanced CODE_OF_CONDUCT.md with a structured table of contents.
- Improved CONTRIBUTING.md with a structured table of contents.
- Refactored Makefile to include dynamic configuration loading from .ini files. @thanks to (@ppfeufer)
- Added database management tasks in database.mk for backup, restore, list, and delete operations.
- Introduced npm.mk for managing npm dependencies and scripts.

### Removed

- unnecessary Test files

## [2.0.0] - 2026-05-31

> [!IMPORTANT]
>
> This Release needs at least Alliance Auth v5
> Please make sure to update your Alliance Auth before you install this APP

### Added

- Compatibility to Alliance Auth v5

## [1.1.3] - 2025-10-21

### Changed

- Updated Translations
- Updated Makefile System
- Updated Contributing

## [1.1.2] - 2025-10-16

### Fixed

- Translation Issue with "Character is not registered in `app_name`."

## [1.1.1] - 2025-10-15

### Added

- Automatic Release Workflow

### Changed

- Updated Dependencies
- Updated Makefile System
- Updated Translations

### Fixed

- Guideline url

## [1.1.0] - 2025-07-11

### Added

- dependabot
- View Test

## [1.0.9] - 2024-10-21 ([@ppfeufer](https://github.com/ppfeufer))

### Changed

- Use AA's native API to generate character portraits
- Pre Commit Update

## [1.0.8] - 2024-09-23 ([@ppfeufer](https://github.com/ppfeufer))

### Changed

- Widget order priority to 5, so the widget always is below the character widgets that come native with Alliance Auth and can be re-arranged with other priority 5 widgets by changing their app position in the `INSTALLED_APPS` list

## [1.0.7] - 2024-09-22 ([@ppfeufer](https://github.com/ppfeufer))

### Added

- Permission check. Only show the widget if the user has permissions to view the Member Audit app

## [1.0.6] - 2024-09-22 ([@ppfeufer](https://github.com/ppfeufer))

### Added

- Missing closing `div`
- Required `alt` attribute to `image` tags

### Fixed

- Widget Bootstrap classes
- Use common widget title template
- Use the actual name for Member Audit

### Changed

- Use app-specific tooltip trigger to prevent unwanted interaction with the Bootstrap default trigger and potentially crash the JS framework
- Let Bootstrap decide where to position the tooltips to prevent unwanted scrollbars and possibly cut-off tooltips
- JS modernized
- All strings are now translatable
- Replaced an unnecessary `br` with a Bootstrao class
- Better widget title

### Removed

- Unnecessary `div` construct around the table
- Unnecessary Django template tags
- Unnecessary JS variable
- Unnecessary Bootstrap classes
- Unnecessary font color as it was not readable in a lot of the Bootstrap themes

## [1.0.5] - 2024-09-04

### Added

- German Translation
- Icon Handler

### Changed

- Description Text

## [1.0.1-1.0.4] - 2024-07-29

### Added

- MemberAudit Checker also shows if all Chars registred.

### Removed

- Python Support 3.8, 3.9

## [1.0.1] - 2024-07-05

### Added

- Initial public release

<!-- Links -->

[1.0.1-1.0.4]: https://github.com/Geuthur/aa-memberaudit-dashboard/compare/v1.0.1...v1.0.4 "1.0.1-1.0.4"
[1.0.5]: https://github.com/Geuthur/aa-memberaudit-dashboard/compare/v1.0.4...v1.0.5 "1.0.5"
[1.0.6]: https://github.com/Geuthur/aa-memberaudit-dashboard/compare/v1.0.5...v1.0.6 "1.0.6"
[1.0.7]: https://github.com/Geuthur/aa-memberaudit-dashboard/compare/v1.0.6...v1.0.7 "1.0.7"
[1.0.8]: https://github.com/Geuthur/aa-memberaudit-dashboard/compare/v1.0.7...v1.0.8 "1.0.8"
[1.0.9]: https://github.com/Geuthur/aa-memberaudit-dashboard/compare/v1.0.8...v1.0.9 "1.0.9"
[1.1.0]: https://github.com/Geuthur/aa-memberaudit-dashboard/compare/v1.0.9...v1.1.0 "1.1.0"
[1.1.1]: https://github.com/Geuthur/aa-memberaudit-dashboard/compare/v1.1.0...v1.1.1 "1.1.1"
[1.1.2]: https://github.com/Geuthur/aa-memberaudit-dashboard/compare/v1.1.1...v1.1.2 "1.1.2"
[1.1.3]: https://github.com/Geuthur/aa-memberaudit-dashboard/compare/v1.1.2...v1.1.3 "1.1.3"
[2.0.0]: https://github.com/Geuthur/aa-memberaudit-dashboard/compare/v1.1.3...v2.0.0 "2.0.0"
[2.0.1]: https://github.com/Geuthur/aa-memberaudit-dashboard/compare/v2.0.0...v2.0.1 "v2.0.1"
[in development]: https://github.com/Geuthur/aa-memberaudit-dashboard/compare/v2.0.1...HEAD "In Development"

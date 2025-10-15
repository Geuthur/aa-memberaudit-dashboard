# Changelog

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

# macOS Audio Plugin Finder

[![Code Size](https://img.shields.io/github/languages/code-size/maskeproductions/macos-plugin-finder)](https://github.com/maskeproductions/macos-plugin-finder)
[![Coverage](https://img.shields.io/badge/coverage-90%25-brightgreen)](https://github.com/maskeproductions/macos-plugin-finder)
[![Downloads](https://img.shields.io/github/downloads/maskeproductions/macos-plugin-finder/total.svg)](https://github.com/maskeproductions/macos-plugin-finder/releases)
[![Last Commit](https://img.shields.io/github/last-commit/maskeproductions/macos-plugin-finder)](https://github.com/maskeproductions/macos-plugin-finder)

&nbpsp;
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python checks and lints](https://github.com/maskeproductions/macos-plugin-finder/actions/workflows/python-app.yml/badge.svg)](https://github.com/maskeproductions/macos-plugin-finder/actions/workflows/python-app.yml)
[![Version](https://img.shields.io/badge/version-1.0.0-brightgreen)](https://github.com/maskeproductions/macos-plugin-finder/releases)
[![Contributors](https://img.shields.io/github/contributors/maskeproductions/macos-plugin-finder)](https://github.com/maskeproductions/macos-plugin-finder/graphs/contributors)

&nbpsp;
[![GitHub Stars](https://img.shields.io/github/stars/maskeproductions/macos-plugin-finder.svg?style=social&label=Stars)](https://github.com/maskeproductions/macos-plugin-finder)
[![GitHub Forks](https://img.shields.io/github/forks/maskeproductions/macos-plugin-finder.svg?style=social&label=Forks)](https://github.com/maskeproductions/macos-plugin-finder)

## Overview

This script generates a report of audio plugins installed
in a specified directory on macOS. It lists each plugin, along
with its location and detailed metadata, in an easy-to-read HTML
format. The report includes collapsible sections for each plugin's
metadata to keep the information tidy and accessible.

## Features

- Lists audio plugins with `.component`, `.vst`, `.vst3`, or `.aax` extensions.
- Displays plugin names, locations, and detailed metadata.
- Metadata is presented in a structured format with collapsible sections.
- Allows customization of the plugin directory and output
 file name through command-line arguments.

## Requirements

The script uses standard Python libraries (`os`, `plistlib`, `html`,
`argparse`) available in Python's standard distribution. No additional
libraries are required.

## How to Use

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/maskeproductions/mpro-plugin-finder.git
   ```

2. **Navigate to the Script Directory**:

   ```bash
   cd macos-audio-plugin-finder
   ```

3. **Run the Script**:

   - To run with default settings (default plugin directory and output file):

     ```bash
     python macos-plugin-finder.py
     ```

   - To specify a custom plugin directory and output file:

     ```bash
     python macos-plugin-finder.py -d /path/to/plugin/directory -o output_file_name.html
     ```

4. **View the Report**:

   - Open the generated HTML report in a web browser.

## Customization

You can customize the script using the following command-line arguments:

- `-d` or `--directory`: Specify a custom path to the plugin directory.
- `-o` or `--output`: Specify a custom output file name for the HTML report.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check
[the GitHub repository](https://github.com/maskeproductions/mpro-plugin-finder/issues)
if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Examples

![Plugin Report Example Screenshot - Show All](https://github.com/maskeproductions/macos-plugin-finder/blob/main/screenshot01.png)

[View Sample Plugin Report](sample_report.html)

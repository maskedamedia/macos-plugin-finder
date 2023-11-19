"""This module generates a report of audio plugins installed in a specified directory on macOS."""

import os
import plistlib
import html
import argparse

# Set up command line argument parsing
parser = argparse.ArgumentParser(description="Generate a report of audio plugins.")
parser.add_argument(
    "-d",
    "--directory",
    default="/Library/Audio/Plug-Ins",
    help="Path to the plugin directory",
)
parser.add_argument(
    "-o", "--output", default="plugin_report.html", help="Output HTML file name"
)

args = parser.parse_args()

plugin_dir = args.directory
report_file = args.output


def format_metadata(metadata, indent=0):
    """Format the metadata for display in the HTML report."""
    formatted_text = f"<ul style='padding-left: {indent * 20}px;'>"
    for key, value in metadata.items():
        formatted_key = html.escape(str(key))
        if isinstance(value, dict):
            formatted_value = format_metadata(value, indent + 1)
        elif isinstance(value, list):
            formatted_value = format_list(value, indent + 1)
        else:
            formatted_value = html.escape(str(value))
        formatted_text += (
            f"<li><strong>{formatted_key}:</strong> {formatted_value}</li>"
        )
    formatted_text += "</ul>"
    return formatted_text


def format_list(lst, indent=0):
    """Format a list within the metadata for display."""
    formatted_text = f"<ul style='padding-left: {indent * 20}px;'>"
    for item in lst:
        if isinstance(item, dict):
            formatted_item = format_metadata(item, indent + 1)
        elif isinstance(item, list):
            formatted_item = format_list(item, indent + 1)
        else:
            formatted_item = html.escape(str(item))
        formatted_text += f"<li>{formatted_item}</li>"
    formatted_text += "</ul>"
    return formatted_text


def create_html_report(plugin_list):
    """Generate an HTML report from the list of plugins."""
    with open(report_file, "w", encoding="utf-8") as file:
        file.write("<html><head>")
        file.write("<style> /* CSS styles */ </style>")
        file.write(
            """
        <script>
        function toggleMetadata(id) {
            var x = document.getElementById(id);
            if (x.style.display === 'none') { x.style.display = 'block'; }
            else { x.style.display = 'none'; }
        }

        function showAllMetadata() {
            var metadatas = document.querySelectorAll('.metadata');
            metadatas.forEach(function(metadata) {
                metadata.style.display = 'block';
            });
        }

        function hideAllMetadata() {
            var metadatas = document.querySelectorAll('.metadata');
            metadatas.forEach(function(metadata) {
                metadata.style.display = 'none';
            });
        }
        </script>
        """
        )
        file.write("</head><body>")
        file.write(
            "<h1 style='font-size: 20px; text-align: center;'>Audio Plugin Report</h1>"
        )
        file.write("<button onclick='showAllMetadata()'>Show All</button>")
        file.write("<button onclick='hideAllMetadata()'>Hide All</button>")

        for index, plugin in enumerate(plugin_list):
            file.write(
                f"<div class='plugin'><h2 onclick='toggleMetadata(\"meta{index}\")'>"
                f"{plugin['name']}</h2>"
            )

            file.write(f"<p>Location: {plugin['location']}</p>")
            file.write(f"<div class='metadata' id='meta{index}'>")
            if "metadata" in plugin:
                formatted_metadata = format_metadata(plugin["metadata"])
                file.write(formatted_metadata)
            file.write("</div></div>")

        file.write("</body></html>")


def list_plugins(directory):
    """List all audio plugins in the specified directory."""
    plugin_list = []
    for root, directories, _ in os.walk(directory):
        for dir_name in directories:  # Renamed from 'directory' to 'dir_name'
            if (
                dir_name.endswith(".component")
                or dir_name.endswith(".vst")
                or dir_name.endswith(".vst3")
                or dir_name.endswith(".aax")
            ):
                plugin_info = {
                    "name": dir_name,
                    "location": os.path.join(root, dir_name),
                }
                info_plist_path = os.path.join(root, dir_name, "Contents", "Info.plist")
                if os.path.exists(info_plist_path):
                    with open(info_plist_path, "rb") as f:
                        plugin_info["metadata"] = plistlib.load(f)
                plugin_list.append(plugin_info)
    return plugin_list


plugins = list_plugins(plugin_dir)
create_html_report(plugins)
print(f"Report generated: {report_file}")

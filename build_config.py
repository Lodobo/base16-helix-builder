#!/usr/bin/python

import os
import yaml
import re
from pathlib import Path

helix_base_config = """ 

"ui.background" = { bg = "base00" }
"ui.virtual.whitespace" = "base03"
"ui.menu" = { fg = "base05", bg = "base01" }
"ui.menu.selected" = { fg = "base01", bg = "base04" }
"ui.linenr" = { fg = "base03" }
"ui.popup" = { bg = "base01" }
"ui.window" = { bg = "base01" }
"ui.linenr.selected" = { fg = "base04", modifiers = ["bold"] }
"ui.selection" = { bg = "base02" }
"comment" = { fg = "base03", modifiers = ["italic"] }
"ui.statusline" = { fg = "base04", bg = "base01" }
"ui.cursor" = { fg = "base04", modifiers = ["reversed"] }
"ui.cursor.primary" = { fg = "base05", modifiers = ["reversed"] }
"ui.text" = "base05"
"operator" = "base05"
"ui.text.focus" = "base05"
"variable" = "base08"
"constant.numeric" = "base09"
"constant" = "base09"
"attribute" = "base09"
"type" = "base0A"
"ui.cursor.match" = { fg = "base0A", modifiers = ["underlined"] }
"string"  = "base0B"
"variable.other.member" = "base0B"
"constant.character.escape" = "base0C"
"function" = "base0D"
"constructor" = "base0D"
"special" = "base0D"
"keyword" = "base0E"
"label" = "base0E"
"namespace" = "base0E"
"ui.help" = { fg = "base06", bg = "base01" }

"markup.heading" = "base0D"
"markup.list" = "base08"
"markup.bold" = { fg = "base0A", modifiers = ["bold"] }
"markup.italic" = { fg = "base0E", modifiers = ["italic"] }
"markup.strikethrough" = { modifiers = ["crossed_out"] }
"markup.link.url" = { fg = "base09", modifiers = ["underlined"] }
"markup.link.text" = "base08"
"markup.quote" = "base0C"
"markup.raw" = "base0B"

"diff.plus" = "base0B"
"diff.delta" = "base09"
"diff.minus" = "base08"

"diagnostic" = { modifiers = ["underlined"] }
"ui.gutter" = { fg = "base04" }
"info" = "base0D"
"hint" = "base03"
"debug" = "base03"
"warning" = "base09"
"error" = "base08"

"ui.bufferline" = { fg = "base04", bg = "base00" }
"ui.bufferline.active" = { fg = "base06", bg = "base01" }

"""

def main():    
    path = Path("schemes")

    os.makedirs("configs", exist_ok=True)

    for file_path in path.iterdir():
        if file_path.is_file():
            with open(file_path, 'r') as stream:
                scheme = yaml.safe_load(stream)
                string_builder = []

                string_builder.append(helix_base_config)
                string_builder.append("[palette]\n")
                string_builder.append(f"# scheme: {scheme["scheme"]}\n")
                string_builder.append(f"# author: {scheme["author"]}\n")
                string_builder.append(f"base00 = '#{scheme["base00"]}'\n")
                string_builder.append(f"base01 = '#{scheme["base01"]}'\n")
                string_builder.append(f"base02 = '#{scheme["base02"]}'\n")
                string_builder.append(f"base03 = '#{scheme["base03"]}'\n")
                string_builder.append(f"base04 = '#{scheme["base04"]}'\n")
                string_builder.append(f"base05 = '#{scheme["base05"]}'\n")
                string_builder.append(f"base06 = '#{scheme["base06"]}'\n")
                string_builder.append(f"base07 = '#{scheme["base07"]}'\n")
                string_builder.append(f"base08 = '#{scheme["base08"]}'\n")
                string_builder.append(f"base09 = '#{scheme["base09"]}'\n")
                string_builder.append(f"base0A = '#{scheme["base0A"]}'\n")
                string_builder.append(f"base0B = '#{scheme["base0B"]}'\n")
                string_builder.append(f"base0C = '#{scheme["base0C"]}'\n")
                string_builder.append(f"base0D = '#{scheme["base0D"]}'\n")
                string_builder.append(f"base0E = '#{scheme["base0E"]}'\n")
                string_builder.append(f"base0F = '#{scheme["base0F"]}'\n")

                full_config = "".join(string_builder)

                name = scheme["scheme"]
                name = ''.join(char.lower() if char.isalpha() else '-' for char in name)
                name = re.sub('-+', '-', name)
                name = re.sub('-$', '', name)
                filename = f"{name}.toml"

                # Write the modified string to a file in the output directory
                output_file_path = os.path.join("configs", filename)
                
                with open(output_file_path, "w") as config_file:
                    # Writing data to a file
                    config_file.write(full_config)

if __name__ == "__main__":
    main()

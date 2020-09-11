 #!/usr/bin/env python

from gimpfu import *
import os

defaultdir = os.getenv("HOME", "/tmp")

def gimp_palette_export_pal(palette, directory, filename):
    pdb.gimp_context_push()
    size = pdb.gimp_palette_get_info(palette)
    with open(os.path.join(directory, filename), "w") as f:
        f.write("JASC-PAL\n0100\n%d\n" % size)
        for i in range(size):
            color = pdb.gimp_palette_entry_get_color(palette, i)
            rgb = [color.red, color.green, color.blue]
            line = " ".join([str(int(x * 255)) for x in rgb])
            f.write(line+"\n")
    pdb.gimp_context_pop()
    #return

register(
    "gimp-palette-export-pal",
    "Export the active palette to JASC PAL (.pal)",
    "Export the active palette to JASC PAL (.pal)",
    "Tianmaru",
    "Tianmaru",
    "2020",
    "<Palettes>/Export as/JASC...",
    "",
    [
        (PF_PALETTE, "palette",  "Palette", ""),
        (PF_DIRNAME, "directory",  "Directory", defaultdir),
        (PF_STRING, "filename",  "File name", "palette.pal"),
    ],
    [],
    gimp_palette_export_pal)

main()

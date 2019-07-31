 #!/usr/bin/env python

from gimpfu import *
import os

defaultdir = os.getenv("HOME", "/tmp")

def gimp_palette_export_pal(palette, directory, filename, n):
    pdb.gimp_context_push()
    size = pdb.gimp_palette_get_info(palette)
    n = max(0, min(n, 256))
    if n == 0:
        n = size
    with open(os.path.join(directory, filename), "w") as f:
        f.write("JASC-PAL\n0100\n%d\n" % n)
        for i in range(n):
            if i < size:
                color = pdb.gimp_palette_entry_get_color(palette, i)
                r = int(color.red * 255)
                g = int(color.green * 255)
                b = int(color.blue * 255)
            else:
                r = i
                g = i
                b = i
            f.write("%d %d %d\n" % (r,g,b))
    pdb.gimp_context_pop()
    #return

register(
    "gimp-palette-export-pal",
    "Export the active palette to .pal",
    "Export the active palette to a color palette file (.pal) in JASC format.",
    "Tianmaru",
    "Tianmaru",
    "2019",
    "<Palettes>/Export as/Palette file...",
    "",
    [
        (PF_PALETTE, "palette",  "Palette", ""),
        (PF_DIRNAME, "directory",  "Directory", defaultdir),
        (PF_STRING, "filename",  "File name", "palette.pal"),
        (PF_INT, "n", "number of colors (use 0 for palette size)", 0),
    ],
    [],
    gimp_palette_export_pal)

main()

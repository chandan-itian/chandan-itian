# Rebuilding the profile banner

The artwork is an original Blender scene created for this profile. The README uses a static WebP render; no JavaScript or external widget service is required.

Requirements: Blender 4.3+, Python 3 with Pillow, DejaVu Sans fonts on Linux.

Run from the repository root:

```sh
blender -b -t 6 --python source/render_banner.py
python3 source/compose_banner.py
```

The first command creates an editable `source/profile-scene.blend` and a transparent `assets/scene.png`. The second combines the rendered scene with typography into `assets/hero.webp`.

The Blender scene includes extruded code lettering, beveled terminal geometry, floating tiles, metal materials and area lighting. Denoising is disabled to support Blender builds without OpenImageDenoise.

Only this profile repository is involved. No workflow reads private repositories or requires a token.

#!/opt/homebrew/bin/python3
"""
Cut the winnowed.app site images from the raw App Store captures.

Frameless on purpose: the site adds its own rounded corners and shadow, and
the marketing headlines would duplicate copy already on the page. So this
only resizes. It does not composite the way build_frames.py does.

Shebang points at Homebrew's python3 because /usr/bin/python3 forwards to
whatever Xcode's active developer directory is, which is the beta and does
not have Pillow.

Usage:
    ./build_site_images.py
    /opt/homebrew/bin/python3 build_site_images.py
"""

import os
from PIL import Image

# Same folder build_frames.py reads. Six captures named 01-stack.png
# through 06-banner.png.
SOURCE_DIR = "raw"

# Drop straight into the site repo's images folder when you are ready to
# push. Keeping it local until then, since Cloudflare deploys on push and
# the site must not change before 2.0 is approved.
OUTPUT_DIR = "site-images"

# 720 wide, which is 1440 on a retina display and what the July batch used.
TARGET_WIDTH = 720

# (source capture, site filename)
IMAGES = [
    ("01-stack.png",  "stack.png"),
    ("04-review.png", "review.png"),
    ("05-scan.png",   "also-01-scan.png"),
    ("02-siri.png",   "also-05-siri.png"),
    ("07-outro.png",      "also-02-gradient.png"),
    ("08-history.png",    "also-03-history.png"),
    ("09-onboarding.png", "also-04-device.png"),
]


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("Building winnowed.app site images")

    for source_name, output_name in IMAGES:
        source_path = os.path.join(SOURCE_DIR, source_name)
        output_path = os.path.join(OUTPUT_DIR, output_name)

        image = Image.open(source_path).convert("RGB")
        ratio = TARGET_WIDTH / image.width
        height = int(image.height * ratio)
        resized = image.resize((TARGET_WIDTH, height), Image.LANCZOS)
        resized.save(output_path, "PNG", optimize=True)

        print(f"  {output_name:22s} {resized.size[0]} x {resized.size[1]}")

    print(f"\nWrote {len(IMAGES)} images to ./{OUTPUT_DIR}/")
    print("Still needed, no v2.0 capture exists for any of these:")
    for name in ["widget.png", "also-02-gradient.png",
                 "also-03-history.png", "also-04-device.png"]:
        print(f"  {name}")


if __name__ == "__main__":
    main()

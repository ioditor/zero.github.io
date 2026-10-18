# User-supplied fonts

Input: Fonts.zip attached to the referenced conversation, copied byte-for-byte as Original-Fonts.zip. The user explicitly requested embedding their own fonts in this project and its portable build/PDF exports. Application font TTF files are unchanged from that archive. Full metadata, hashes and coverage appear in FONT-AUDIT.json.

The archive contains Flow Regular, Mono Regular and Still Regular, each in TTF (glyf) and OTF (CFF). These are alternate formats of the respective family, not six families. No Zero Still or Zero Still Mono family is present. No license text file is included. No font has embedding/subsetting restriction bits (OS/2.fsType = 0).

Mono/Still name ID 13: “See accompanying LICENSE.txt. Permission to use, modify and redistribute.” The referenced LICENSE.txt was not in the supplied archive. Copyright: “Copyright 2026 Zero Still project contributors.”

Flow has no name ID 13 or 14 license entry. Its copyright reads: “Zero Still original outlines, 2026. Prepared for the project owner.” Redistribution in this requested project relies on the user's explicit representation that these are their fonts and their instruction to bundle them; fsType alone is not a copyright license. No new license or authorship claim is added by this implementation.

Original files and names were not modified or merged. Noto Sans retains its existing OFL notice in NotoSans-OFL.txt.

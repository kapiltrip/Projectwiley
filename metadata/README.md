# Metadata Output

Generated assets:
- `catalog.json` and `catalog.csv`: cross-paper index.
- `reading_index.md`: human-readable overview of the 50 papers.
- `meatdatagenerated/text`: full extracted text per PDF.
- `meatdatagenerated/json`: per-paper metadata, abstract, headings, figure captions, and output paths.
- `../html`: one editable HTML file per PDF.
- `../images`: citation manifests and figure-reference index for later Wiley-style figure insertion.

Regenerate by running:

```powershell
python metadata\_tools\process_papers.py
```

name: Update Visual Product Map
on:
  schedule:
    - cron: '0 0 * * *' # Runs every night at midnight
  workflow_dispatch:      # Allows you to run it manually with a button

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install sharepy pandas openpyxl
      - name: Run Generator
        run: python generate_map.py
      - name: Commit and Push changes
        run: |
          git config --global user.name 'ProductMapBot'
          git config --global user.email 'bot@intel.com'
          git add PRODUCT_MAP.md
          git commit -m "Auto-update Product Map from SharePoint" || exit 0
          git push

# Data Naming Convention Validator

This is a configurable tool that validates datasets against user-defined naming conventions, flags invalid entries, and generates audit reports for file-based data pipelines.

The tool is built using PySide6 GUI, with an understanding of UX design: easy navigation, straightforward rules, color-coded output, and custom dark-themed UI built using Qt Style Sheets (QSS).

#### Purpose of the tool:
Naming conventions in any data pipeline are a foundational concern. Inconsistent identifiers would cause ingestion scripts to break and create downstream data quality issues. This tool demonstrates an understanding of data validation logic, configurable rule systems, and audit reporting: core skills in pipeline and data quality engineering.

---

## Features & Architecture (v0.7.0)

* **PySide6 (Qt) GUI Framework**: Intuitive single-window interface allowing users to define rules, browse folders, and view colour-coded results without leaving the application. The seamless interface allows users to navigate and understand the tool within seconds.
* **Custom Validation Rules:** Allows users to define custom naming conventions (prefixes and extensions) to match specific project needs.
* **Real-Time Visual Feedback:** Instantly colour-codes files (Green for valid, Red for invalid) within the list view, enabling immediate identification of naming errors.
* **Production Log Exporting:** Generates structured `.txt` validation reports detailing compliant and non-compliant assets, crucial for pipeline tracking, automated ingestion prep, and team/department feedback.
* **Error Prevention:** Built-in safeguards with basic exception and attribute handling to prevent the app from crashing if users attempt to export a report before choosing a folder.

---

## Prerequisites (Tech Stack)

* Python 3.10+ installed on your machine.
* pip install PySide6

---

## System Architecture

```text
├── asset_validator.py      # Primary application containing the UI and validation logic
├── README.md               # Project documentation and developer overview
├── LICENSE                 # MIT Licensing details
└── .gitignore              # Python .gitignore details
```

---

## How to Use

Simply launch the application script via your command line interface or IDE:

```bash
python asset_validator.py
```
1. Open `asset_validator.py` file.
2. Run the program and the application window titled **Data Naming Convention Validator** will pop up.
3. Fill in the required prefixes and file extensions you want to flag in the text input field.
4. Click the **Browse Folders** button to browse for directories and select your folder.
5. The interface will instantly display and flag assets that do not meet your intended criteria in the app frame.
6. You can also create a report log of your files once you have validated your assets by clicking the **Export Log** button.

---

## License
Distributed under the MIT License. See `LICENSE` for details.
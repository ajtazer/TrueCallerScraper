# TrueCallerScraper

TrueCallerScraper is a Python script that automates the extraction of profile names from the TrueCaller app using ADB (Android Debug Bridge) and OCR (Optical Character Recognition).

## Features

- Search phone numbers on TrueCaller and extract profile names.
- Capture screenshots and perform OCR to extract profile names.
- Save profile names to an output file.
- Fully functional and ready to use.

## Prerequisites

To run this script, you need to have the following tools and packages installed:

- Python 3
- ADB (Android Debug Bridge)
- pytesseract
- Pillow

## Installation

1. Clone this repository to your local machine.
2. Install the required Python packages by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure that ADB (Android Debug Bridge) is properly installed and set up on your machine. If you haven't installed ADB yet, you can refer to external sources like XDA Developers for detailed instructions on installing ADB for your specific operating system.

Note: Setting up ADB is outside the scope of this guide, and it's important to have ADB properly installed and configured before running the TrueCallerScraper script.


## Usage

1. Connect your Android device to your computer and ensure that USB debugging is enabled.

2. Open the TrueCaller app on your Android device and navigate to the desired chat or search page.

3. Update the script with the appropriate coordinates and settings for your device, if necessary.

4. Run the script using the following command:

```bash
python truecaller_scraper.py
```

The script will enter phone numbers, search on TrueCaller, capture screenshots, extract profile names, and save them to an output file.

## Customization
1. You can customize the script by modifying the following:

2. Adjusting the coordinates for tapping on the screen to match your device's layout.
3. Adding additional functionalities or error handling based on your requirements.

## Contribution
Contributions to this project are welcome! If you have any suggestions, improvements, or bug fixes, please feel free to open an issue or submit a pull request.
# Real-Time Price Tracker

## Overview
This project is a **real-time price tracker** that helps users monitor product prices on Amazon. It allows users to enter multiple Amazon product URLs and receive notifications via email whenever a price drop is detected, no matter how small the decrease is. Built with Python, Streamlit, and integrated with SendGrid for email notifications, this tool runs automatically without the need for constant manual checks.

## Key Features
- **Real-Time Price Monitoring**: Track prices of Amazon products in real-time.
- **Multiple Products**: Users can add as many Amazon product links as they want to track.
- **Email Notifications**: Get notified via email whenever a price drops, with no need to provide your Google account password (uses SendGrid).
- **Automated Tracking**: The script automatically runs in the background and checks for price changes, ensuring you never miss a price drop.

## Note:
- This tracker currently **only works with Amazon product links**. 

## Technologies Used:
- Python
- Streamlit (for the web interface)
- BeautifulSoup (for web scraping)
- SendGrid (for email notifications)


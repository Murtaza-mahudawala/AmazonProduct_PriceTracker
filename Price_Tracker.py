from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import requests
from bs4 import BeautifulSoup
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Dictionary to store previous prices
previous_prices = {}

# Function to get product details
def get_product_details(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Fetch product name
    product_name = soup.find("span", {"id": "productTitle"})
    product_name_text = product_name.get_text(strip=True) if product_name else "Product name not found"

    # Fetch product price
    price = soup.find("span", {"class": "a-price-whole"})
    price_text = price.get_text(strip=True) if price else "Price not found"

    return product_name_text, price_text

# Function to send email notifications using SendGrid
def send_email(subject, body, to_email):
    sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY')) 
    email = Mail(
        from_email='pricetracker842@gmail.com',  
        to_emails=to_email,
        subject=subject,
        plain_text_content=body
    )
    
    try:
        response = sg.send(email)
        print(f"Email sent to {to_email}, Status Code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to track price changes
def track_products(product_urls, emails):
    for url, email in zip(product_urls, emails):
        name, current_price = get_product_details(url)
        if current_price != "Price not found":
            current_price_value = int(float(current_price.replace(',', '')))
            if url in previous_prices:
                previous_price_value = previous_prices[url]
                if current_price_value < previous_price_value:
                    subject = f"Price Drop Alert for {name}!"
                    body = f"The price of '{name}' has dropped!\nOld Price: ₹{previous_price_value}\nNew Price: ₹{current_price}"
                    send_email(subject, body, email)
            previous_prices[url] = current_price_value

# Streamlit UI
st.title("Real-Time Price Tracker")

# Input for product URLs
product_urls = st.text_area("Enter product URLs (one per line):").splitlines()

# Input for user emails
user_emails = st.text_area("Enter your email (one per line):").splitlines()

if st.button("Start Tracking"):
    track_products(product_urls, user_emails)
    st.success("Tracking started! You will receive notifications via email if prices drop.")

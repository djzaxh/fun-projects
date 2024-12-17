import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from email.mime.text import MIMEText
import smtplib

# Function to log in to Netflix
def login_to_netflix(driver, email, password):
    driver.get("https://www.netflix.com/login")
    email_input = driver.find_element(By.NAME, "userLoginId")
    password_input = driver.find_element(By.NAME, "password")
    
    email_input.send_keys(email)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)  # Wait for the page to load

# Function to scrape subscription data
def scrape_subscription_data(driver):
    driver.get("https://www.netflix.com/your_account_page")  # Replace with your account page URL
    time.sleep(5)  # Wait for the account page to load
    subscription_info = driver.find_element(By.CLASS_NAME, "subscription-class")  # Update class name
    return subscription_info.text

# Function to save data to CSV
def save_to_csv(data, filename='subscription_data.csv'):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Plan', 'Renewal Date', 'Payment Method'])  # Example headers
        writer.writerow(data)  # Write the actual data

# Function to send email reminders
def send_reminder(email, subscription_info):
    msg = MIMEText(f"Reminder: Your subscription will renew on {subscription_info['renewal_date']}.")
    msg['Subject'] = 'Subscription Renewal Reminder'
    msg['From'] = 'hello.noresponse.zach.got.you@gmail.com'  # Replace with your email
    msg['To'] = email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:  # Replace with your SMTP server
        server.starttls()
        server.login('hello.noresponse.zach.got.you@gmail.com', 'mqms xyrg clbx lgpd')  # Replace with your email and password
        server.sendmail(msg['From'], [msg['To']], msg.as_string())

# Main function to run the scraper
def main():
    # User credentials
    email = input("email")  # Replace with your email
    password = input("your_password")          # Replace with your password

    # Set up the WebDriver
    driver = webdriver.Safari()  # Make sure to have the appropriate driver installed
    try:
        login_to_netflix(driver, email, password)
        subscription_info = scrape_subscription_data(driver)
        print(subscription_info)  # Display the scraped data

        # Save to CSV
        save_to_csv(['Your Plan', 'Renewal Date', 'Payment Method'])  # Replace with actual data
        
        # Optionally send reminders
        # send_reminder(email, {'renewal_date': '2024-01-01'})  # Example usage

    finally:
        # Close the WebDriver
        driver.quit()

if __name__ == "__main__":
    main()
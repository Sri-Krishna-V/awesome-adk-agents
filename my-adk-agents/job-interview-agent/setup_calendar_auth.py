#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Calendar OAuth 2.0 Setup Script for Job Interview Agent

This script helps you set up OAuth 2.0 authentication for Google Calendar API.
Run this script once to generate the token.pickle file needed for calendar access.
"""

import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json


class CalendarAuthSetup:
    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/calendar']
        self.credentials_file = 'credentials.json'
        self.token_file = 'token.pickle'
        
    def check_credentials_file(self):
        """Check if credentials.json exists and is valid"""
        if not os.path.exists(self.credentials_file):
            print(f"ERROR: {self.credentials_file} not found!")
            print("Please follow these steps:")
            print("1. Go to Google Cloud Console (https://console.cloud.google.com/)")
            print("2. Create a new project or select existing project")
            print("3. Enable Google Calendar API")
            print("4. Go to 'Credentials' > 'Create Credentials' > 'OAuth 2.0 Client ID'")
            print("5. Choose 'Desktop application'")
            print("6. Download the JSON file and save it as 'credentials.json'")
            return False
            
        try:
            with open(self.credentials_file, 'r') as f:
                creds_data = json.load(f)
                if 'installed' not in creds_data and 'web' not in creds_data:
                    print("ERROR: Invalid credentials.json format!")
                    print("Make sure you downloaded OAuth 2.0 credentials, not service account credentials.")
                    return False
            return True
        except json.JSONDecodeError:
            print("ERROR: Invalid JSON format in credentials.json")
            return False
    
    def setup_oauth(self):
        """Set up OAuth 2.0 authentication"""
        print("🚀 Starting Google Calendar OAuth setup...")
        
        if not self.check_credentials_file():
            return False
            
        creds = None
        
        # Check if token already exists
        if os.path.exists(self.token_file):
            print(f"📁 Found existing {self.token_file}")
            with open(self.token_file, 'rb') as token:
                creds = pickle.load(token)
                
        # If there are no (valid) credentials available, let the user log in
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                print("🔄 Refreshing expired token...")
                try:
                    creds.refresh(Request())
                    print("✅ Token refreshed successfully!")
                except Exception as e:
                    print(f"❌ Failed to refresh token: {e}")
                    print("🔄 Starting new authentication flow...")
                    creds = None
                    
            if not creds:
                print("🌐 Opening browser for authentication...")
                print("📝 Please:")
                print("1. Sign in to your Google account")
                print("2. Grant calendar access permissions")
                print("3. Complete the authorization process")
                
                try:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        self.credentials_file, self.SCOPES)
                    creds = flow.run_local_server(port=0)
                    print("✅ Authentication successful!")
                except Exception as e:
                    print(f"❌ Authentication failed: {e}")
                    return False
                    
            # Save the credentials for the next run
            with open(self.token_file, 'wb') as token:
                pickle.dump(creds, token)
                print(f"💾 Credentials saved to {self.token_file}")
        
        return creds
    
    def test_calendar_access(self, creds):
        """Test calendar access with the credentials"""
        print("🧪 Testing calendar access...")
        
        try:
            service = build('calendar', 'v3', credentials=creds)
            
            # Get calendar list
            calendar_list = service.calendarList().list().execute()
            calendars = calendar_list.get('items', [])
            
            if calendars:
                print("✅ Calendar access successful!")
                print(f"📅 Found {len(calendars)} calendar(s):")
                for calendar in calendars[:5]:  # Show first 5 calendars
                    print(f"   • {calendar['summary']} ({calendar['id']})")
                    
                if len(calendars) > 5:
                    print(f"   ... and {len(calendars) - 5} more")
                    
                print(f"\n💡 Tip: Use your primary calendar ID in .env file:")
                primary_calendar = next((cal for cal in calendars if cal.get('primary')), calendars[0])
                print(f"   GOOGLE_CALENDAR_ID={primary_calendar['id']}")
                
            else:
                print("⚠️  No calendars found, but authentication was successful")
                
            return True
            
        except Exception as e:
            print(f"❌ Calendar access test failed: {e}")
            return False
    
    def run_setup(self):
        """Run the complete setup process"""
        print("=" * 60)
        print("🎯 Job Interview Agent - Google Calendar Setup")
        print("=" * 60)
          # Setup OAuth
        creds = self.setup_oauth()
        if not creds:
            print("\nSetup failed!")
            return False
            
        # Test access
        if not self.test_calendar_access(creds):
            print("\nSetup completed but calendar access test failed!")
            return False
            
        print("\n" + "=" * 60)
        print("Setup completed successfully!")
        print("=" * 60)
        print("Next steps:")
        print("1. Copy .env.example to .env")
        print("2. Update GOOGLE_CALENDAR_ID in .env with your calendar ID")
        print("3. Run the interview agent: python main.py")
        print("=" * 60)
        
        return True


def main():
    """Main function"""
    setup = CalendarAuthSetup()
    
    try:
        success = setup.run_setup()
        if success:
            print("\n✅ All done! You can now use the Job Interview Agent.")
        else:
            print("\n❌ Setup incomplete. Please check the errors above.")
            
    except KeyboardInterrupt:
        print("\n\n⏹️  Setup cancelled by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()

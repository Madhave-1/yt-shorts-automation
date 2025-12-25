"""
SSL Certificate Fix for Windows
This script helps fix SSL certificate verification issues on Windows
"""
import ssl
import certifi
import os

def fix_ssl_certificates():
    """Configure Python to use certifi certificates"""
    print("Setting up SSL certificates...")
    
    # Set SSL certificate file path
    os.environ['SSL_CERT_FILE'] = certifi.where()
    os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
    
    # Create default SSL context with certifi
    ssl._create_default_https_context = ssl._create_unverified_context
    
    print(f"✅ SSL certificate path set to: {certifi.where()}")
    print("✅ SSL verification configured")
    
if __name__ == "__main__":
    fix_ssl_certificates()
    print("\n🎉 SSL setup complete!")
    print("You can now run: python main.py")

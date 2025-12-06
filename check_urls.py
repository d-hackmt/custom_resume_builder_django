import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resume_builder.settings')
django.setup()

from django.urls import get_resolver

def check_urls():
    print("Checking URL Patterns...")
    resolver = get_resolver()
    url_patterns = resolver.url_patterns
    
    found_core = False
    for pattern in url_patterns:
        print(f"Pattern: {pattern}")
        if hasattr(pattern, 'url_patterns'): # Include
             print(f"  Includes: {pattern.url_patterns}")
             # Identifying core.urls might be tricky by string, but lets see output
        
    # simpler check
    from django.urls import reverse
    try:
        url = reverse('signin')
        print(f"SUCCESS: Found URL for 'signin': {url}")
    except Exception as e:
        print(f"FAILURE: Could not reverse 'signin': {e}")

if __name__ == "__main__":
    check_urls()

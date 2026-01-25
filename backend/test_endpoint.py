
import requests
import time

url = "http://localhost:8000/predict/fish_species"
# Create a dummy image or use a real one if we can find it. 
# We'll just create a tiny dummy image.
from PIL import Image
import io

img = Image.new('RGB', (100, 100), color = 'red')
img_byte_arr = io.BytesIO()
img.save(img_byte_arr, format='JPEG')
img_byte_arr = img_byte_arr.getvalue()

files = {'file': ('test.jpg', img_byte_arr, 'image/jpeg')}

print("⏳ Sending request to backend...")
try:
    start = time.time()
    response = requests.post(url, files=files, timeout=10)
    end = time.time()
    print(f"✅ Response received in {end - start:.2f}s")
    print(f"Status: {response.status_code}")
    print(f"Body: {response.text}")
except requests.exceptions.Timeout:
    print("❌ Request timed out! Backend might be hanging.")
except Exception as e:
    print(f"❌ Error: {e}")

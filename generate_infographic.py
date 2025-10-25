import os
import requests
import json
import base64
from datetime import datetime

# --- CẤU HÌNH ---
API_KEY = "sk-z1Mro4GecX29FoRGMBGCiw"
API_URL = "https://api.thucchien.ai/gemini/v1beta/models/gemini-2.5-flash-image-preview:generateContent"
OUTPUT_DIR = "output_images" # <-- Tên thư mục để lưu ảnh

# --- PROMPT MỚI DÀNH CHO VIỆC CHỈNH SỬA HÌNH ẢNH ---
IMAGE_EDIT_PROMPT = """
Please analyze the attached image, which is a draft for an infographic about 'Luật Bảo vệ dữ liệu cá nhân 2025' in Vietnamese.
Your task is to regenerate it into a professional, high-resolution, and clean version.
Follow these instructions:
1.  **Style:** Apply a modern, minimalist, flat design aesthetic.
2.  **Color Palette:** Use deep blue (#0D47A1) as the primary color, white (#FFFFFF) for background/text, and a vibrant yellow (#FFC107) for accents, highlights, and icons.
3.  **Layout:** Re-organize the content from the image into a clear, logical, and spacious layout. A three-column structure is preferred.
4.  **Typography:** Use a single, clear, legible sans-serif font that supports Vietnamese characters. Ensure all text is sharp and easy to read.
5.  **Content:** Retain the core textual information from the provided image but present it in a more structured way with clear headings and illustrative icons.
The final output should be a polished infographic ready for public viewing.
"""

def encode_image_to_base64(image_path):
    """Đọc file ảnh và mã hóa sang định dạng base64."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file hình ảnh tại đường dẫn: {image_path}")
        return None

def generate_image_with_context(prompt_text, image_path, aspect_ratio="16:9"):
    """
    Gửi yêu cầu đến API để tạo hình ảnh, có kèm theo hình ảnh ngữ cảnh.
    """
    if not API_KEY:
        print("Lỗi: Vui lòng thiết lập biến môi trường GOOGLE_API_KEY.")
        return

    base64_image_data = encode_image_to_base64(image_path)
    if not base64_image_data:
        return

    headers = {
        'x-goog-api-key': API_KEY,
        'Content-Type': 'application/json',
    }

    parts = [
        {"text": prompt_text},
        {
            "inline_data": {
                "mime_type": "image/png",
                "data": base64_image_data
            }
        }
    ]

    request_body = {
      "contents": [{"parts": parts}],
      "generationConfig": {
          "imageConfig": {
              "aspectRatio": aspect_ratio
          }
      }
    }

    print(f"Đang gửi yêu cầu (kèm hình ảnh '{image_path}') đến API...")
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(request_body))
        response.raise_for_status() 

        response_data = response.json()
        
        image_data_base64 = response_data["candidates"][0]["content"]["parts"][0]["inlineData"]["data"]
        image_data = base64.b64decode(image_data_base64)
        
        # --- THAY ĐỔI: Tự động tạo thư mục và lưu file vào đó ---
        # 1. Tạo thư mục nếu nó chưa tồn tại
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        # 2. Tạo tên file và đường dẫn đầy đủ
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_basename = f"infographic_edited_{timestamp}.png"
        full_path = os.path.join(OUTPUT_DIR, file_basename)
        
        # 3. Lưu file ảnh vào đường dẫn mới
        with open(full_path, "wb") as f:
            f.write(image_data)
        
        print(f"Thành công! Hình ảnh đã được lưu tại: {full_path}")

    except requests.exceptions.HTTPError as errh:
        print(f"Lỗi HTTP: {errh}")
        print(f"Nội dung lỗi từ server: {response.text}")
    except requests.exceptions.RequestException as err:
        print(f"Lỗi Request: {err}")
    except KeyError:
        print("Lỗi: Không tìm thấy dữ liệu hình ảnh trong phản hồi từ API.")
        print("Phản hồi nhận được:", response_data)
    except Exception as e:
        print(f"Đã có lỗi xảy ra: {e}")

if __name__ == "__main__":
    image_file_path = "context.png"
    
    generate_image_with_context(IMAGE_EDIT_PROMPT, image_file_path, aspect_ratio="16:9")
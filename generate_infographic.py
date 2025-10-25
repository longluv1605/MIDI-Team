import os
import requests
import json
import base64
from datetime import datetime

# --- CẤU HÌNH ---
API_KEY = "sk-z1Mro4GecX29FoRGMBGCiw"
API_URL = "https://api.thucchien.ai/gemini/v1beta/models/gemini-2.5-flash-image-preview:generateContent"
OUTPUT_DIR = "output_images" # <-- Tên thư mục để lưu ảnh

# --- PROMPT DÀNH CHO VIỆC CHỈNH SỬA HÌNH ẢNH ---
IMAGE_EDIT_PROMPT = """
Cung cấp hình ảnh cho tôi dựa trên mô tả sau:

### **Prompt Tổng Thể cho AI Tạo Infographic**

**Chủ đề:** Infographic tóm tắt Luật Bảo vệ dữ liệu cá nhân 2025 của Việt Nam.

**Yêu cầu chung:**
*   **Kích thước:** 3937 x 7874 pixels (tỷ lệ 1:2, khổ dọc).
*   **Phong cách:** Hiện đại, tối giản (minimalist), sạch sẽ, chuyên nghiệp. Sử dụng icon và biểu đồ phẳng (flat design).
*   **Bảng màu chủ đạo:**
    *   **Nền:** Trắng (`#FFFFFF`) hoặc xám rất nhạt (`#F5F7FA`).
    *   **Màu chính:** Xanh dương đậm (`#0A2A4E`) - cho tiêu đề và các đề mục chính.
    *   **Màu nhấn:** Xanh lam sáng (`#007BFF`), Xanh ngọc (`#17A2B8`), Vàng (`#FFC107`).
    *   **Màu chữ:** Đen (`#333333`) cho nội dung, trắng cho các vùng nền tối.
*   **Font chữ:** Sử dụng font sans-serif hiện đại, dễ đọc (ví dụ: Montserrat, Lato, Be Vietnam Pro). Tiêu đề in đậm, lớn. Nội dung chữ vừa phải.
*   **Bố cục:** Theo cấu trúc trong `context.png`, chia thành các khối rõ ràng, có khoảng trắng hợp lý giữa các phần. Ngôn ngữ trên ảnh: **Tiếng Việt**.

---

### **Cấu trúc và Nội dung chi tiết từng phần**

**1. Phần Tiêu đề (Header)**
*   **Kích thước:** `3500 x 600 px`.
*   **Nội dung:**
    *   Dòng tiêu đề chính (lớn, in đậm): **LUẬT BẢO VỆ DỮ LIỆU CÁ NHÂN 2025**
    *   Dòng phụ (nhỏ hơn): **NHỮNG ĐIỀU BẠN CẦN BIẾT ĐỂ BẢO VỆ QUYỀN RIÊNG TƯ**
*   **Hình ảnh:** Nền xanh dương đậm (`#0A2A4E`), chữ trắng. Có thể thêm một vài họa tiết chấm bi hoặc đường kẻ mờ để tạo chiều sâu.

**2. Khối 1: Định nghĩa & Biểu tượng (Hàng ngang 3 ô)**
*   **Kích thước chung của hàng:** `3500 x 1200 px`.

    *   **Ô 1: Dữ liệu cá nhân CƠ BẢN**
        *   **Kích thước:** `1100 x 1100 px`.
        *   **Nội dung:**
            *   **Tiêu đề:** Phần 1: Dữ liệu cá nhân là gì?
            *   **Nội dung chính:** **Dữ liệu CƠ BẢN:** Là thông tin định danh phổ biến.
            *   **Ví dụ (dạng list + icon):** Họ tên, Ngày sinh, SĐT, Email, Số CCCD.
        *   **Hình ảnh:** Một icon hình người (user profile) đơn giản. Xung quanh là các icon nhỏ tượng trưng cho ví dụ: điện thoại, email, thẻ căn cước.

    *   **Ô 2: Biểu tượng chính**
        *   **Kích thước:** `1100 x 1100 px`.
        *   **Hình ảnh:** Một biểu tượng **chiếc khiên** lớn, hiện đại, màu xanh lam sáng (`#007BFF`). Bên trong chiếc khiên là **biểu tượng ổ khóa** phát sáng nhẹ. Hình ảnh phải thể hiện sự an toàn, bảo mật tuyệt đối.

    *   **Ô 3: Dữ liệu cá nhân NHẠY CẢM**
        *   **Kích thước:** `1100 x 1100 px`.
        *   **Nội dung:**
            *   **Tiêu đề:** (Không cần lặp lại tiêu đề Phần 1)
            *   **Nội dung chính:** **Dữ liệu NHẠY CẢM:** Là thông tin riêng tư, cần bảo vệ nghiêm ngặt.
            *   **Ví dụ (dạng list + icon):** Sức khỏe (icon trái tim/ bệnh án), Tài chính (icon tiền tệ), Sinh trắc học (icon vân tay), Quan điểm chính trị.
        *   **Hình ảnh:** Một icon hình "dấu vân tay" hoặc "chuỗi DNA". Xung quanh là các icon nhỏ: trái tim, biểu đồ tài chính, lá phiếu.

**3. Khối 2: Quyền & Nghĩa vụ (Hàng ngang 2 ô)**
*   **Kích thước chung của hàng:** `3500 x 1600 px`.

    *   **Ô 1: 8 Quyền Vàng của bạn**
        *   **Kích thước:** `1700 x 1500 px`.
        *   **Nội dung:**
            *   **Tiêu đề:** Phần 2: 8 Quyền Vàng của bạn
            *   **Nội dung (rút gọn, dùng từ khóa):** Được biết, Đồng ý (hoặc rút lại), Xem & Sửa, Yêu cầu Xóa, Khiếu nại, Yêu cầu Bồi thường, Tự bảo vệ.
        *   **Hình ảnh:** Hình ảnh một người đang đứng giơ cao một **chiếc chìa khóa vàng** (`#FFC107`) đầy quyền năng. Xung quanh là 8 icon nhỏ, phẳng, minh họa cho các quyền (con mắt, dấu tick, bút chì, thùng rác, cái búa thẩm phán...).

    *   **Ô 2: 4 Nghĩa vụ cần nhớ**
        *   **Kích thước:** `1700 x 1500 px`.
        *   **Nội dung:**
            *   **Tiêu đề:** Phần 3: 4 Nghĩa vụ cần nhớ
            *   **Nội dung (rút gọn):** 1. Tự bảo vệ dữ liệu. 2. Tôn trọng dữ liệu người khác. 3. Cung cấp thông tin chính xác. 4. Tuân thủ pháp luật.
        *   **Hình ảnh:** Bốn icon được xếp thẳng hàng hoặc dạng lưới.
            1.  Icon người và chiếc khiên.
            2.  Icon hai người bắt tay.
            3.  Icon tài liệu có dấu tick.
            4.  Icon cán cân công lý.

**4. Khối 3: Các quy định nổi bật (Ô ngang dài)**
*   **Kích thước:** `3500 x 1600 px`.
*   **Nội dung:**
    *   **Tiêu đề:** Phần 4: Các quy định nổi bật
    *   **Nội dung (chia 4 cột nhỏ hoặc 4 dòng có icon):**
        *   **IM LẶNG KHÔNG LÀ ĐỒNG Ý:** Cần có sự cho phép rõ ràng, tự nguyện. (Icon: bong bóng chat bị gạch chéo).
        *   **THÔNG BÁO TRONG 72 GIỜ:** Tổ chức phải báo cáo khi có sự cố rò rỉ dữ liệu. (Icon: đồng hồ đếm ngược hiển thị 72h).
        *   **XỬ LÝ KHÔNG CẦN ĐỒNG Ý:** Trong các trường hợp khẩn cấp (tính mạng, an ninh quốc gia). (Icon: xe cứu thương hoặc cờ tổ quốc).
        *   **QUẢNG CÁO PHẢI CÓ SỰ ĐỒNG Ý:** Phải cho phép người dùng từ chối. (Icon: Megaphone có nút "block" hoặc "từ chối").
*   **Hình ảnh:** Sử dụng các icon tương ứng như mô tả để minh họa cho từng điểm, tạo sự trực quan.

**5. Khối 4: Điểm mới & Ví dụ (Ô ngang dài)**
*   **Kích thước:** `3500 x 1800 px`.
*   **Nội dung:** Chia ô này làm 2 phần dọc.

    *   **Bên trái - Phần 5: Điểm mới cần lưu ý**
        *   **Nội dung:**
            *   **Hiệu lực:** 01/01/2026 (Icon: Lịch).
            *   **Chế tài rất nặng:** Phạt tới 5% tổng doanh thu. (Icon: túi tiền lớn có dấu %).
            *   **Bắt buộc Đánh giá tác động:** Trước khi xử lý/chuyển dữ liệu. (Icon: tài liệu và kính lúp).
            *   **Ưu đãi doanh nghiệp nhỏ:** Miễn trừ một số quy định trong 5 năm đầu. (Icon: mầm cây đang lớn).

    *   **Bên phải - Phần 6: Ví dụ thực tế**
        *   **Nội dung:**
            *   **Ví dụ 1:** App bán hàng phải dùng checkbox "Đồng ý nhận quảng cáo" và không được tick sẵn. (Icon: màn hình điện thoại có checkbox chưa được chọn).
            *   **Ví dụ 2:** Khi bạn yêu cầu xóa tài khoản, công ty phải xóa hoàn toàn dữ liệu của bạn. (Icon: một hồ sơ người dùng bị kéo vào biểu tượng thùng rác).

*   **Hình ảnh:** Mỗi phần có các icon minh họa riêng như đã mô tả, ngăn cách bằng một đường kẻ mờ ở giữa.

**6. Phần Chân trang (Footer)**
*   **Kích thước:** `3500 x 300 px`.
*   **Nội dung:**
    *   "Nguồn: Tóm tắt từ Luật Bảo vệ Dữ liệu Cá nhân Việt Nam 2025"
    *   Có thể thêm logo của tổ chức (nếu có).
*   **Hình ảnh:** Nền xanh dương đậm (`#0A2A4E`) giống header, chữ trắng. Đơn giản và gọn gàng.
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
    print("--- Bắt đầu script ---")
    if not API_KEY:
        print("Lỗi nghiêm trọng: Biến môi trường GOOGLE_API_KEY chưa được thiết lập hoặc không tìm thấy.")
        print("Vui lòng chạy lệnh 'setx GOOGLE_API_KEY \"your_real_api_key\"' và khởi động lại terminal.")
        return

    print(f"Đang đọc và mã hóa hình ảnh từ: {image_path}")
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

    print(f"Đang gửi yêu cầu đến API: {API_URL}")
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(request_body))
        response.raise_for_status() 

        response_data = response.json()
        
        if not response_data.get("candidates"):
            print("\nLỗi: Phản hồi từ API không chứa 'candidates'.")
            full_response_str = json.dumps(response_data, indent=2)
            print(f"Phản hồi nhận được (một phần): {full_response_str[:500]}...")
            return

        candidate = response_data["candidates"][0]

        if "content" not in candidate:
            print("\nLỗi: API không trả về nội dung hình ảnh.")
            print("Lý do có thể là do bộ lọc an toàn của API hoặc prompt không phù hợp.")
            candidate_str = json.dumps(candidate, indent=2, ensure_ascii=False)
            print(f"Chi tiết từ API (một phần): {candidate_str[:500]}...")
            return
            
        # --- THAY ĐỔI QUAN TRỌNG ---
        # Lặp qua các 'parts' để tìm phần chứa dữ liệu hình ảnh
        image_part = None
        for part in candidate["content"]["parts"]:
            if "inlineData" in part:
                image_part = part
                break
        
        if not image_part:
            print("\nLỗi: Không tìm thấy 'inlineData' chứa hình ảnh trong phản hồi của API.")
            candidate_str = json.dumps(candidate, indent=2, ensure_ascii=False)
            print(f"Chi tiết từ API (một phần): {candidate_str[:500]}...")
            return
        
        image_data_base64 = image_part["inlineData"]["data"]
        image_data = base64.b64decode(image_data_base64)
        
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_basename = f"infographic_edited_{timestamp}.png"
        full_path = os.path.join(OUTPUT_DIR, file_basename)
        
        with open(full_path, "wb") as f:
            f.write(image_data)
        
        print(f"\nThành công! Hình ảnh đã được lưu tại: {full_path}")

    except requests.exceptions.HTTPError as errh:
        print(f"\nLỗi HTTP: {errh}")
        error_content = response.text[:500] 
        print(f"Nội dung lỗi từ server (một phần): {error_content}...")
        print("\n=> Gợi ý: Lỗi này thường do API Key không hợp lệ hoặc không có quyền truy cập mô hình. Vui lòng kiểm tra lại API Key của bạn.")
    except requests.exceptions.RequestException as err:
        print(f"\nLỗi Request: {err}")
        print("\n=> Gợi ý: Không thể kết nối đến server. Vui lòng kiểm tra lại kết nối mạng và địa chỉ API_URL.")
    except (KeyError, IndexError) as e:
        print(f"\nLỗi: Cấu trúc dữ liệu trong phản hồi API không như mong đợi ({e}).")
        if 'response_data' in locals():
            full_response_str = json.dumps(response_data, indent=2, ensure_ascii=False)
            print(f"Toàn bộ phản hồi để gỡ lỗi (một phần): {full_response_str[:500]}...")
        else:
            print(f"Toàn bộ phản hồi để gỡ lỗi (một phần): {response.text[:500]}...")
    except Exception as e:
        print(f"\nĐã có lỗi không xác định xảy ra: {e}")
    
    print("--- Kết thúc script ---")

if __name__ == "__main__":
    image_file_path = "context.png"
    generate_image_with_context(IMAGE_EDIT_PROMPT, image_file_path, aspect_ratio="9:16")
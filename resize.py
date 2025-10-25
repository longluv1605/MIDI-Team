from PIL import Image
import os

def resize_image(input_path, output_path, new_size):
    """
    Thay đổi kích thước của một hình ảnh và lưu nó.

    :param input_path: Đường dẫn đến file ảnh gốc.
    :param output_path: Đường dẫn để lưu file ảnh đã thay đổi kích thước.
    :param new_size: Một tuple (width, height) cho kích thước mới.
    """
    try:
        with Image.open(input_path) as img:
            print(f"Đang đọc ảnh từ: {input_path}")
            print(f"Kích thước gốc: {img.size}")
            
            # Sử dụng Image.LANCZOS (hoặc Image.Resampling.LANCZOS) để có chất lượng tốt nhất
            resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
            
            print(f"Đã thay đổi kích thước thành: {resized_img.size}")
            
            resized_img.save(output_path)
            print(f"Thành công! Ảnh đã được lưu tại: {output_path}")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file ảnh tại đường dẫn '{input_path}'")
    except Exception as e:
        print(f"Đã có lỗi xảy ra: {e}")

if __name__ == "__main__":
    # --- CẤU HÌNH ---
    
    # Thư mục chứa ảnh
    image_directory = "output_images"
    
    # Tên file ảnh gốc
    input_filename = "infographic_edited_20251025_102558.png"
    
    # Tên file ảnh sau khi resize
    output_filename = "resized_infographic.png"
    
    # Kích thước mới (chiều rộng, chiều cao)
    target_size = (3937, 7978)

    # Tạo đường dẫn đầy đủ
    input_image_path = os.path.join(image_directory, input_filename)
    output_image_path = os.path.join(image_directory, output_filename)

    # Gọi hàm để thay đổi kích thước
    resize_image(input_image_path, output_image_path, target_size)
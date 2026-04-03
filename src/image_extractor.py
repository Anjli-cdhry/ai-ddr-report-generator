import fitz
import os

def extract_images(pdf_path, output_folder):
    doc = fitz.open(pdf_path)
    image_paths = []

    os.makedirs(output_folder, exist_ok=True)

    for page_index in range(len(doc)):
        page = doc[page_index]
        images = page.get_images(full=True)

        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)

            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            image_name = f"{os.path.basename(pdf_path)}_page{page_index+1}_img{img_index}.{image_ext}"
            image_path = os.path.join(output_folder, image_name)

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            image_paths.append(image_path)

    return image_paths
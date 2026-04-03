from src.ai_processor import generate_ddr_report
from src.pdf_parser import extract_text_from_pdf
from src.image_extractor import extract_images
import os


inspection_pdf = "inspection.pdf"
thermal_pdf = "thermal.pdf"

os.makedirs("outputs/images", exist_ok=True)

print("🔄 Extracting text...")

inspection_text = extract_text_from_pdf(inspection_pdf)
thermal_text = extract_text_from_pdf(thermal_pdf)

print("\n✅ Inspection Text Preview:\n")
print(inspection_text[:500])

print("\n✅ Thermal Text Preview:\n")
print(thermal_text[:500])

print("\n🔄 Extracting images...")

images_1 = extract_images(inspection_pdf, "outputs/images")
images_2 = extract_images(thermal_pdf, "outputs/images")

print("\n✅ Extracted Images:")
for img in images_1 + images_2:
    print(img)

print("\n🧠 Generating DDR Report...\n")

report = generate_ddr_report(inspection_text, thermal_text)

print("\n📄 FINAL DDR REPORT:\n")
print(report)


import os
os.makedirs("outputs/reports", exist_ok=True)

with open("outputs/reports/ddr_report.txt", "w", encoding="utf-8") as f:
    f.write(report)

print("\n✅ Report saved in outputs/reports/")
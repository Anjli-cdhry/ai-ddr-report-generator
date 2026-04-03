# 🧠 AI DDR Report Generator

An AI-powered system that processes inspection and thermal PDF reports and generates a structured Damage Diagnostic Report (DDR).

---

## 🚀 Features

- 📄 Extracts text from inspection and thermal PDFs  
- 🖼️ Extracts images from reports  
- 🧠 Generates structured DDR report  
- ⚙️ Modular architecture for AI integration  
- 📁 Saves output in structured format  

---

## 🏗️ Project Structure
```
ai-ddr-report-generator/
│
├── app.py
├── src/
│ ├── pdf_parser.py
│ ├── image_extractor.py
│ ├── ai_processor.py
│ └── utils.py
│
├── outputs/
│ ├── images/
│ └── reports/
│
├── inspection.pdf
├── thermal.pdf
├── requirements.txt
└── README.md
```
---

## ⚙️ How It Works

1. Extracts text from PDFs  
2. Extracts images for visual inspection  
3. Processes data  
4. Generates DDR report with:
   - Issue Summary  
   - Observations  
   - Root Cause  
   - Severity  
   - Recommendations  

---

## 🧠 AI Integration

The system is designed to integrate LLM-based reasoning for intelligent report generation.

Due to API quota limitations, a fallback rule-based logic is used, but the architecture supports real AI integration.

---

## ▶️ Run the Project

```bash
pip install -r requirements.txt
python app.py
---
📄 Output
Generated report:
outputs/reports/ddr_report.txt
🎯 Future Improvements
Streamlit UI
Real-time AI integration
PDF report generation automation
---
````
👩‍💻 Author

Anjali
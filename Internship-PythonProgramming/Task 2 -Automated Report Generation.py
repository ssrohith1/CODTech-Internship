import pandas as pd
from fpdf import FPDF

class AutomatedReport:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_data(self):
        try:
            self.data = pd.read_csv(self.file_path)
        except Exception as e:
            print(f"Error reading file: {e}")
            exit()

    def analyze_data(self):
        if self.data is not None:
            summary = self.data.describe()
            return summary
        else:
            print("No data available for analysis.")
            return None

    def generate_pdf_report(self, summary):
        class PDF(FPDF):
            def header(self):
                self.set_font("Arial", "B", 16)
                self.cell(200, 10, "Automated Data Analysis Report", ln=True, align="C")
                self.ln(10)

            def footer(self):
                self.set_y(-15)
                self.set_font("Arial", "I", 10)
                self.cell(0, 10, "Generated Automatically", align="C")
        
        pdf = PDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, "Summary Statistics:", ln=True, align="L")
        pdf.ln(10)

        for col in summary.columns:
            pdf.cell(200, 10, f"{col}:", ln=True, align="L")
            for index, value in summary[col].items():
                pdf.cell(200, 10, f"  {index}: {value:.2f}", ln=True, align="L")
            pdf.ln(5)

        pdf.output("Automated_Report.pdf")
        print("PDF report generated: Automated_Report.pdf")

if __name__ == "__main__":
    FILE_PATH = "topics.csv"  # Change this to your file path
    
    report = AutomatedReport(FILE_PATH)
    report.read_data()
    summary = report.analyze_data()
    if summary is not None:
        report.generate_pdf_report(summary)
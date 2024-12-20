# **Digital Transformation of Senior Health Care**

## **Project Overview**
This project focuses on transforming the senior health care experience through digital innovation. By transitioning from paper-based assessments to a streamlined digital platform, the project aims to improve efficiency, accessibility, and scalability in health assessments. It also integrates data analytics to uncover meaningful insights and generate personalized wellness reports, empowering seniors to take proactive steps toward improving their well-being.

## **Files Included**
- **`cleaning_and_eda.R`**: R script for data cleaning, exploratory data analysis (EDA), and preprocessing survey responses.
- **`generate_reports.py`**: Python script for creating personalized wellness reports based on analyzed data.
- **`template.html`**: HTML template used by the Python script for generating dynamic reports.
- **`sample_report_1.html`**: Example of a personalized wellness report.
- **`sample_report_2.html`**: Another example showcasing the functionality and design of the reports.

## **Getting Started**
### **Prerequisites**
- **R**: Install the latest version along with essential libraries (`tidyverse`, `dplyr`, `ggplot2`).
- **Python 3.x**: Install with the required libraries (`pandas`, `jinja2`, `matplotlib`).
- **SQL Database**: Set up an SQL database to store and manage data.
- **Virtual Environment (Optional)**: Create one to manage Python dependencies.

### **Steps**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>

2. **Set Up R Environment**:
   - Open `cleaning_and_eda.R` in your preferred R editor.
   - Install the required R packages if not already installed.
   - Run the script to clean and preprocess the data.

3. **Set Up Python Environment**:
   - Navigate to the repository directory.
   - Install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```
   - Run the `generate_reports.py` script to create dynamic reports:
     ```bash
     python generate_reports.py
     ```

4. **View Reports**:
   - Open the `sample_report_1.html` and `sample_report_2.html` files in any web browser to see examples of the personalized reports.

## **Acknowledgements**
This project was developed in collaboration with Total Well-Being SG (TWBSG), a nonprofit organization dedicated to improving the health and well-being of seniors. Special thanks to the TWBSG team for their insights and support throughout the project.

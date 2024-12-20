import pandas as pd
import pdfkit
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader

options = {
    'page-size': 'A4',
    'margin-top': '10mm',
    'margin-right': '10mm',
    'margin-bottom': '10mm',
    'margin-left': '10mm',
    }

# Load the data
df = pd.read_csv('output_d23.csv')

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('report_template_final.html')

def generate_report(participant):
    # Extract data for the participant
    shapesg_id = participant['shapesg_id']
    wellness_score = participant['wellness_score']
    avg_score = participant.get('avg_score', 'N/A')
    medical1_burden_cat = participant['medical1_burden_cat']
    gsq1_category = participant['gsq1_category']
    moca1_category = participant['moca1_category']
    cope1_cat = participant['cope1_cat']
    screen1_cat = participant['screen1_cat']
    bmi = participant['bmi1']
    bmi_category = participant['bmi1_cat']
    whr = participant['whr1']
    whr_category = participant['whr1_cat']
    weight = participant['wt1']
    height = participant['ht1']

      
    # Extract aggregated screening scores
    screen1_tot = participant.get('screen1_tot', 'N/A')
    screen1_norm = participant.get('screen1_norm', 'N/A')
    screen1_cat = participant.get('screen1_cat', 'N/A')
    
    # Extract individual screening items (e.g., vaccinations and checkups)
    screening_items = {key: participant[key] for key in participant.index if key.startswith('screen1_')}
    
    
    # Define risk levels for sorting
    risk_priority = {
        'High': 1,
        'Medium': 2,
        'Low': 3
    }
    
    # Prepare risk domains list
    risk_domains = [
    {'name': 'Medical Conditions', 'category': medical1_burden_cat, 'risk': 'High' if medical1_burden_cat in ['very_high_health_burden', 'high_health_burden'] else 'Medium' if medical1_burden_cat == 'moderate_health_burden' else 'Low'},
    {'name': 'Sleep Quality', 'category': gsq1_category, 'risk': 'High' if gsq1_category == 'poor' else 'Medium' if gsq1_category == 'moderate' else 'Low'},
    {'name': 'Cognitive Well-Being (MoCA)', 'category': moca1_category, 'risk': 'High' if moca1_category == 'severe_impairment' else 'Medium' if moca1_category == 'moderate_impairment' else 'Low'},
    {'name': 'Emotional Coping', 'category': cope1_cat, 'risk': 'High' if cope1_cat == 'emerging_resilience' else 'Medium' if cope1_cat == 'moderate_resilience' else 'Low'},
    {'name': 'Screening Engagement', 'category': screen1_cat, 'risk': 'High' if screen1_cat == 'not_engaged' else 'Medium' if screen1_cat == 'partially_engaged' else 'Low'},
    {'name': 'Body Mass Index (BMI)', 'category': bmi_category, 'risk': 'High' if bmi_category == 'obesity' else 'Medium' if bmi_category == 'overweight' else 'Low'},
    {'name': 'Waist-Hip Ratio (WHR)', 'category': whr_category, 'risk': 'High' if whr_category == 'high_risk' else 'Low'}
]
    
    # Sort the risk domains by priority: High > Medium > Low
    sorted_risk_domains = sorted(risk_domains, key=lambda x: risk_priority[x['risk']])
    
    
    # Render the HTML report using the template
    html_out = template.render(
        shapesg_id=shapesg_id,
        wellness_score=int(wellness_score),
        avg_score=int(avg_score),
        bmi=bmi,
        bmi_category=bmi_category,
        whr=whr,
        whr_category=whr_category,
        weight=weight,
        height=height,
        medical1_burden_cat=medical1_burden_cat,
        gsq1_category=gsq1_category,
        moca1_category=moca1_category,
        cope1_cat=cope1_cat,
        screen1_tot=screen1_tot,
        screen1_norm=screen1_norm,
        screen1_cat=screen1_cat,
        screening_items=screening_items,
        risk_domains=sorted_risk_domains
    )

    with open("test.html", 'w') as f:
        f.write(html_out)
    
    # Generate PDF
    output_file = f"report_{shapesg_id}.pdf"
    pdfkit.from_string(html_out, output_file)
    print(f"Generated report for {shapesg_id}")


# Generate report for only the first five participant
for _, participant in df.head(5).iterrows():
    generate_report(participant)
    
# # Generate report for a specific participant
# specific_id = '2023-001'  # Replace with the ID you want to test
# filtered_df = df[df['shapesg_id'] == specific_id]

# for _, participant in filtered_df.iterrows():
#     generate_report(participant)

# # Generate reports for all participants
# for _, participant in df.iterrows():
#     generate_report(participant)

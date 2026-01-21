UIDAI Aadhaar Update Anomaly Detection System
Overview

This project was developed as part of the UIDAI Data Hackathon 2026.
It implements a statistical surveillance framework to analyze Aadhaar enrolment and update activity and detect abnormal patterns across states, districts, and pincodes.

The objective is to move beyond descriptive analytics and demonstrate how large-scale Aadhaar transaction data can be translated into operational insights that support proactive monitoring, targeted audits, and system improvement.

Problem Statement

Aadhaar enrolment and update operations generate large volumes of transactional data daily. While most updates are citizen-driven and organic, sudden spikes in biometric or demographic updates often indicate:

Faulty biometric devices

Mass correction or update drives

Software or backend issues

Potential operator misuse

Such issues are typically identified through delayed audits or complaints. This project proposes a data-driven, automated approach to detect abnormal behaviour early using statistical methods.

Dataset

The analysis uses the anonymised Aadhaar enrolment and update datasets provided by UIDAI as part of the hackathon.

Data Categories

Enrolment counts (age-wise)

Biometric update counts

Demographic update counts

Geographic identifiers (state, district, pincode)

Time dimension (daily records)

Note:
Raw CSV datasets are not included in this repository due to:

GitHub file size limits

Sensitivity of large-scale Aadhaar operational data

The repository focuses on code, methodology, and results.
Data can be shared separately if required by evaluators.

Methodology
1. Data Aggregation

Daily enrolment, biometric, and demographic updates aggregated at pincode level

Age-wise counts consolidated into operational metrics

2. Rate Computation

Update-to-enrolment ratios computed to normalise for population and activity size

3. Noise Reduction

Rolling averages applied to smooth short-term fluctuations

4. Anomaly Detection

Z-score based anomaly detection applied to rolling metrics

Extreme deviations from historical behaviour flagged as high-risk events

5. Risk Ranking

Each pincode assigned a consolidated anomaly score

High-risk pincodes and states ranked for operational attention

Key Results and Visualisations

State-Level Anomaly Intensity

<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/9c7b75a5-1860-4729-b6f2-6d7ca8d202bd" />

This chart presents the top states ranked by mean anomaly intensity.
Higher values indicate regions where Aadhaar update activity consistently deviates from historical norms, highlighting areas that may require enhanced operational monitoring or audit prioritisation.

Relationship Between Biometric and Demographic Anomalies
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/dee0b7c8-330a-4049-85a7-ee88491ca372" />

This scatter plot visualises the relationship between biometric and demographic anomaly scores at the pincode level.
Most observations cluster around normal ranges, while extreme outliers indicate coordinated or systemic update behaviour rather than random variation.

Forensic Pincode Case Study 
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/493a0d55-2efa-4acc-a636-858995646011" />
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/623a2e8b-acd0-41f5-b79b-54341430e8a9" />
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/2857a798-02b9-4d23-be69-8e9672802837" />


This time-series plot shows anomaly score trends for a high-risk pincode.
Sharp spikes exceeding Z-score thresholds indicate statistically extreme behaviour inconsistent with organic enrolment-driven updates.
Such patterns are commonly associated with mass update drives, device-level failures, or potential operator misuse and warrant immediate investigation.

Operational Impact

The proposed framework enables UIDAI to:

Move from reactive audits to proactive monitoring

Prioritise field inspections based on quantified risk

Detect systemic issues early

Improve Aadhaar data quality and operational efficiency

This approach is scalable, automated, and suitable for integration into existing UIDAI monitoring workflows.

# Phase 2 Results

## Root Causes

1.  **Material weaknesses in entity-level controls and model validation:**
    Evidence: "in addition, material weaknesses were identified in certain entity level controls and ‘the control over the review and validation of th..."

2.  **High degree of auditor judgment and effort required for ECL calculations:**
    Evidence: "performing audit procedures to evaluate the reasonableness of the calculations of ECL on customer loans with shared credit risk characteristics required a high degree of auditor judgment and an increased extent of effort."

3.  **Significant volume of underlying data for ECL sourced from IT systems:**
    Evidence: "There is also a significant volume of data used in the ECL which is sourced from relevant Information Technology (IT) systems."

4.  **Reliance on operating effectiveness of manual and IT controls for data transfer and processing:**
    Evidence: "We tested operating effectiveness of certain manual and IT controls over data transfer, information capture and processing in the generation of the underlying statistical data, as well as IT general controls related to user access for the relevant IT systems."

## 5 Whys

**Problem:** Material weaknesses were identified in certain entity-level controls and the control over the review and validation of models.

1.  **Why** were material weaknesses identified in certain entity-level controls and the control over the review and validation of models?
    *   **Because** evaluating the reasonableness of Expected Credit Loss (ECL) calculations required a high degree of auditor judgment and an increased extent of effort, suggesting existing controls may not be sufficiently robust or consistently applied.
    *   Evidence: "in addition, material weaknesses were identified in certain entity level controls and ‘the control over the review and validation of th..." and "performing audit procedures to evaluate the reasonableness of the calculations of ECL on customer loans with shared credit risk characteristics required a high degree of auditor judgment and an increased extent of effort."

2.  **Why** did the ECL calculations require such a high degree of judgment and effort?
    *   **Because** the ECL calculations involve significant judgment in incorporating macroeconomic forward-looking information and utilize a significant volume of data sourced from various IT systems.
    *   Evidence: "In addition, the ECL includes significant judgment in incorporating macroeconomic forward looking information in its impairment calculations using scenarios for direct adjustment of default probabilities. There is also a significant volume of data used in the ECL which is sourced from relevant Information Technology (IT) systems."

3.  **Why** is there significant judgment and a large volume of data involved in ECL calculations?
    *   **Because** the Group calculates ECL on a collective basis for loans to customers with shared credit risk characteristics, which necessitates the use of complex estimates for Probability of Default (PD), Loss Given Default (LGD), and Exposure at Default (EAD).
    *   Evidence: "The Group calculates ECL on a collective basis for loans to ‘customers with shared credit risk characteristics and uses estimates of the Probability of Default (PD), the Loss Given Default (LGD) and the Exposure at Default (EAD)."

4.  **Why** is the ECL calculation process so critical and complex?
    *   **Because** the loss allowance for expected credit loss on loans to customers represents a material amount (KZT 295,843 million as at 31 December 2024), making its accurate and reliable calculation fundamental for financial reporting.
    *   Evidence: "As disclosed in Note 12 as at 31 December 2024, the loss allowance for expected credit loss ("ECL") on loans to customers amounted to KZT 295,843 million."

5.  **Why** is the accuracy of ECL calculations so important?
    *   **Because** material misstatements in financial statements, whether due to fraud or error, could reasonably be expected to influence the economic decisions of users.
    *   Evidence: "Misstatements can arise from fraud or error and are considered material if, individually or in the aggregate, they could reasonably be expected to influence the economic decisions of users taken on the basis of these consolidated financial statements."

## Metrics to Monitor

1.  **Accuracy of Expected Credit Loss (ECL) calculations.**
    Evidence: "We involved internal credit specialists to assist us in evaluating and challenging the assumptions and methodologies used to develop the PD, LGD, EAD and the forecasted macroeconomic variables, which included testing the mathematical accuracy of the ECL;"

2.  **Completeness and accuracy of underlying data used in ECL models.**
    Evidence: "We tested the completeness and accuracy of the underlying data used in the ECL;"

3.  **Operating effectiveness of manual and IT controls over data transfer, information capture, and processing.**
    Evidence: "We tested operating effectiveness of certain manual and IT controls over data transfer, information capture and processing in the generation of the underlying statistical data, as well as IT general controls related to user access for the relevant IT systems."

4.  **Timeliness of credit decisions.**
    Evidence: "The Group has developed an automated, centralized and big data- driven proprietary loan approval process that enables it to make instant credit decisions."

5.  **Quality of approved loans.**
    Evidence: "The quality of approved loans are monitore..."

## Proposed AI Agent

**Purpose:** To enhance the accuracy, consistency, and efficiency of Expected Credit Loss (ECL) calculations and strengthen the underlying data and control processes.

**Inputs:**
1.  **Underlying data for ECL:** This includes data used for Probability of Default (PD), Loss Given Default (LGD), and Exposure at Default (EAD) calculations.
    Evidence: "We tested the completeness and accuracy of the underlying data used in the ECL;"
2.  **Macroeconomic forward-looking information:** Data used in impairment calculations, including scenarios for direct adjustment of default probabilities.
    Evidence: "In addition, the ECL includes significant judgment in incorporating macroeconomic forward looking information in its impairment calculations using scenarios for direct adjustment of default probabilities."
3.  **ECL model assumptions and methodologies:** The current parameters and logic used to develop PD, LGD, and EAD.
    Evidence: "We involved internal credit specialists to assist us in evaluating and challenging the assumptions and methodologies used to develop the PD, LGD, EAD and the forecasted macroeconomic variables..."
4.  **Logs and records from data transfer, information capture, and processing systems:** To monitor the operational effectiveness of controls.
    Evidence: "We tested operating effectiveness of certain manual and IT controls over data transfer, information capture and processing in the generation of the underlying statistical data..."

**Outputs:**
1.  **Validated ECL calculations:** Providing more accurate and consistent ECL figures for financial reporting.
    Evidence: "the loss allowance for expected credit loss ("ECL") on loans to customers amounted to KZT 295,843 million."
2.  **Identified data anomalies and inconsistencies:** Highlighting issues in the completeness and accuracy of the underlying data.
    Evidence: "We tested the completeness and accuracy of the underlying data used in the ECL;"
3.  **Recommendations for control improvements:** Suggestions for strengthening manual and IT controls related to data processing and model validation.
    Evidence: "material weaknesses were identified in certain entity level controls and ‘the control over the review and validation of th..."
4.  **Automated reports on ECL model performance and assumption validity:** To support ongoing review and validation processes.
    Evidence: "the control over the review and validation of th..."

**Decisions:**
1.  **Flagging potential material misstatements in ECL calculations:** Based on deviations from expected ranges or identified data integrity issues.
    Evidence: "Identify and assess the risks of material misstatement of the consolidated financial statements, whether due to fraud or error..."
2.  **Suggesting adjustments to ECL model parameters or macroeconomic assumptions:** Based on real-time data analysis and historical performance trends.
    Evidence: "In addition, the ECL includes significant judgment in incorporating macroeconomic forward looking information in its impairment calculations using scenarios for direct adjustment of default probabilities."
3.  **Identifying specific control weaknesses in data processing workflows:** Pinpointing areas of failure or inefficiency in data transfer and capture.
    Evidence: "We tested operating effectiveness of certain manual and IT controls over data transfer, information capture and processing..."

**Non-Goals:**
1.  **Replacing human judgment entirely in strategic financial decisions:** The AI agent serves as an analytical tool to assist, not replace, the high degree of auditor and management judgment required for complex financial assessments.
    Evidence: "performing audit procedures to evaluate the reasonableness of the calculations of ECL on customer loans with shared credit risk characteristics required a high degree of auditor judgment and an increased extent of effort."
2.  **Directly managing or executing financial transactions:** The agent's scope is limited to analysis, validation, and reporting, not operational financial activities.
    Evidence: Not found in evidence.
3.  **Providing legal or regulatory compliance advice:** The agent focuses on data and calculation accuracy, not the interpretation or application of legal or regulatory frameworks.
    Evidence: "The Company is regulated by the National Bank of the Republic of Kazakhstan ("NBRK”) and the Agency of the Republic of Kazakhstan for Regulation and Development of Financial Market."
4.  **Developing new financial products or services:** The agent's function is to support the integrity of existing financial reporting processes, not product innovation.
    Evidence: Not found in evidence.

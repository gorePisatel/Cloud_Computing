# Phase 2 Results

## Root Causes

1.  **Reliance on estimates and judgment in Expected Credit Loss (ECL) calculations:** The calculation of ECL involves significant judgment, particularly in incorporating macroeconomic forward-looking information.
    Evidence: "The Group calculates ECL on a collective basis for loans to ‘customers with shared credit risk characteristics and uses estimates of the Probability of Default (PD), the Loss Given Default (LGD) and the Exposure at Default (EAD). In addition, the ECL includes significant judgment in incorporating macroeconomic forward looking information in its impairment calculations using scenarios for direct adjustment of default probabilities."

2.  **Material weaknesses in certain entity-level controls and data validation:** The audit identified specific control deficiencies related to the review and validation of data.
    Evidence: "in addition, material weaknesses were identified in certain entity level controls and ‘the control over the review and validation of th..."

3.  **Complexity and volume of data used in ECL calculations:** A large volume of data from various IT systems is used for ECL, which contributes to the complexity of ensuring completeness and accuracy.
    Evidence: "There is also a significant volume of data used in the ECL which is sourced from relevant Information Technology (IT) systems."

4.  **Dependence on continuous product innovation and network effects for business growth:** The company's business model relies on ongoing product innovation and the generation of powerful network effects for sustained growth and strong financial performance.
    Evidence: "Our business model, reinforced by our highly recognizable brand and continuing product innovation, generates powerful network effects, which has resulted in growth across all our platforms and strong financial performance."

## 5 Whys

**Problem:** Material weaknesses were identified in certain entity-level controls and data validation related to Expected Credit Loss (ECL) calculations.

1.  **Why** were material weaknesses identified in certain entity-level controls and data validation?
    *   Evidence: "in addition, material weaknesses were identified in certain entity level controls and ‘the control over the review and validation of th..."
    *   **Because** there is a significant volume of underlying data used in the ECL, sourced from various Information Technology (IT) systems, making comprehensive validation challenging.
    *   Evidence: "There is also a significant volume of data used in the ECL which is sourced from relevant Information Technology (IT) systems."

2.  **Why** does the significant volume of data from IT systems lead to weaknesses in controls and validation?
    *   **Because** the operating effectiveness of certain manual and IT controls over data transfer, information capture, and processing, as well as IT general controls related to user access, may not be robust enough to manage the scale and complexity.
    *   Evidence: "+ We tested operating effectiveness of certain manual and IT controls over data transfer, information capture and processing in the generation of the underlying statistical data, as well as IT general controls related to user access for the relevant IT systems."

3.  **Why** might these controls not be fully robust for managing the data?
    *   **Because** the Group relies on significant judgment and estimates in its ECL calculations, particularly when incorporating macroeconomic forward-looking information, which introduces inherent subjectivity and complexity into the validation process.
    *   Evidence: "The Group calculates ECL on a collective basis for loans to ‘customers with shared credit risk characteristics and uses estimates of the Probability of Default (PD), the Loss Given Default (LGD) and the Exposure at Default (EAD). In addition, the ECL includes significant judgment in incorporating macroeconomic forward looking information in its impairment calculations using scenarios for direct adjustment of default probabilities."

4.  **Why** does reliance on significant judgment and estimates contribute to control weaknesses?
    *   **Because** the inherent subjectivity and complexity of these estimates, especially when adjusting default probabilities based on macroeconomic scenarios, makes it difficult to establish fully automated and consistently effective controls for ensuring the completeness and accuracy of all underlying data and assumptions.
    *   Evidence: "In addition, the ECL includes significant judgment in incorporating macroeconomic forward looking information in its impairment calculations using scenarios for direct adjustment of default probabilities."

5.  **Why** is it difficult to establish fully automated and consistently effective controls for subjective estimates?
    *   Not found in evidence.

## Metrics to Monitor

1.  **Expected Credit Loss (ECL) allowance on loans to customers:** This is a key financial metric directly impacted by the identified root causes.
    Evidence: "As disclosed in Note 12 as at 31 December 2024, the loss allowance for expected credit loss ("ECL") on loans to customers amounted to KZT 295,843 million."

2.  **Accuracy of Probability of Default (PD), Loss Given Default (LGD), and Exposure at Default (EAD) estimates:** These are critical components of the ECL calculation.
    Evidence: "The Group calculates ECL on a collective basis for loans to ‘customers with shared credit risk characteristics and uses estimates of the Probability of Default (PD), the Loss Given Default (LGD) and the Exposure at Default (EAD)."

3.  **Technology & product development expenses:** Monitoring these expenses can indicate investment in innovation and platform development.
    Evidence: "Technology & product development (60,807) (88,657) (109,553)"

4.  **Completeness and accuracy of underlying data used in ECL:** This directly addresses the data quality and control weaknesses.
    Evidence: "We tested the completeness and accuracy of the underlying data used in the ECL;"

5.  **Net Income:** This provides an overall measure of financial performance, which is influenced by the effectiveness of operations and risk management.
    Evidence: "NET INCOME 588,844 848,770 __1,056,834"

## Proposed AI Agent

**Purpose:** To enhance the accuracy and efficiency of Expected Credit Loss (ECL) calculations and improve data validation processes by leveraging advanced data analysis and automation.

Evidence: "As disclosed in Note 12 as at 31 December 2024, the loss allowance for expected credit loss ("ECL") on loans to customers amounted to KZT 295,843 million. The Group calculates ECL on a collective basis for loans to ‘customers with shared credit risk characteristics and uses estimates of the Probability of Default (PD), the Loss Given Default (LGD) and the Exposure at Default (EAD). In addition, the ECL includes significant judgment in incorporating macroeconomic fo..."
Evidence: "There is also a significant volume of data used in the ECL which is sourced from relevant Information Technology (IT) systems. in addition, material weaknesses were identified in certain entity level controls and ‘the control over the review and validation of th..."

**Inputs:**
*   Historical customer loan data (e.g., payment history, credit characteristics).
*   Macroeconomic forward-looking information and scenarios.
*   Underlying data from relevant Information Technology (IT) systems used in ECL calculations.

Evidence: "The Group calculates ECL on a collective basis for loans to ‘customers with shared credit risk characteristics and uses estimates of the Probability of Default (PD), the Loss Given Default (LGD) and the Exposure at Default (EAD). In addition, the ECL includes significant judgment in incorporating macroeconomic forward looking information in its impairment calculations using scenarios for direct adjustment of default probabilities. There is also a significant volume of data used in the ECL which is sourced from relevant Information Technology (IT) systems."

**Outputs:**
*   Calculated estimates for Probability of Default (PD), Loss Given Default (LGD), and Exposure at Default (EAD).
*   Proposed Expected Credit Loss (ECL) allowance figures.
*   Reports highlighting potential inconsistencies, anomalies, or gaps in the input data for review.
*   Analysis supporting the evaluation of macroeconomic assumptions used in ECL models.

Evidence: "The Group calculates ECL on a collective basis for loans to ‘customers with shared credit risk characteristics and uses estimates of the Probability of Default (PD), the Loss Given Default (LGD) and the Exposure at Default (EAD)."
Evidence: "We tested the completeness and accuracy of the underlying data used in the ECL;"
Evidence: "In addition, the ECL includes significant judgment in incorporating macroeconomic forward looking information in its impairment calculations using scenarios for direct adjustment of default probabilities."

**Capabilities/Support for Decisions:**
*   Automate aspects of the ECL calculation process to improve efficiency and consistency.
*   Identify and flag data points that deviate significantly from expected patterns or historical norms for human investigation.
*   Provide analytical support to internal credit specialists in evaluating and challenging the assumptions and methodologies used for PD, LGD, EAD, and macroeconomic variables.

Evidence: "The Group has developed an automated, centralized and big data- driven proprietary loan approval process that enables it to make instant credit decisions." (Demonstrates existing capability for data-driven processes).
Evidence: "We involved internal credit specialists to assist us in evaluating and challenging the assumptions and methodologies used to develop the PD, LGD, EAD and the forecasted macroeconomic variables, which included testing the mathematical accuracy of the ECL;"
Evidence: "There is also a significant volume of data used in the ECL which is sourced from relevant Information Technology (IT) systems."

**Non-Goals:**
*   Replacing human judgment in the final determination and approval of the Expected Credit Loss (ECL) allowance.
*   Directly managing or implementing IT general controls, user access controls, or other manual controls over data transfer and processing.
*   Making final credit approval decisions for individual customers or loans.

Evidence: "...performing audit procedures to evaluate the reasonableness of the calculations of ECL on customer loans with shared credit risk characteristics required a high degree of auditor judgment and an increased extent of effort."
Evidence: "+ We tested operating effectiveness of certain manual and IT controls over data transfer, information capture and processing in the generation of the underlying statistical data, as well as IT general controls related to user access for the relevant IT systems."
Evidence: "The Group has developed an automated, centralized and big data- driven proprietary loan approval process that enables it to make instant credit decisions."

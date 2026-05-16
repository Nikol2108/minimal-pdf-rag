# Minimal PDF RAG Application

A minimal Retrieval-Augmented Generation (RAG) application built with Python, LangChain, OpenAI embeddings, and FAISS.
The system loads a PDF document, splits it into chunks, stores embeddings in a local vector database, retrieves the most relevant chunks for a user question, and generates an answer based only on the retrieved context.

# How to Run

```bash
pip install -r requirements.txt
```

Create a .env file and add:
```bash
OPENAI_API_KEY=your_api_key
```

Run the application:
```bash
python main.py
```

---

# PDF Used

**Infection Prevention Guidelines for Safe Patient Care**

Location:

```bash
data/Infection-Prevention-Guidelines-for-Safe-Patient-Care.pdf
```

---

# Example Questions and Answers

## Question 1

**Q :** How long is perishable home-cooked food allowed to be kept in the nourishment refrigerator, and what must be written on its label?

**A :** Perishable home-cooked food is allowed to be kept in the nourishment refrigerator for 7 days from the date it is placed in the refrigerator. The label must include the patient's name and the date it is placed in the refrigerator.

### Source Chunks:

```text
--- Source 1 | page 11 | data/Infection-Prevention-Guidelines-for-Safe-Patient-Care.pdf ---
not consumed within 4 hours of being removed from temperature control,  should be refrigerated in a refrigeration unit that is 41°F or less and labeled  with the patient's name and the date it is placed in the refrigerator.  Refrigerated food from home is good for 7 days from the date it is placed in  the refrigerator. Any unlabeled (patient name and/or date placed in  refrigerator) home-prepared/home-cooked food should be discarded  immediately. This pertains to all patient nourishment refrigerators including  those in patient rooms.  e. Un-opened commercially prepared food with an expiration date (i.e., milk  carton) may be stored in the nourishment room refrigerator until the date of
```

```text
--- Source 2 | page 11 | data/Infection-Prevention-Guidelines-for-Safe-Patient-Care.pdf ---
carton) may be stored in the nourishment room refrigerator until the date of  expiration. It must be discarded on the date of expiration.  2. Employees/Visitors  • Staff are not allowed to eat or drink in a patient's room. Visitors may eat or  drink in the patient's room unless the patient is on Enteric, Airborne, or  Droplet Precautions. Visitors of patients on Contact or Enteric Precautions  may use the microwave or nutrition areas as long as hand hygiene is  performed according to policy.  3. Patients  • Patient consumption of food prepared by an individual outside the hospital
```

```text
--- Source 3 | page 11 | data/Infection-Prevention-Guidelines-for-Safe-Patient-Care.pdf ---
and Plant Engineering or management notified if there is deviation from this  range. Breast milk, laboratory specimens and medications will not be stored  with patient nutrition. If temperatures are recorded via a wireless monitoring  system (RFID) (e.g., AeroScout), logs are not necessary.  • In outpatient settings: Perishable (e.g., meats, fish, dairy products,  vegetables) patient nutrition refrigerator temperatures are  monitored and logged on days the clinic is open.  d. Home-prepared/home-cooked foods that are perishable if not refrigerated if  not consumed within 4 hours of being removed from temperature control,
```

```text
--- Source 4 | page 11 | data/Infection-Prevention-Guidelines-for-Safe-Patient-Care.pdf ---
COPY in a drawer, separate labeled container, or section within the refrigerator.  V. Nourishment  1. Refrigerated Food Storage (Nourishment Refrigerators)  a. Food storage in patient care areas must not be stored in a refrigerator used  to store medicines, chemicals, or specimens.  b. All refrigerators will be cleaned when soiled.  c. Temperatures should be monitored on patient nourishment refrigerators and  recorded daily or be monitored via the RFID system. The temperature should  be maintained at appropriate temperature for the refrigerators intended use  and Plant Engineering or management notified if there is deviation from this.
```
---

## Question 2

**Q :** What is the required distance that patient care supplies must be stored from a sink, unless a splashguard is present?

**A :** Patient care supplies must be stored at least 3 feet from a sink unless a splashguard is present.

### Source Chunks:

```text
--- Source 1 | page 14 | data/Infection-Prevention-Guidelines-for-Safe-Patient-Care.pdf ---
AE. Supply Rooms and Storage of Supplies  1. All patient care items should be stored at least 8 inches from the floor.  2. Patient care supplies must be stored at least 3 feet from a sink unless a splashguard  is present.  3. Patient care supplies should be removed from the primary shipping container and not  used for storage on the unit.  4. Clean patient care items may be stored in the dirty utility room only when contained  within an enclosed cabinet.  Infection Prevention Guidelines for Safe Patient Care. Retrieved 04/2024. Official copy at http://unchealthcare- uncmc.policystat.com/policy/14684923/. Copyright © 2024 UNC Medical Center Page 15 of 23
```

```text
--- Source 2 | page 15 | data/Infection-Prevention-Guidelines-for-Safe-Patient-Care.pdf ---
COPY 5. Clean items used for direct patient care and hand hygiene products (i.e., hand soap,  alcohol-based hand rub, paper towels) cannot be stored under the sink due to the risk  of water contamination. Items not used for direct patient care (e.g., empty sharps  containers, cleaning supplies, trash bags, empty soiled instrument transport  containers) and items going for reprocessing or disposal (e.g., battery buckets,  recycling buckets for used patient equipment) may be stored under sinks.  6. Doors to soiled utility rooms must be kept closed.  7. Only those supplies essential for a patient's care should be kept in the patient's room.
```

```text
--- Source 3 | page 15 | data/Infection-Prevention-Guidelines-for-Safe-Patient-Care.pdf ---
7. Only those supplies essential for a patient's care should be kept in the patient's room.  At the time of patient discharge, unused items may be saved and used for another  patient, including the supplies of those patients on Contact Precautions, as long as the  item is not visibly soiled, the packaging has not been opened or compromised. These  recommendations may be changed or altered during an ongoing outbreak situation.  8. Once tape has been removed from the patient care item supply drawer it is considered  contaminated and must not be replaced in the drawer, since tape is a single patient  use item.  AF. Visitors/Consulting Groups
```

```text
--- Source 4 | page 10 | data/Infection-Prevention-Guidelines-for-Safe-Patient-Care.pdf ---
procedures, transvaginal ultrasound, transrectal ultrasound procedures).  S. Medication Preparation  1. Medication preparation areas should be kept clean and free of clutter. Medication  preparation areas should be wiped with an approved EPA-registered disinfectant at  least once each shift and when visibly soiled.  2. Medications should not be prepared near areas of splashing water (e.g., within 3 feet  of a sink). Alternatively, a splashguard can be mounted beside the sink.  3. Aseptic technique must be used when entering a medication vial and hand hygiene  should be performed before preparing a medication. Vials should be handled with
```
---

## Question 3

**Q :** According to the Spaulding classification scheme, what type of disinfection or treatment do "Critical Items" require, and what are two examples of such items?

**A :** Critical Items require sterilization. Two examples of critical items include surgical instruments and certain catheters.

### Source Chunks:

```text
--- Source 1 | page 5 | data/Infection-Prevention-Guidelines-for-Safe-Patient-Care.pdf ---
Patient Care Items  Semi-critical  Items: Require  at least high- level  disinfection  Contact intact mucous  membranes or non-intact skin.  (Examples include but not  limited to some endoscopes,  endocavitary probes,  diaphragm fittings rings,  laryngeal blades.)  Infection Prevention policy:  High Level Disinfection (HLD)  – Manual reprocessing of  reusable semi-critical medical  devices  Infection Prevention policy:  Endoscope  Non-critical  Items: Require  low-level  disinfection  Contact intact skin but not  mucous membranes.  (Examples include but not  limited to bed pans, blood  pressure cuffs, and  stethoscopes.)  Infection Prevention policy:  Cleaning and Disinfection of
```

```text
--- Source 2 | page 4 | data/Infection-Prevention-Guidelines-for-Safe-Patient-Care.pdf ---
regarding the cleaning and maintenance of these items.  b. Cleaning Routines and Cleaning Agents  a. The Spaulding classification scheme is a rational approach to disinfection  and sterilization of reusable patient care equipment and/or devices. Based  on the degree of risk of infection involved in the use of items, the scheme  divides reusable patient care items into three distinct categories: 1) critical;  2) semi-critical; 3) non-critical.  i. Semi-critical and critical items (i.e., reusable instruments and  medical devices requiring high-level disinfected or sterilized prior  to use on another patient) should be wiped to remove gross soil
```

```text
--- Source 3 | page 5 | data/Infection-Prevention-Guidelines-for-Safe-Patient-Care.pdf ---
be accessed for decontamination, the equipment must be labeled  with a BIOHAZARD tag denoting the area of contamination.  ii. Ensure that single use items are discarded properly and used for  only one patient as described in the Infection Prevention policy:  Reuse of Single Use Devices (SUDs) .  Critical  Items: Require  sterilization  Enter/contact normally sterile  tissue or the vascular system.  (Examples include but not  limited to surgical instruments,  certain catheters, implants,  laparoscopes, arthroscopes.)  Infection Prevention policy:  Sterilization of Reusable  Patient Care Items  Semi-critical  Items: Require  at least high- level  disinfection  Contact intact mucous
```

```text
--- Source 4 | page 6 | data/Infection-Prevention-Guidelines-for-Safe-Patient-Care.pdf ---
COPY High Level Disinfection (HLD) – Manual reprocessing of reusable semi-critical medical  devices.  a. Examples in addition to the items in the above table would include rectal and  vaginal probes.  b. Endoscopes should be reprocessed following the policy, Infection  Prevention: Endoscope.  e. For Non-critical reusable patient equipment, reusable patient care items and  environmental surfaces refer to Infection Prevention policy: Cleaning and Disinfection  of Non-critical Items.  F. Electronics  1. Used by staff.  a. Gloves must be removed and perform hand hygiene after providing patient  care and prior to use of computer equipment. Keyboards will be disinfected  daily using a Sani-Cloth.
```
---

# Design Notes
I built this project using LangChain, OpenAI embeddings (text-embedding-3-small), FAISS, and gpt-4o-mini.
I chose FAISS as the local vector store because it is lightweight, fast, and simple to use for similarity search in small RAG applications.
It allows storing embeddings locally without needing an external database setup, which made it a good fit for the limited time scope of the assignment.
I used OpenAI embeddings for semantic similarity search and gpt-4o-mini as the LLM because it provides good performance while keeping the implementation simple and cost-effective.
Since the assignment was limited to 90 minutes, I focused on building a clean and readable end-to-end RAG pipeline for a single PDF document. I tried to keep the code modular and easy to follow by separating each stage of the process into dedicated functions.
One limitation of the current approach is that retrieval quality depends mostly on chunking and similarity search. The system also works with a single PDF and does not include reranking, metadata filtering, or conversation memory.
With more time, I would improve retrieval quality using reranking or hybrid search, support multiple PDFs with dynamic vector stores, and add stronger error handling and evaluation logic.

---

# Tools Used

I used ChatGPT as a supporting tool for discussing implementation ideas and debugging during development.

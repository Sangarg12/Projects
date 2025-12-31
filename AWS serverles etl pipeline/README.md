Hospital JSON ➜ Parquet ➜ Athena ➜ QuickSight 🚀
This repo contains an AWS serverless analytics pipeline that:

reads nested hospital JSON files from Amazon S3 📥

flattens the JSON into a tabular format 🧩

writes the transformed output as Parquet back to S3 🧱

runs an AWS Glue Crawler to create/update an Athena table 🗂️

enables dashboards in Amazon QuickSight using Athena as the source 📊

Architecture 🏗️
Amazon S3 (Raw Zone) 📦: Stores incoming JSON files.

AWS Lambda ⚡: Triggered on S3 upload; parses, flattens, and converts JSON → Parquet.

Amazon S3 (Curated Zone) 🧊: Stores Parquet outputs (analytics-ready).

AWS Glue Crawler + Data Catalog 🧠: Discovers schema & maintains table metadata for Athena.

Amazon Athena 🔍: Queries curated Parquet data through the catalog.

Amazon QuickSight 👁️: Builds datasets and dashboards using Athena.

Data model (output) 🧾
Grain: 1 row per medicine line item in an order 💊
Flattened columns include:

🧾 Order: medicine_order_id, order_date, order_status, order_type, priority

🧍 Patient: patient_id, patient_name, gender, date_of_birth

🏥 Encounter: encounter_id, encounter_type, admission_date, discharge_date

🧑‍⚕️ Doctor: doctor_id, doctor_name, department

💊 Medicine: medicine_id, medicine_name, dosage, frequency, route, medicine_start_date, medicine_end_date

🏨 Hospital: hospital_id, hospital_name, location

Repo structure (suggested) 🗂️
src/

lambda_function.py ⚡ (Lambda handler + flatten logic)

infra/ 🏗️ (optional)

IaC templates (CloudFormation/Terraform/CDK)

sample-data/ 🧪 (optional)

Example JSON file(s) for testing

README.md 📘

Prerequisites ✅
AWS account with access to: S3, Lambda, Glue, Athena, QuickSight 🔐

S3 bucket with:

Raw input prefix (example): hospital_json_input/ 📥

Curated output prefix (example): hospital_parquet_output/ 📤

Glue crawler created (example name used in code): hospital_json_crawler 🕷️

Lambda runtime includes dependencies:

pandas 🐼

pyarrow 🏹 (for Parquet writing)

Configuration ⚙️
Update these based on your environment:

🪣 S3 bucket + raw/curated prefixes

🕷️ Glue crawler name (in code: hospital_json_crawler)

🧭 Glue database/table naming (configured in crawler)

How it works (step-by-step) 🔁
Upload a JSON file to the raw S3 prefix 📤

S3 event triggers Lambda ⚡

Lambda:

reads the JSON file 📖

flattens nested structures into a DataFrame 🧩

writes a timestamped Parquet file to curated prefix 🧱🕒

Lambda starts the Glue crawler 🕷️

Glue crawler updates/creates the table in Glue Data Catalog 🗂️

Athena queries the table 🔍 and QuickSight visualizes it 📊

Deployment (high level) 🧰
Create S3 bucket + prefixes 🪣

Create Glue crawler pointing to curated Parquet prefix 🕷️

Deploy Lambda with dependencies (layer or container image recommended) 📦

Configure S3 event notification → Lambda 🔔⚡

Validate table in Athena with a simple query 🔍

Create QuickSight dataset from Athena + build dashboards 📊

Validation checklist 🧪
Parquet files appear in curated prefix after JSON upload ✅

Glue crawler run succeeds ✅

Athena returns expected row counts (medicine-line item level) ✅

QuickSight dataset refresh works and visuals load ✅

Common pitfalls ⚠️
Mixed formats 🧨: Keep raw JSON and curated Parquet in separate prefixes.

Schema drift 🧬: JSON structure changes can break/alter inferred schema.

Lambda packaging 📦: pyarrow is heavy—use layers or container images.

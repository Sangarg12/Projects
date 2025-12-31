# Hospital JSON ➜ Parquet ➜ Athena ➜ QuickSight 🚀

This repo contains an AWS serverless analytics pipeline that:
1. 📥 Reads nested hospital JSON files from Amazon S3
2. 🧩 Flattens the JSON into a tabular format
3. 🧱 Writes the transformed output as Parquet back to S3
4. 🗂️ Runs an AWS Glue Crawler to create/update an Athena table
5. 📊 Enables dashboards in Amazon QuickSight using Athena as the source

## Architecture 🏗️

- **Amazon S3 (Raw Zone)** 📦: Stores incoming JSON files
- **AWS Lambda** ⚡: Triggered on S3 upload; parses, flattens, and converts JSON → Parquet
- **Amazon S3 (Curated Zone)** 🧊: Stores Parquet outputs (analytics-ready)
- **AWS Glue Crawler + Data Catalog** 🧠: Discovers schema & maintains table metadata for Athena
- **Amazon Athena** 🔍: Queries curated Parquet data through the catalog
- **Amazon QuickSight** 👁️: Builds datasets and dashboards using Athena

## Data Model (Output) 🧾

**Grain:** 1 row per medicine line item in an order 💊

Flattened columns include:

- 🧾 **Order**: `medicine_order_id`, `order_date`, `order_status`, `order_type`, `priority`
- 🧍 **Patient**: `patient_id`, `patient_name`, `gender`, `date_of_birth`
- 🏥 **Encounter**: `encounter_id`, `encounter_type`, `admission_date`, `discharge_date`
- 🧑‍⚕️ **Doctor**: `doctor_id`, `doctor_name`, `department`
- 💊 **Medicine**: `medicine_id`, `medicine_name`, `dosage`, `frequency`, `route`, `medicine_start_date`, `medicine_end_date`
- 🏨 **Hospital**: `hospital_id`, `hospital_name`, `location`

## Repository Structure (Suggested) 🗂️

```
.
├── src/
│   └── lambda_function.py       ⚡ (Lambda handler + flatten logic)
├── infra/                       🏗️ (optional)
│   ├── cloudformation.yaml
│   └── terraform/
├── sample-data/                 🧪 (optional)
│   └── example.json
├── README.md                    📘
└── CONTRIBUTING.md              🤝
```

## Prerequisites ✅

- AWS account with access to: S3, Lambda, Glue, Athena, QuickSight 🔐
- S3 bucket with:
  - Raw input prefix (example): `hospital_json_input/` 📥
  - Curated output prefix (example): `hospital_parquet_output/` 📤
- Glue crawler created (example name used in code): `hospital_json_crawler` 🕷️
- Lambda runtime includes dependencies:
  - `pandas` 🐼
  - `pyarrow` 🏹 (for Parquet writing)
  - `boto3` (included in Lambda runtime)

## Configuration ⚙️

Update these based on your environment:

| Parameter | Example Value | Description |
|-----------|---------------|-------------|
| S3 Bucket | `my-hospital-data` | Your S3 bucket name |
| Raw Prefix | `hospital_json_input/` | Where JSON files are uploaded |
| Curated Prefix | `hospital_parquet_output/` | Where Parquet files are written |
| Glue Crawler Name | `hospital_json_crawler` | Crawler that catalogs the data |
| Glue Database | `hospital_analytics` | Glue Data Catalog database name |
| Glue Table | `hospital_orders` | Generated table name (by crawler) |

## How It Works (Step-by-Step) 🔁

1. 📤 Upload a JSON file to the raw S3 prefix
2. ⚡ S3 event triggers Lambda
3. Lambda performs:
   - 📖 Reads the JSON file
   - 🧩 Flattens nested structures into a DataFrame
   - 🧱 Writes a timestamped Parquet file to curated prefix (e.g., `hospital_output_20250101_10:30:45.parquet`)
4. 🕷️ Lambda starts the Glue crawler
5. 🗂️ Glue crawler updates/creates the table in Glue Data Catalog
6. 🔍 Athena queries the table and QuickSight visualizes it 📊

## Deployment (High Level) 🧰

### Step 1: Create S3 Bucket & Prefixes 🪣

```bash
# Create bucket (if not exists)
aws s3 mb s3://my-hospital-data --region us-east-1

# Create prefixes
aws s3api put-object --bucket my-hospital-data --key hospital_json_input/
aws s3api put-object --bucket my-hospital-data --key hospital_parquet_output/
```

### Step 2: Create Glue Crawler 🕷️

1. Navigate to AWS Glue Console → Crawlers
2. Create a new crawler named `hospital_json_crawler`
3. Set data source to: `s3://my-hospital-data/hospital_parquet_output/`
4. Create or select Glue database: `hospital_analytics`
5. Output table name: `hospital_orders` (auto-configured)
6. Review and create crawler

### Step 3: Deploy Lambda Function ⚡

1. Create a new Lambda function with Python 3.11 runtime
2. Copy the code from `src/lambda_function.py`
3. Add Lambda layer or include these dependencies in deployment package:
   - `pandas`
   - `pyarrow`
4. Set Lambda execution role with permissions:
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": ["s3:GetObject", "s3:PutObject"],
         "Resource": "arn:aws:s3:::my-hospital-data/*"
       },
       {
         "Effect": "Allow",
         "Action": ["glue:StartCrawler"],
         "Resource": "arn:aws:glue:*:*:crawler/hospital_json_crawler"
       }
     ]
   }
   ```

### Step 4: Configure S3 Event Notification 🔔⚡

1. Go to S3 Bucket → Properties → Event Notifications
2. Create event for ObjectCreated → Lambda → Select your Lambda function
3. Set filter prefix to: `hospital_json_input/`
4. Save

### Step 5: Validate in Athena 🔍

```sql
-- Check if table exists
SHOW TABLES IN hospital_analytics;

-- Run sample query
SELECT COUNT(*) as total_medicine_records
FROM hospital_analytics.hospital_orders;

-- Check schema
DESCRIBE hospital_analytics.hospital_orders;
```

### Step 6: Create QuickSight Dataset & Dashboards 📊

1. Open Amazon QuickSight
2. Create new dataset → Select Athena
3. Choose database: `hospital_analytics` and table: `hospital_orders`
4. Proceed to build visuals (charts, KPIs, filters, etc.)
5. Publish dashboard

## Validation Checklist 🧪

- ✅ Parquet files appear in curated prefix after JSON upload
- ✅ Glue crawler run succeeds and table schema is correct
- ✅ Athena returns expected row counts (medicine-line item level)
- ✅ QuickSight dataset refresh works and visuals load correctly
- ✅ Row count validation: Total output rows = sum of medicines across all source records

## Common Pitfalls ⚠️

| Issue | Solution |
|-------|----------|
| 🧨 Mixed formats in one S3 location | Keep raw JSON and curated Parquet in separate prefixes |
| 🧬 Schema drift after JSON structure changes | Monitor crawler logs and manually update schema in Glue if needed |
| 📦 Lambda timeout/memory error with `pyarrow` | Use Lambda layers (~200MB+) or container images for large dependencies |
| 🔐 Permission denied errors | Verify Lambda IAM role has S3 + Glue permissions |
| 🕷️ Crawler fails to infer schema | Check S3 prefix contains valid Parquet files; crawler logs in CloudWatch |

## Future Improvements 🌱

- 📅 **Partitioning**: Partition Parquet by `order_date` for faster Athena queries
- ✅ **Data Quality**: Add validation checks (null counts, duplicates, referential integrity)
- 🧭 **Orchestration**: Use AWS Step Functions for retries, error handling, and monitoring
- ♻️ **Incremental Processing**: Implement delta/incremental load strategy instead of full loads
- 🔄 **Schema Evolution**: Handle schema changes (e.g., new columns in JSON)
- 📈 **Performance**: Optimize Parquet compression (`snappy` vs `gzip`) and file sizes

## Testing Locally 🧪

```python
# Test the flatten function locally
import json
from lambda_function import flatten

with open('sample-data/example.json', 'r') as f:
    data = json.load(f)

df = flatten(data)
print(df.head())
print(f"Total rows: {len(df)}")
print(f"Columns: {df.columns.tolist()}")

# Optionally save to local Parquet for inspection
df.to_parquet('test_output.parquet')
```

## Contributing 🤝

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Commit changes: `git commit -m "Add your message"`
3. Push to branch: `git push origin feature/your-feature`
4. Open a Pull Request

## Troubleshooting 🔧

### Lambda doesn't trigger on S3 upload
- Verify event notification is configured on correct bucket prefix
- Check Lambda execution role has S3 permissions
- Review CloudWatch logs for errors

### Glue crawler fails
- Check S3 path exists and contains valid Parquet files
- Verify crawler IAM role has S3 read permissions
- Review crawler logs in AWS Glue console

### Athena query fails or returns no results
- Ensure Glue table was created/updated by crawler
- Run `SHOW PARTITIONS table_name;` if using partitioning
- Check Athena query results in S3 (Athena writes query results to a results bucket)

### QuickSight can't connect to Athena
- Verify QuickSight has Athena permissions and S3 results bucket access
- Check QuickSight region matches Athena region
- Test Athena query directly before using in QuickSight

## License 📜

This project is licensed under the MIT License - see LICENSE file for details

## Support 💬

For issues, questions, or suggestions:
- Open a GitHub Issue
- Check existing issues for similar problems
- Include error logs and AWS service outputs when reporting bugs

---

**Last Updated:** December 2025  
**Maintained By:** Analytics Team  
**Status:** Active ✅

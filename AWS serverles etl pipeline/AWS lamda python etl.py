import json
import boto3
import os
import pandas as pd 
from io import BytesIO
from datetime import datetime


def flatten(data):

    flattened_rows = []
    
    for record in data:
        order = record.get("order_details", {})
        patient = record.get("patient", {})
        encounter = record.get("encounter", {})
        doctor = record.get("prescribing_doctor", {})
        hospital = record.get("hospital", {})
    
        for med in record.get("medicines", []):
            row = {
                # Order details
                "medicine_order_id": order.get("medicine_order_id"),
                "order_date": order.get("order_date"),
                "order_status": order.get("order_status"),
                "order_type": order.get("order_type"),
                "priority": order.get("priority"),
    
                # Patient details
                "patient_id": patient.get("patient_id"),
                "patient_name": patient.get("name"),
                "gender": patient.get("gender"),
                "date_of_birth": patient.get("date_of_birth"),
    
                # Encounter details
                "encounter_id": encounter.get("encounter_id"),
                "encounter_type": encounter.get("encounter_type"),
                "admission_date": encounter.get("admission_date"),
                "discharge_date": encounter.get("discharge_date"),
    
                # Doctor details
                "doctor_id": doctor.get("doctor_id"),
                "doctor_name": doctor.get("name"),
                "department": doctor.get("department"),
    
                # Medicine details
                "medicine_id": med.get("medicine_id"),
                "medicine_name": med.get("medicine_name"),
                "dosage": med.get("dosage"),
                "frequency": med.get("frequency"),
                "route": med.get("route"),
                "medicine_start_date": med.get("start_date"),
                "medicine_end_date": med.get("end_date"),
    
                # Hospital details
                "hospital_id": hospital.get("hospital_id"),
                "hospital_name": hospital.get("hospital_name"),
                "location": hospital.get("location")
            }
    
            flattened_rows.append(row)
    
    # Convert to DataFrame
    df = pd.DataFrame(flattened_rows)
    return df

def lambda_handler(event, context):
    # TODO implement
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    print(bucket_name)
    file_name = event["Records"][0]["s3"]["object"]["key"]
    print(file_name)

    s3 = boto3.client("s3")
    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    content = response["Body"].read().decode("utf-8")
    print("File successfully read from S3")
    data = json.loads(content)
    flatten(data)
    print("File successfully flattened")
    df = flatten(data)
    
    #BytesIO allows Lambda to write Parquet files entirely in memory, avoiding /tmp, improving performance and simplifying S3 uploads.
    
    parquet_buffer = BytesIO()
    df.to_parquet(parquet_buffer, index=False, engine='pyarrow')
    print("File successfully converted to parquet")
    
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H:%M:%S")

    target_file = f'hospital_parquet_output/hospital_output_{timestamp}.parquet'

    s3.put_object(Bucket=bucket_name, Key=target_file, Body=parquet_buffer.getvalue())
    print("File successfully written to S3")
    
    # run crawler
    glue = boto3.client('glue')
    crawler_name = 'hospital_json_crawler'
    glue.start_crawler(Name=crawler_name)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

# IoT Sensor Data Pipeline on AWS

A serverless IoT data pipeline that simulates an electrical sensor publishing 
temperature and voltage readings to AWS, stores them in a database, 
monitors for anomalies, and displays them on a live dashboard.

## Architecture

Python Sensor Script → AWS IoT Core → AWS Lambda → DynamoDB
                                                  → CloudWatch Alarms → SNS Email Alerts
                                     API Gateway → Lambda → Dashboard on S3

## AWS Services Used

- **AWS IoT Core** - Ingests sensor data securely using MQTT protocol
- **AWS Lambda** - Serverless processing of incoming sensor data
- **Amazon DynamoDB** - NoSQL database storing all sensor readings
- **Amazon API Gateway** - REST API exposing sensor data to the dashboard
- **Amazon S3** - Hosts the static frontend dashboard
- **Amazon CloudWatch** - Monitors Lambda for errors and anomalies
- **Amazon SNS** - Sends email alerts when alarms trigger
- **AWS IAM** - Least privilege security roles for all services

## Project Features

- Real time temperature and voltage simulation
- Secure device authentication using X.509 certificates
- Serverless architecture with zero idle costs
- Live dashboard showing latest 10 sensor readings
- Automated email alerts on Lambda errors
- Full IAM security throughout pipeline

## Cost

Total project cost: $0 (within AWS Free Tier)

| Service | Free Tier Limit | This Project Usage |
|---------|----------------|-------------------|
| IoT Core | 2.25M messages/month | ~500 messages |
| Lambda | 1M requests/month | ~200 requests |
| DynamoDB | 25GB storage | <1MB |
| API Gateway | 1M calls/month | ~50 calls |
| S3 | 5GB storage | <1MB |

## Setup Instructions

### Prerequisites
- AWS Account
- Python 3.13
- AWS CLI configured

### Steps
1. Clone this repository
2. Create IoT Thing and download certificates
3. Install dependencies: `pip install awsiotsdk`
4. Update certificate paths in `sensor.py`
5. Run sensor: `python sensor.py`
6. View dashboard at your S3 website URL

## Background

I built this project to bridge my Electrical Engineering background 
with cloud computing. IoT sensor monitoring is a real world use case 
in industrial automation and smart systems — combining my domain 
knowledge with AWS cloud services.

## Live Dashboard

http://iot-sensor-dashboard-zoha.s3-website-us-east-1.amazonaws.com

## Author

Zoha Mahveen | AWS Certified Solutions Architect Associate

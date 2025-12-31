# Serverless Architecture Assignments

This repository contains the code and step-by-step tasks related to Serverless Architecture using AWS Lambda, Boto3, SNS, etc.

---

## Environment

### Cloud Platform
- **Provider:** AWS

### Operating System
- **EC2 AMI::** Ubuntu 20.04 LTS
- **AWS Lambda Runtime:** Python 3.x (AWS-managed runtime)

### AWS Services Used
- EC2
- Lambda
- S3
- SNS

---

## Assignment-1: Automated Instance Management Using AWS Lambda and Boto3

**Objective:** In this assignment, you will gain hands-on experience with AWS Lambda and Boto3, Amazon's SDK for Python. You will create a Lambda function that will automatically manage EC2 instances based on their tags.

**Task:** You're tasked to automate the stopping and starting of EC2 instances based on tags.

### Step 1: Create EC2 Instances with Tag configurations

1. Login to AWS console, goto EC2 Service
2. Click on Launch Instance

    <img width="1567" height="387" alt="image" src="https://github.com/user-attachments/assets/ec2f03dd-4838-48ba-9424-0e79e02f635d" />

3. Fill in the server name and click on add additional tags and add **Key:** Action and **Value:** Auto-Stop

    <img width="1111" height="895" alt="image" src="https://github.com/user-attachments/assets/488c8416-e3b2-420a-ac9d-fced35d6d58c" />
    <img width="1093" height="445" alt="image" src="https://github.com/user-attachments/assets/7e8425d9-0280-40fb-b85a-883b360dcb1f" />

4. Select all the requirements and click on **Launch instance**
5. Repeat the same steps to Launch another instance with **Key:** Action and **Value:** Auto-Start

    <img width="1404" height="98" alt="image" src="https://github.com/user-attachments/assets/41dd5c29-f41a-499c-ad5d-52017ee30d2c" />

### Step 2: Create IAM Role for AWS Lambda

1. Search and navigate to the **IAM** service in AWS console

    <img width="1043" height="233" alt="image" src="https://github.com/user-attachments/assets/1555b222-2497-436b-9aa3-ad5c5abc3400" />

2. On the left handside, click on **Roles**

    <img width="309" height="549" alt="image" src="https://github.com/user-attachments/assets/a4216c7c-5c37-4d6d-a89d-17528a27c58c" />

3. Click on **Create role**

    <img width="1710" height="418" alt="image" src="https://github.com/user-attachments/assets/77056d94-89f3-4f68-b3a0-d1995e568730" />

4. Select **Trusted entity type** as **AWS service** and **Use case** as **Lambda**

    <img width="1697" height="706" alt="image" src="https://github.com/user-attachments/assets/451c0791-19e7-4325-b314-34dd06f65a5b" />

5. Click on **Next**
6. In the Permissions page, search for **AmazonEC2FullAccess** and **AWSLambdaBasicExecutionRole** policy and select them

    <img width="1697" height="427" alt="image" src="https://github.com/user-attachments/assets/57fe0483-3117-489c-92ca-2f20e9a529bc" />

> Note: AmazonEC2FullAccess is used for learning purposes.  
> In production, least-privilege IAM policies should be applied.

7. Click on **Next**
8. Enter the Role name and click on Create role

    <img width="379" height="151" alt="image" src="https://github.com/user-attachments/assets/57ca167e-3d2c-498c-9b3d-be2d108f2aa3" />

9. Verify if the Role has created

    <img width="1148" height="183" alt="image" src="https://github.com/user-attachments/assets/8568dd0f-cffc-4dee-9ca0-2521f77db060" />

### Step 3: Create AWS Lambda Function

1. Search and navigate to the **AWS Lambda Dashboard**

    <img width="1044" height="224" alt="image" src="https://github.com/user-attachments/assets/ba36e323-d8de-4721-a5a0-70e160fefb08" />

2. Click on **Create a function**

    <img width="449" height="224" alt="image" src="https://github.com/user-attachments/assets/634d2ac6-de08-490f-8037-470675fb05a3" />

3. Choose **Author from scratch**
4. Configure basic settings

  - Function name: `EC2-Auto-Start-Stop`
  - Runtime: `Python 3.X`
  - Architecture: `x86_64`

    <img width="1414" height="753" alt="image" src="https://github.com/user-attachments/assets/1ed46ca5-2825-49ed-976d-06cc4abbec11" />

5. Expand **Change default execution role**, select Use an existing role and select the role created in previous step

    <img width="1407" height="364" alt="image" src="https://github.com/user-attachments/assets/7bff3b9a-9279-430e-a02c-357700116996" />

6. Click on **Create function**, upon succesful creation of the function below page will be loaded.

    <img width="1422" height="937" alt="image" src="https://github.com/user-attachments/assets/e3f3e865-2df3-4e1e-92ef-0d7c7fed3627" />

### Step 4: Add Boto3 Code to Start and Stop EC2 Instances Based on Tags

1. Go to the function created in previous step
2. Click on **Code** section (Refer to the final screenshot in the previous step)
3. Add the code from `EC2-Auto-Start-Stop-lambda-function.py` file in this repository
4. Click **Deploy** to save the function

    <img width="1422" height="659" alt="image" src="https://github.com/user-attachments/assets/4f9bb462-e0dd-419c-9227-6cdee27ee9d1" />
    <img width="1422" height="172" alt="image" src="https://github.com/user-attachments/assets/3499bcf4-9c12-4fca-a3e5-479f9bbb1177" />

### Step 5: Manually invoke the function

1. On your AWS Lambda function page, click on **Test** section
2. Select **Test event action** as **Create new event**, enter **Event name**, **Event JSON** can be left to Default
3. Click on **Test** to invoke the function

    <img width="1422" height="782" alt="image" src="https://github.com/user-attachments/assets/ac785179-2f5f-4e64-b0b3-62febba0220c" />

4. Once manual invokation is done, below status will be observed

    <img width="1401" height="880" alt="image" src="https://github.com/user-attachments/assets/f2342af2-e38c-4009-bb84-b3c6b070fdb3" />

5. Click on Monitor section, then click on **View CloudWatch logs**

    <img width="1401" height="344" alt="image" src="https://github.com/user-attachments/assets/6a98d7a9-3b22-4e86-ad45-94d641b01f83" />

6. Select the latest **log stream**

    <img width="1665" height="765" alt="image" src="https://github.com/user-attachments/assets/d883708b-8818-4790-9485-8e618213b4f7" />
    <img width="1710" height="493" alt="image" src="https://github.com/user-attachments/assets/8969429e-b9b6-4024-82e6-db1bfda5f229" />

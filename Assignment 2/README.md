# Assignment-2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3

## Objective

To gain experience with AWS Lambda and Boto3 by creating a Lambda function that will automatically clean up old files in an S3 bucket.

## Task

Automate the deletion of files older than 30 days in a specific S3 bucket.

---

## Environment

### Cloud Platform
- **Provider:** AWS

### Operating System
- **AWS Lambda Runtime:** Python 3.x (AWS-managed runtime)

### AWS Services Used
- S3
- Lambda

---

## Procedure

### Step 1: Create S3 Bucket

1. Login to AWS console, goto S3 Service
2. Click on **Create bucket**

    <img width="1568" height="370" alt="image" src="https://github.com/user-attachments/assets/e9b28134-a243-4e99-85e7-484f1d98bb55" />

3. Select **Bucket type** as **General purpose**
4. Enter a unique **Bucket name**

    <img width="1704" height="774" alt="image" src="https://github.com/user-attachments/assets/b3c9a9d3-99bd-47d4-84da-a49bf2a1553e" />

5.  Uncheck Block all public access option and acknowledge the prompt below

    <img width="1632" height="497" alt="image" src="https://github.com/user-attachments/assets/8905b45d-1374-40d2-b6f9-4d0333e79811" />

6.  Leave all the other settings to Default and click on **Create bucket**

### Step 2: Upload files to S3 Bucket

1. Click on the S3 bucket created in previous step
2. Click on **Upload**

    <img width="1710" height="259" alt="image" src="https://github.com/user-attachments/assets/7d1ad270-3dbc-424f-98b0-007208a05c61" />

3. Upload files by drag and drop, and click on **Upload**

    <img width="1710" height="721" alt="image" src="https://github.com/user-attachments/assets/7139f1fa-c141-48d2-8b2d-3ca659cec5df" />

### Step 3: Create IAM Role

1. Search and navigate to the **IAM** service in AWS console

    <img width="1043" height="233" alt="image" src="https://github.com/user-attachments/assets/1555b222-2497-436b-9aa3-ad5c5abc3400" />

2. On the left handside, click on **Roles**

    <img width="309" height="549" alt="image" src="https://github.com/user-attachments/assets/a4216c7c-5c37-4d6d-a89d-17528a27c58c" />

3. Click on **Create role**

    <img width="1710" height="418" alt="image" src="https://github.com/user-attachments/assets/77056d94-89f3-4f68-b3a0-d1995e568730" />

4. Select **Trusted entity type** as **AWS service** and **Use case** as **Lambda**

    <img width="1697" height="706" alt="image" src="https://github.com/user-attachments/assets/451c0791-19e7-4325-b314-34dd06f65a5b" />

5. Click on **Next**
6. In the Permissions page, search for **AmazonS3FullAccess** and **AWSLambdaBasicExecutionRole** policy and select them

    <img width="1710" height="374" alt="image" src="https://github.com/user-attachments/assets/3d02380f-cd93-4411-b45c-5d89a6dc8430" />

> **Note: AmazonS3FullAccess is used for learning purposes.**  
> **In production, least-privilege IAM policies should be applied.**

7. Enter the Role name and click on Create role

    <img width="379" height="151" alt="image" src="https://github.com/user-attachments/assets/57ca167e-3d2c-498c-9b3d-be2d108f2aa3" />

8. Verify if the Role has created

    <img width="1710" height="374" alt="image" src="https://github.com/user-attachments/assets/e04c9c4d-48f9-4093-87bc-d15dbcfd6b82" />

### Step 4: Create Lambda Function

1. Search and navigate to the **AWS Lambda Dashboard**

    <img width="1044" height="224" alt="image" src="https://github.com/user-attachments/assets/ba36e323-d8de-4721-a5a0-70e160fefb08" />

2. Click on **Create a function**

    <img width="449" height="224" alt="image" src="https://github.com/user-attachments/assets/634d2ac6-de08-490f-8037-470675fb05a3" />

3. Choose **Author from scratch**
4. Configure basic settings

  - Function name: `s3-auto-cleanup`
  - Runtime: `Python 3.X`
  - Architecture: `x86_64`

    <img width="1394" height="743" alt="image" src="https://github.com/user-attachments/assets/ef85a832-bc6d-4706-9733-ccc107151773" />

5. Expand **Change default execution role**, select Use an existing role and select the role created in previous step

    <img width="1394" height="296" alt="image" src="https://github.com/user-attachments/assets/d8cbf713-f443-4b03-bca4-9de1d4d9c08b" />

6. Click on **Create function**, upon succesful creation of the function below page will be loaded.

    <img width="1394" height="901" alt="image" src="https://github.com/user-attachments/assets/b7c97a12-9d7a-4e0e-a2c5-29296154ae24" />

### Step 5: Add Boto3 Code to the Lambda Function

1. Go to the function created in previous step
2. Click on **Code** section (Refer to the final screenshot in the previous step)
3. Add the code from `S3-cleanup-lambda-function.py` file in this repository
4. Click **Deploy** to save the function

    <img width="1411" height="829" alt="image" src="https://github.com/user-attachments/assets/cc6a34bd-c477-4b7b-8c92-1913d873d160" />

    <img width="1411" height="153" alt="image" src="https://github.com/user-attachments/assets/878dbbb4-816c-454b-b636-2509d735ac99" />

### Step 6: Manually invoke the function

1. On your AWS Lambda function page, click on **Test** section
2. Select **Test event action** as **Create new event**, enter **Event name**, **Event JSON** can be left to Default
3. Click on **Test** to invoke the function

    <img width="1422" height="782" alt="image" src="https://github.com/user-attachments/assets/ac785179-2f5f-4e64-b0b3-62febba0220c" />

> For testing purpose, `cleanup_date` has been set to `1 Minute`

4. Once manual invokation is done, below status will be observed

    <img width="1383" height="793" alt="image" src="https://github.com/user-attachments/assets/ea8b8748-0594-4b12-88c2-c25dfc531533" />

5. Click on Monitor section, then click on **View CloudWatch logs**

    <img width="1401" height="344" alt="image" src="https://github.com/user-attachments/assets/6a98d7a9-3b22-4e86-ad45-94d641b01f83" />

6. Select the latest **log stream**

    <img width="1654" height="767" alt="image" src="https://github.com/user-attachments/assets/9a9053a1-b464-4e0c-b147-863431e350fb" />

    <img width="1676" height="531" alt="image" src="https://github.com/user-attachments/assets/f9543497-3d3c-495a-b7aa-c1b72140dd4d" />

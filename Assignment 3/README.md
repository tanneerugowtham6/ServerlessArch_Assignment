# Assignment-3: Automatic EBS Snapshot and Cleanup Using AWS Lambda and Boto3

## Objective

To automate the backup process for your EBS volumes and ensure that backups older than a specified retention period are cleaned up to save costs.

## Task

Automate the creation of snapshots for specified EBS volumes and clean up snapshots older than 30 days.

---

## Environment

### Cloud Platform
- **Provider:** AWS

### Operating System
- **AWS Lambda Runtime:** Python 3.x (AWS-managed runtime)

### AWS Services Used
- EBS
- Lambda

---

## Procedure

### Step 1: EBS Setup – Identify or Create the Volume

1. Login to AWS console, goto EC2 Service
2. In the leftside menu, under **Elastic Block Store** click on **Volumes**

    <img width="266" height="760" alt="image" src="https://github.com/user-attachments/assets/d0df60c7-ed78-4e7c-99d0-534322312fec" />

3. Click on **Create volume**

    <img width="1710" height="200" alt="image" src="https://github.com/user-attachments/assets/65e4972d-9399-4984-8dd0-c210d7bc8315" />

4. Enter **Volume Type** as **gp3**, **Size** as **10GB**
5. Select **Availability zone** same as EC2 instance

    <img width="1177" height="880" alt="image" src="https://github.com/user-attachments/assets/ac6221cb-a40a-4582-9594-b8d927d4f5dd" />

6.  Click on **Create volume**, once created nate down the **volume id**

    <img width="1632" height="497" alt="image" src="https://github.com/user-attachments/assets/8905b45d-1374-40d2-b6f9-4d0333e79811" />

7.  Leave all the other settings to Default and click on **Create bucket**

### Step 2: Create IAM Role

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

    <img width="1710" height="374" alt="image" src="https://github.com/user-attachments/assets/3d02380f-cd93-4411-b45c-5d89a6dc8430" />

> **Note: AmazonEC2FullAccess is used for learning purposes.**  
> **In production, least-privilege IAM policies should be applied.**

7. Enter the Role name and click on Create role

    <img width="379" height="151" alt="image" src="https://github.com/user-attachments/assets/57ca167e-3d2c-498c-9b3d-be2d108f2aa3" />

8. Verify if the Role has created

    <img width="1710" height="374" alt="image" src="https://github.com/user-attachments/assets/e04c9c4d-48f9-4093-87bc-d15dbcfd6b82" />

### Step 3: Create Lambda Function

1. Search and navigate to the **AWS Lambda Dashboard**

    <img width="1044" height="224" alt="image" src="https://github.com/user-attachments/assets/ba36e323-d8de-4721-a5a0-70e160fefb08" />

2. Click on **Create a function**

    <img width="449" height="224" alt="image" src="https://github.com/user-attachments/assets/634d2ac6-de08-490f-8037-470675fb05a3" />

3. Choose **Author from scratch**
4. Configure basic settings

  - Function name: `ebs-snapshot-backup`
  - Runtime: `Python 3.X`
  - Architecture: `x86_64`

    <img width="1397" height="792" alt="image" src="https://github.com/user-attachments/assets/49466b33-a2cd-41eb-a35d-b6c477ed61d3" />

5. Expand **Change default execution role**, select **Use an existing role** and select the role created in previous step

    <img width="1397" height="297" alt="image" src="https://github.com/user-attachments/assets/7eb92123-e838-49ae-9c05-79aa591f12e5" />

6. Click on **Create function**, upon succesful creation of the function below page will be loaded.

    <img width="1397" height="907" alt="image" src="https://github.com/user-attachments/assets/018171fd-3351-4d2b-82dd-9378ac2840e2" />

7. Click on **Configuration**, under **General configuration** click on **Edit**
8. Change the timeout duration to **1 minute**

    <img width="1432" height="827" alt="image" src="https://github.com/user-attachments/assets/ce48a6af-abca-4571-84eb-412a159e587b" />

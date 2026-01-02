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

    <img width="1697" height="427" alt="image" src="https://github.com/user-attachments/assets/57fe0483-3117-489c-92ca-2f20e9a529bc" />

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

### Step 4: Add Boto3 Code to the Lambda Function

1. Go to the function created in previous step
2. Click on **Code** section (Refer to the final screenshot in the previous step)
3. Add the code from `EBS-Snapshot-lambda-function.py` file in this repository
4. Click **Deploy** to save the function

    <img width="1432" height="773" alt="image" src="https://github.com/user-attachments/assets/e08b1354-038b-41a9-8e4a-2fefc4d5dbc1" />

    <img width="1432" height="101" alt="image" src="https://github.com/user-attachments/assets/d5f956a7-04bd-4ce0-b361-dd96b5a7b276" />

### Step 5: Manually invoke the function

1. On your AWS Lambda function page, click on **Test** section
2. Select **Test event action** as **Create new event**, enter **Event name**, **Event JSON** can be left to Default
3. Click on **Test** to invoke the function

    <img width="1432" height="773" alt="image" src="https://github.com/user-attachments/assets/ed2276a0-b628-4a59-b0fe-17b77b52be32" />

> For testing purpose, `cleanup_time` has been uncommented and time has been set to `1 Minute`

4. Once manual invokation is done, below status will be observed

    <img width="1432" height="773" alt="image" src="https://github.com/user-attachments/assets/9fe2f716-efa3-486b-99ab-a5efb6dd53a7" />

5. Click on Monitor section, then click on **View CloudWatch logs**

    <img width="1401" height="344" alt="image" src="https://github.com/user-attachments/assets/6a98d7a9-3b22-4e86-ad45-94d641b01f83" />

6. Select the latest **log stream**

    <img width="1698" height="760" alt="image" src="https://github.com/user-attachments/assets/9e2530c4-30ec-47d7-81a0-69f7835420c8" />

    <img width="1667" height="505" alt="image" src="https://github.com/user-attachments/assets/fde74bb2-541b-429d-a31e-3ca9458f1443" />

7. Navigate to the EC2 service from AWS Console and click on Snapshots on the left sidebar

    Before retention changed to 1 minute
    <img width="1698" height="258" alt="image" src="https://github.com/user-attachments/assets/db283a4a-472b-4a8d-83d8-de1bbbaed43a" /> 

    After retention test changed to 1 minute
    <img width="1493" height="129" alt="image" src="https://github.com/user-attachments/assets/0b3cff35-e6d4-42d6-b83e-83e0f7d6e542" />


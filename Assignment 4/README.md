# Assignment-4: Auto-Tagging EC2 Instances on Launch Using AWS Lambda and Boto3

## Objective

Learn to automate the tagging of EC2 instances as soon as they are launched, ensuring better resource tracking and management.

## Task

Automatically tag any newly launched EC2 instance with the current date and a custom tag.

---

## Environment

### Cloud Platform
- **Provider:** AWS

### Operating System
- **AWS Lambda Runtime:** Python 3.x (AWS-managed runtime)

### AWS Services Used
- EC2
- Lambda

---

## Procedure

### Step 1: EC2 Setup – Confirm You Can Launch Instances

1. Login to AWS console, goto EC2 Service
2. Verify if the **Launch Instance** button is not grayed out

    <img width="1710" height="199" alt="image" src="https://github.com/user-attachments/assets/0756c69f-de63-4c97-aea4-7df25fcff25f" />

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

  - Function name: `ec2-auto-tag-on-launch`
  - Runtime: `Python 3.X`
  - Architecture: `x86_64`

    <img width="1437" height="657" alt="image" src="https://github.com/user-attachments/assets/cf24f118-53f3-4f4c-bbdc-1ffdd3f465ed" />

5. Expand **Change default execution role**, select **Use an existing role** and select the role created in previous step

    <img width="1427" height="268" alt="image" src="https://github.com/user-attachments/assets/8182ea94-892b-4976-90f0-49464728e252" />

6. Click on **Create function**, upon succesful creation of the function below page will be loaded.

    <img width="1437" height="741" alt="image" src="https://github.com/user-attachments/assets/70dab938-85b6-40b9-b28d-c41ed6d9f096" />

7. Click on **Configuration**, under **General configuration** click on **Edit**
8. Change the timeout duration to **1 minute**

    <img width="1437" height="820" alt="image" src="https://github.com/user-attachments/assets/a0ca65ec-a8a7-4a6a-a2a4-4ef5a900fa6c" />

### Step 4: Add Boto3 Code to the Lambda Function

1. Go to the function created in previous step
2. Click on **Code** section (Refer to the final screenshot in the previous step)
3. Add the code from `EC2-auto-tagging-lambda-function.py` file in this repository
4. Click **Deploy** to save the function

    <img width="1437" height="710" alt="image" src="https://github.com/user-attachments/assets/f11d4bd6-8041-4356-984a-1e84734366fd" />

    <img width="1437" height="95" alt="image" src="https://github.com/user-attachments/assets/2dc6960b-1c79-4c0d-8d4d-5252100a9f6c" />
### Step 5: Create EventBridge Rule (Trigger Lambda on EC2 Launch)

1. In AWS Console search and navigate to **Amazon EventBridge** service

    <img width="973" height="209" alt="image" src="https://github.com/user-attachments/assets/d8b40d0a-adb6-4df0-8863-3d7dc7e1940e" />

2. In the left sidebar, click on **Rules**

    <img width="260" height="554" alt="image" src="https://github.com/user-attachments/assets/29b3f5cf-1522-45c7-9a3d-16b58e243219" />

3. Click on **Create rule**

    <img width="1701" height="512" alt="image" src="https://github.com/user-attachments/assets/8c4000da-8ede-4c8d-a595-e475c2ae9ccc" />

4. Enter the details and click on **Next**

    - **Rule-name:** 'ec2-launch-auto-tag'
    - **Description:** Auto Tagging on EC2 instance launch

    <img width="1701" height="563" alt="image" src="https://github.com/user-attachments/assets/f246a72e-0214-4544-b0f1-0f07f2fa248a" />

5. Under the **Events** section, **Event source** as **AWS events or EventBridge partner events**

    <img width="1701" height="512" alt="image" src="https://github.com/user-attachments/assets/a8e70d8e-9a89-489f-817f-f288f173c356" />

6. Under the Event Pattern section, set the configurations as below

    - **Creation method:** Use pattern form
    - **Event source:** AWS services
    - **AWS service:** EC2
    - **Event type:** EC2 Instance State-change Notification
    - **Event Type Specification 1:** Specific state(s)
      - Select **Specific state(s)** as **running**

    <img width="1186" height="688" alt="image" src="https://github.com/user-attachments/assets/8d6ef9da-404d-48e9-bc50-0c25d23b33b0" />

7. Click on **Next**
8. Under the **Target 1** section

    - **Target types:** AWS service
    - **Select a target:** Lambda function
    - **Target location:** Target in this account
    - **Function:** Select the function created in previous step (ec2-auto-tag-on-launch)
    
    Leave the remaining settings to Default

    <img width="1186" height="832" alt="image" src="https://github.com/user-attachments/assets/c911dbf0-904f-46ee-ba3b-83fa1d7c4119" />

10. Click on **Create rule**

    <img width="320" height="165" alt="image" src="https://github.com/user-attachments/assets/533894f9-34fc-4368-af76-32d7643c17c9" />

    <img width="1704" height="529" alt="image" src="https://github.com/user-attachments/assets/87a6ae2c-9908-45d9-8fb1-df39481a4814" />

### Step 6: Testing

1. Goto EC2 Service and Launch an EC2 Instance

    <img width="1704" height="133" alt="image" src="https://github.com/user-attachments/assets/c0b2cfad-bc04-4d68-85c0-98a2067bf2b9" />

2. Click on Monitor section, then click on **View CloudWatch logs**

    <img width="1401" height="344" alt="image" src="https://github.com/user-attachments/assets/6a98d7a9-3b22-4e86-ad45-94d641b01f83" />

3. Select the latest **log stream**

    <img width="1704" height="667" alt="image" src="https://github.com/user-attachments/assets/765388ab-5ac2-4db9-96bc-dc482921ca69" />

    <img width="1704" height="388" alt="image" src="https://github.com/user-attachments/assets/28a92061-cbce-4267-a52d-a4fc5ca05d0d" />

4. Click on the newly created instance, goto **Tags** section, verify if the tags applied

    <img width="756" height="268" alt="image" src="https://github.com/user-attachments/assets/3e03f634-fcb9-45e2-9647-10676b6732b5" />

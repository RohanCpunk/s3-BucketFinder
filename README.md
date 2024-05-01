# Introduction 
Myself RohanCpunk
By day, I'm a cybersec evangelist, advocating for digital safety and resilience. But when night falls, I transform into a vigilante hacker, prowling the shadows to combat cyber threats. Balancing these dual roles, I'm committed to defending the digital realm and ensuring its security, day and night. 

# s3-BucketFinder
Written this script to ease out my work but thaught it would be grate if i can help others in that too this s3BucketFinder is Python Script for Identifying World-Editable s3 Buckets

# Risk 
Publicly available editable S3 buckets pose significant risks to data security and privacy. Unintentional exposure can lead to unauthorized access, data leaks, and potential exploitation by malicious actors. Such misconfigurations may result in sensitive information being compromised, reputational damage, and regulatory non-compliance, making robust access controls imperative for safeguarding data integrity.

# Description:

S3BucketFinder is a powerful Python script designed to uncover potentially sensitive misconfigurations in AWS S3 buckets. With the increasing adoption of cloud services, securing data stored in the cloud is paramount. However, misconfigured S3 buckets can inadvertently expose sensitive information to the public, leading to data breaches and security vulnerabilities.

This script utilizes the Boto3 library, the official AWS SDK for Python, to interact with the AWS S3 API. It intelligently scans through a specified range of AWS regions, examining each S3 bucket's access control settings. Specifically, it identifies buckets that have been configured with overly permissive access control policies, allowing public write access.


# Key Features:

1. Efficient Scanning: The script efficiently traverses through specified AWS regions, minimizing resource consumption while maximizing coverage.
2. Customizable Options: Users can tailor the script by specifying AWS access credentials, target regions, and other parameters to suit their specific needs.
3. Detailed Reporting: S3BucketFinder generates detailed reports listing discovered world-editable S3 buckets, along with their respective AWS regions and access control settings.


# Potential Use Cases: 
This tool can be invaluable for security professionals, AWS administrators, and penetration testers to identify and remediate potential security risks associated with misconfigured S3 buckets.

Note : Make sure you have configured your AWS credential using "aws configure" or by setting environment varibales. This script will iterate thruogh all buckets and check all their ACLs to identify those accesicble by everyone. Rememeber to handle any exceptions that may occur during the process 

Please replace 'http://acs.amazonaws.com/groups/global/AllUsers' with 'http://acs.amazonaws.com/groups/global/AuthenticatedUsers' if you want to find buckets accecible by authenticated users only !!! Happy bucket hunting !!!

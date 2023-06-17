# Encrypt data using AWS KMS
aWS: Amazon Web Services
KMS: Key Management Service

[source](https://www.coursera.org/learn/data-encryption-using-aws-kms-ust/ungradedLti/BDxG6/data-encryption-using-aws-kms-from-ust)


# Process
- Goto account dropdown
- My Security Credentials
- create access key (downlod or save the key)
- configurer aws cli (confirm by `aws --version`)
* Programatically login to aws console
    - `aws configure --profile iamadmin-general`
    - Enter the access key and secret access key

* Customer Managed keys (CMK)
    - logical representation of a master key
    - can be used to encrypt and decrypt data
        - search: kms
        - create key -> symmetric key -> alias: mykey -> iamadmin (can manage) -> iamadmin (can use) -> finish
        - click on key generated -> key rotation -> automatically rotate every year -> save changes

* encrypt data using symmetric CMK
    - (login)
    - echo "lets start the battle. get ready with the guns" > test_msg.txt
    - aws kms encrypt --key-id alias/mykey --plaintext fileb://test_msg.txt --output text --query CiphertextBlob --profile iamadmin-general > test_msg_encrypted.txt
    - certutil -decode test_msg_encrypted.txt test_msg_encrypted_decoded.txt    # to decode the encrypted file from base64 to text
    - type test_msg_encrypted_decoded.txt   # cypher text

* Decrypt data using symmetric  CMK
    - aws kms decrypt --ciphertext-blob fileb://test_msg_encrypted.txt --output text --query Plaintext --profile iamadmin-general | base64 --decode > test_msg_decrypted.txt
    - certutil -decode test_msg_decrypted.txt test_msg_decrypted_decoded.txt    # to decode the encrypted file from base64 to text
    - type test_msg_decrypted_decoded.txt   # plain text

* Create Assymmetric CMK
    **public key for encryption and private key for decryption**
    - (login)
    - create key -> asymmetric key -> usage: Encrypt/Decrypt -> key-specs: RSA_2048 -> alias: myasymkey -> iamadmin (can manage) -> iamadmin (can use) -> finish
    - click on key generated -> key rotation -> automatically rotate every year -> save changes # to rotate the key every year
    - click on key generated -> public key -> copy the key and save it in a file named public_key.pem

* Delete 'Customer Managed Keys':
    - check the key -> key actions -> schedule key deletion -> 7 days -> confirm check-box -> schedule deletion

# Learning Objectives


# Course Objectives
In this course, we are going to focus on three learning objectives:

Learn to create, train and evaluate neural network models with TensorFlow and Keras.

Understand the basics of neural networks.

Learn to solve classification problems with the help of neural networks.

further courses:
https://www.coursera.org/professional-certificates/tensorflow-in-practice?trk_location=reading_gp&trk_slug=tensorflow-beginner-basic-image-classification

https://www.coursera.org/specializations/machine-learning-tensorflow-gcp?trk_location=reading_gp&trk_slug=tensorflow-beginner-basic-image-classification

https://www.coursera.org/specializations/advanced-machine-learning-tensorflow-gcp?trk_location=reading_gp&trk_slug=tensorflow-beginner-basic-image-classification

https://www.coursera.org/specializations/tensorflow-data-and-deployment?trk_location=reading_gp&trk_slug=tensorflow-beginner-basic-image-classification

https://www.coursera.org/specializations/tensorflow2-deeplearning?trk_location=reading_gp&trk_slug=tensorflow-beginner-basic-image-classification
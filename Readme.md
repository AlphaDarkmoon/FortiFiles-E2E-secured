# Docs Manager
------------

A Django-based project that enables users to upload and download files with end-to-end encryption, providing a simple yet effective interface for managing files and documents.

![Upload Page](https://i.ibb.co/HhSjq36/upload-file.png)
------
![File List](https://i.ibb.co/tLThqSR/file-list-0.png)

## Description
-----------

Docs Manager allows users to register, log in, upload files, and download files securely and encrypted, utilizing the `django-encrypted-files` package along with an AES key.

Key Features:
-   Only the user who uploaded a file can download it, ensuring privacy and security.

## Getting Started


### Dependencies


#### To run Docs Manager, ensure you have the following dependencies installed:

-   Python 3
-   Poetry
-   Django
-   Django-encrypted-files
-   Python-Decouple

### Installation Steps
------------------

1.  Install Poetry: Follow the official documentation for installation.
2.  Add Dependencies: Use Poetry to add the required dependencies.
3.  Create Environment File: Generate a `.env` file using `.env.example` as a reference.

Executing the Program
---------------------

1.  Start Poetry Shell:


    `poetry shell `

2.  Make Migrations and Migrate:


    `python manage.py makemigrations file_manager python manage.py migrate `

3.  Start Django Server:


    `python manage.py runserver `

4.  User Registration and File Management:

    -   Register a new user, log in, and upload files, which will be securely stored in the `/upload` folder.

### Authors


Contributors to this project include:

-   [AlphaDarkmoon](https://github.com/AlphaDarkmoon)

### Version History


-   0.2 (Upcoming)

    -   Complete UI enhancements
    -   File statistics feature
    -   Protection against XSS and other cyber threats

-   0.1 (Initial Release)

    -   Basic registration/login functionality
    -   File upload and download capabilities
    -   Secure access limited to authenticated users

### License

This project is free to use for educational purposes.
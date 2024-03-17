# AutoGenAutomotive

AutoGenAutomotive is an AI-driven automated customer support system designed to assist users in diagnosing car damage and providing repair solutions. The system leverages cutting-edge technologies, including OpenAI's API for image analysis and Flask for web development, to offer an intuitive and efficient user experience.

## Features

- **Image Analysis**: Users can upload images of car damage, and the system uses OpenAI's API to analyze the images and determine the type and extent of damage.

- **Database Integration**: AutoGenAutomotive integrates with a MySQL database to check the availability of spare parts required for repair.

- **Email Notification**: Once the analysis is complete, the system sends an email to the user's provided email address, detailing the damage assessment, spare part availability, and estimated repair costs.

## Technologies Used

- **OpenAI API**: Used for image analysis to identify car damage.

- **Flask**: Employed for web development, providing a user-friendly interface for uploading images and entering email addresses.

- **MySQL**: Integrated with the system to store and retrieve spare part availability information.

- **smtplib**: Utilized for sending email notifications to users with repair details.

## How it Works

1. **Image Upload**: Users upload images of car damage along with their email addresses and a brief description of the problem through the web interface.

2. **Image Analysis**: OpenAI's API analyzes the uploaded images to identify the type and severity of the damage.

3. **Database Query**: The system queries the MySQL database to check the availability of spare parts required for repair.

4. **Email Notification**: Once the analysis and database query are complete, the system sends an email to the user's provided email address, containing detailed information about the damage assessment, spare part availability, and estimated repair costs.


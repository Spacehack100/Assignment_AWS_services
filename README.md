# AWS services assignment   -   By Jens Kersemans

This pythonscript requires boto3. Install this with the following commands:
pip install boto3

It also requires that the AWS cli is set up with a user with the following permissions:
    - ComprehendFullAccess
    - AmazonPollyFullAccess

The script uses 2 services:
    - Number 1 and 2 return the dominant language (and certainty) of the provided text.
      Option 1 takes the text from a commandline input, while option 2 in the text.txt file looks.
    - The second service, going for option 3, asks for a text input and then translates this into speech (only english).
      The resulting audiofile is dropped in the same map as the script file.

Option 4 exits the program.

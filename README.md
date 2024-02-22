# WhatsApp ChatGPT Assistant
ChatGPT-powered personal assistant that you could message on WhatsApp :)

Note, as of July/August 2023, [A2P 10DLC registration](https://console.twilio.com/us1/develop/sms/regulatory-compliance/a2p-10dlc-overview) is required for US messaging. Thie means you'd need to register your Twilio virtual number before being able to text anyone (including yourself).

This tutorial focuses on the WhatsApp usecase since it requires no registration. 

This project is inspired by the following two tutorials:
1. [Text Chatbot with chatGPT](https://www.twilio.com/en-us/blog/building-chatbot-chatgpt-api-twilio-programmable-sms-python)
2. [WhatsApp Chatbot with chatGPT](https://deysusovan93.medium.com/creating-a-whatsapp-chatbot-with-chatgpt-simplify-customer-interaction-and-boost-engagement-4603c9920876)



## Development Pre-requisite
In order to develop locally, you would need the following:
- Python 
- OpenAI account (Sign up and get $5 free API credits)
- Twilio account (Sign up and get $15 with trial account)

## Getting started
1. Follow STEP 1 and 2 of [this openAI API tutorial](https://platform.openai.com/docs/quickstart?context=python).

2. Clone this repo. `Cd` to this directory.

3. Create a virtual environment
```
python3 -m venv venv
```

4. Activate the environment

MacOS 
```
source venv/bin/activate
```
Windows
```
venv\Scripts\activate
```
5. Install dependencies
```
pip install -r requirements.txt
```

## Start the ChatBot
1. Start the Flask application. Note as off Feb 21, there's only one endpoint with URL `/bot`.
```
flask run
```
2. Leave the Flask app running. Open a new terminal and provision a  temporary public URL that we can give to Twilio:
```
ngrok http 5000
```

3. Add the Forwarding address to Twilio... TODO: finish this readme lol

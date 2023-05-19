# [Avocaptcha](https://avocaptcha.com)

## Overview
ChatGPT and DALL-E based captcha solution. The captcha implementation demo is based on Django, Python3, SQLite, Ajax, OpenAI REST API. A valid API key is required for testing on your host. 

## Impact
* Most of the captcha tools are either boring, confusing or frustrating. An average human captcha solving is above 20 seconds, while every day we spend 500 years of captcha solving - the same captcha can be resolved by paid online resolvers in less than 5 seconds.  It is a crucial part of our data protection mechanisms, why can't we make it more safe while make it easier?

## Differences
* More intuitive than usual reCaptcha solutions - simply recognise objects. 
* Gamification - AI generated images are exciting to look at, see how weird and yet simple the outputs are.

## Data flow
1. The implementation of the captcha is quite simple. With a predefined ChatGPT prompt we make a request: 
```
Request: "Give me a list of 5 random objects"
```  
```
Response:"1. Lamp, 2. Bicycle, 3. Pen, 4. Phone, 5. Chair"
```  
2. The prompt result then will be given to the DALL-E API endpoint, requesting an image with predefined resolution. The prompt can be (and should be) extended with additional parameters for higher difficulty.  
```
Request: "Lamp, Bicycle, Pen, Phone, Chair blend"
```
3. The image is displayed to the user along with an input field. User must describe the content of the image.
4. The user input is sanitized, then given to the ChatGPT API to compare the initial keyword string and the user input string. ChatGPT is requested to return the comparison result with a distinctive number in JSON format.  
```
Request: "Please tell me the difference between these two strings, please consider synonims and spelling errors. Please return the similarity in a 0-100% value in JSON format. Please return only this similarity value, and no other.
"bicycle avocado carrot"
"ketchup bicycle""
```  
```
Response: "{"similarity": 33.33}"
``` 

## Features
* Highly customizable prompts, where you can
	* Define object numbers
	* Object obfuscation prompts
* Custom image resolution

## Plans
* Easily applicable JS module
* API backend with custom tensor model
* Prompt engineering - better GPT prompts

## Install
1. Install the required modules defined in ```requirements.txt```
2. Run the django host either from manage.py, or host with uwsgi

## Team
* Martin Polyak - API, Backend, Frontend ([polyakmartin@draken.hu](mailto:polyakmartin@draken.hu))
* Krisztian Gava - API, Backend, Servers ([gavakrisztian@draken.hu](mailto:gavakrisztian@draken.hu))
* Szabolcs Viktor Ladik - UI, UX, PM ([ladikszabolcs@draken.hu](mailto:ladikszabolcs@draken.hu))  

## License
The MIT License (MIT)

Copyright (c) 2023 Draken OÜ <info@draken.ee>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Draken OÜ](https://draken.ee)
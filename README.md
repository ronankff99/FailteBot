# FailteBot
FáilteBot - A multilingual chatbot for refugees in Ireland

## Explainer
This is a Final Year Project for the Software Development Lvl 8 program at Munster Technological University. It is a modification to a Rasa 1 chatbot that allows for easy implementation of multilingualism. Content for the conversations has been taken from 'The Guide to Living Independently', available at www.gov.ie. If you would like a copy of the thesis I can be reached at my username + @gmail.com.

### Steps for running:
0. Install Python 3.7.x and add the 'python' command to your PATH
1. Establish a Python virtual environment with the command 
> python -m venv env
2. Activate the virtual environment. Use the command 
> .\env\Scripts\activate"
3. Update your version of pip with
> python -m pip install --upgrade pip
4. Install Rasa 1.x with 
> pip install rasa
5. Navigate to main directory and run 
> rasa run actions
6. Navigate to same directory in another console window and run
> rasa run -m models --enable-api --cors "*"
7. Open index.html
8. Start chatting!
9. If you would prefer to just chat via cmdline and go as far as step 5 and then run
> rasa shell
in a separate console window
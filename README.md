
# Harini - Fast and Intelligent Scheduling Assistant 


Harini is an intelligent, conversational appointment booking assistant designed to seamlessly handle the end-to-end scheduling process for individuals and professionals. Built with cutting-edge AI, Harini understands user intent through natural conversations and takes care of booking, confirming, and managing appointments in real time.

With deep integration into Google Calendar, Harini checks your availability, avoids conflicts, and intelligently finds open time slots based on both user preferences and calendar constraints. Once a suitable slot is identified, Harini not only creates the calendar event but also automatically sends personalized email confirmations to all participants.

What sets Harini apart is her proactive communication — after scheduling, she can also initiate a phone call to confirm the appointment, providing a human-like follow-up experience that boosts reliability and trust.

✨ Key Features:
🗓️ Smart Calendar Integration – Syncs with Google Calendar to find and manage time slots.

🧠 Conversational AI – Book appointments via natural language conversations.

📧 Automated Email Notifications – Sends detailed confirmations and reminders to participants.

📞 Call-based Confirmation – Initiates a confirmation call post-booking for added assurance.

🔄 Real-Time Conflict Resolution – Suggests alternate slots if scheduling conflicts are detected.

🔒 Privacy-Focused – Operates securely using only necessary permissions.

👩‍💼 Use Cases:
Professionals managing client meetings

Healthcare practitioners scheduling appointments

Consultants, coaches, and freelancers organizing sessions







## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## Deployment and local running 

To deploy this project run clone the repo and goto the directory

### Conda environment setup

$ conda create -n <environment name> python -y 

$ conda activate <environment name>

$ pip install uv 

$ uv pip install -r requirements.txt 


### Setup Docker and run the following commands 

$ sudo systemctl start Docker

$ langgraph up 






# ⚙️ Technology and Frameworks
Harini is built using a modern stack of AI-first tools and frameworks to deliver seamless agentic behavior and multi-modal interaction:

#🧠 LangGraph:
 Serves as the backbone for orchestrating complex agentic workflows, enabling Harini to reason, decide, and act across multiple steps with memory and context.

# ✉️ Composio:
 Handles integrations with productivity tools like Google Calendar and Gmail, allowing Harini to schedule appointments, send confirmation emails, and manage event details with ease.

# 📞 Bland AI: 
Powers the voice-calling capability, enabling Harini to initiate real-time phone calls for appointment confirmations or follow-ups, adding a human touch to digital interactions.






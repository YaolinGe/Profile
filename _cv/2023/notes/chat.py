company = """Microsoft University"""

description = """
Finally, the application portal for Microsoft University for 2023 is open!

On behalf of Microsoft, Glasspaper People is looking for you who want to participate in Microsoft University 2023! In this educational course, you will receive training and attractive certifications within Microsoft technology under the auspices of Microsoft. You will get a permanent job ahead of the course with a leading partner or customer of Microsoft, and full salary during the course itself. We are looking for skilled candidates for courses within Business Intelligence, Machine Learning and Productivity with Office 365. After completing the training, you are able to work interdisciplinary with business development and technology within the aforementioned areas.

Your application will be available to several of Microsoft's partners and customers, which are many of Norway's most attractive technology and consulting companies. These are companies that want to recruit candidates with expertise in Microsoft technology, and your application means that you can have several exciting employers to choose from. Microsoft University is a unique door opener for new graduates, and the program is ranked among IT students as the most attractive trainee program in Norway.

A position as a consultant with a Microsoft partner or customer will offer great variety and an exciting everyday life. Examples of tasks you can get are:
• Analysis of customer needs and data
• Design of solution
• Development / implementation / migration of solutions
• Training of users
• Project management
• Assistance in sales processes

Who should apply?
You have a minimum of 3 years of higher education in one or more of the areas below:
• Computer engineering / Informatics / System development
• IT administration
• Development / IT in general
• Information systems
• Economics with IT subjects
• Industrial economy
• Communication technology
• Mathematics/physics/statistics
• E-business
• Business Intelligence / Business Analytics
• Database
• Other IT-related lines

What you get by attending Microsoft University:
• A kick-start to your career by receiving certification and courses under the auspices of Microsoft
• Full salary during the education period
• Forge useful relationships and networks with other participants and recognized companies
• Permanent job with a leading Norwegian Microsoft partner or customer of Microsoft
As a person, you are social, hardworking and reliable. Furthermore, it is desirable that you are structured, results-oriented, proactive and customer-oriented. Please note that we are looking for you who are juniors and have from 0-3 years of relevant full-time experience. The ability to communicate well orally and in writing in Norwegian, English, Swedish or Danish is a requirement.

Briefly about the process further:
Microsoft University starts in August 2023, but we have ongoing admissions and the deadline to apply is March 2023. We will fill around 80 places and recommend you apply early. Glasspaper conducts initial interviews on behalf of Microsoft and their partners. If you go further in the process, you will be profiled for many of the country's leading technology companies who, according to needs and preferences, will contact the applicants who best match their needs. A partner company or customer will then offer you a permanent job if you are relevant and will also offer you a place at Microsoft University. Everyone who participates in Microsoft University has been given a job before the start of the course and receives full salary from the first day of the course. The course itself takes place in Oslo.

This is how you apply:
By pressing search here, you will get to an application form. Here you must fill in your contact information, so that recruiters can contact you for further information.

Feel free to contact our recruitment officer for Microsoft University in Glasspaper People Andrea Mardal, andrea.mardal@glasspaper.no, 916 70 070 if you would like more information.
We look forward to receiving your application!

*According to GDPR, please apply via the system, and not directly to the contact person listed in this advertisement.
"""

background = """
•	Ph.D. candidate in the statistics group at Dept. of mathematical sciences at NTNU.
•	Experience with data-driven machine learning software system development.
•	Experience with software architecture design and data analytics.
•	Practice agile methodologies and test-driven development in a daily routine.
"""

tasks = """
•	Design and implement multi-scale data-driven machine learning software systems for remote sensing.
•	Develop data-driven models and software to incorporate various in-situ data including the satellite data collected in the ocean to better understand the phenomenon of water mass mixing.
•	Deploy and integrate the systems onboard an unmanned robot for several successful field experiments.
•	Collaborate and communicate closely with multiple customers including SINTEF Ocean, AURLab NTNU, LSTS, and MARETEC for knowledge dissemination to foster novel ideas.
•	Document and publish the results to relevant stakeholders and clients and share knowledge with the public. Three papers were accomplished.
"""

position = "Machine Learning, Business Intelligence"

# prompt = f"""
# Imagine you will have an interview with the company called OptoScale which has the following about page: {company}. The job has the description as {description}. You are about to finish your phd and having the following background {background} and you have done the following tasks during your phd {tasks}.
#
# Your task is to answer interview questions as you are the interviewee and I am the interviewer. Answer concrete and concise. Do not start making your own questions.
#
# You need to give a short explanation on why you answer like that.
# """


prompt = f"""
Imagine you are applying for a position: {position} at company: {company}.

You are finishing your phd and you have the following background: {background}

During your phd, you are mainly working with the following tasks: {tasks}

Your task is to generate a three paragrah long application letter with an enthusiastic tone of your interests and motivation for applying for the position given the description {description}

You cannot fake extra experience, all the experience must be based on your background and tasks you have been involved during your phd.
"""
print("=============================================================")
print(prompt)

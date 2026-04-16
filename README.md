# AI Peer Mentorship Matching App using Python and Flask

A web application that matches students with mentors using a weighted scoring algorithm based on academics and interests. The system is available on Render and uses backend API design, data processing, and real-time matching logic.

---

## Live Demo (on Render it may take a while to load up if it is inactive)
User Page:       https://ai-peer-mentorship.onrender.com/

Mentor Portal:   https://ai-peer-mentorship.onrender.com/mentor

## Demo Video
[Watch Demo Video](https://drive.google.com/drive/folders/1sOQ57ZvytCMk69VBPsdx6Qom198dXHQB)

---

## Features

- Flask REST API backend
- Student-to-mentor matching system
- Weighted scoring algorithm (interest, major, language, year)
- Mentor onboarding portal
- Real-time JSON request handling
- Logging system for backend events
- Fully deployed on Render

---

## System Overview

1. User submits student profile through web interface
2. Flask receives JSON data via `/match` endpoint
3. System compares student against all mentors
4. Weighted scoring algorithm calculates best match:
   - Interest match (+3)
   - Major match (+2)
   - Language match (+2)
   - Year proximity (+1)
5. Highest scoring mentor is returned instantly

---

## Matching Algorithm

Each mentor is scored:

- Interest match → +3
- Major match → +2
- Language match → +2
- Year difference ≤ 1 → +1

The mentor with the highest total score is selected.

---

## Tech Used

- Python
- Flask
- HTML / JavaScript
- JSON (data storage)
- Render (deployment platform)

---

Screenshots

[Student Portal + Match Result](https://drive.google.com/file/d/1XhH0cXTnyOkVGt6m5Gjxejg5nF3hHt_2/view?usp=sharing)

[Mentor Portal](https://drive.google.com/file/d/1cutndJPC5nlxCjPVELqizScdRG6N_GbA/view?usp=drive_link)

---

📈 Future Improvements
- Transition from JSON storage to PostgreSQL or Supabase
- Add authentication system for users
- Improve UI themes and colors
- Implement semantic search using embeddings
- Add admin dashboard for system monitoring
- Improve scalability for production use (ie within a college)

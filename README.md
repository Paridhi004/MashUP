# Mashup Generator Project

This project consists of two required parts:

1. **Program 1** – Command Line Mashup Generator  
2. **Program 2** – Web Service Mashup Generator  

The system downloads YouTube videos of a given singer, extracts audio, trims the first Y seconds from each, merges them into a single file, and delivers the result.

---

# Program 1: Command Line Mashup

## Description

A Python command-line tool that:

- Downloads N YouTube videos of a given singer
- Converts videos to audio
- Cuts first Y seconds from each audio
- Merges all trimmed clips
- Generates a single output MP3 file

---

## Usage
`python <RollNumber>.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>`

### Example:
`python 102303715.py "Sharry Maan" 20 25 output.mp3`

# Program 2: Web Service Mashup

## Description

A Flask-based web application that:

- Accepts user input through a web form:
  - Singer Name
  - Number of Videos
  - Duration of each clip
  - Email ID
- Generates mashup
- Compresses output into ZIP format
- Sends result file to provided email

---

## Web Form Inputs

- Singer Name
- Number of Videos
- Duration (seconds)
- Email ID (must be valid)

---

## How It Works

1. User submits form
2. Server processes mashup
3. Output file is zipped
4. Email sent with ZIP attachment

## Website Link:
https://mash-up.onrender.com/

# Author
Paridhi Rastogi  
B.Tech Computer Science  

<h1>Docker Studies</h1>

<p>This repository contains practical exercises to learn Docker, from simple scripts to more complex applications with Python, Docker Compose, and MiniLibX.</p>

<h2>Prerequisites</h2>
<p>Before running any exercises, make sure you have installed:</p>
<ul>
  <li><strong>Docker:</strong> <a href="https://docs.docker.com/get-docker/">Install Docker</a></li>
  <li><strong>Docker Compose:</strong> <a href="https://docs.docker.com/compose/install/">Install Docker Compose</a></li>
</ul>

<h2>Clone the repository</h2>
<pre> git clone https://github.com/sabrinafn/Docker-studies.git </pre>
<pre> cd Docker-studies </pre>

<h2>Repository Structure</h2>
<pre>
Docker-studies/
├── 00-python-message/
├── 01-python-app/
└── 02-minilib-game/
</pre>

<h2>Exercise 00: Python Message</h2>
<p>A simple Python script that prints a message using Docker.</p>
<ol>
  <li>Navigate to the exercise directory:
    <pre>cd 00-python-message</pre>
  </li>
  <li>Build the Docker image:
    <pre>docker build -t python-message .</pre>
  </li>
  <li>Run the container:
    <pre>docker run python-message</pre>
  </li>
</ol>

<h2>Exercise 01: Python App</h2>
<p>A Python application with dependencies, served via <code>uvicorn</code> and optionally visualized with Streamlit. Uses Docker Compose for multi-container orchestration (server, frontend, and database).</p>
<ol>
  <li>Navigate to the exercise directory:
    <pre>cd 01-python-app</pre>
  </li>
  <li>Build and run using Docker Compose:
    <pre>docker compose build</pre>
    <pre>docker compose up</pre>
  </li>
</ol>
<p>The API server will be available at <code>http://localhost:8001</code> and the Streamlit frontend at <code>http://localhost:8501</code>.</p>


<h2>Exercise 02: MiniLibx Game</h2>

<p><strong>So Long</strong> is a 2D game built with the MiniLibX library. You control a banana cat navigating walls, collecting milk bottles, and trying to reach the blender exit.</p>


<ol>
  <li>Navigate to the exercise directory:
    <pre>cd 02-minilib-game</pre>
  </li>
  <li>Build and run using Makefile:
    <pre>make build</pre>
    <pre>make run</pre>
    <pre>make map MAP=map42</pre>
    <p>Replace <code>map42</code> with any of the available maps below.</p>
  </li>
  <li>Makefile Commands:
<table>
  <tr><th>Command</th><th>Description</th></tr>
  <tr><td>make build</td><td>Build the Docker image for the game</td></tr>
  <tr><td>make run</td><td>Start the container in the background</td></tr>
  <tr><td>make map MAP=mapname</td><td>Run the game with a specific map (e.g., MAP=map42)</td></tr>
  <tr><td>make clean</td><td>Stop containers and remove images/volumes</td></tr>
  <tr><td>make help</td><td>Show help message</td></tr>
</table>
  </li>
  <li>Available Maps
<table>
   <tr><th>Map name</th></tr>
   <tr><td>map00</td></tr>
   <tr><td>map01</td></tr>
   <tr><td>map03</td></tr>
   <tr><td>map04</td></tr>
   <tr><td>map05</td></tr>
   <tr><td>map42</td></tr>
</table>
</li>
</ol>




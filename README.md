# Timekeeper ⏱️

[![GitHub license](https://img.shields.io/github/license/kjanker/stlite-timekeeper.svg)](https://github.com/kjanker/stlite-timekeeper/blob/main/LICENSE)

Timekeeper is a simple web app to track time in meetings and keep them timeboxed. It is made with [Streamlit](https://streamlit.io) and deployed as client side application with [stlite](https://github.com/whitphx/stlite).

## 💁 How can I use it?

You can access the deployed web application hosted with Github Pages [here](https://www.kjanker.com/stlite-timekeeper/). Since the execution is completely client site, you can simple download the [index.html](https://github.com/kjanker/stlite-timekeeper/blob/main/index.html) file and run it offline and locally.

## 📝 Building notes

The code of the working streamlit app [(app.py)](https://github.com/kjanker/stlite-timekeeper/blob/main/app.py) is almost fully copied over and embedded into the html file. Only `time.sleep` has to be replaced with `await asyncio.sleep` - due to implementation of [Pyodide](https://github.com/pyodide/pyodide).

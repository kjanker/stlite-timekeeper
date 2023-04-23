import datetime
import random
import time

import streamlit as st

WAIT_STEPPER = 1
WAIT_BEFORE_TIMER = 3
WAIT_AFTER_TIMER = 1
LINE_BREAK = """
"""

DEFAULT_DURATION = datetime.time(minute=10)
DEFAULT_NAMES = LINE_BREAK.join(["Emma", "John", "Clark"])

# setup top primary UI
st.set_page_config(page_title="Timeboxer")
st.title("Timekeeper ⏱️")
placeholder_current = st.empty()
placeholder_current.info("👈 Start an new timeboxed session on the left!")
# setup sidebar
sidebar = st.sidebar
form = sidebar.form(key="sidebar")
duration = form.slider(
    label="⏱️ How long do we have?",
    min_value=datetime.time(minute=1),
    max_value=datetime.time(minute=45),
    value=DEFAULT_DURATION,
    step=datetime.timedelta(seconds=15),
    format="mm:ss",
)
people = form.text_area(
    label="🙋 Who is with us?",
    value=DEFAULT_NAMES,
    height=200,
).split(LINE_BREAK)
shuffle = form.checkbox(
    label="🔀 Shuffle names randomly",
    value=True,
)
if form.form_submit_button(
    label="Let's go!",
    type="primary",
    use_container_width=True,
):
    # start time keeping
    duration = datetime.datetime.combine(datetime.date.min, duration) - datetime.datetime.min
    people = [p.strip() for p in people if p.strip()]
    if shuffle:
        random.shuffle(people)
    duration_per_each = (duration / len(people)).seconds
    # set up remaining primary UI
    progress_bar = st.progress(0)
    placeholder_history = st.empty()
    # iterate all people
    for active_index in range(len(people)):
        # init new active person
        progress_bar.progress(0.0)
        text_name = f"""**{people[active_index]}**:"""
        text_time = f"""You have {datetime.timedelta(seconds=duration_per_each)} left."""
        placeholder_current.info(text_name + " Next up! " + text_time)
        time.sleep(WAIT_BEFORE_TIMER)
        # iterate timer of active person
        for second in range(duration_per_each):
            text_time = f"""You have {datetime.timedelta(seconds=duration_per_each-second)} left."""
            progress = second / duration_per_each
            if progress < 0.5:
                placeholder_current.success(text_name + " Go! " + text_time)
            elif progress < 0.8:
                placeholder_current.warning(text_name + " Halfway. " + text_time)
            else:
                placeholder_current.error(text_name + " Come to the end. " + text_time)
            progress_bar.progress(progress)
            time.sleep(WAIT_STEPPER)
        progress_bar.progress(1.0)
        placeholder_current.error(text_name + " Time's up!")
        time.sleep(WAIT_AFTER_TIMER)
        # update list of finished people
        finished_people = people[: active_index + 1]
        with placeholder_history.container():
            for index, name in enumerate(reversed(finished_people)):
                st.info(f"""**{name}** is done.""")
    # finishing up
    placeholder_current.success("🏁 All finished!")
    st.balloons()

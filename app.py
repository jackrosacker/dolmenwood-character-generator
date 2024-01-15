import streamlit as st
from character import Character, Die
import pandas as pd

st.title("Dice Roller")

num_of_dice = st.number_input(
    "Number of dice", min_value=1, max_value=100, value=1, step=1
)

sides = st.number_input("Number of sides", min_value=2, max_value=100, value=2, step=2)

total, roll_results = Die(sides=sides).roll_dice(num_of_dice=num_of_dice)

if st.button(f"Roll {num_of_dice} d {sides}", type="primary"):
    st.write(f"Total: **{total}**")

    with st.expander("See individual roll results"):
        # src: discuss.streamlit.io/t/python-list-output-as-markdown-lists-beautify-lists/23303/2
        # return list results as unspaced markdown bullets
        s = ""
        for result in roll_results:
            s += f"- {result}\n"
        st.markdown(s)

st.divider()

st.title("Dolmenwood Character Generator")

if st.button("Generate Ability Scores", type="primary"):
    a_character = Character()

    a_character.generate_ability_scores()

    replacement_dict = {
        "str": "Strength",
        "int": "Intelligence",
        "wis": "Wisdom",
        "dex": "Dexterity",
        "con": "Constitution",
        "cha": "Charisma",
    }

    df = (
        pd.DataFrame.from_dict(a_character.ability_scores, orient="index")
        .reset_index()
        .replace(replacement_dict)
    )

    # st.table(df.style.hide())

    st.dataframe(df, column_config={"index": "Ability", "0": "Score"}, hide_index=True)

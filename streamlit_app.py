import streamlit as st
import random

positive_sentences_about_leyla = [
    "Leyla, your kindness knows no bounds.",
    "You have an incredible sense of humour that brightens everyone’s day.",
    "Your intelligence is truly inspiring.",
    "Leyla, you are a beacon of positivity.",
    "Your creativity is unmatched.",
    "You have a heart of gold.",
    "Leyla, your smile lights up the room.",
    "You are an amazing listener.",
    "Your compassion for others is extraordinary.",
    "Leyla, you are a natural leader.",
    "You have a remarkable talent for bringing people together.",
    "Your dedication to your work is admirable.",
    "Leyla, your resilience is awe-inspiring.",
    "You have an infectious enthusiasm for life.",
    "Your generosity is deeply appreciated.",
    "Leyla, you possess a unique charm.",
    "You have a wonderful sense of style.",
    "Your passion for what you do is evident in everything you achieve.",
    "Leyla, your optimism is contagious.",
    "You are incredibly thoughtful.",
    "Your loyalty to your friends and family is unwavering.",
    "Leyla, you have a sharp and insightful mind.",
    "Your presence is calming and reassuring.",
    "You are a true inspiration to those around you.",
    "Leyla, your work ethic is exemplary.",
    "You have a fantastic ability to solve problems.",
    "Your honesty is refreshing and appreciated.",
    "Leyla, you are a source of constant motivation.",
    "You have an impeccable taste.",
    "Your perseverance in the face of challenges is remarkable.",
    "Leyla, you are a ray of sunshine.",
    "You have a profound ability to empathise with others.",
    "Your attention to detail is impressive.",
    "Leyla, your laughter is infectious.",
    "You have a delightful sense of adventure.",
    "Your creativity knows no limits.",
    "Leyla, you are incredibly resourceful.",
    "You have a knack for making people feel special.",
    "Your intelligence shines through in everything you do.",
    "Leyla, you are a joy to be around.",
    "You have a talent for making the best out of any situation.",
    "Your kindness is a true gift to everyone who knows you.",
    "Leyla, you are wonderfully unique.",
    "You have an amazing ability to inspire others.",
    "Your positivity makes the world a better place.",
    "Leyla, you are exceptionally talented.",
    "You have a warm and welcoming nature.",
    "Your sense of fairness is commendable.",
    "Leyla, you have a beautiful spirit.",
    "You are always willing to help others.",
    "Your dedication to your passions is truly inspiring.",
    "Leyla, you have a remarkable ability to stay calm under pressure.",
    "You are an exceptional friend.",
    "Your curiosity about the world is admirable.",
    "Leyla, you have a heart full of love.",
    "You are a pillar of strength for those around you.",
    "Your creativity brings joy to many.",
    "Leyla, you are a true visionary.",
    "You have a wonderful way of seeing the good in people.",
    "Your patience is truly remarkable.",
    "Leyla, you are endlessly fascinating.",
    "You have a remarkable ability to make people laugh.",
    "Your insights are always valuable and thought-provoking.",
    "Leyla, you are a breath of fresh air.",
    "You have a unique perspective on life.",
    "Your commitment to your values is inspiring.",
    "Leyla, you are wonderfully dependable.",
    "You have a talent for making everyone feel included.",
    "Your kindness leaves a lasting impression.",
    "Leyla, you are a true gem.",
    "You have an exceptional ability to learn and grow.",
    "Your enthusiasm for life is unmatched.",
    "Leyla, you are beautifully authentic.",
    "You have a wonderful way with words.",
    "Your ability to connect with others is a true gift.",
    "Leyla, you are a joy to know.",
    "You have a remarkable sense of justice.",
    "Your creativity and innovation are inspiring.",
    "Leyla, you have a captivating presence.",
    "You are an amazing storyteller.",
    "Your wisdom is beyond your years.",
    "Leyla, you are a shining star.",
    "You have a wonderful sense of balance in life.",
    "Your kindness spreads happiness wherever you go.",
    "Leyla, you have a delightful personality.",
    "You are a true trailblazer.",
    "Your dedication to excellence is evident in everything you do.",
    "Leyla, you are a master at bringing out the best in people.",
    "You have a spirit that is both fierce and gentle.",
    "Your kindness and compassion make the world a better place.",
    "Leyla, you are an inspiration to us all.",
    "You have a heart that is pure and true.",
    "Your positivity is a light in the darkness.",
    "Leyla, you are a gift to everyone who knows you.",
    "You have a remarkable ability to uplift those around you.",
    "Your strength and grace are truly admirable.",
    "Leyla, you are an extraordinary person."
]

st.title("Leyla is cool.")
st.image("https://i.imgur.com/Z0JIEmj.png", caption="Leyla is cool indeed", width=250)  # Use a local image
# Or use an image UR
# st.image("https://example.com/leyla.jpg", caption="Leyla is Cool")



st.write("You are cool, and well all know it. If you ever suspect this is not correct, click on the button below to see why:")



if st.button("I am cool, but why?"):
    st.write(random.choice(positive_sentences_about_leyla))


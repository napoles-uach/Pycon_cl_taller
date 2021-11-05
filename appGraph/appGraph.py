import streamlit as st
import streamlit.components.v1 as components
from pyvis.network import Network
import numpy as np


st.title('Add nodes to the graph! ')
st.header('(to show session_state)')

#st.title('Counter Example')
#count = 0

#increment = st.button('Increment')
#if increment:
#    count += 1

#st.write('Count = ', count)
#st.stop()


# Check if 'count' already exists in session_state
# If not, then initialize it to 0
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('Add')
if increment:
    st.session_state.count += 1

st.write('Count = ', st.session_state.count)


valor=st.session_state.count

net = Network()
for i in range(valor):
    net.add_node(i, label=i)

#generate a list of random integers between 0 and valor
random_list_1 = [np.random.randint(0, valor) for i in range(valor)]
random_list_2 = [np.random.randint(0, valor) for i in range(valor)]
#zip the two lists together to form pairs
pairs = list(zip(random_list_1, random_list_2))
#add the edges to the network
for pair in pairs:
    net.add_edge(pair[0], pair[1])


net.show('test.html')
HtmlFile = open("test.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()

components.html(source_code, height = 900,width=900)










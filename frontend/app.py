import streamlit as st
import  streamlit_vertical_slider  as svs
import numpy as np
import pandas as pd
import requests
import plotly.graph_objects as go
from st_btn_select import st_btn_select
from sklearn.preprocessing import MinMaxScaler

st.set_page_config(layout="wide")
st.markdown("""
<style>
#wrapper{
    position: relative;
    width: 100%;
    height: auto;
}
.big-font {
    font-size:11em !important;

}
.foreground{
    z-index: 100;
    position:relative;
    }

.background{
    color: #999999;
    position: absolute;
    z-index: 0;
    top: 0;
    left: auto;
    right: 0;
    }

@keyframes hideshow {
  0% { opacity: 1; }
  50% { opacity: 0; }
  100% { opacity: 1; }
}
.scatterlayer path:nth-of-type(odd) {
  animation: hideshow 10s ease infinite;
  animation-delay: 250ms
}

</style>
""", unsafe_allow_html=True)


html = '<svg  viewBox="220 350 230 2520"  class="logo-svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="716" height="2550" style="background: white;"><defs id="defs-bce2be"><g class="clips"><clipPath id="clipbce2bepolar-for-traces"><path d="M278,0A278,278 0,1,0 -278,-3.404518101629642e-14A278,278 0,1,0 278,6.809036203259284e-14Z" transform="translate(278,278)"></path></clipPath></g><g class="gradients"></g><g class="patterns"></g></defs><g class="bglayer"></g><g class="draglayer"></g><g class="layer-below"><g class="imagelayer"></g><g class="shapelayer"></g></g><g class="cartesianlayer"></g><g class="polarlayer"><g class="polar"><g class="polarsublayer draglayer"><path class="angulardrag drag cursor-move" style="fill: transparent; stroke-width: 0px; pointer-events: all;" d="M278,0A278,278 0,1,0 -278,-3.404518101629642e-14A278,278 0,1,0 278,6.809036203259284e-14ZM308,0A308,308 0,1,1 -308,-3.7719121413738476e-14A308,308 0,1,1 308,7.543824282747695e-14Z" transform="translate(358,628.5)"></path><rect class="radialdrag-inner drag cursor-crosshair" style="fill: transparent; stroke-width: 0px; pointer-events: all;" x="-25" y="-25" width="50" height="50" transform="translate(333,628.5)"></rect><rect class="radialdrag drag cursor-crosshair" style="fill: transparent; stroke-width: 0px; pointer-events: all;" x="-25" y="-25" width="50" height="50" transform="translate(661,628.5)"></rect><path class="maindrag drag cursor-crosshair" style="fill: transparent; stroke-width: 0px; pointer-events: all;" d="M278,0A278,278 0,1,0 -278,-3.404518101629642e-14A278,278 0,1,0 278,6.809036203259284e-14Z" transform="translate(358,628.5)"></path></g><g class="polarsublayer plotbg"><path d="M278,0A278,278 0,1,0 -278,-3.404518101629642e-14A278,278 0,1,0 278,6.809036203259284e-14Z" transform="translate(358,628.5)" style="fill: rgb(100, 100, 100); fill-opacity: 0.1;"></path></g><g class="polarsublayer backplot"><g class="maplayer"></g></g><g class="polarsublayer angular-grid" style="fill: none;"><path class="angularaxisgrid" d="M358,628.5L636,628.5" style="stroke: rgb(255, 255, 255); stroke-opacity: 1; stroke-width: 1px;"></path><path class="angularaxisgrid" d="M358,628.5L531.3301649167279,411.15084787388776" style="stroke: rgb(255, 255, 255); stroke-opacity: 1; stroke-width: 1px;"></path><path class="angularaxisgrid" d="M358,628.5L296.1391803601446,357.47004041345303" style="stroke: rgb(255, 255, 255); stroke-opacity: 1; stroke-width: 1px;"></path><path class="angularaxisgrid" d="M358,628.5L107.5306547231275,507.8803205253188" style="stroke: rgb(255, 255, 255); stroke-opacity: 1; stroke-width: 1px;"></path><path class="angularaxisgrid" d="M358,628.5L107.53065472312747,749.1196794746811" style="stroke: rgb(255, 255, 255); stroke-opacity: 1; stroke-width: 1px;"></path><path class="angularaxisgrid" d="M358,628.5L296.13918036014456,899.529959586547" style="stroke: rgb(255, 255, 255); stroke-opacity: 1; stroke-width: 1px;"></path><path class="angularaxisgrid" d="M358,628.5L531.3301649167279,845.8491521261124" style="stroke: rgb(255, 255, 255); stroke-opacity: 1; stroke-width: 1px;"></path></g><g class="polarsublayer radial-grid" style="fill: none;" transform="translate(358,628.5)"><path class="xgrid" d="M54.85,0A54.85,54.85 0,1,0 -54.85,-6.717187693323232e-15A54.85,54.85 0,1,0 54.85,1.3434375386646464e-14Z" style="stroke: rgb(255, 255, 255); stroke-opacity: 1; stroke-width: 1px;"></path><path class="xgrid" d="M109.7,0A109.7,109.7 0,1,0 -109.7,-1.3434375386646464e-14A109.7,109.7 0,1,0 109.7,2.686875077329293e-14Z" style="stroke: rgb(255, 255, 255); stroke-opacity: 1; stroke-width: 1px;"></path><path class="xgrid" d="M164.55,0A164.55,164.55 0,1,0 -164.55,-2.01515630799697e-14A164.55,164.55 0,1,0 164.55,4.03031261599394e-14Z" style="stroke: rgb(255, 255, 255); stroke-opacity: 1; stroke-width: 1px;"></path><path class="xgrid" d="M219.4,0A219.4,219.4 0,1,0 -219.4,-2.686875077329293e-14A219.4,219.4 0,1,0 219.4,5.373750154658586e-14Z" style="stroke: rgb(255, 255, 255); stroke-opacity: 1; stroke-width: 1px;"></path><path class="xgrid" d="M274.25,0A274.25,274.25 0,1,0 -274.25,-3.358593846661616e-14A274.25,274.25 0,1,0 274.25,6.717187693323232e-14Z" style="stroke: rgb(255, 255, 255); stroke-opacity: 1; stroke-width: 1px;"></path></g><g class="polarsublayer frontplot" transform="translate(80,350.5)"><g class="barlayer"></g><g class="scatterlayer"><g class="trace scatter trace8c3f91" style="stroke-miterlimit: 2; opacity: 0.8;"><g class="fills" clip-path="url(#clipbce2bepolar-for-traces)"></g><g class="errorbars"></g><g class="lines"><path class="js-line" style="vector-effect: non-scaling-stroke; fill: none; stroke: rgb(99, 110, 250); stroke-opacity: 1; stroke-width: 5px; opacity: 1;" d="M552.25,278L376.63,154.32L259.19,195.6L204.55,242.63L203.09,314.07L242.55,433.31L364.2,386.1L552.25,278" clip-path="url(#clipbce2bepolar-for-traces)"></path></g><g class="points"><path class="point" transform="translate(552.25,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(99, 110, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(376.63,154.32)" style="opacity: 1; stroke-width: 0px; fill: rgb(99, 110, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(259.19,195.6)" style="opacity: 1; stroke-width: 0px; fill: rgb(99, 110, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(204.55,242.63)" style="opacity: 1; stroke-width: 0px; fill: rgb(99, 110, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(203.09,314.07)" style="opacity: 1; stroke-width: 0px; fill: rgb(99, 110, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(242.55,433.31)" style="opacity: 1; stroke-width: 0px; fill: rgb(99, 110, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(364.2,386.1)" style="opacity: 1; stroke-width: 0px; fill: rgb(99, 110, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(552.25,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(99, 110, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path></g><g class="text"></g></g><g class="trace scatter tracef1c368" style="stroke-miterlimit: 2; opacity: 0.8;"><g class="fills" clip-path="url(#clipbce2bepolar-for-traces)"></g><g class="errorbars"></g><g class="lines"><path class="js-line" style="vector-effect: non-scaling-stroke; fill: none; stroke: rgb(239, 85, 59); stroke-opacity: 1; stroke-width: 5px; opacity: 1;" d="M551.13,278L377.4,153.36L275.87,268.65L226,252.96L210.45,310.53L224.3,513.26L377.01,402.15L551.13,278" clip-path="url(#clipbce2bepolar-for-traces)"></path></g><g class="points"><path class="point" transform="translate(551.13,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(377.4,153.36)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(275.87,268.65)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(226,252.96)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(210.45,310.53)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(224.3,513.26)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(377.01,402.15)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(551.13,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path></g><g class="text"></g></g><g class="trace scatter traceee7315" style="stroke-miterlimit: 2; opacity: 0.8;"><g class="fills" clip-path="url(#clipbce2bepolar-for-traces)"></g><g class="errorbars"></g><g class="lines"><path class="js-line" style="vector-effect: non-scaling-stroke; fill: none; stroke: rgb(0, 204, 150); stroke-opacity: 1; stroke-width: 5px; opacity: 1;" d="M550.16,278L412.43,109.43L272.14,252.33L264.07,271.29L203.83,313.72L218.02,540.79L393.35,422.65L550.16,278" clip-path="url(#clipbce2bepolar-for-traces)"></path></g><g class="lines"><path class="js-line" style="vector-effect: non-scaling-stroke; fill: none; stroke: rgb(182, 232, 128); stroke-opacity: 1; stroke-width: 5px; opacity: 1;" d="M549.27,278L343.12,196.34L271.45,249.32L254.55,266.71L161.89,333.92L243.6,428.73L422.36,459.02L549.27,278" clip-path="url(#clipbce2bepolar-for-traces)"></path></g><g class="points"><path class="point" transform="translate(548.83,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 151, 255); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(314.56,232.16)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 151, 255); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(276.43,271.14)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 151, 255); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(277.68,277.84)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 151, 255); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(215.6,308.05)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 151, 255); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(233.88,471.32)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 151, 255); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(398.11,428.61)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 151, 255); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(548.83,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 151, 255); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path></g><g class="text"></g></g><g class="trace scatter traceecd63f" style="stroke-miterlimit: 2; opacity: 0.8;"><g class="fills" clip-path="url(#clipbce2bepolar-for-traces)"></g><g class="errorbars"></g><g class="lines"><path class="js-line" style="vector-effect: non-scaling-stroke; fill: none; stroke: rgb(254, 203, 82); stroke-opacity: 1; stroke-width: 5px; opacity: 1;" d="M548.77,278L418.14,102.26L270.46,244.95L248.79,263.93L253.13,289.98L248.53,407.1L323.35,334.86L548.77,278" clip-path="url(#clipbce2bepolar-for-traces)"></path></g><g class="points"><path class="point" transform="translate(548.77,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(254, 203, 82); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(418.14,102.26)" style="opacity: 1; stroke-width: 0px; fill: rgb(254, 203, 82); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(270.46,244.95)" style="opacity: 1; stroke-width: 0px; fill: rgb(254, 203, 82); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(248.79,263.93)" style="opacity: 1; stroke-width: 0px; fill: rgb(254, 203, 82); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(253.13,289.98)" style="opacity: 1; stroke-width: 0px; fill: rgb(254, 203, 82); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(248.53,407.1)" style="opacity: 1; stroke-width: 0px; fill: rgb(254, 203, 82); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(323.35,334.86)" style="opacity: 1; stroke-width: 0px; fill: rgb(254, 203, 82); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(548.77,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(254, 203, 82); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path></g><g class="text"></g></g><g class="trace scatter traceea1e50" style="stroke-miterlimit: 2; opacity: 0.8;"><g class="fills" clip-path="url(#clipbce2bepolar-for-traces)"></g><g class="errorbars"></g><g class="lines"><path class="js-line" style="vector-effect: non-scaling-stroke; fill: none; stroke: rgb(99, 110, 250); stroke-opacity: 1; stroke-width: 5px; opacity: 1;" d="M548.76,278L384.25,144.77L276.46,271.25L242.87,261.08L109.64,359.08L248.23,408.41L356.43,376.34L548.76,278" clip-path="url(#clipbce2bepolar-for-traces)"></path></g><g class="points"><path class="point" transform="translate(548.42,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(171, 99, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(362.16,172.46)" style="opacity: 1; stroke-width: 0px; fill: rgb(171, 99, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(258.72,193.52)" style="opacity: 1; stroke-width: 0px; fill: rgb(171, 99, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(275.91,276.99)" style="opacity: 1; stroke-width: 0px; fill: rgb(171, 99, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(243.2,294.76)" style="opacity: 1; stroke-width: 0px; fill: rgb(171, 99, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(270.67,310.11)" style="opacity: 1; stroke-width: 0px; fill: rgb(171, 99, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(278,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(171, 99, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(548.42,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(171, 99, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path></g><g class="text"></g></g><g class="trace scatter trace3a1175" style="stroke-miterlimit: 2; opacity: 0.8;"><g class="fills" clip-path="url(#clipbce2bepolar-for-traces)"></g><g class="errorbars"></g><g class="lines"><path class="js-line" style="vector-effect: non-scaling-stroke; fill: none; stroke: rgb(255, 161, 90); stroke-opacity: 1; stroke-width: 5px; opacity: 1;" d="M548.37,278L421.19,98.44L274.09,260.85L277.87,277.94L250.63,291.18L221.01,527.68L364.59,386.58L548.37,278" clip-path="url(#clipbce2bepolar-for-traces)"></path></g><g class="points"><path class="point" transform="translate(548.37,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(421.19,98.44)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(274.09,260.85)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(277.87,277.94)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(250.63,291.18)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(221.01,527.68)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(364.59,386.58)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(548.37,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path></g><g class="text"></g></g><g class="trace scatter trace399fbc" style="stroke-miterlimit: 2; opacity: 0.8;"><g class="fills" clip-path="url(#clipbce2bepolar-for-traces)"></g><g class="errorbars"></g><g class="lines"><path class="js-line" style="vector-effect: non-scaling-stroke; fill: none; stroke: rgb(25, 211, 243); stroke-opacity: 1; stroke-width: 5px; opacity: 1;" d="M548.35,278L387.68,140.47L253.26,169.62L210.89,245.68L254.6,289.27L263.34,342.22L278.09,278.11L548.35,278" clip-path="url(#clipbce2bepolar-for-traces)"></path></g><g class="points"><path class="point" transform="translate(548.35,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(25, 211, 243); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(387.68,140.47)" style="opacity: 1; stroke-width: 0px; fill: rgb(25, 211, 243); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(253.26,169.62)" style="opacity: 1; stroke-width: 0px; fill: rgb(25, 211, 243); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(210.89,245.68)" style="opacity: 1; stroke-width: 0px; fill: rgb(25, 211, 243); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(254.6,289.27)" style="opacity: 1; stroke-width: 0px; fill: rgb(25, 211, 243); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(263.34,342.22)" style="opacity: 1; stroke-width: 0px; fill: rgb(25, 211, 243); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(278.09,278.11)" style="opacity: 1; stroke-width: 0px; fill: rgb(25, 211, 243); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(548.35,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(25, 211, 243); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path></g><g class="text"></g></g><g class="trace scatter tracead1f98" style="stroke-miterlimit: 2; opacity: 0.8;"><g class="fills" clip-path="url(#clipbce2bepolar-for-traces)"></g><g class="errorbars"></g><g class="lines"><path class="js-line" style="vector-effect: non-scaling-stroke; fill: none; stroke: rgb(255, 102, 146); stroke-opacity: 1; stroke-width: 5px; opacity: 1;" d="M548.32,278L425.38,93.19L273.52,258.36L217.99,249.1L272.78,280.52L253.02,387.44L350.27,368.62L548.32,278" clip-path="url(#clipbce2bepolar-for-traces)"></path></g><g class="points"><path class="point" transform="translate(548.32,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 102, 146); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(425.38,93.19)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 102, 146); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(273.52,258.36)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 102, 146); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(217.99,249.1)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 102, 146); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(272.78,280.52)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 102, 146); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(253.02,387.44)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 102, 146); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(350.27,368.62)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 102, 146); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(548.32,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 102, 146); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path></g><g class="text"></g></g><g class="trace scatter trace75e6fe" style="stroke-miterlimit: 2; opacity: 0.8;"><g class="fills" clip-path="url(#clipbce2bepolar-for-traces)"></g><g class="errorbars"></g><g class="lines"><path class="js-line" style="vector-effect: non-scaling-stroke; fill: none; stroke: rgb(182, 232, 128); stroke-opacity: 1; stroke-width: 5px; opacity: 1;" d="M548.31,278L395.3,130.92L276.79,272.7L54.28,170.26L136.87,345.97L225.05,509.99L380.99,407.15L548.31,278" clip-path="url(#clipbce2bepolar-for-traces)"></path></g><g class="points"><path class="point" transform="translate(548.31,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(182, 232, 128); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(395.3,130.92)" style="opacity: 1; stroke-width: 0px; fill: rgb(182, 232, 128); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(276.79,272.7)" style="opacity: 1; stroke-width: 0px; fill: rgb(182, 232, 128); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(54.28,170.26)" style="opacity: 1; stroke-width: 0px; fill: rgb(182, 232, 128); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(136.87,345.97)" style="opacity: 1; stroke-width: 0px; fill: rgb(182, 232, 128); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(225.05,509.99)" style="opacity: 1; stroke-width: 0px; fill: rgb(182, 232, 128); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(380.99,407.15)" style="opacity: 1; stroke-width: 0px; fill: rgb(182, 232, 128); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(548.31,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(182, 232, 128); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path></g><g class="text"></g></g><g class="trace scatter trace776b20" style="stroke-miterlimit: 2; opacity: 0.8;"><g class="fills" clip-path="url(#clipbce2bepolar-for-traces)"></g><g class="errorbars"></g><g class="lines"><path class="js-line" style="vector-effect: non-scaling-stroke; fill: none; stroke: rgb(255, 151, 255); stroke-opacity: 1; stroke-width: 5px; opacity: 1;" d="M548.3,278L410.91,111.34L276.53,271.56L274.91,276.51L278,278L219.82,532.92L360.44,381.37L548.3,278" clip-path="url(#clipbce2bepolar-for-traces)"></path></g><g class="points"><path class="point" transform="translate(548.3,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 151, 255); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(410.91,111.34)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 151, 255); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(276.53,271.56)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 151, 255); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(274.91,276.51)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 151, 255); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(278,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 151, 255); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(219.82,532.92)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 151, 255); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(360.44,381.37)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 151, 255); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(548.3,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 151, 255); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path></g><g class="text"></g></g><g class="trace scatter traceae3236" style="stroke-miterlimit: 2; opacity: 0.8;"><g class="fills" clip-path="url(#clipbce2bepolar-for-traces)"></g><g class="errorbars"></g><g class="lines"><path class="js-line" style="vector-effect: non-scaling-stroke; fill: none; stroke: rgb(254, 203, 82); stroke-opacity: 1; stroke-width: 5px; opacity: 1;" d="M548.26,278L365.59,168.16L255.63,180.01L174.5,228.16L244.23,294.26L227.59,498.85L448.99,492.42L548.26,278" clip-path="url(#clipbce2bepolar-for-traces)"></path></g><g class="points"><path class="point" transform="translate(548.26,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(254, 203, 82); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(365.59,168.16)" style="opacity: 1; stroke-width: 0px; fill: rgb(254, 203, 82); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(255.63,180.01)" style="opacity: 1; stroke-width: 0px; fill: rgb(254, 203, 82); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(174.5,228.16)" style="opacity: 1; stroke-width: 0px; fill: rgb(254, 203, 82); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(244.23,294.26)" style="opacity: 1; stroke-width: 0px; fill: rgb(254, 203, 82); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(227.59,498.85)" style="opacity: 1; stroke-width: 0px; fill: rgb(254, 203, 82); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(448.99,492.42)" style="opacity: 1; stroke-width: 0px; fill: rgb(254, 203, 82); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(548.26,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(254, 203, 82); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path></g><g class="text"></g></g><g class="trace scatter trace5057cf" style="stroke-miterlimit: 2; opacity: 0.8;"><g class="fills" clip-path="url(#clipbce2bepolar-for-traces)"></g><g class="errorbars"></g><g class="lines"><path class="js-line" style="vector-effect: non-scaling-stroke; fill: none; stroke: rgb(99, 110, 250); stroke-opacity: 1; stroke-width: 5px; opacity: 1;" d="M548.21,278L369.02,163.87L259.67,197.67L213.98,247.17L59.61,383.17L229.69,489.67L391.2,419.95L548.21,278" clip-path="url(#clipbce2bepolar-for-traces)"></path></g><g class="points"><path class="point" transform="translate(548.21,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(99, 110, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(369.02,163.87)" style="opacity: 1; stroke-width: 0px; fill: rgb(99, 110, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(259.67,197.67)" style="opacity: 1; stroke-width: 0px; fill: rgb(99, 110, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(213.98,247.17)" style="opacity: 1; stroke-width: 0px; fill: rgb(99, 110, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(59.61,383.17)" style="opacity: 1; stroke-width: 0px; fill: rgb(99, 110, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(229.69,489.67)" style="opacity: 1; stroke-width: 0px; fill: rgb(99, 110, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(391.2,419.95)" style="opacity: 1; stroke-width: 0px; fill: rgb(99, 110, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(548.21,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(99, 110, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path></g><g class="text"></g></g><g class="trace scatter trace6e2572" style="stroke-miterlimit: 2; opacity: 0.8;"><g class="fills" clip-path="url(#clipbce2bepolar-for-traces)"></g><g class="errorbars"></g><g class="lines"><path class="js-line" style="vector-effect: non-scaling-stroke; fill: none; stroke: rgb(239, 85, 59); stroke-opacity: 1; stroke-width: 5px; opacity: 1;" d="M548.19,278L376.63,154.32L277.34,275.09L273.87,276.01L68.44,378.92L246.14,417.58L381.1,407.28L548.19,278" clip-path="url(#clipbce2bepolar-for-traces)"></path></g><g class="points"><path class="point" transform="translate(548.19,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(376.63,154.32)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(277.34,275.09)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(273.87,276.01)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(68.44,378.92)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(246.14,417.58)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(381.1,407.28)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(548.19,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path></g><g class="text"></g></g><g class="trace scatter tracef26a11" style="stroke-miterlimit: 2; opacity: 0.8;"><g class="fills" clip-path="url(#clipbce2bepolar-for-traces)"></g><g class="errorbars"></g><g class="lines"><path class="js-line" style="vector-effect: non-scaling-stroke; fill: none; stroke: rgb(0, 204, 150); stroke-opacity: 1; stroke-width: 5px; opacity: 1;" d="M548.18,278L353.4,183.45L256.58,184.16L30.91,159.01L210.45,310.53L244.35,425.45L368.36,391.31L548.18,278" clip-path="url(#clipbce2bepolar-for-traces)"></path></g><g class="points"><path class="point" transform="translate(548.18,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(0, 204, 150); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(353.4,183.45)" style="opacity: 1; stroke-width: 0px; fill: rgb(0, 204, 150); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(256.58,184.16)" style="opacity: 1; stroke-width: 0px; fill: rgb(0, 204, 150); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(30.91,159.01)" style="opacity: 1; stroke-width: 0px; fill: rgb(0, 204, 150); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(210.45,310.53)" style="opacity: 1; stroke-width: 0px; fill: rgb(0, 204, 150); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(244.35,425.45)" style="opacity: 1; stroke-width: 0px; fill: rgb(0, 204, 150); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(368.36,391.31)" style="opacity: 1; stroke-width: 0px; fill: rgb(0, 204, 150); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(548.18,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(0, 204, 150); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path></g><g class="text"></g></g><g class="trace scatter trace2ad1d6" style="stroke-miterlimit: 2; opacity: 0.8;"><g class="fills" clip-path="url(#clipbce2bepolar-for-traces)"></g><g class="errorbars"></g><g class="lines"><path class="js-line" style="vector-effect: non-scaling-stroke; fill: none; stroke: rgb(171, 99, 250); stroke-opacity: 1; stroke-width: 5px; opacity: 1;" d="M548.18,278L405.2,118.5L277.1,274.05L175.33,228.56L166.3,331.79L220.56,529.65L352.74,371.72L548.18,278" clip-path="url(#clipbce2bepolar-for-traces)"></path></g><g class="points"><path class="point" transform="translate(548.18,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(171, 99, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(405.2,118.5)" style="opacity: 1; stroke-width: 0px; fill: rgb(171, 99, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(277.1,274.05)" style="opacity: 1; stroke-width: 0px; fill: rgb(171, 99, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(175.33,228.56)" style="opacity: 1; stroke-width: 0px; fill: rgb(171, 99, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(166.3,331.79)" style="opacity: 1; stroke-width: 0px; fill: rgb(171, 99, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(220.56,529.65)" style="opacity: 1; stroke-width: 0px; fill: rgb(171, 99, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(352.74,371.72)" style="opacity: 1; stroke-width: 0px; fill: rgb(171, 99, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(548.18,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(171, 99, 250); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path></g><g class="text"></g></g><g class="trace scatter trace9b5e70" style="stroke-miterlimit: 2; opacity: 0.8;"><g class="fills" clip-path="url(#clipbce2bepolar-for-traces)"></g><g class="errorbars"></g><g class="lines"><path class="js-line" style="vector-effect: non-scaling-stroke; fill: none; stroke: rgb(255, 161, 90); stroke-opacity: 1; stroke-width: 5px; opacity: 1;" d="M548.14,278L397.96,127.57L273.35,257.63L136.93,210.06L254.9,289.13L262.89,344.19L344.05,360.82L548.14,278" clip-path="url(#clipbce2bepolar-for-traces)"></path></g><g class="points"><path class="point" transform="translate(548.14,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(397.96,127.57)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(273.35,257.63)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(136.93,210.06)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(254.9,289.13)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(262.89,344.19)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(344.05,360.82)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(548.14,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path></g><g class="text"></g></g><g class="trace scatter trace2db6ca" style="stroke-miterlimit: 2; opacity: 0.8;"><g class="fills" clip-path="url(#clipbce2bepolar-for-traces)"></g><g class="errorbars"></g><g class="lines"><path class="js-line" style="vector-effect: non-scaling-stroke; fill: none; stroke: rgb(25, 211, 243); stroke-opacity: 1; stroke-width: 5px; opacity: 1;" d="M548.14,278L367.88,165.3L274.56,262.93L151.12,216.9L137.6,345.61L227.44,499.5L368.69,391.72L548.14,278" clip-path="url(#clipbce2bepolar-for-traces)"></path></g><g class="points"><path class="point" transform="translate(548.14,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(25, 211, 243); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(367.88,165.3)" style="opacity: 1; stroke-width: 0px; fill: rgb(25, 211, 243); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(274.56,262.93)" style="opacity: 1; stroke-width: 0px; fill: rgb(25, 211, 243); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(151.12,216.9)" style="opacity: 1; stroke-width: 0px; fill: rgb(25, 211, 243); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(137.6,345.61)" style="opacity: 1; stroke-width: 0px; fill: rgb(25, 211, 243); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(227.44,499.5)" style="opacity: 1; stroke-width: 0px; fill: rgb(25, 211, 243); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(368.69,391.72)" style="opacity: 1; stroke-width: 0px; fill: rgb(25, 211, 243); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(548.14,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(25, 211, 243); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path></g><g class="text"></g></g><g class="trace scatter trace33d753" style="stroke-miterlimit: 2; opacity: 0.8;"><g class="fills" clip-path="url(#clipbce2bepolar-for-traces)"></g><g class="errorbars"></g><g class="lines"><path class="js-line" style="vector-effect: non-scaling-stroke; fill: none; stroke: rgb(255, 102, 146); stroke-opacity: 1; stroke-width: 5px; opacity: 1;" d="M548.13,278L386.92,141.42L276.29,270.52L153.63,218.1L229.95,301.14L263.49,341.57L319.08,329.51L548.13,278" clip-path="url(#clipbce2bepolar-for-traces)"></path></g><g class="points"><path class="point" transform="translate(548.13,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 102, 146); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(386.92,141.42)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 102, 146); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(276.29,270.52)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 102, 146); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(153.63,218.1)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 102, 146); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(229.95,301.14)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 102, 146); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(263.49,341.57)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 102, 146); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(319.08,329.51)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 102, 146); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(548.13,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 102, 146); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path></g><g class="text"></g></g><g class="trace scatter tracec9f8f8" style="stroke-miterlimit: 2; opacity: 0.8;"><g class="fills" clip-path="url(#clipbce2bepolar-for-traces)"></g><g class="errorbars"></g><g class="lines"><path class="js-line" style="vector-effect: non-scaling-stroke; fill: none; stroke: rgb(182, 232, 128); stroke-opacity: 1; stroke-width: 5px; opacity: 1;" d="M548.02,278L368.26,164.82L273.87,259.92L224.5,252.24L200.15,315.49L248.68,406.44L372.86,396.95L548.02,278" clip-path="url(#clipbce2bepolar-for-traces)"></path></g><g class="points"><path class="point" transform="translate(548.02,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(182, 232, 128); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(368.26,164.82)" style="opacity: 1; stroke-width: 0px; fill: rgb(182, 232, 128); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(273.87,259.92)" style="opacity: 1; stroke-width: 0px; fill: rgb(182, 232, 128); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(224.5,252.24)" style="opacity: 1; stroke-width: 0px; fill: rgb(182, 232, 128); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(200.15,315.49)" style="opacity: 1; stroke-width: 0px; fill: rgb(182, 232, 128); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(248.68,406.44)" style="opacity: 1; stroke-width: 0px; fill: rgb(182, 232, 128); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(372.86,396.95)" style="opacity: 1; stroke-width: 0px; fill: rgb(182, 232, 128); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(548.02,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(182, 232, 128); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path></g><g class="text"></g></g><g class="trace scatter trace9743c5" style="stroke-miterlimit: 2; opacity: 0.8;"><g class="fills" clip-path="url(#clipbce2bepolar-for-traces)"></g><g class="errorbars"></g><g class="lines"><path class="js-line" style="vector-effect: non-scaling-stroke; fill: none; stroke: rgb(255, 151, 255); stroke-opacity: 1; stroke-width: 5px; opacity: 1;" d="M548,278L278,278L274.92,264.49L125.24,204.44L230.83,300.71L270.37,311.42L327.93,340.61L548,278" clip-path="url(#clipbce2bepolar-for-traces)"></path></g><g class="lines"><path class="js-line" style="vector-effect: non-scaling-stroke; fill: none; stroke: rgb(255, 161, 90); stroke-opacity: 1; stroke-width: 5px; opacity: 1;" d="M547.91,278L357.97,177.72L276.06,269.48L248.38,263.73L219.28,306.28L278,278L366.41,388.86L547.91,278" clip-path="url(#clipbce2bepolar-for-traces)"></path></g><g class="points"><path class="point" transform="translate(547.91,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(357.97,177.72)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(276.06,269.48)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(248.38,263.73)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(219.28,306.28)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(278,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(366.41,388.86)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(547.91,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(255, 161, 90); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path></g><g class="text"></g></g><g class="points"><path class="point" transform="translate(547.16,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(427.28,90.8)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(236.9,97.91)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(141.94,212.48)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(249.3,291.82)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(263.49,341.57)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(380.98,407.13)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path><path class="point" transform="translate(547.16,278)" style="opacity: 1; stroke-width: 0px; fill: rgb(239, 85, 59); fill-opacity: 1;" d="M3,0A3,3 0 1,1 0,-3A3,3 0 0,1 3,0Z"></path></g><g class="text"></g></g></g></g><g class="polarsublayer angular-line"><path style="fill: none; stroke: rgb(255, 255, 255); stroke-opacity: 1;" d="M278,0A278,278 0,1,0 -278,-3.404518101629642e-14A278,278 0,1,0 278,6.809036203259284e-14Z" transform="translate(358,628.5)" stroke-width="1"></path></g></g></g><g class="smithlayer"></g><g class="ternarylayer"></g><g class="geolayer"></g><g class="funnelarealayer"></g><g class="pielayer"></g><g class="iciclelayer"></g><g class="treemaplayer"></g><g class="sunburstlayer"></g><g class="glimages"></g></svg>'


st.markdown(f'<div id="wrapper"><div class="foreground"><p class="big-font"><i>Rhythm</i> </br> Radar</p><p style="text-align:right;"> Your <i> customizable</i> Music Recommendation System</p> </div><div class="background" >{html}</div></div>', unsafe_allow_html=True)



search,  customise = st.tabs(["1. Select your Song and Artist", "2. Customise with DJ mixx"])

with search:
    col_song, col_artist = st.columns(2)
    with col_song:
        input_title = st.text_input("Please input your song title", max_chars=30)
    with col_artist:
        input_artist = st.text_input("Please input your song artist", max_chars=30)
    st.write("We will search for recommendations for:", f"*{input_artist}, {input_title}*")

    if input_artist and input_title:
        st.success("Sufficient Information to search for recommendations")
        "Please proceed after Optional Settings for recommendations"
    else:
        st.warning("Please specify at least Title and Artist")

    ""
    # Amount Recommendations asked
    "Next, adjust the **amount of recommendations** you want to get"
    recom_amount = st.slider("How many recommendations would you like?", 1, 100, value=5)
    ""


with customise:


    "### How do _you_ want your similarity to be measured"
    "There are several ways to measure 'similarity'. Here, you can choose between two. Have fun playing around!"
    sim_measure = st_btn_select(('Cosine', 'RBF'))
    st.write("Chosen similarity measure:", sim_measure)
    if sim_measure == "Polynomial":
        poly_degree = st.number_input("Please specifiy polynomial degree", min_value=2, max_value=10, value=2)
        st.info("Note default degree of 2")
    ""
    # Individual weights on (selected) features
    "### Become _your_ own DJ"
    "Let the _algorithm_ know what about the song is important to _you_."
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        danceability = svs.vertical_slider(
                            key="danceability",
                            default_value=1,
                            step=0.1,
                            min_value=0,
                            max_value=10
                            )
        "danceability"
    with col2:
        energy = svs.vertical_slider(
                            key="energy",
                            default_value=1,
                            step=0.1,
                            min_value=0,
                            max_value=10
                            )
        "energy"
    with col3:
        key = svs.vertical_slider(
                            key="key",
                            default_value=1,
                            step=0.1,
                            min_value=0,
                            max_value=10
                            )
        "key"

    with col4:
        mode = svs.vertical_slider(
                            key="mode",
                            default_value=1,
                            step=0.1,
                            min_value=0,
                            max_value=10
                            )
        "mode"
    with col5:
        speechiness = svs.vertical_slider(
                            key="speechiness",
                            default_value=1,
                            step=0.1,
                            min_value=0,
                            max_value=10
                            )
        "speechniness"
    col6, col7, col8, col9, col10 = st.columns(5)

    with col6:
        acousticness = svs.vertical_slider(
                            key="acousticness",
                            default_value=1,
                            step=0.1,
                            min_value=0,
                            max_value=10
                            )
        "acousticness"


    with col7:
        instrumentalness = svs.vertical_slider(
                            key="instrumentalness",
                            default_value=1,
                            step=0.1,
                            min_value=0,
                            max_value=10
                            )
        "instrumentalness"
    with col8:
        liveness = svs.vertical_slider(
                            key="liveness",
                            default_value=1,
                            step=0.1,
                            min_value=0,
                            max_value=10
                            )
        "liveness"
    with col9:
        tempo = svs.vertical_slider(
                            key="tempo",
                            default_value=1,
                            step=0.1,
                            min_value=0,
                            max_value=10
                            )
        "tempo"
    with col10:
        valence = svs.vertical_slider(
                                key="valence",
                                default_value=1,
                                step=0.1,
                                min_value=0,
                                max_value=10
                                )
        "valence"


######## API CALL #######
    url = 'https://test-t3ozapnnrq-ew.a.run.app/predict'
    params = {
                'track_input':  input_title,
                'artist_input': input_artist,
                'n_recommendations': recom_amount,
                'metric':sim_measure.lower(),
                'danceability' : danceability,
                'energy' : energy,
                'key' : key,
                'mode' : mode,
                'speechiness' : speechiness,
                'acousticness' : acousticness,
                'instrumentalness' : instrumentalness,
                'liveness' : liveness,
                'valence' : valence,
                'tempo' : tempo
        }

submit_button =  st.button('Get Recommendations')

if submit_button:
    params_song = params.copy()
    params_song["n_recommendations"] = 0
    with st.spinner('Wait for it...'):
        response_0 = requests.get(url, params = params_song )
        prev_url_song = response_0.json()['prevurl']
        st.audio(prev_url_song[0])


    with st.spinner('Wait for it...'):
        response = requests.get(url, params=params)
        #st.write(response)
    if response.status_code == 200:

        #st.write(response.json())
        prev_urls = response.json()['prevurl']
        prev_songs = [f'<audio id="{url}" controls="" src="{url}" class="stAudio" style="width: 70px;"></audio>' for url in prev_urls]
        track_id = response.json()['track_id']
        similarity = response.json()['similarity']
        track_name = response.json()['track_name']
        artist = response.json()['artists']
        danceability = response.json()['danceability']
        key = response.json()['key']
        mode = response.json()['mode']
        speechiness = response.json()['speechiness']
        acousticness = response.json()['acousticness']
        instrumentalness = response.json()['instrumentalness']
        liveness = response.json()['liveness']
        valence = response.json()['valence']
        tempo = response.json()['tempo']


        recommendations =  pd.DataFrame({'track_id' : track_id,
                                    'similarity' : similarity,
                                    'track_name' : track_name,
                                    'artist' : artist,
                                    'danceability' : danceability,
                                    'key' : key,
                                    'mode' : mode,
                                    'speechiness' : speechiness,
                                    'acousticness' : acousticness,
                                    'instrumentalness' : instrumentalness,
                                    'liveness' : liveness,
                                    'valence' : valence,
                                    'tempo' : tempo,
                                    'similarity' : similarity,

                                    })

        recommendations.drop(columns=["track_id"], axis=1, inplace=True)
        recommendations.reset_index(drop=True, inplace=True)
        recommendations.rename(columns={"similarity": "Level of Similarity",
                                        "track_name": "Song Title",
                                        "artist": "Song Artist"}, inplace=True)
        recommendations["song_preview"] = prev_songs

        rc_scaled = recommendations.copy()
        feature_scale = ["danceability","key" ,"mode","speechiness" ,"acousticness","instrumentalness","liveness","valence","tempo"]
        scaler = MinMaxScaler()
        rc_scaled[feature_scale] = pd.DataFrame(scaler.fit_transform(rc_scaled[feature_scale]), columns = feature_scale)
        features = ["Level of Similarity","danceability","speechiness" ,"acousticness","liveness","valence","tempo","Level of Similarity"]

        fig = go.Figure()
        for row in rc_scaled.iterrows():
            fig.add_trace(go.Scatterpolar(
                    line = dict(width=5),
                    opacity=0.8,
                    r = row[1][features],
                    theta=features,
                    fill='none',
                    name= f" {row[1]['Song Title']} by {row[1]['Song Artist']} ",
                    textposition="top center"
                ))
        fig.update_layout(
        font=dict(
        size=23,
        ),
        width=950,
        height=950,
        polar=dict(
            radialaxis=dict(
            visible=True
            ),
        ),
        legend=dict(
            orientation="h",

        ),
        hovermode="x unified"
        )

        fig.update_traces(
            hovertemplate="<br>".join([
                "The %{theta} score is %{r}"
            ])
        )

        st.plotly_chart(fig, use_container_width=True)
        st.write(recommendations.to_html(escape=False, index=False), unsafe_allow_html=True)
    else:
        st.write("Bad Connection Gateway")

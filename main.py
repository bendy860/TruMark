import streamlit as st


class Lok:
    def __init__(self):
        self.rating = 340.0
        self.weight = 60.0
        self.arrow = 405.0
        self.string_weight = 35.0
        self.poteg = 30.0
        self.kinetic= 75.65
        self.fps=290
        self.ATA= 40
        self.stabi_dolzina=30

    def dodaj_fps(self,fps):
        self.fps=fps
    def dodaj_kinetic(self, KE):
        self.kinetic=KE

    def dodoj_sprendjo_tezo_dolzino(self,l):
        self.stabi_dolzina=l

    def dodaj_ATA(self, ata):
        self.ATA=ata


if "moj_lok" not in st.session_state:
    st.session_state.moj_lok = Lok()

lok = st.session_state.moj_lok

st.title("TruMark- Archery Tuner")


st.sidebar.title("TruMark")


st.sidebar.header("Current Setup")
col1, col2 = st.sidebar.columns(2)
with col1:
    st.sidebar.metric("Bow Weight", f"{lok.weight:.0f} lbs")
    st.sidebar.metric("Draw Length", f"{lok.poteg:.1f}″")
with col2:
    st.sidebar.metric("FPS", f"{round(lok.fps)}")
st.sidebar.divider()
st.sidebar.metric("Total Arrow Weight", f"{lok.arrow} gr")
if lok.fps > 0:
    st.sidebar.metric("Kinetic Energy", f"{lok.kinetic} ft-lbs")
st.sidebar.divider()
if lok.arrow / lok.weight < 5:
    st.sidebar.error("TOO LIGHT ARROW")
elif lok.arrow / lok.weight < 6:
    st.sidebar.warning("Fast")
else:
    st.sidebar.success("Arrow weight OK")

st.sidebar.divider()


page = st.sidebar.radio("Choose tool", ["Home page",
                                        "FPS Calculator",
                                        "Spine Selector" ,
                                        "Paper Tune",
                                        "Creep Tuning",
                                        "Arrow Builder & FrontOfCenter (FOC)",
                                        "Kinetic energy",
                                        "Target Stabilizer setup",
                                        "Hunting Stabilizer setup"])
# ====================== END OF SIDEBAR ======================


if page == "Home page":
    st.header("Welcome to the TruMark- archery tuner!")
    st.write("Please, if you haven't already, input the correct ratings for your setup in the FPS CALCULATOR tool")


elif page == "FPS Calculator":
    st.header("FPS Calculator")

    # Vrednosti se zdaj berejo in shranjujejo direktno v obj
    lok.rating = st.number_input("IBO/ATA speed (FPS)", value=lok.rating)
    lok.weight = st.number_input("Bow weight (lbs)", value=lok.weight)
    lok.arrow = st.number_input("Arrow weight (grains)", value=lok.arrow)
    lok.string_weight = st.number_input("Added weight on the string (grains)", value=lok.string_weight)
    lok.poteg = st.number_input("Draw length (inch)", value=lok.poteg)

    total_arrow_weight = lok.arrow + lok.string_weight
    faktor_potega = (lok.poteg - 30) * 10

    predicted_fps = (lok.rating + faktor_potega - ((total_arrow_weight - (lok.weight * 5)) / 3)) - 3.5
    lok.dodaj_fps(predicted_fps)

    st.divider()
    st.success(f"Predicted FPS: {round(predicted_fps)} FPS")
    if lok.arrow // lok.weight < 5:
        st.warning("!!! TOO LIGHT OF AN ARROW, FOLLOW 5gr/pound")


elif page == "Spine Selector":
    st.header("Spine Selection Tool")

    puscica=st.selectbox("Choose the brand of the arrows in your setup",["GOLD TIP",
                                                                        "EASTON" ,
                                                                        "BLACK EAGLE",
                                                                        "VICTORY",
                                                                        "Carbon Express"]
                         )
    if st.button("Find your spine!") :
        if puscica == "GOLD TIP":
            if lok.fps > 315:
                st.image("gold_tip_nad_315.jpg")
            else:
              st.image("gold_tip_pod 315..jpg")

        elif puscica == "EASTON":
         st.image("easton_spine_chart.jpg")

        elif puscica == "BLACK EAGLE":
            st.image("BE_spine_chart.jpg")

        elif puscica == "VICTORY":
            st.image("VIC_spine_chart.jpg")

        elif puscica == "Carbon Express":
            st.image("CX_spine_chart.jpg")







elif page == "Paper Tune":
    st.header("Paper Tuning tool")
    st.warning("ALWAYS CHECK YOUR TIMING AND SPINE FIRST")
    st.write("Here you can setup your bow using paper tuning")
    st.write("YOU NEED: 2 arrows and some A4 paper")
    st.write("\n")

    levo_desno= st.selectbox("Are your arrow holes: NOCK",  ["LEFT", "RIGHT"])
    l_d_razdalja= st.slider("By how much? (mm)", 0, 150, 0)
    gor_dol= st.selectbox("Are your arrow holes: NOCK", ["HIGH", "LOW"])
    g_dol_razdalja = st.slider("By how much? (mm)",0,40, 0, key=1)


    if st.button("FIX YOUR TUNE:)"):

        col_a, col_b = st.columns(2)
        with col_a:
            if l_d_razdalja != 0:
                if l_d_razdalja < 6:
                    st.warning(f"Move your REST to the {levo_desno} by 1-2 turns")
                elif l_d_razdalja < 26:
                    st.warning(f"Twist your {levo_desno} yolk by 1-2twists")
                elif l_d_razdalja < 101:
                    st.warning(f"SHIM your CAM to the {levo_desno}")
                else:
                    st.warning(f"Check your arrow spine again or SHIM your CAM to the {levo_desno}")






        with col_b:
            if l_d_razdalja != 0:
                if g_dol_razdalja < 6:
                    st.warning(f"Move your REST {gor_dol} by 1-2 turns")
                elif l_d_razdalja < 21:
                    st.warning(f"Move your REST {gor_dol} by 3-4 turns")
                else:
                    st.warning(f"Check and adjust your NOCKING point HEIGHT")
                    if gor_dol == "HIGH":
                        st.warning("LOWER your nocking point")
                    else:
                        st.warning("Move your nocking point UP")










elif page == "Creep Tuning":
    st.header("Creep Tuning")
    st.write("Input the differance in the impact point")

    normal = st.number_input("Normal shot", value=0.0)
    hard = st.number_input(" Strong shot", value=0.0)

    if st.button("Analyze"):
        diff = hard - normal
        if diff > 0.5:
            st.warning("Add twists to the upper cable.")
        elif diff < -0.5:
            st.warning("Add twists to the lower cable.")
        else:
            st.balloons()
            st.success("Perfect :)")

elif page == "Arrow Builder & FrontOfCenter (FOC)":
    st.header("Front of Center (FOC)")
    st.write("1. Measure (in inches) from the throat of the nock to the end of the shaft.")
    st.write(
        "2. Find the balance point of the shaft (with components installed) and measure from the throat of the nock to said balance point.")

    dolzina = st.number_input("Measured length (L)", value=30.0, step=0.1)
    balance = st.number_input("The balance point of the arrow (ABP)", value=0.0, step=0.1)

    st.divider()
    teza_na_gr= st.number_input("Shaft weight (GR per INCH)",value=8.3)
    spica= st.number_input("Point weight (GR)",value= 120)
    point_insert= st.number_input("Point insert weight (GR)", value=0)
    nock= st.number_input("Nock weight (GR)", value=4.5)
    pero_gr= st.number_input("Weight of a single vane", value=10.5)
    st_peres= st.slider("Select the number of vanes",2,8,3)
    wrap= st.number_input("Wrap weight (leave at 0 if none)", value= 0.0)

    lok.arrow= round(teza_na_gr*dolzina+spica+point_insert+nock+pero_gr*st_peres+wrap, 2)

    if st.button("Calculate weight of the arrow"):
        st.write(f"Arrow weight is {lok.arrow}")

    if st.button("Calculate FOC"):
        if dolzina > 0 and balance > 0:
            foc_result = ((balance / dolzina) - 0.5) * 100

            st.divider()
            st.metric(label="Your Arrow FOC", value=f"{round(foc_result, 2)} %")

            if 8 <= foc_result <= 15:
                st.success("This is a great")
            elif foc_result < 8:
                st.warning("Low FOC: Your arrow might be unstable. Consider a heavier point.")
            else:
                st.info("High FOC: Great for penetration and stability, but expect more drop at distance.")
        else:
            st.error("Please enter values greater than 0.")

elif page == "Kinetic energy":

    game=[("Nothing...you should probably input correct ratings or get something stronger ¯\_(ツ)_/¯"),("Small game","ex. Rabbits, Small birds"), ("Medium game", "ex. White-tails / Antelopes ") , ("Large game","ex. Black bears,Elk") , ("Big game","ex. Grizzlies, Buffalo")]
    st.header("Kinetic energy")
    st.write("Here we calcuate the actual energy output that your setup will give out")
    ke = round((lok.arrow * lok.fps ** 2) / 450240,2)
    x=0

    st.warning(f"The bow outputs {ke} foot-pounds of energy")
    if ke<25:
        x=0
    elif ke>25 and ke<42:
        x=1
    elif ke > 42 and ke < 66:
        x=2

    elif ke > 66:
        x=3
    st.success(f"With your current setup you can hunt up to: {game[x]}")


elif page == "Target Stabilizer setup":
    st.header("TARGET/3D setup")
    Stil = st.slider("Please slide to where you want your bow to be (snappy - steady)", 0.5, 1.5, 1.0, step=0.01)

    sprednji_dolzina = st.number_input("Input the length of the FRONT rod", 6, 42, 30)
    zadnja_dolzina = st.number_input("Input the length of the BACK rod", 1, 42, 12)
    stevilo_back_rod = st.selectbox("How many side-rods are you running?", [1, 2])
    ATA = st.number_input("Input the ATA (AXLE to AXLE) of your bow", 29, 42, 40)
    riser_opcija=st.select_slider("select your riser geometry", ["REFLEX", "DEFLEX"], "REFLEX" )

    if st.button("What is REFLEX / DEFLEX?"):
        col_a, col_b = st.columns(2)
        with col_a:
            st.write("REFLEX")
            st.image("SUPRA_X_REFLEX.jpg")

        with col_b:
            st.write("DEFLEX")
            st.image("DOMINATOR_DUO_X_DEFLEX.jpg")


    if st.button("Calculate"):
        base = 7.5 * (ATA / 40) * Stil  # Base around 7.5 oz at 37 ATA

        sprednja_teza = round(base * (30 / sprednji_dolzina) ** 0.6, 1)

        sprednji_moment = sprednja_teza * sprednji_dolzina

        zadnja_teza_total = round(sprednji_moment / zadnja_dolzina, 1)

        if riser_opcija == "DEFLEX":
            sprednja_teza = round(1.2 * sprednja_teza, 1)

        if stevilo_back_rod == 2:
            zadnja_teza_per_bar = round(zadnja_teza_total / 2, 1)
        else:
            zadnja_teza_per_bar = zadnja_teza_total

        st.warning("LET-OFF calculations are made to make your setup HEAVIER the less % you have!!")
        let_ja_ne = st.radio("Include let off in the calculations?", ["NO", "YES"])
        if let_ja_ne == "YES":
            let_off = st.slider("letoff %", 60, 90, 75)
            let_off_multiplajr = 1.08 - (let_off - 75) * 0.0075
            napis_let_off = f"{let_off}% included in the calculations"
        else:
            let_off_multiplajr = 1.0
            napis_let_off = ""
        st.subheader("Recommended Weights")

        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric("Front Stabilizer", f"{sprednja_teza} oz", )
        with col_b:
            st.metric("Back Bar (each)", f"{zadnja_teza_per_bar} oz", )
        with col_c:
            st.metric("Total Back Weight", f"{zadnja_teza_total} oz")




elif page == "Hunting Stabilizer setup":
    st.header("Hunting setup")
    #Stil = st.slider("Please slide to where you want your bow to be (snappy - steady)", 0.5, 1.5, 1.0, step=0.01)


    sprednji_dolzina = st.number_input("Input the length of the FRONT rod", 6, 15, 12)
    zadnja_dolzina = st.number_input("Input the length of the BACK rod", 1, 15, 12)
    stevilo_back_rod = st.selectbox("How many side-rods are you running?", [None ,1, 2])
    ATA = st.number_input("Input the ATA (AXLE to AXLE) of your bow", 27, 36, 32)
    riser_opcija=st.select_slider("select your riser geometry", ["REFLEX", "DEFLEX"], "REFLEX" )

    if st.button("What is REFLEX / DEFLEX?"):
        col_a, col_b = st.columns(2)
        with col_a:
            st.write("REFLEX")
            st.image("SUPRA_X_REFLEX.jpg")

        with col_b:
            st.write("DEFLEX")
            st.image("DOMINATOR_DUO_X_DEFLEX.jpg")


    namen_setup=st.selectbox("What kind of hunting?", ["On the field", "From a blind (turkey hunting)", "From a tree stand", "Closed hunting stand"])
    x=1
    if namen_setup== "On the field":
        x=1
    elif namen_setup== "From a blind":
        x=0.80
    elif namen_setup== "From a tree stand":
        x=0.65
    elif namen_setup== "Closed hunting stand":
        x=0.75
    st.warning("LET-OFF calculations are made to make your setup HEAVIER the less % you have!!")
    let_ja_ne = st.radio("Include let off in the calculations?", ["NO", "YES"])
    if let_ja_ne == "YES":
        let_off = st.slider("letoff %", 60, 90, 75)
        let_off_multiplajr = 1.08 - (let_off - 75) * 0.0075
        napis_let_off = f"{let_off}% included in the calculations"
    else:
        let_off_multiplajr = 1.0
        napis_let_off= ""

    if st.button("Calculate"):

        base = (5 * (ATA / 34) )
               # * Stil# Base around 7.5 oz at 37 ATA

        sprednja_teza = round(base * (15 / sprednji_dolzina) ** 0.6 * let_off_multiplajr* x, 1)

        sprednji_moment = sprednja_teza * sprednji_dolzina

        zadnja_teza_total = round(sprednji_moment / zadnja_dolzina, 1)

        if riser_opcija == "DEFLEX":
            sprednja_teza = round(1.25 * sprednja_teza, 1)

        if stevilo_back_rod == 2:
            zadnja_teza_per_bar = round(zadnja_teza_total / 2, 1)
        else:
            zadnja_teza_per_bar = zadnja_teza_total



        st.subheader("Recommended Weights")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric("Front Stabilizer", f"{sprednja_teza} oz",delta=napis_let_off)
        with col_b:
            st.metric("Back Bar (each)", f"{zadnja_teza_per_bar} oz",  delta=napis_let_off)
        with col_c:
            st.metric("Total Back Weight", f"{zadnja_teza_total} oz")



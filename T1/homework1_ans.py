minimum_score_to_accept = 14
st1_info = ["5.Reza Kadkhodaei Miandoabi", 986432, [13.5 ,15.6, 14.0]]
st2_info = ["17.Shahab Hosseinalizadeh", 986548, [18.2, 15.9, 11.9]]
st3_info = ["23.Negar Nabizadeh Estalkhkoohi", 986953, [19.4 ,7.0, 14]]

st1_name = st1_info[0][2:6]
st2_name = st2_info[0][3:9]
st3_name = st3_info[0][3:8]

st1_family = st1_info[0][7:-10]
st2_family = st2_info[0][10:]
st3_fimily = st3_info[0][9:-14]

st1_mean = (st1_info[2][0] + st1_info[2][1] + st1_info[2][2])/3
st2_mean = (st2_info[2][0] + st2_info[2][1] + st2_info[2][2])/3
st3_mean = (st3_info[2][0] + st3_info[2][1] + st3_info[2][2])/3

st1_accepted = st1_mean > minimum_score_to_accept
st2_accepted = st2_mean > minimum_score_to_accept
st3_accepted = st2_mean > minimum_score_to_accept

print("")
if st1_accepted and st2_accepted and st3_accepted:
    print("Class level is high")
elif st1_accepted or st2_accepted or st3_accepted:
    print("Class level is middle")
else:
    print("Class level is low")

print("")
if st1_mean > st2_mean and st1_mean > st3_mean:
    print(st1_name + " " + st1_family + " is the best student")
elif st2_mean > st1_mean and st2_mean > st3_mean:
    print(st2_name + " " + st2_family + " is the best student")
elif st3_mean > st1_mean and st3_mean > st2_mean:
    print(st3_name + " " + st3_family + " is the best student")

all_data = [st1_info, st2_info, st3_info]

print(all_data)

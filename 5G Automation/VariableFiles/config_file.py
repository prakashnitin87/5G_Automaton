#Attach messages
message_1 = 'Random Access Preamble Transmission - msg1'
message_2 = 'Random Access Response Report - msg2\n'
message_3 = 'UE Identification Message Report - msg3'
message_4 = 'Contention Resolution Message Report - msg4'

# locker path
dir_path = "G:\TestCases"
loc_path = "G:\TestCases\Locker"

#path for UE and gNB
ue_path = r"G:\TestCases\Locker\UE"
gNB_path = r"G:\TestCases\Locker\gNB"
path1 = r"G:\TestCases\Locker\UE\Request.txt"
path2 = r"G:\TestCases\Locker\gNB\Response.txt"

#path for validation
path3 = r"G:\TestCases\Locker\UE\Response.txt"
path4 = r"G:\TestCases\Locker\gNB\Request.txt"

#password for locker
pw = "nitin"
pw1 = "nitin"

#path for PLMNs
path = 'G:/PLMNs'
ref = "-90dBm"

#path for Emergency call
src1 = "G:/TestCases/Locker/UE/PDN_request.txt"
des1 = "G:/TestCases/Locker/Proxy"

#Criteria for Cell selection
sib1_msg = 'Srxlev > 0 and Squal > 0'

#values
Sintrasearchp = "-80dBm"
Sintrasearchq = "-20dB"
Qhyst = "0"
Qmeas = "-82dBm"
Qmean = "-85dBm"
Qoff = "0"
Qofft = "0"
Srxlev = "-92dBm"
Squal = "-30dB"

#Condition for Cell reselection triggering
cond_1 = "Srxlev > Sintrasearchp and Squal > Sintrasearchq"
cond_2 = "Srxlev < Sintrasearchp and Squal < Sintrasearchq"

#Criteria for Cell Ranking
Rs = "Qmeas + Qhyst - Qofft"
Rn = "Qmean - Qoff - Qofft"

#Criteria for Intra-frequency Cell Reselection
cond_3 = "Rn > Rs"

#path for intra-frequency cell reselection
src2 = "G:/TestCases/Locker/UE/SIB.txt"
des2 = "G:/TestCases/Locker/gNB"
sib = "G:/TestCases/Locker/gNB/SIB.txt"
src3 = "G:/TestCases/Locker/UE/Reselection_criteria.txt"
resel_msg = "G:/TestCases/Locker/gNB/Reselection_criteria.txt"
Rs_path = "G:/TestCases/Locker/UE/Rs.txt"

#folder Path for Handover
ue = r"G:\TestCases\Locker\Handover\UE"
cell_a = r"G:\TestCases\Locker\Handover\Source gNB\Cell_A"
cell_b = r"G:\TestCases\Locker\Handover\Target gNB\Cell_B"
amf = r"G:\TestCases\Locker\Handover\AMF"
smf = r"G:\TestCases\Locker\Handover\SMF"

#msg paths
msg_3 = r"G:\TestCases\Locker\Handover\Source gNB\Cell_A\gNB config.txt"
msg_9 = r"G:\TestCases\Locker\Handover\Source gNB\Cell_A\HO_req.txt"
msg_1 = r"G:\TestCases\Locker\Handover\Source gNB\Cell_A\meas_control.txt"
msg_11 = r"G:\TestCases\Locker\Handover\Source gNB\Cell_A\RRC.txt"
msg_7 = r"G:\TestCases\Locker\Handover\Source gNB\Cell_A\Xn_request.txt"
msg_5 = r"G:\TestCases\Locker\Handover\Target gNB\Cell_B\gNB_Config.txt"
msg_10 = r"G:\TestCases\Locker\Handover\Target gNB\Cell_B\HO_response.txt"
msg_13 = r"G:\TestCases\Locker\Handover\Target gNB\Cell_B\Rach_response.txt"
msg_14 = r"G:\TestCases\Locker\Handover\Target gNB\Cell_B\Xn_path.txt"
msg_8 = r"G:\TestCases\Locker\Handover\Target gNB\Cell_B\Xn_response.txt"
msg_2 = r"G:\TestCases\Locker\Handover\UE\measurement_report.txt"
msg_12 = r"G:\TestCases\Locker\Handover\UE\Rach_req.txt"
msg_4 = r"G:\TestCases\Locker\Handover\AMF\amf_config.txt"
msg_6 = r"G:\TestCases\Locker\Handover\AMF\amf_config2.txt"
msg_15 = r"G:\TestCases\Locker\Handover\AMF\bearer_req.txt"
msg_16 = r"G:\TestCases\Locker\Handover\SMF\bearer_response.txt"
msg_17 = r"G:\TestCases\Locker\Handover\AMF\Xn_path_Response.txt"

*** Settings ***
Library     os
Resource    ${EXEC_DIR}/Res/attach_keyword.robot
Variables   ${EXEC_DIR}/VariableFiles/config_file.py
Library     ${EXEC_DIR}/Lib/attach_function.py

*** Test Cases ***

TC_attach_1.2: RACH_Procedure
     Unlock a Window Folder
     Moving UE files to gNB folder
     Moving gNB files to UE folder
     RACH Request Validation
     RACH Response Validation
     Lock a Window Folder


TC_attach_1.8: Emergency_Call
     Emergency_callsetup

TC_attach_1.22: Intra-frequency cell reselection
     Intra_frequency cell reselection

TC_attach_1.29: PLMN_selected manually
     PLMN selection

TC_Handover_1.17: Handover during VONR call
     VONR_Handover
     Handover_validation

TC_Handover_1.18: Handover during VOIP call
     VOIP_Handover
     Source_gNB_Vaidation
     Target_gNB_Validation
     NGC_1_Core_Validation
     NGC-2_Core_Validation

TC_Handover_1.19: Handover failure during active call
     Radio link failure
     gNB Vaildation
     amf validation
     ue validation




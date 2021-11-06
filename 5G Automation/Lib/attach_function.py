import os
import sys
sys.path.insert(0, r"C:\Users\Dell\PycharmProjects\5G Automation\VariableFiles")
import config_file
import shutil

class attach_function:

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        pass

    def unlock(self):

        # Unlock the folder
        pw = config_file.pw

        # while True:
        pw1 = config_file.pw1
        if pw1 == pw:
            os.chdir(config_file.dir_path)
            if not os.path.exists(config_file.loc_path):
                if not os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}"):
                    os.mkdir("Locker")
                    print("Locker Folder Successfully created")

                else:
                    os.popen('attrib -h -s -r Locker')
                    os.rename("Locker.{645ff040-5081-101b-9f08-00aa002f954e}", "Locker")
                    print("Locker Folder has been Successfully Unlocked")
                    # break

            else:
                print("Locker folder is not LOCKED")

        else:
            print("wrong password! Try again later")

    def mov_ue2gnb(self):
        try:
            src = r"G:\TestCases\Locker\UE\Request.txt"
            des = r"G:\TestCases\Locker\gNB"
            shutil.move(src, des)
            print('Move UE -> gNB')
        except shutil.Error:
            print('gNB: File already exist')

    def mov_gnb2ue(self):
        try:
            src = r'G:\TestCases\Locker\gNB\Response.txt'
            des = r"G:\TestCases\Locker\UE"
            shutil.move(src, des)
            print('Move gNB -> UE')
        except shutil.Error:
            print('UE: File already exist')

    def validate_gnb(self):
        path = r"G:\TestCases\Locker\gNB\Request.txt"
        if not path:
            return 'gNB: No such file exits'
        req_file = open(path, 'r')
        if 'Random Access Preamble Transmission - (Msg1)' and 'UE Identification Message Report - (Msg3)':
            print('Validation for gnb is Successful')
        else:
            print('Validation is Unsuccessful')

    def validate_ue(self):
        path = r"G:\TestCases\Locker\UE\Response.txt"
        if not path:
            return 'UE: No such file exits'
        req_file = open(path, 'r')
        if 'Random Access Response Report - (Msg2)' and 'Contention Resolution Message Report - (Msg4)':
            print('Validation for UE is Successful')
        else:
            print('Validation is Unsuccessful')

    def as_search(self):
        path = config_file.path
        ref = config_file.ref
        for file in os.listdir(path):

            plmn = open(path+'/'+file ,"r")
            read_file = plmn.read()
            if ref in read_file:
                print(file)
                print('UE has successfully selected PLMN')

    def move_pdn(self):
        src1 = config_file.src1
        des1 = config_file.des1
        shutil.move(src1, des1)
        print('file move successfully')
        path = "G:/TestCases/Locker/Proxy/PDN_request.txt"

        file = open(path ,"r")
        file_read = file.read()
        if 'Dial 911' in file_read:
            print('Emergency call successful')
        else:
            print('Not Successful')

    def sib2(self):
        src2 = config_file.src2
        des2 = config_file.des2
        shutil.move(src2, des2)
        print('SIB msg moved to gNB')
        path = config_file.sib
        file = open(path, "r")
        file_read = file.read()
        if 'Srxlev > 0 and Squal > 0' in file_read:
            print('Cell selection successfull')
        else:
            print('Cell Selection not successful')

        #Cell Reselection Criteria

        src3 = config_file.src3
        des3 = config_file.des2
        shutil.move(src3, des3)
        print('File moved successfully')
        path = config_file.resel_msg
        file = open(path, "r")
        file_read = file.read()
        if 'Srxlev < Sintrasearchp and Squal < Sintrasearchq' in file_read:
            print('Cell reselection criteria successful and searching for neighbour cells')
        else:
            print('Cell reselection criteria not successful')


        #Measurement Report of neighbouring cells

        RSRPn = [-105,-100,-110,-95,-97]
        Rn = sorted(RSRPn, reverse=True)
        print(Rn)

        #Compairing the Serving cell and neighbouring cell

        path = config_file.Rs_path
        Rs = open(path, "r")
        Rs_read = Rs.read()
        Rs_read = int(Rs_read)
        if Rs_read < Rn[0]:
            print('Neighbour cell is selected')
        else:
            print('Stay on serving cell')

    # HANDOVER TestCases

    def inter_cellHO(self):
        cell_a = config_file.msg_1
        ue = config_file.ue
        shutil.move(cell_a, ue)

        ue = config_file.msg_2
        cell_a = config_file.cell_a
        shutil.move(ue, cell_a)

        cell_a = config_file.msg_3
        amf = config_file.amf
        shutil.move(cell_a, amf)

        amf = config_file.msg_4
        cell_b = config_file.cell_b
        shutil.move(amf, cell_b)

        cell_b = config_file.msg_5
        amf = config_file.amf
        shutil.move(cell_b, amf)

        amf = config_file.msg_6
        cell_a = config_file.cell_a
        shutil.move(amf, cell_a)

        cell_a = config_file.msg_7
        cell_b = config_file.cell_b
        shutil.move(cell_a, cell_b)

        cell_b = config_file.msg_8
        cell_a = config_file.cell_a
        shutil.move(cell_b, cell_a)

        cell_a = config_file.msg_9
        cell_b = config_file.cell_b
        shutil.move(cell_a, cell_b)

        cell_b = config_file.msg_10
        cell_a = config_file.cell_a
        shutil.move(cell_b, cell_a)

        cell_a = config_file.msg_11
        ue = config_file.ue
        shutil.move(cell_a, ue)

        ue = config_file.msg_12
        cell_b = config_file.cell_b
        shutil.move(ue, cell_b)

        cell_b = config_file.msg_13
        ue = config_file.ue
        shutil.move(cell_b, ue)

        cell_b = config_file.msg_14
        amf = config_file.amf
        shutil.move(cell_b, amf)

        amf = config_file.msg_15
        smf = config_file.smf
        shutil.move(amf, smf)

        smf = config_file.msg_16
        amf = config_file.amf
        shutil.move(smf, amf)

        amf = config_file.msg_17
        cell_b = config_file.cell_b
        shutil.move(amf, cell_b)

    #def validate_ue(self):






    def vonr(self):
        ue = r"G:\TestCases\Locker\UE\Meas_rep.txt"
        gnb1 = r"G:\TestCases\Locker\gNB"
        shutil.move(ue, gnb1)
        print('Measurement report sent')

        #gnb1 to gnb2
        gnb1 = r"G:\TestCases\Locker\gNB\req.txt"
        gnb2 = r"G:\TestCases\Locker\Target gNB"
        shutil.move(gnb1, gnb2)
        print('request message sent to target gNB')

        #gnb1 to ue
        gnb1 = r"G:\TestCases\Locker\gNB\HO_req.txt"
        ue = r"G:\TestCases\Locker\UE"
        shutil.move(gnb1, ue)
        print('HO request sent')

        #ue to gnb2
        ue = r"G:\TestCases\Locker\UE\HO2gnb2.txt"
        gnb2 = r"G:\TestCases\Locker\Target gNB"
        shutil.move(ue, gnb2)
        print('HO to gNB2')

        #gnb2 to gnb1
        gnb2 = r"G:\TestCases\Locker\Target gNB\context_rel.txt"
        gnb1 = r"G:\TestCases\Locker\gNB"
        shutil.move(gnb2, gnb1)
        print('UE is connected_please release context')

    def validation(self):
        path = r"G:\TestCases\Locker\UE\HO_req.txt"
        file = open(path,"r")
        file_read = file.read()
        if 'Handover to gNB2' in file_read:
            print('Validation for ue is successfull')
        else:
            print('Validation is unsuccessfull')

            #validation for gnb1

        path = r"G:\TestCases\Locker\gNB\Meas_rep.txt"
        file = open(path, "r")
        file_read = file.read()
        if 'Mesurement report of gNB1' in file_read:
            print('Validation for gnb1 is successfull')
        else:
            print('Validation is unsuccessfull')

        path = r"G:\TestCases\Locker\gNB\context_rel.txt"
        file = open(path, "r")
        file_read = file.read()
        if 'Release context information' in file_read:
            print('Validation for gnb1 is successfull')
        else:
            print('Validation is unsuccessfull')

            #Validation for gnb2
        path = r"G:\TestCases\Locker\Target gNB\req.txt"
        file = open(path, "r")
        file_read = file.read()
        if 'Ok for Handover' in file_read:
            print('Validation for gnb2 is successfull')
        else:
            print('Validation is unsuccessfull')

        path = r"G:\TestCases\Locker\Target gNB\HO2gnb2.txt"
        file = open(path, "r")
        file_read = file.read()
        if 'are you ready for handover' in file_read:
            print('Validation for gnb2 is successfull')
        else:
            print('Validation is unsuccessfull')

    #HANDOVER during VOIP Calls

    def voip(self):
        ue = r"G:\TestCases\Locker\UE\Meas_rep.txt"
        gnb1 = r"G:\TestCases\Locker\gNB"
        shutil.move(ue, gnb1)
        print('Measurement report sent')

        #gnb1 to 5gc1
        gnb1 = r"G:\TestCases\Locker\gNB\req.txt"
        ngc1 = r"G:\TestCases\Locker\5GC_1"
        shutil.move(gnb1, ngc1)
        print('Req msg sent to 5GC_1')

        #5gc1 t0 5gc2
        ngc1 = r"G:\TestCases\Locker\5GC_1\HO_req.txt"
        ngc2 = r"G:\TestCases\Locker\5GC_2"
        shutil.move(ngc1, ngc2)
        print('Req msg sent to 5GC_2')

        #5gc2 to gnb2
        ngc2 = r"G:\TestCases\Locker\5GC_2\Handover_req.txt"
        gnb2 = r"G:\TestCases\Locker\Target gNB"
        shutil.move(ngc2, gnb2)
        print('request message sent to target gNB')

        #5gc1 to gnb1
        ngc1 = r"G:\TestCases\Locker\5GC_1\HO_res.txt"
        gnb1 = r"G:\TestCases\Locker\gNB"
        shutil.move(ngc1, gnb1)
        print('Response msg sent to gNB')

        #ue to gnb2
        ue = r"G:\TestCases\Locker\UE\HO2gnb2.txt"
        gnb2 = r"G:\TestCases\Locker\Target gNB"
        shutil.move(ue, gnb2)
        print('HO to gNB2')

        #gnb2 to 5gc2
        gnb2 = r"G:\TestCases\Locker\Target gNB\Handover_Res.txt"
        ngc2 = r"G:\TestCases\Locker\5GC_2"
        shutil.move(gnb2, ngc2)
        print('UE is connected')

        #5gc1 to gnb1
        ngc1 = r"G:\TestCases\Locker\5GC_1\Cntxt_rel.txt"
        gnb1 = r"G:\TestCases\Locker\gNB"
        shutil.move(ngc1, gnb1)
        print('UE is connected_please release context')

    def val_gNB1(self):
        path = r"G:\TestCases\Locker\gNB\Meas_rep.txt"
        file = open(path, "r")
        file_read = file.read()
        if 'Mesurement report of gNB1' in file_read:
            print('Validation for gnb1 is successfull')
        else:
            print('Validation is unsuccessfull')

        path = r"G:\TestCases\Locker\gNB\HO_res.txt"
        file = open(path, "r")
        file_read = file.read()
        if 'Tell UE to connect to gNB2' in file_read:
            print('Validation for gnb1 is successfull')
        else:
            print('Validation is unsuccessfull')

        path = r"G:\TestCases\Locker\gNB\Cntxt_rel.txt"
        file = open(path, "r")
        file_read = file.read()
        if 'HO Succeeded Release UE context' in file_read:
            print('Validation for gnb1 is successfull')
        else:
            print('Validation is unsuccessfull')

    def val_gNB2(self):
        path = r"G:\TestCases\Locker\Target gNB\Handover_req.txt"
        file = open(path, "r")
        file_read = file.read()
        if 'UE wants to connect Ok for HO' in file_read:
            print('Validation for gnb2 is successful')
        else:
            print('Validation is unsuccessful')

        path = r"G:\TestCases\Locker\Target gNB\HO2gnb2.txt"
        file = open(path, "r")
        file_read = file.read()
        if 'are you ready for handover' in file_read:
            print('Validation for gnb2 is successfull')
        else:
            print('Validation is unsuccessfull')

    def val_5GC1(self):
        path =  r"G:\TestCases\Locker\5GC_1\req.txt"
        file = open(path, "r")
        file_read = file.read()
        if 'Ok for Handover' in file_read:
            print('Validation for 5GC_1 is successful')
        else:
            print('Validation is unsuccessful')

    def val_5GC2(self):
        path = r"G:\TestCases\Locker\5GC_2\HO_req.txt"
        file = open(path, "r")
        file_read = file.read()
        if 'Is it ok for Handover' in file_read:
            print('Validation for 5GC_2 is successful')
        else:
            print('Validation is unsuccessful')

        path = r"G:\TestCases\Locker\5GC_2\Handover_Res.txt"
        file = open(path, "r")
        file_read = file.read()
        if 'UE is connected' in file_read:
            print('Validation for 5GC_2 is successful')
        else:
            print('Validation is unsuccessful')

    #Radio link failure

    def rlf(self):
        ue = r"G:\TestCases\Locker\UE\message_1.txt"
        gNB = r"G:\TestCases\Locker\Target gNB"
        shutil.move(ue, gNB)
        print('message sent successfully')

        gNB = r"G:\TestCases\Locker\Target gNB\HO_fail.txt"
        amf = r"G:\TestCases\Locker\AMF"
        shutil.move(gNB, amf)
        print('RLF failure')

        gNB = r"G:\TestCases\Locker\Target gNB\message_2.txt"
        ue = r"G:\TestCases\Locker\UE"
        shutil.move(gNB, ue)
        print('Reestablishment response message')

    def val_gNB(self):
        path = r"G:\TestCases\Locker\Target gNB\message_1.txt"
        file = open(path, "r")
        file_read = file.read()
        if 'RLM and signal quality report' and 'RRC Connection Reestablishment request' and 'Reestablishment complete' in file_read:
            print('Validation for gNB is successful')
        else:
            print('Validation is unsuccessful')

    def val_amf(self):
        path = r"G:\TestCases\Locker\AMF\HO_fail.txt"
        file = open(path, "r")
        file_read = file.read()
        if 'Preparation of Resource failed Handover failed' in file_read:
            print('Validation for amf is successful')
        else:
            print('Validation is unsuccessful')

    def val_ue(self):
        path = r"G:\TestCases\Locker\UE\message_2.txt"
        file = open(path, "r")
        file_read = file.read()
        if 'RRC Connection reestablishment response message' in file_read:
            print('Validation for ue is successful')
        else:
            print('Validation is unsuccessful')

























    def lock(self):  # lock the folder

        p_w = config_file.pw

        # while True:
        pw1 = config_file.pw1
        if p_w == pw1:
            os.chdir(config_file.dir_path)
            # print("Your path Successfully Changed")
            # If Locker folder or Recycle bin does not exist then we will be create Locker Folder

            if os.path.exists(config_file.loc_path):
                os.rename("Locker", "Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
                os.popen('attrib +h +s +r Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
                print("Locker folder has been successfully locked")
                # sys.exit()
                # break

            else:
                os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
                os.mkdir("Locker")
                print("Locker Folder Successfully created")
                os.rename("Locker", "Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
                os.popen('attrib +h +s +r Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
                print("Locker folder has been successfully locked")
                # break

        else:
            print("wrong password! Try again later")

            # break

np = attach_function
#np.unlock(None)
#np.mov_ue2gnb(None)
#np.mov_gnb2ue(None)
#np.validate_gnb(None)
#np.validate_ue(None)
#np.lock(None)
#np.as_search(None)
#np.move_pdn(None)
#np.sib2(None)
#np.vonr(None)
#np.validation(None)
#np.voip(None)
#np.val_gNB1(None)
#np.val_gNB2(None)
#np.val_5GC1(None)
#np.val_5GC2(None)
#np.rlf(None)
#np.val_gNB(None)
#np.val_amf(None)
#np.val_ue(None)

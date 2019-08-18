import requests
import xml.etree.ElementTree as ET 
import os

def mk_elec_lawlist():
    elec_lawname = [
        r'電気事業法',
        r'電気事業法施行令',
        r'電気事業法施行規則',
        r'電気設備に関する技術基準を定める省令',
        r'電気設備の技術基準の解釈',
        r'電気関係報告規則',
        r'電気工事士法',
        r'電気工事士法施行令',
        r'電気工事士法施行規則',
        r'電気工事業の業務の適正化に関する法律',
        r'電気工事業の業務の適正化に関する法律施行令',
        r'電気工事業の業務の適正化に関する法律施行規則',
        r'電気用品安全法',
        r'電気用品安全法施行令',
        r'電気用品安全法施行規則',
        r'労働安全衛生法',
        r'労働安全衛生法施行令',
        r'消防法',
        r'消防法施行令',
        r'消防法施行規則'
    ]

    return elec_lawname


# e-Govから法令の一覧を取得
def get_lawlist(path_lawlist):
    url_lawlist = 'https://elaws.e-gov.go.jp/api/1/lawlists/1' # api/{Version}/lawdata/{法令番号}

    with requests.get(url_lawlist) as res_lawlist:
        print(res_lawlist.status_code)

        with open(path_lawlist, 'w') as f_lawlist:
            f_lawlist.write(res_lawlist.text)


# 法令一覧から目的の法令の法令番号を調べる
def mk_LawName_LawNo_list(path_lawlist):
    ET_root = ET.parse(path_lawlist)
    ET_root = ET_root.getroot()
    list_all_LawName = [i.text for i in ET_root.findall('.//LawName')]
    list_all_LawNo = [i.text for i in ET_root.findall('.//LawNo')]
    list_elec_lawname = mk_elec_lawlist()

    list_LawName = []
    list_LawNo = []
    for i_elec_law in list_elec_lawname:
        if i_elec_law in list_all_LawName:
            num_LawName_index = list_all_LawName.index(i_elec_law)
            str_LawName = list_all_LawName[num_LawName_index]
            str_LawNo = list_all_LawNo[num_LawName_index]
            # print(str_LawName)
            # print(str_LawNo)
            list_LawName.append(str_LawName)
            list_LawNo.append(str_LawNo)

    return list_LawName, list_LawNo


# 法令番号をもとにe-Govから法令の本文を取得
def get_lawdata(law_name, law_num):
    os.mkdir('law_xml')

    for i_loop, i_lawdata in enumerate(law_num):
        path_lawname = 'law_xml/' + law_name[i_loop] + '.xml'
        lawdata_url = 'https://elaws.e-gov.go.jp/api/1/lawdata/'+i_lawdata

        with requests.get(lawdata_url) as res_lawdata:
            print(res_lawdata.status_code)

            with open(path_lawname, 'w') as f_lawname:
                f_lawname.write(res_lawdata.text)


def main():
    path_lawlist = 'lawlist.xml'
    # get_lawlist(path_lawlist)
    law_name, law_num = mk_LawName_LawNo_list(path_lawlist)

    get_lawdata(law_name, law_num)


if __name__ == '__main__':
    main()


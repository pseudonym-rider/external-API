import requests
import xml.etree.ElementTree as ElementTree

license_num = input();

def call():
    URL = "https://teht.hometax.go.kr/wqAction.do?actionId=ATTABZAA001R08&screenId=UTEABAAA13&popupYn=false&realScreenId"
    payload = '<map id="ATTABZAA001R08"><pubcUserNo/><mobYn>N</mobYn><inqrTrgtClCd>1</inqrTrgtClCd><txprDscmNo>' + license_numd + '</txprDscmNo><dongCode>24</dongCode><psbSearch>Y</psbSearch><map id="userReqInfoVO"/></map><nts<nts>nts>29c4GV6socWM7xjDgh5wQzEBVHYC4ZMSsrDHL2CGWIYQ18'
    res = requests.post(URL, data=payload, headers={'Content-Type': 'text/xml'})
    xml = ElementTree.fromstring(res.text).findtext("trtCntn")
    result =  xml.replace("\n","").replace("\t", " ") + "\n"
    return result

print(call())
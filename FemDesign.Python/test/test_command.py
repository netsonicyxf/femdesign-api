from femdesign.calculate.command import *
from femdesign.calculate.analysis import Analysis, CombSettings

def test_cmd_open():
    file_path = "myFilePath.str"
    xmlCmdOpen = CmdOpen(file_path).to_xml_element()

    assert xmlCmdOpen.tag == "cmdopen"
    assert xmlCmdOpen.attrib.get("command") == "; CXL CS2SHELL OPEN"
    
    filename = xmlCmdOpen.find("filename")
    assert filename.text == os.path.join( os.getcwd(), file_path )
    
def test_cmd_child():
    file_path = "template.dsc"
    xmlCmdChild = CmdChild("template.dsc").to_xml_element()

    assert xmlCmdChild.tag == "cmdchild"
    assert xmlCmdChild.text == os.path.join( os.getcwd(), file_path)

    try:
        xmlCmdChild = CmdChild("template.3dm").to_xml_element()
    except Exception as e:
        assert isinstance(e, ValueError)
        assert str(e) == "file_name must have suffix .dsc"

def test_cmd_save():
    file_path = "myFilePath.str"
    xmlCmdSave = CmdSave(file_path).to_xml_element()

    assert xmlCmdSave.tag == "cmdsave"
    assert xmlCmdSave.attrib.get("command") == "; CXL CS2SHELL SAVE"
    
    filename = xmlCmdSave.find("filename")
    assert filename.text == os.path.join( os.getcwd(), file_path )

def test_cmd_user():
    for user in User:
        xmlCmdUser = CmdUser(user).to_xml_element()

        assert xmlCmdUser.attrib.get("command") == f"; CXL $MODULE {user.name}"
        assert xmlCmdUser.tag == "cmduser"

def test_cmd_end_session():
    xmlCmdEndSession = CmdEndSession().to_xml_element()

    assert xmlCmdEndSession.tag == "cmdendsession"
    assert xmlCmdEndSession.text == None
    assert xmlCmdEndSession.attrib == {}

def test_analysis():
    xmlAnalysis = Analysis.StaticAnalysis().to_xml_element()

    assert xmlAnalysis.tag == "analysis"

    assert xmlAnalysis.attrib.get("calcCase") == "1"
    assert xmlAnalysis.attrib.get("calcComb") == "1"
    assert xmlAnalysis.find("Comb") is None
    assert xmlAnalysis.attrib.get("calcStab") == "0"

    xmlAnalysis = Analysis.StaticAnalysis(True, True).to_xml_element()
    assert xmlAnalysis.attrib.get("calcCase") == "1"
    assert xmlAnalysis.attrib.get("calcComb") == "1"
    assert xmlAnalysis.find("comb") is None

    xmlAnalysis = Analysis.StaticAnalysis(True, False).to_xml_element()
    assert xmlAnalysis.attrib.get("calcCase") == "1"
    assert xmlAnalysis.attrib.get("calcComb") == "0"
    assert xmlAnalysis.find("comb") is None

    xmlAnalysis = Analysis.FrequencyAnalysis().to_xml_element()
    assert xmlAnalysis.attrib.get("calcFreq") == "1"
    assert xmlAnalysis.find("comb") is None
    assert xmlAnalysis.find("freq") is not None

def test_cmd_proj_descr():
    xmlCmdProjDescr = CmdProjDescr("Test project", "Test project description", "Test designer", "Test signature", "Comment", None).to_xml_element()

    xmlCmdProjDescr.tag == "cmdprojdescr"

    assert xmlCmdProjDescr.attrib.get("szProject") == "Test project"
    assert xmlCmdProjDescr.attrib.get("szDescription") == "Test project description"
    assert xmlCmdProjDescr.attrib.get("szDesigner") == "Test designer"
    assert xmlCmdProjDescr.attrib.get("szSignature") == "Test signature"
    assert xmlCmdProjDescr.attrib.get("szComment") == "Comment"

    assert xmlCmdProjDescr.attrib.get("read") == "0"
    assert xmlCmdProjDescr.attrib.get("reset") == "0"

    assert xmlCmdProjDescr.find("item") is None

    items = {"a": "a_txt", "b": "b_txt"}
    xmlCmdProjDescr = CmdProjDescr(None, None, None, None, None, items, 0, 0).to_xml_element()

    xmlCmdProjDescr.tag == "cmdprojdescr"

    assert xmlCmdProjDescr.attrib.get("szProject") == None
    assert xmlCmdProjDescr.attrib.get("szDescription") == None
    assert xmlCmdProjDescr.attrib.get("szDesigner") == None
    assert xmlCmdProjDescr.attrib.get("szSignature") == None
    assert xmlCmdProjDescr.attrib.get("szComment") == None

    assert xmlCmdProjDescr.attrib.get("read") == "0"
    assert xmlCmdProjDescr.attrib.get("reset") == "0"

    assert xmlCmdProjDescr.find("item") is not None
    assert len( xmlCmdProjDescr.findall("item") ) == 2

def test_cmd_listgen():
    xmlCmdListGen = CmdListGen("bscfile.bsc", "outfile.csv", None, True, True, True).to_xml_element()

    assert xmlCmdListGen.tag == "cmdlistgen"
    assert xmlCmdListGen.attrib.get("bscfile") == os.path.join( os.getcwd(), "bscfile.bsc" )
    assert xmlCmdListGen.attrib.get("outfile") == os.path.join( os.getcwd(), "outfile.csv" )
    assert xmlCmdListGen.attrib.get("regional") == "1"
    assert xmlCmdListGen.attrib.get("fillcells") == "1"
    assert xmlCmdListGen.attrib.get("headers") == "1"
    assert xmlCmdListGen.find("GUID") is None
    assert len( xmlCmdListGen.findall("GUID") ) == 0


    guids = [uuid.uuid4(), uuid.uuid4()]
    xmlCmdListGen = CmdListGen("result.bsc", "outfile.csv", guids, False, False, False).to_xml_element()

    assert xmlCmdListGen.tag == "cmdlistgen"
    assert xmlCmdListGen.attrib.get("bscfile") == os.path.join( os.getcwd(), "result.bsc" )
    assert xmlCmdListGen.attrib.get("outfile") == os.path.join( os.getcwd(), "outfile.csv" )
    assert xmlCmdListGen.attrib.get("regional") == "0"
    assert xmlCmdListGen.attrib.get("fillcells") == "0"
    assert xmlCmdListGen.attrib.get("headers") == "0"
    assert xmlCmdListGen.find("GUID") is not None
    assert len( xmlCmdListGen.findall("GUID") ) == 2

    xmlCmdListGen = CmdListGen("result.bsc").to_xml_element()

    assert xmlCmdListGen.tag == "cmdlistgen"
    assert xmlCmdListGen.attrib.get("bscfile") == os.path.join( os.getcwd(), "result.bsc" )
    assert xmlCmdListGen.attrib.get("outfile") == os.path.join( os.getcwd(), "result.csv" )
    assert xmlCmdListGen.attrib.get("regional") == "1"
    assert xmlCmdListGen.attrib.get("fillcells") == "1"
    assert xmlCmdListGen.attrib.get("headers") == "1"
    assert xmlCmdListGen.find("GUID") is None
    assert len( xmlCmdListGen.findall("GUID") ) == 0

def test_cmd_config():
    file_path = "config.xml"
    xmlCmdConfig = CmdConfig(file_path).to_xml_element()

    assert xmlCmdConfig.tag == "cmdconfig"
    assert xmlCmdConfig.attrib.get("file") == os.path.join( os.getcwd(), file_path )

def test_cmd_interaction_surface():
    guid = uuid.uuid4()
    
    xmlCmdInteractionSurface = CmdInteractionSurface(guid, "surface.txt", 0.0, False).to_xml_element()

    assert xmlCmdInteractionSurface.tag == "cmdinteractionsurface"
    assert xmlCmdInteractionSurface.attrib.get("guid") == str(guid)
    assert xmlCmdInteractionSurface.attrib.get("outfile") == os.path.join( os.getcwd(), "surface.txt" )
    assert xmlCmdInteractionSurface.attrib.get("offset") == "0.0"
    assert xmlCmdInteractionSurface.attrib.get("fUlt") == "false"

    xmlCmdInteractionSurface = CmdInteractionSurface(guid, "surface.txt", 5.2, True).to_xml_element()

    assert xmlCmdInteractionSurface.tag == "cmdinteractionsurface"
    assert xmlCmdInteractionSurface.attrib.get("guid") == str(guid)
    assert xmlCmdInteractionSurface.attrib.get("outfile") == os.path.join( os.getcwd(), "surface.txt" )
    assert xmlCmdInteractionSurface.attrib.get("offset") == "5.2"
    assert xmlCmdInteractionSurface.attrib.get("fUlt") == "true"
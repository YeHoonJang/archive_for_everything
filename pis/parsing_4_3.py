
import urllib.request
from bs4 import BeautifulSoup


def parsing(xml_file):
    # open xml file
    with open(xml_file, "r", encoding="utf8") as patent_xml:
        xml = patent_xml.read()

    soup = BeautifulSoup(xml, "lxml")
    # print(soup)


    # tag
    tag_name = [tag.name for tag in soup.find_all()]
    # print(tag_name)
    # print(tag_name)




    # Conver xml to dict by using xmltodict
    import pprint
    import xmltodict
    doc = xmltodict.parse(xml)

    # pprint.pprint(doc)



    # 050104 xml file
    # 변수 설정


    patent_country = doc['us-patent-grant']['@country']
    upg_date_produced = doc['us-patent-grant']['@date-produced']
    upg_date_publ = doc['us-patent-grant']['@date-publ']
    upg_dtd = doc['us-patent-grant']['@dtd-version']
    upg_file = doc['us-patent-grant']['@file']
    upg_id = doc['us-patent-grant']['@id']
    upg_lang = doc['us-patent-grant']['@lang']
    upg_status = doc['us-patent-grant']['@status']
    ubdg_publ_doc_id_country = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['publication-reference']['document-id']['country']
    ubdg_publ_doc_id_doc_number = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['publication-reference']['document-id']['doc-number']
    ubdg_publ_doc_id_kind = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['publication-reference']['document-id']['kind']
    ubdg_publ_doc_id_date = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['publication-reference']['document-id']['date']
    ubdg_appli_appl_type = doc['us-patent-grant']['us-bibliographic-data-grant']['application-reference']['@appl-type']
    ubdg_appli_doc_id_doc_country = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['application-reference']['document-id']['country']
    ubdg_appli_doc_id_doc_number = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['application-reference']['document-id']['doc-number']
    ubdg_appli_doc_id_date = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['application-reference']['document-id']['date']
    ubdg_appli_doc_id_series_code = doc['us-patent-grant']['us-bibliographic-data-grant']['us-application-series-code']
    ubdg_utog_len_grant = doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant']['length-of-grant']
    ubdg_classificattion_locarno_edition = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['classification-locarno']['edition']
    ubdg_classificattion_locarno_main_classification = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['classification-locarno']['main-classification']
    ubdg_classificattion_national_country = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national']['country']
    ubdg_classificattion_national_main_classification = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national']['main-classification']
    ubdg_invention_title_id = doc['us-patent-grant']['us-bibliographic-data-grant']['invention-title']['@id']
    ubdg_invention_title_text = doc['us-patent-grant']['us-bibliographic-data-grant']['invention-title']['#text']
    ubdg_number_of_claims = doc['us-patent-grant']['us-bibliographic-data-grant']['number-of-claims']
    ubdg_us_exemplary_claim = doc['us-patent-grant']['us-bibliographic-data-grant']['us-exemplary-claim']
    ubdg_figures_number_of_drawing_sheets = doc['us-patent-grant']['us-bibliographic-data-grant']['figures'][
        'number-of-drawing-sheets']
    ubdg_figures_number_of_figures = doc['us-patent-grant']['us-bibliographic-data-grant']['figures'][
        'number-of-figures']
    ubdg_parties_applicants_applicant_sequence = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant']['@sequence']
    ubdg_parties_applicants_applicant_app_type = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant']['@app-type']
    ubdg_parties_applicants_applicant_designation = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant']['@designation']
    ubdg_parties_applicants_applicant_addressbook_last_name = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant']['addressbook']['last-name']
    ubdg_parties_applicants_applicant_addressbook_first_name = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant']['addressbook']['first-name']
    ubdg_parties_applicants_applicant_addressbook_address_street = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant']['addressbook']['address']['state']
    ubdg_parties_applicants_applicant_addressbook_address_city = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant']['addressbook']['address']['city']
    ubdg_parties_applicants_applicant_addressbook_address_country = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant']['addressbook']['address']['country']
    ubdg_parties_applicants_applicant_residence_country = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant']['residence']['country']
    ubdg_parties_inventors_inventor_sequence = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor']['@sequence']
    ubdg_parties_inventors_inventor_designation = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor']['@designation']
    ubdg_parties_inventors_inventor_addressbook = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor']['addressbook']
    ubdg_parties_inventors_inventor_last_name = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor']['addressbook']['last-name']
    ubdg_parties_inventors_inventor_first_name = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor']['addressbook']['first-name']
    ubdg_parties_inventors_inventor_city = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor']['addressbook']['address']['city']
    ubdg_parties_inventors_inventor_state = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor']['addressbook']['address']['state']
    ubdg_parties_inventors_inventor_country = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor']['addressbook']['address']['country']
    ubdg_parties_agents_agent_sequence = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['agents']['agent']['@sequence']
    ubdg_parties_agents_agent_rep_type = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['agents']['agent']['@rep-type']
    ubdg_parties_agents_agent_addressbook_lastname = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['agents']['agent']['addressbook']['last-name']
    ubdg_parties_agents_agent_addressbook_firstname = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['agents']['agent']['addressbook']['first-name']
    ubdg_parties_agents_agent_addressbook_address_country = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['agents']['agent']['addressbook']['address']['country']
    ubdg_examiners_primary_examiner_last_name = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['last-name']
    ubdg_examiners_primary_examiner_first_name = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['first-name']
    ubdg_examiners_primary_examiner_department = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['department']
    ubdg_examiners_assistant_examiner_last_name = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['assistant-examiner']['last-name']
    ubdg_examiners_assistant_examiner_first_name = \
    doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['assistant-examiner']['first-name']
    ubdg_claims_id = doc['us-patent-grant']['claims']['claim']['@id']
    ubdg_claims_num = doc['us-patent-grant']['claims']['claim']['@num']
    ubdg_claims_text = doc['us-patent-grant']['claims']['claim']['claim-text']

    # citaion  변수설쩡

    patcit = []
    for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-references-cited']['us-citation'])):
        patcit.append((doc['us-patent-grant']['us-bibliographic-data-grant']['us-references-cited']['us-citation'])[i])
    # print(patcit[0])



    # classification_national variable
    classification_national = []
    for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-field-of-classification-search']['classification-national'])):
        classification_national.append((doc['us-patent-grant']['us-bibliographic-data-grant'][
                                            'us-field-of-classification-search']['classification-national'])[i])

    # print(classification_national[0])

    # figure
    figure = []
    for i in range(len(doc['us-patent-grant']['drawings']['figure'])):
        figure.append((doc['us-patent-grant']['drawings']['figure'])[i])

    # print(figure[0])

    # description
    p = []
    for i in range(len(doc['us-patent-grant']['description']['description-of-drawings']['p'])):
        p.append((doc['us-patent-grant']['description']['description-of-drawings']['p'])[i])
        # print(p[1])

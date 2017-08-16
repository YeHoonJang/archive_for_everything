
from bs4 import BeautifulSoup


def parsing(xml_file):
    # open xml file
    # with open(xml_file, "r", encoding="utf8") as patent_xml:
    #     xml = patent_xml.read()

    soup = BeautifulSoup(xml_file, "html.parser")
    # print(soup)


    # tag
    tag_name = [tag.name for tag in soup.find_all()]
    # print(tag_name)
    # print(tag_name)




    # Conver xml to dict by using xmltodict
    import pprint
    import xmltodict
    doc = xmltodict.parse(xml_file)

    # pprint.pprint(doc)



    # 050104 xml file
    # 변수 설정
    var_list = []
    try:

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
        ubdg_appli_doc_id_doc_number = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['application-reference']['document-id']['doc-number']
        ubdg_appli_doc_id_date = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['application-reference']['document-id']['date']
        ubdg_appli_doc_id_series_code = doc['us-patent-grant']['us-bibliographic-data-grant']['us-application-series-code']
        ubdg_priority_claims_sequence = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['priority-claims']['priority-claim']['@sequence']
        ubdg_priority_claims_kind = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['priority-claims']['priority-claim']['@kind']
        ubdg_priority_claims_country = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['priority-claims']['priority-claim']['country']
        ubdg_priority_claims_doc_number = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['priority-claims']['priority-claim']['doc-number']
        ubdg_priority_claims_date = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['priority-claims']['priority-claim']['date']
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
            doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['@sequence']
        ubdg_parties_applicants_applicant_app_type = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['@app-type']
        ubdg_parties_applicants_applicant_designation = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['@designation']
        ubdg_parties_applicants_applicant_addressbook_last_name = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook'][
                'last-name']
        ubdg_parties_applicants_applicant_addressbook_first_name = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook'][
                'first-name']
        ubdg_parties_applicants_applicant_addressbook_address_street = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook'][
                'address']['street']
        ubdg_parties_applicants_applicant_addressbook_address_city = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook'][
                'address']['city']
        ubdg_parties_applicants_applicant_addressbook_address_country = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook'][
                'address']['country']
        ubdg_parties_applicants_applicant_nationality_country = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['nationality'][
                'country']
        ubdg_parties_applicants_applicant_residence_country = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['residence'][
                'country']
        ubdg_parties_agents_agent_sequence = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['@sequence']
        ubdg_parties_agents_agent_rep_type = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['@rep-type']
        ubdg_parties_agents_agent_addressbook_orgname = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['addressbook'][
                'orgname']
        ubdg_parties_agents_agent_addressbook_address_country = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['addressbook'][
                'address'][
                'country']
        ubdg_examiners_primary_examiner_last_name = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['last-name']
        ubdg_examiners_primary_examiner_first_name = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['first-name']
        ubdg_examiners_primary_examiner_department = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['department']
        ubdg_claims_id = doc['us-patent-grant']['claims']['claim']['@id']
        ubdg_claims_num = doc['us-patent-grant']['claims']['claim']['@num']
        ubdg_claims_text = doc['us-patent-grant']['claims']['claim']['claim-text']


        # citaion  변수설쩡

        patcit = []
        for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['citation'])):
            patcit.append((doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['citation'])[i])
        print(patcit[0])

        # for k in patcit:
        #     for p in patcit[k]:
        #         print(p)
        #     # print(k)
        # print(k)
        # classification_national variable
        classification_national = []
        for i in range(
                len(doc['us-patent-grant']['us-bibliographic-data-grant']['field-of-search'][
                        'classification-national'])):
            classification_national.append(
                (doc['us-patent-grant']['us-bibliographic-data-grant']['field-of-search']['classification-national'])[
                    i])

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

    except:
        pass

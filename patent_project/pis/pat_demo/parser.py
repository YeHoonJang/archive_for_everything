class parser(object):


    def __init__(self,xml):

        #common things
        self.doc = xmltodict.parser(xml)
        self.upg_patent_country= doc['us-patent-grant']['@country']
        self.upg_date_produced = doc['us-patent-grant']['@date-produced']
        self.upg_date_publ = doc['us-patent-grant']['@date-publ']
        self.upg_dtd= doc['us-patent-grant']['@dtd-version']
        self.upg_file = doc['us-patent-grant']['@file']
        self.upg_id = doc['us-patent-grant']['@id']
        self.upg_lang = doc['us-patent-grant']['@lang']
        self.upg_status = doc['us-patent-grant']['@status']
        self.ubdg_publ_doc_id_country = doc['us-patent-grant']['us-bibliographic-data-grant']['publication-reference']['document-id']['country']
        self.ubdg_publ_doc_id_doc_number = doc['us-patent-grant']['us-bibliographic-data-grant']['publication-reference']['document-id']['doc-number']
        self.ubdg_publ_doc_id_kind = doc['us-patent-grant']['us-bibliographic-data-grant']['publication-reference']['document-id']['kind']
        self.ubdg_publ_doc_id_date = doc['us-patent-grant']['us-bibliographic-data-grant']['publication-reference']['document-id']['date']
        self.ubdg_appli_appl_type = doc['us-patent-grant']['us-bibliographic-data-grant']['application-reference']['@appl-type']
        self.ubdg_appli_country = doc['us-patent-grant']['us-bibliographic-data-grant']['application-reference']['document-id']['country']
        self.ubdg_appli_doc_id_doc_number = doc['us-patent-grant']['us-bibliographic-data-grant']['application-reference']['document-id']['doc-number']
        self.ubdg_appli_doc_id_date = doc['us-patent-grant']['us-bibliographic-data-grant']['application-reference']['document-id']['date']
        self.ubdg_appli_doc_id_series_code = doc['us-patent-grant']['us-bibliographic-data-grant']['us-application-series-code']
        self.ubdg_invention_title_id = doc['us-patent-grant']['us-bibliographic-data-grant']['invention-title']['@id']
        self.ubdg_invention_title_text = doc['us-patent-grant']['us-bibliographic-data-grant']['invention-title']['#text']
        self.ubdg_figures_number_of_drawing_sheets = doc['us-patent-grant']['us-bibliographic-data-grant']['figures']['number-of-drawing-sheets']
        self.ubdg_figures_number_of_figures = doc['us-patent-grant']['us-bibliographic-data-grant']['figures']['number-of-figures']
        self.ubdg_claims_claim_id = doc['us-patent-grant']['claims']['claim']['@id']
        self.ubdg_claims_id =doc['us-patent-grant']['claims']['@id']
        self.ubdg_claims_num = doc['us-patent-grant']['claims']['claim']['@num']
        self.ubdg_claims_text = doc['us-patent-grant']['claims']['claim']['claim-text']
        self.upg_description = doc['us-patent-grant']['description']
        #claim
        self.ubdg_priority_claims_sequence = None
        self.ubdg_priority_claims_kind = None
        self.ubdg_priority_claims_country = None
        self.ubdg_priority_claims_doc_number= None
        self.ubdg_priority_claims_date = None
        #relation
        self.us_related_documents=None
        self.different_tags=None
        self.get_relation=None
        self.ubdg_relateddoc_relation_parentdoc_di_country=None
        self.ubdg_relateddoc_relation_parentdoc_di_doc_number=None
        self.ubdg_relateddoc_relation_parentdoc_di_kind=None
        self.ubdg_relateddoc_relation_parentdoc_di_date=None
        self.ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_country=None
        self.ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_doc_number=None
        self.ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_kind=None
        self.ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_date=None
        self.ubdg_relateddoc_relation_parentdoc_childdoc_country=None
        self.ubdg_relateddoc_relation_parentdoc_childdoc_doc_number=None
        self.ubdg_relateddoc_relation_parentdoc_parent_status=None
        self.ubdg_relateddoc_relation_parentdoc_di_country=None
        self.ubdg_relateddoc_relation_parentdoc_di_doc_number=None
        self.ubdg_relateddoc_relation_parentdoc_di_kind=None
        self.ubdg_relateddoc_relation_parentdoc_di_date=None
        self.ubdg_relateddoc_relation_parentdoc_childdoc_country=None
        self.ubdg_relateddoc_relation_parentdoc_childdoc_doc_number=None
        self.realtion_parent_grant_doc_country=None
        self.realtion_parent_grant_doc_number=None
        self.realtion_parent_grant_doc_kind=None
        self.realtion_parent_grant_doc_date=None
        self.relation_parent_status=None
        #citation
        self.patcit =None
        self.patcit_num =None
        self.patcit_country =None
        self.patcit_doc_country =None
        self.patcit_kind=None
        self.patcit_name=None
        self.patcit_date=None
        self.nplcit_num= None
        self.nplcit_othercit=None
        self.npl_category=None
        #assistant examiner(option) be NULL
        self.ubdg_examiners_assistant_examiner_last_name = None
        self.ubdg_examiners_assistant_examiner_first_name = None
        #additional_info
        self.classification_add_info=None
        self.classification_add=None
        #us_relation
        self.ubdg_relateddoc_us_relation_parentdoc_di_country = None
        self.ubdg_relateddoc_us_relation_parentdoc_di_doc_number = None
        self.ubdg_relateddoc_us_relation_parentdoc_di_kind = None
        self.ubdg_relateddoc_us_relation_parentdoc_di_date = None
        self.ubdg_relateddoc_us_relation_parentdoc_parentgrantdoc_di_country = None
        self.ubdg_relateddoc_us_relation_parentdoc_parentgrantdoc_di_doc_number = None
        self.ubdg_relateddoc_us_relation_parentdoc_parentgrantdoc_di_kind = None
        self.ubdg_relateddoc_us_relation_parentdoc_parentgrantdoc_di_date = None
        self.ubdg_relateddoc_us_relation_parentdoc_childdoc_country = None
        self.ubdg_relateddoc_us_relation_parentdoc_childdoc_doc_number = None
        self.ubdg_relateddoc_us_relation_parentdoc_parent_status = None
        self.ubdg_us_sir_flag_sir_text=None
        self.ubdg_classificattion_locarno_edition= None
        self.ubdg_classificattion_locarno_main_classification= None
        self.ubdg_classificattion_national_country= None
        self.ubdg_classificattion_national_main_classification= None
        self.ubdg_number_of_claims= None
        self.ubdg_us_exemplary_claim= None
        self.ubdg_figures_number_of_drawing_sheets= None
        self.ubdg_figures_number_of_figures = None
        self.ubdg_examiners_primary_examiner_last_name= None
        self.ubdg_examiners_primary_examiner_first_name= None
        self.ubdg_examiners_primary_examiner_department = None
        #termofgrant
        self.ubdg_utog_len_grant = None
        self.ubdg_utog_text_grant = None
        self.ubdg_utog_extension_grant = None
        self.ubdg_utog_disclaimer_grant = None
        self.ubdg_utog_lapse_grant = None
        #null
        #abstract
        self.ubdg_abstract = None
        #null
        #drawing
        self.ubdg_drawing= None
        #null
        #sequence list
        self.ubdg_us_sequence_list_doc= None
        #null
        #table external
        self.ubdg_table_external_doc= None
        #null
        #chemistry
        self.ubdg_us_chemistry= None
        #null
        #math
        self.ubdg_us_math= None
        self.ubdg_provisional_appl_doc_country= None
        self.ubdg_provisional_appl_doc_number= None
        self.ubdg_provisional_appl_doc_kind= None
        self.ubdg_provisional_appl_doc_date= None
        self.ubdg_provisional_appl_status= None
        self.ubdg_related_publ_doc_country= None
        self.ubdg_related_publ_doc_number= None
        self.ubdg_related_publ_doc_kind= None
        self.ubdg_related_publ_doc_date= None
        self.ubdg_pct_or_regional_filling_data_document_id= None
        self.ubdg_pct_or_regional_filling_data_us_date= None
        self.ubdg_pct_or_regional_publishing_data_document_id= None
        self.ubdg_pct_or_regional_publishing_data_gazette_reference= None
        self.ubdg_patent_family_priority_application= None
        self.ubdg_bio_deposit_depositary= None
        self.ubdg_bio_deposit_bio_accno= None
        self.ubdg_bio_deposit_id= None
        self.ubdg_bio_deposit_num= None
        self.ubdg_bio_deposit_url= None
        self.ubdg_bio_deposit_dnum= None
        self.ubdg_bio_deposit_date= None
        self.ubdg_bio_deposit_term= None
        self.ubdg_bio_deposit_dtext= None
        self.ubdg_us_issued_on_continued_prosecution_application_cpa_text =None
        self.ubdg_rule_47_flag = None
        self.ubdg_classification_ipc = None
        self.ubdg_text = None
        self.ubdg_date_search_completed= None
        self.ubdg_date_search_report_mailed= None
        self.ubdg_place_of_search= None
        self.ubdg_search_report_publication= None
        self.ubdg_searcher= None
        self.ubdg_us_microform_quantity= None
        #classification
        self.classification_national=None
        self.classification_country=None
        self.classification_main=None
        #botantic
        self.ubdg_us_botantic_latin_name = None
        self.ubdg_us_botantic_variety = None


    class parserVer40(Parser):
        def __init__(self,xml):
            super().__init__(xml)
            #agents #null
            self.ubdg_parties_agents_agent_rep_type=None
            self.ubdg_parties_agents_agent_addressbook_orgname=None
            self.ubdg_parties_agents_agent_addressbook_address_country=None

            #address_street
            self.ubdg_parties_applicants_applicant_addressbook_address_street = self.doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['street']
            #applicant
            self.ubdg_parties_applicants_applicant_sequence =None
            self.ubdg_parties_applicants_applicant_app_type=None
            self.ubdg_parties_applicants_applicant_designation=None
            self.ubdg_parties_applicants_applicant_addressbook_last_name=None
            self.ubdg_parties_applicants_applicant_addressbook_first_name=None
            self.ubdg_parties_applicants_applicant_addressbook_address_city=None
            self.ubdg_parties_applicants_applicant_addressbook_address_country=None
            self.ubdg_parties_applicants_applicant_nationality_country=None
            self.ubdg_parties_applicants_applicant_residence_country=None
            self.applicant=None
            self.applicant_sequence=None
            self.applicant_designation=None
            self.applicant_app_type=None
            self.applicant_address_last_name=None
            self.applicant_address_first_name=None
            self.applicant_address_city=None
            self.applicant_address_state=None
            self.applicant_address_country=None
            self.applicant_nationality_country=None
            self.applicant_residence_country=None
            #inventor
            self.parties_inventors_inventor_sequence=None
            self.ubdg_parties_inventors_inventor_designation=None
            self.ubdg_parties_inventors_inventor_addressbook_last_name=None
            self.ubdg_parties_inventors_inventor_addressbook_first_name=None
            self.ubdg_parties_inventors_inventor_addressbook_address_city=None
            self.ubdg_parties_inventors_inventor_addressbook_address_state=None
            self.ubdg_parties_inventors_inventor_addressbook_address_country=None
            self.inventor=None
            self.inventor_sequence=None
            self.inventor_designation=None
            self.inventor_address_last_name=None
            self.inventor_address_first_name=None
            self.inventor_address_city=None
            self.inventor_address_state=None
            self.inventor_address_country=None
            #assignee
            self.ubdg_assignees_assignee_address_orgname =None
            self.ubdg_assignees_assignee_address_role=None
            self.ubdg_assignees_assignee_address_address_city=None
            self.ubdg_assignees_assignee_address_address_state=None
            self.ubdg_assignees_assignee_address_address_country=None

            self.ubdg_us_deceased_inventor_sequence= None
            self.ubdg_us_deceased_inventor_addressbook= None
            self.ubdg_parties_correspondence_address_customer_number= None
            self.ubdg_parties_correspondence_address_addressbook= None

        #null
        def assisatntExaminer(self,xml):
            null_variables = []
            null_variables.append(ubdg_examiners_assistant_examiner_last_name)
            null_variables.append(ubdg_examiners_assistant_examiner_first_name)

            null_tag = []
            null_tag.append(doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['assistant-examiner']['last-name'])
            null_tag.append(doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['assistant-examiner']['first-name'])

            for v,t in zip(null_variables, null_tag):
                if v == t:
                    v =  t
                    #null
        def drawing(self,xml):
            ubdg_drawing = doc['us-patent-grant']['drawings']
            #null
        def sequenceListDoc(self,xml):
            ubdg_us_sequence_list_doc = doc['us-patent-grant']['us-sequence-list-doc']
            #null
        def tableExternalDoc(self,xml):
            ubdg_table_external_doc = doc['us-patent-grant']['table-external-doc']
            #null
        def usChemistry(self,xml):
            ubdg_us_chemistry = doc['us-patent-grant']['us-chemistry']
            #null
        def usMath(self,xml):
            ubdg_us_math = doc['us-patent-grant']['us-math']
            #null
        def abstract(self,xml):
            ubdg_abstract = doc['us-patent-grant']['abstract']
            #null
        def usBotantic(self, xml):
            ubdg_us_botantic_latin_name=doc['us-patent-grant']['us-bibliographic-data-grant']['us-botantic']['latin-name']
            ubdg_us_botantic_variety=doc['us-patent-grant']['us-bibliographic-data-grant']['us-botantic']['variety']
            #null
        def termOfGrant(self,xml):
            ubdg_utog_len_grant = doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant']['length-of-grant']
            ubdg_utog_text_grant = doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant']['text']
            ubdg_utog_extension_grant = doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant']['us-term-extension']
            ubdg_utog_disclaimer_grant = doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant']['disclaimer']
            ubdg_utog_lapse_grant = doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant']['lapse-of-patent']
            #null
        def classificationsIpcrID(self, xml):
            ubdg_us_botantic_latin_name=doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['@id']
            #null
        def biblioClassifiacationLocarno(self, xml):
            ubdg_classificattion_locarno_edition = doc['us-patent-grant']['us-bibliographic-data-grant']['classification-locarno']['edition']
            ubdg_classificattion_locarno_main_classification = doc['us-patent-grant']['us-bibliographic-data-grant']['classification-locarno']['main-classification']
            #null
        def biblioClassifiacationNational(self,xml):
            ubdg_classificattion_national_country = doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national']['country']
            ubdg_classificattion_national_main_classification = doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national']['main-classification']
            #null
        def nuumberOfClaims(self, xml):
            ubdg_number_of_claims = doc['us-patent-grant']['us-bibliographic-data-grant']['number-of-claims']
            #null
        def Exemplary_claim(self, xml):
            ubdg_us_exemplary_claim = doc['us-patent-grant']['us-bibliographic-data-grant']['us-exemplary-claim']

            #null
        def examiners(self, xml):
            ubdg_examiners_primary_examiner_last_name = doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['last-name']
            ubdg_examiners_primary_examiner_first_name = doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['first-name']
            ubdg_examiners_primary_examiner_department = doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['department']
            #null
        def usFlagSirText(self,xml):
            ubdg_us_sir_flag_sir_text = ['us-patent-grant']['us-bibliographic-data-grant']['us-sir-flag']['@sir-text']


        def assignee(self,xml):

            ubdg_assignees_assignee_address_orgname = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['orgname']
            ubdg_assignees_assignee_address_role = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['role']
            ubdg_assignees_assignee_address_address_city = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['address']['city']
            ubdg_assignees_assignee_address_address_state = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['address']['state']
            ubdg_assignees_assignee_address_address_country = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['address']['country']


            #null
        def usIssuedOnContinuedProsecutionApplication(self,xml):
            ubdg_us_issued_on_continued_prosecution_application_cpa_text = doc['us-patent-grant']['us-bibliographic-data-grant']['us-issued-on-continued-prosecution-application']['grant-cpa-text']
            #null

        def rule47flag(self,xml ):
            ubdg_rule_47_flag = doc['us-patent-grant']['us-bibliographic-data-grant']['rule-47-flag']
            #null
        def classificationIpc(self, xml):
            ubdg_classification_ipc =doc['us-patent-grant']['us-bibliographic-data-grant']['classification-ipc']


            #null
        def text(self, xml):
            ubdg_text = doc['us-patent-grant']['us-bibliographic-data-grant']['text']

            #null
        def referencesCitedExceptCitation(self, xml):
            ubdg_date_search_completed = doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['date-search-completed']
            ubdg_date_search_report_mailed = doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['date-search-report-mailed']
            ubdg_place_of_search = doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['place-of-search']
            ubdg_search_report_publication =doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['search-report-publication']
            ubdg_searcher = doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['searcher']



            #null
        def usMicroformquantity(self, xml):
            ubdg_us_microform_quantity = doc['us-patent-grant']['us-bibliographic-data-grant']['us-microform-quantity']
            #null
        def usDeceasedInventor(self, xml):
            ubdg_us_deceased_inventor_sequence = doc['us-patent-grant']['us-bibliographic-data-grant']['us-deceased-inventor']['@sequence']
            ubdg_us_deceased_inventor_addressbook = doc['us-patent-grant']['us-bibliographic-data-grant']['us-deceased-inventor']['addressbook']


            #null
        def correspondenceAddress(self,xml):
            ubdg_parties_correspondence_address_customer_number = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['correspondence-address']['customer-number']
            ubdg_parties_correspondence_address_addressbook = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['correspondence-address']['addressbook']


            #null
        def pctOrRegionalFillingData(self,xml):
            ubdg_pct_or_regional_filling_data_document_id = doc['us-patent-grant']['us-bibliographic-data-grant']['pct-or-regional-filling-data']['document-id']
            try:
                ubdg_pct_or_regional_filling_data_us_date = doc['us-patent-grant']['us-bibliographic-data-grant']['pct-or-regional-filling-data']['us-371c124-date']#null
            except:
                pass
                #null
        def pctOrReginalPublishingData(self, xml):
            ubdg_pct_or_regional_publishing_data_document_id = doc['us-patent-grant']['us-bibliographic-data-grant']['pct-or-regional-publishing-data']['document-id']
            try:
                ubdg_pct_or_regional_publishing_data_gazette_reference = doc['us-patent-grant']['us-bibliographic-data-grant']['pct-or-regional-publishing-data']['gazette-reference']#null
            except:
                pass
                #null
        def parentFamily (self, xml):
            ubdg_patent_family_priority_application = doc['us-patent-grant']['us-bibliographic-data-grant']['patent-family']['priority-application']
            #null
        def bioDeposit(self, xml):
            ubdg_bio_deposit_depositary = doc['us-patent-grant']['us-bibliographic-data-grant']['depositary']
            ubdg_bio_deposit_bio_accno = doc['us-patent-grant']['us-bibliographic-data-grant']['bio-accno']
            ubdg_bio_deposit_id = doc['us-patent-grant']['us-bibliographic-data-grant']['@id']
            ubdg_bio_deposit_num = doc['us-patent-grant']['us-bibliographic-data-grant']['@num']
            ubdg_bio_deposit_url = doc['us-patent-grant']['us-bibliographic-data-grant']['@url']
            ubdg_bio_deposit_dnum = doc['us-patent-grant']['us-bibliographic-data-grant']['@dnum']
            try:
                ubdg_bio_deposit_date = doc['us-patent-grant']['us-bibliographic-data-grant']['date']#null
            except:
                pass
            try:
                ubdg_bio_deposit_term = doc['us-patent-grant']['us-bibliographic-data-grant']['term']#null
            except:
                pass
            try:
                ubdg_bio_deposit_dtext = doc['us-patent-grant']['us-bibliographic-data-grant']['dtext']#null
            except:
                pass
                #NULL
        def agent(self,xml):

            ubdg_parties_agents_agent_sequence = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['@sequence']
            ubdg_parties_agents_agent_rep_type = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['@rep-type']
            ubdg_parties_agents_agent_addressbook_orgname = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['addressbook']['orgname']
            ubdg_parties_agents_agent_addressbook_address_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['addressbook']['address']['country']

        def patcit(self,xml):
            patcit=[]
            for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['citation'])):
                patcit.append((doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['citation'])[i])


            patcit_num = []
            patcit_country = []
            patcit_doc_number = []
            patcit_kind = []
            patcit_name = []
            patcit_date = []
            nplcit_num =[]
            nplcit_othercit=[]
            npl_category=[]

            for j in patcit:
                patcit_number = j['patcit']['@num']
                patcit_doc_country = j['patcit']['document-id']['country']
                patcit_doc_docnumber = j['patcit']['document-id']['doc-number']
                patcit_doc_kind = j['patcit']['document-id']['kind']
                patcit_doc_name = j['patcit']['document-id']['name']
                patcit_doc_date = j['patcit']['document-id']['date']
                patcit_num.append(patcit_number)
                patcit_country.append(patcit_doc_country)
                patcit_doc_number.append(patcit_doc_docnumber)
                patcit_kind.append(patcit_doc_kind)
                patcit_name.append(patcit_doc_name)
                patcit_date.append(patcit_doc_date)
                #null
                nplcit_number = j['nplcit']['@num']#null
                nplcit_othercitation = j['nplcit']['othercit']#null
                category_in_npl = j['category']#null
                nplcit_num.append(nplcit_number)
                nplcit_othercit.append(nplcit_othercitation)
                npl_category.append(category_in_npl)
                #null
        def classification(self,xml):
            classification_national = []

            for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['field-of-search']['classification-national'])):
                classification_national.append((doc['us-patent-grant']['us-bibliographic-data-grant']['field-of-search']['classification-national'])[i])

            classification_country = []
            classification_main = []
            classification_add_info =[]#null
            for i in classification_national:
                classification_add = i['additional-info']#null
                classificiation_c = i['country']
                classificiation_m = i['main-classification']
                classification_country.append(classificiation_c)
                classification_main.append(classificiation_m)
                classification_add_info.append(classification_add)#null

        def applicant(self,xml):

            #applicant가 1개일 경우
            if range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant'])) == 0:

                ubdg_parties_applicants_applicant_sequence = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['@sequence']
                ubdg_parties_applicants_applicant_app_type = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['@app-type']
                ubdg_parties_applicants_applicant_designation = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['@designation']
                ubdg_parties_applicants_applicant_addressbook_last_name = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['last-name']
                ubdg_parties_applicants_applicant_addressbook_first_name = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['first-name']
                ubdg_parties_applicants_applicant_addressbook_address_street = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['street']
                ubdg_parties_applicants_applicant_addressbook_address_city = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['city']
                ubdg_parties_applicants_applicant_addressbook_address_state = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['state']
                ubdg_parties_applicants_applicant_addressbook_address_postcode = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['postcode']
                ubdg_parties_applicants_applicant_addressbook_address_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['country']
                ubdg_parties_applicants_applicant_nationality_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['nationality']['country']
                ubdg_parties_applicants_applicant_residence_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['residence']['country']

            #applicant가 2개이상일   경우
            else:
                applicant = []
                for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant'])):
                    applicant.append((doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant'])[i])

                applicant_sequence =[]
                applicant_app_type =[]
                applicant_designation =[]
                applicant_address_last_name =[]
                applicant_address_first_name =[]
                applicant_address_city =[]
                applicant_address_state =[]
                applicant_address_country =[]
                applicant_nationality_country =[]
                applicant_residence_country =[]
                applicant_address_street = []
                applicant_address_postcode=[]


                for i in applicant:
                    ubdg_parties_applicants_applicant_sequence = i['@sequence']
                    ubdg_parties_applicants_applicant_app_type = i['@app-type']
                    ubdg_parties_applicants_applicant_designation = i['@designation']
                    ubdg_parties_applicants_applicant_addressbook_last_name = i['addressbook']['last-name']
                    ubdg_parties_applicants_applicant_addressbook_first_name = i['addressbook']['first-name']#null
                    ubdg_parties_applicants_applicant_addressbook_address_state = i['addressbook']['address']['state']#null
                    ubdg_parties_applicants_applicant_addressbook_address_street = i['addressbook']['address']['street']#null
                    ubdg_parties_applicants_applicant_addressbook_address_postcode = i['addressbook']['address']['postcode']#null
                    ubdg_parties_applicants_applicant_addressbook_address_city = i['addressbook']['address']['city']#null
                    ubdg_parties_applicants_applicant_addressbook_address_country = i['addressbook']['address']['country']
                    ubdg_parties_applicants_applicant_nationality_country = i['nationality']['country']
                    ubdg_parties_applicants_applicant_residence_country = i['residence']['country']
                    applicant_sequence.append(ubdg_parties_applicants_applicant_sequence)
                    applicant_app_type.append(ubdg_parties_applicants_applicant_app_type)
                    applicant_designation.append(ubdg_parties_applicants_applicant_designation)
                    applicant_address_last_name.append(ubdg_parties_applicanprots_applicant_addressbook_last_name)
                    applicant_address_first_name.append(ubdg_parties_applicants_applicant_addressbook_first_name)
                    applicant_address_street.append(ubdg_parties_applicants_applicant_addressbook_address_street)
                    applicant_address_postcode.append(ubdg_parties_applicants_applicant_addressbook_address_postcode)
                    applicant_address_city.append(ubdg_parties_applicants_applicant_addressbook_address_city)
                    applicant_address_state.append(ubdg_parties_applicants_applicant_addressbook_address_state)
                    applicant_address_country.append(ubdg_parties_applicants_applicant_addressbook_address_country)
                    applicant_nationality_country.append(ubdg_parties_applicants_applicant_nationality_country)
                    applicant_residence_country.append(ubdg_parties_applicants_applicant_residence_country)

        def claim(self):
            ubdg_priority_claims_sequence = doc['us-patent-grant']['us-bibliographic-data-grant']['priority-claims']['priority-claim']['@sequence']
            ubdg_priority_claims_kind['us-patent-grant']['us-bibliographic-data-grant']['priority-claims']['priority-claim']['@kind']
            ubdg_priority_claims_country = doc['us-patent-grant']['us-bibliographic-data-grant']['priority-claims']['priority-claim']['country']
            ubdg_priority_claims_doc_number = doc['us-patent-grant']['us-bibliographic-data-grant']['priority-claims']['priority-claim']['doc-number']#null
            ubdg_priority_claims_date = doc['us-patent-grant']['us-bibliographic-data-grant']['priority-claims']['priority-claim']['date']

        #null
        def inventors(self,xml):
            if range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor'])) == 0:

                ubdg_parties_inventors_inventor_sequence = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['@sequence']
                ubdg_parties_inventors_inventor_designation = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['@designation']
                ubdg_parties_inventors_inventor_addressbook_last_name = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook']['last-name']
                ubdg_parties_inventors_inventor_addressbook_first_name = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook']['first-name']
                ubdg_parties_inventors_inventor_addressbook_address_city = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook']['address']['city']
                ubdg_parties_inventors_inventor_addressbook_address_state = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook']['address']['state']
                ubdg_parties_inventors_inventor_addressbook_address_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook']['address']['country']

            else:
                inventor = []
                for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor'])):
                    applicant.append((doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor'])[i])

                inventor_sequence =[]
                inventor_designation =[]
                inventor_address_last_name =[]
                inventor_address_first_name =[]
                inventor_address_city =[]
                inventor_address_state =[]
                inventor_address_country =[]

                for i in inventor:
                    ubdg_parties_inventors_inventor_sequence = i['@sequence']
                    ubdg_parties_inventors_inventor_designation = i['@designation']
                    ubdg_parties_inventors_inventor_addressbook_last_name = i['addressbook']['last-name']
                    ubdg_parties_inventors_inventor_addressbook_first_name = i['addressbook']['first-name']
                    ubdg_parties_inventors_inventor_addressbook_address_state = i['addressbook']['address']['state']
                    ubdg_parties_inventors_inventor_addressbook_address_city = i['addressbook']['address']['city']
                    ubdg_parties_inventors_inventor_addressbook_address_country = i['addressbook']['address']['country']
                    inventor_sequence.append(ubdg_parties_inventors_inventor_sequence)
                    inventor_designation.append(ubdg_parties_inventors_inventor_designation)
                    inventor_address_last_name.append(ubdg_parties_inventors_inventor_addressbook_last_name)
                    inventor_address_first_name.append(ubdg_parties_inventors_inventor_addressbook_first_name)
                    inventor_address_city.append(ubdg_parties_inventors_inventor_addressbook_address_city)
                    inventor_address_state.append(ubdg_parties_inventors_inventor_addressbook_address_state)
                    inventor_address_country.append(ubdg_parties_inventors_inventor_addressbook_address_country)

                    #null
        def beforeRelation(relation):
            us_related_documents = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']

            different_tags = []
            for i in us_related_documents.keys():
                different_tags.append(i)

            relation_list =[]
            for i in different_tags:
                get_relation = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents'][i]
                if isinstance(get_relation, type(list)) is True:
                    for j in range(len(get_relation)-1):
                        for k in get_relation:
                            relation_list.append(k)
                else:
                    relation_list.append(get_relation)
            relation(relation_list)



            #null
        def relation(has_relation):

            ubdg_relateddoc_relation_parentdoc_di_country= []
            ubdg_relateddoc_relation_parentdoc_di_doc_number =[]
            ubdg_relateddoc_relation_parentdoc_di_kind=[]
            ubdg_relateddoc_relation_parentdoc_di_date=[]
            ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_country=[]
            ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_doc_number=[]
            ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_kind=[]
            ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_date=[]
            ubdg_relateddoc_relation_parentdoc_childdoc_country=[]
            ubdg_relateddoc_relation_parentdoc_childdoc_doc_number=[]
            ubdg_relateddoc_relation_parentdoc_parent_status=[]

            for relation_element in has_relation:

                ubdg_relateddoc_relation_parentdoc_di_country.append(relation_element['relation']['parent-doc']['document-id']['country'])
                ubdg_relateddoc_relation_parentdoc_di_doc_number.append(relation_element['relation']['parent-doc']['document-id']['doc-number'])
                ubdg_relateddoc_relation_parentdoc_di_kind.append(relation_element['relation']['parent-doc']['document-id']['kind'])
                ubdg_relateddoc_relation_parentdoc_di_date.append(relation_element['relation']['parent-doc']['document-id']['date'])

                ubdg_relateddoc_relation_parentdoc_childdoc_country.append(relation_element['relation']['child-doc']['document-id']['country'])
                ubdg_relateddoc_relation_parentdoc_childdoc_doc_number.append(relation_element['relation']['child-doc']['document-id']['doc-number'])

                #null
                try:
                    realtion_parent_grant_doc_country = relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['country']#null
                    realtion_parent_grant_doc_number = relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['doc-number']#null
                    realtion_parent_grant_doc_kind = relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['kind']#null
                    realtion_parent_grant_doc_date = relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['date']#null
                    ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_country.append(realtion_parent_grant_doc_country)
                    ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_doc_number.append(realtion_parent_grant_doc_number)
                    ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_kind.append(realtion_parent_grant_doc_kind)
                    ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_date.append(realtion_parent_grant_doc_date)
                except:
                    pass

                try:
                    try:#null
                        relation_parent_status = relation_element['relation']['parent-doc']['parent_status']
                        ubdg_relateddoc_relation_parentdoc_parent_status.append(relation_parent_status)
                    except:
                        pass

                        #null
        def usRelation(self,xml):
            ubdg_relateddoc_us_relation_parentdoc_di_country= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['document-id']['country']
            ubdg_relateddoc_us_relation_parentdoc_di_doc_number=doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['doc-number']
            ubdg_relateddoc_us_relation_parentdoc_di_kind= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['kind']
            ubdg_relateddoc_us_relation_parentdoc_di_date= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['date']
            ubdg_relateddoc_us_relation_parentdoc_parentgrantdoc_di_country= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['parent-grant-document']['document-id']['country']
            ubdg_relateddoc_us_relation_parentdoc_parentgrantdoc_di_doc_number= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['parent-grant-document']['document-id']['doc-number']
            ubdg_relateddoc_us_relation_parentdoc_parentgrantdoc_di_kind= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['parent-grant-document']['document-id']['kind']
            ubdg_relateddoc_us_relation_parentdoc_parentgrantdoc_di_date= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['parent-grant-document']['document-id']['date']
            ubdg_relateddoc_us_relation_parentdoc_childdoc_country= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['child-doc']['document-id']['country']
            ubdg_relateddoc_us_relation_parentdoc_childdoc_doc_number= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['child-doc']['document-id']['doc-number']
            ubdg_relateddoc_us_relation_parentdoc_parent_status= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['parent_status']

            #null
        def usProvisionalApplication(self,xml):
            ubdg_provisional_appl_doc_country= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['document-id']['country']
            ubdg_provisional_appl_doc_number= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['document-id']['doc-number']
            ubdg_provisional_appl_doc_kind= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['document-id']['kind']
            ubdg_provisional_appl_doc_date= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['document-id']['country']
            #null
            ubdg_provisional_appl_status= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['us-provisional-application-status']
            #null
        def relatedPublication(self,xml):
            ubdg_related_publ_doc_country = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication']['document-id']['country']
            ubdg_related_publ_doc_number = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication']['document-id']['doc-number']
            ubdg_related_publ_doc_kind = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication']['document-id']['kind']
            ubdg_related_publ_doc_date = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication']['document-id']['date']


    class parserVer41(Parser):
        def __init__(self,xml):
            super().__init__(xml)



            #add us-claim-statement
            self.upg_us_claim_statement = doc['us-patent-grant']['us-claim-statement']
            #address_street
            self.ubdg_parties_applicants_applicant_addressbook_address_state = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['state']
            #assignee
            self.ubdg_assignees_assignee_address_orgname =None
            self.ubdg_assignees_assignee_address_role=None
            self.ubdg_assignees_assignee_address_address_city=None
            self.ubdg_assignees_assignee_address_address_state=None
            self.ubdg_assignees_assignee_address_address_country=None
            #agents #null
            self.ubdg_parties_agents_agent_rep_type=None
            self.ubdg_parties_agents_agent_addressbook_orgname=None
            self.ubdg_parties_agents_agent_addressbook_address_country=None
            #further 추가

            self.further=None
            self.further_classification=None
            self.further_class=None


            self.patcit_category= doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['citation']['category']
            self.patcit_classification_country=None
            self.patcit_classification_main=None

            self.us_classifications_ipcr = None
            #applicant
            self.ubdg_parties_applicants_applicant_sequence =None
            self.ubdg_parties_applicants_applicant_app_type=None
            self.ubdg_parties_applicants_applicant_designation=None
            self.ubdg_parties_applicants_applicant_addressbook_last_name=None
            self.ubdg_parties_applicants_applicant_addressbook_first_name=None
            self.ubdg_parties_applicants_applicant_addressbook_address_city=None
            self.ubdg_parties_applicants_applicant_addressbook_address_country=None
            self.ubdg_parties_applicants_applicant_nationality_country=None
            self.ubdg_parties_applicants_applicant_residence_country=None
            self.applicant=None
            self.applicant_sequence=None
            self.pplicant_designation=None
            self.applicant_app_type=None
            self.applicant_address_last_name=None
            self.applicant_address_first_name=None
            self.applicant_address_city=None
            self.applicant_address_state=None
            self.applicant_address_country=None
            self.applicant_nationality_country=None
            self.applicant_residence_country=None
            #null
            self.applicant_address_street=None
            self.applicant_address_postcode=None

            #megaTable
            self.ubdg_mega_table = None

            self.ubdg_us_deceased_inventor_sequence= None
            self.ubdg_us_deceased_inventor_addressbook= None
            self.ubdg_parties_correspondence_address_customer_number= None
            self.ubdg_parties_correspondence_address_addressbook= None

            #inventor
            self.parties_inventors_inventor_sequence=None
            self.ubdg_parties_inventors_inventor_designation=None
            self.ubdg_parties_inventors_inventor_addressbook_last_name=None
            self.ubdg_parties_inventors_inventor_addressbook_first_name=None
            self.ubdg_parties_inventors_inventor_addressbook_address_city=None
            self.ubdg_parties_inventors_inventor_addressbook_address_state=None
            self.ubdg_parties_inventors_inventor_addressbook_address_country=None
            self.inventor=None
            self.inventor_sequence=None
            self.inventor_designation=None
            self.inventor_address_last_name=None
            self.inventor_address_first_name=None
            self.inventor_address_city=None
            self.inventor_address_state=None
            self.inventor_address_country=None


        #null
        def assisatntExaminer(self,xml):
            null_variables = []
            null_variables.append(ubdg_examiners_assistant_examiner_last_name)
            null_variables.append(ubdg_examiners_assistant_examiner_first_name)

            null_tag = []
            null_tag.append(doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['assistant-examiner']['last-name'])
            null_tag.append(doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['assistant-examiner']['first-name'])

            for v,t in zip(null_variables, null_tag):
                if v == t:
                    v =  t

                    #null
        def inventors(self,xml):
            if range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor'])) == 0:

                ubdg_parties_inventors_inventor_sequence = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['@sequence']
                ubdg_parties_inventors_inventor_designation = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['@designation']
                ubdg_parties_inventors_inventor_addressbook_last_name = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook']['last-name']
                ubdg_parties_inventors_inventor_addressbook_first_name = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook']['first-name']
                ubdg_parties_inventors_inventor_addressbook_address_city = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook']['address']['city']
                ubdg_parties_inventors_inventor_addressbook_address_state = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook']['address']['state']
                ubdg_parties_inventors_inventor_addressbook_address_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook']['address']['country']

            else:
                inventor = []
                for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor'])):
                    applicant.append((doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor'])[i])

                inventor_sequence =[]
                inventor_designation =[]
                inventor_address_last_name =[]
                inventor_address_first_name =[]
                inventor_address_city =[]
                inventor_address_state =[]
                inventor_address_country =[]

                for i in inventor:
                    ubdg_parties_inventors_inventor_sequence = i['@sequence']
                    ubdg_parties_inventors_inventor_designation = i['@designation']
                    ubdg_parties_inventors_inventor_addressbook_last_name = i['addressbook']['last-name']
                    ubdg_parties_inventors_inventor_addressbook_first_name = i['addressbook']['first-name']
                    ubdg_parties_inventors_inventor_addressbook_address_state = i['addressbook']['address']['state']
                    ubdg_parties_inventors_inventor_addressbook_address_city = i['addressbook']['address']['city']
                    ubdg_parties_inventors_inventor_addressbook_address_country = i['addressbook']['address']['country']
                    inventor_sequence.append(ubdg_parties_inventors_inventor_sequence)
                    inventor_designation.append(ubdg_parties_inventors_inventor_designation)
                    inventor_address_last_name.append(ubdg_parties_inventors_inventor_addressbook_last_name)
                    inventor_address_first_name.append(ubdg_parties_inventors_inventor_addressbook_first_name)
                    inventor_address_city.append(ubdg_parties_inventors_inventor_addressbook_address_city)
                    inventor_address_state.append(ubdg_parties_inventors_inventor_addressbook_address_state)
                    inventor_address_country.append(ubdg_parties_inventors_inventor_addressbook_address_country)


                    #null
        def termOfGrant(self,xml):
            ubdg_utog_len_grant = doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant']['length-of-grant']
            ubdg_utog_text_grant = doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant']['text']
            ubdg_utog_extension_grant = doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant']['us-term-extension']
            ubdg_utog_disclaimer_grant = doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant']['disclaimer']
            ubdg_utog_lapse_grant = doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant']['lapse-of-patent']
            #null
        def classificationsIpcrID(self, xml):
            ubdg_us_botantic_latin_name=doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['@id']
            #null
        def biblioClassifiacationLocarno(self, xml):
            ubdg_classificattion_locarno_edition = doc['us-patent-grant']['us-bibliographic-data-grant']['classification-locarno']['edition']
            ubdg_classificattion_locarno_main_classification = doc['us-patent-grant']['us-bibliographic-data-grant']['classification-locarno']['main-classification']
            #null
        def biblioClassifiacationNational(self,xml):
            ubdg_classificattion_national_country = doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national']['country']
            ubdg_classificattion_national_main_classification = doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national']['main-classification']
            #null
        def nuumberOfClaims(self, xml):
            ubdg_number_of_claims = doc['us-patent-grant']['us-bibliographic-data-grant']['number-of-claims']
            #null
        def Exemplary_claim(self, xml):
            ubdg_us_exemplary_claim = doc['us-patent-grant']['us-bibliographic-data-grant']['us-exemplary-claim']

            #null
        def examiners(self, xml):
            ubdg_examiners_primary_examiner_last_name = doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['last-name']
            ubdg_examiners_primary_examiner_first_name = doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['first-name']
            ubdg_examiners_primary_examiner_department = doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['department']
            #null
        def usFlagSirText(self,xml):
            ubdg_us_sir_flag_sir_text = ['us-patent-grant']['us-bibliographic-data-grant']['us-sir-flag']['@sir-text']
            #null
        def parentFamily (self, xml):
            ubdg_patent_family_priority_application = doc['us-patent-grant']['us-bibliographic-data-grant']['patent-family']['priority-application']
            #null

        def bioDeposit(self, xml):
            ubdg_bio_deposit_depositary = doc['us-patent-grant']['us-bibliographic-data-grant']['depositary']
            ubdg_bio_deposit_bio_accno = doc['us-patent-grant']['us-bibliographic-data-grant']['bio-accno']
            ubdg_bio_deposit_id = doc['us-patent-grant']['us-bibliographic-data-grant']['@id']
            ubdg_bio_deposit_num = doc['us-patent-grant']['us-bibliographic-data-grant']['@num']
            ubdg_bio_deposit_url = doc['us-patent-grant']['us-bibliographic-data-grant']['@url']
            ubdg_bio_deposit_dnum = doc['us-patent-grant']['us-bibliographic-data-grant']['@dnum']
            try:
                try:#null
                    ubdg_bio_deposit_date = doc['us-patent-grant']['us-bibliographic-data-grant']['date']
            except:
                pass
            try:
                try:#null
                    ubdg_bio_deposit_term = doc['us-patent-grant']['us-bibliographic-data-grant']['term']
            except:
                pass
            try:
                ubdg_bio_deposit_dtext = doc['us-patent-grant']['us-bibliographic-data-grant']['dtext']#null
            except:
                pass
                #null
        def rule47flag(self,xml ):
            ubdg_rule_47_flag = doc['us-patent-grant']['us-bibliographic-data-grant']['rule-47-flag']#null

            #null
        def usIssuedOnContinuedProsecutionApplication(self,xml):
            ubdg_us_issued_on_continued_prosecution_application_cpa_text = doc['us-patent-grant']['us-bibliographic-data-grant']['us-issued-on-continued-prosecution-application']['grant-cpa-text']

            #null
        def rule47flag(self,xml ):
            ubdg_rule_47_flag = doc['us-patent-grant']['us-bibliographic-data-grant']['rule-47-flag']
            #null
        def classificationIpc(self, xml):
            ubdg_classification_ipc =doc['us-patent-grant']['us-bibliographic-data-grant']['classification-ipc']


            #null
        def text(self, xml):
            ubdg_text = doc['us-patent-grant']['us-bibliographic-data-grant']['text']

            #null
        def referencesCitedExceptCitation(self, xml):
            ubdg_date_search_completed = doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['date-search-completed']
            ubdg_date_search_report_mailed = doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['date-search-report-mailed']
            ubdg_place_of_search = doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['place-of-search']
            ubdg_search_report_publication =doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['search-report-publication']
            ubdg_searcher = doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['searcher']



            #null
        def usMicroformquantity(self, xml):
            ubdg_us_microform_quantity = doc['us-patent-grant']['us-bibliographic-data-grant']['us-microform-quantity']
            #null
        def usDeceasedInventor(self, xml):
            ubdg_us_deceased_inventor_sequence = doc['us-patent-grant']['us-bibliographic-data-grant']['us-deceased-inventor']['@sequence']
            ubdg_us_deceased_inventor_addressbook = doc['us-patent-grant']['us-bibliographic-data-grant']['us-deceased-inventor']['addressbook']


            #null
        def correspondenceAddress(self,xml):
            ubdg_parties_correspondence_address_customer_number = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['correspondence-address']['customer-number']
            ubdg_parties_correspondence_address_addressbook = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['correspondence-address']['addressbook']


            #null
        def pctOrRegionalFillingData(self,xml):
            ubdg_pct_or_regional_filling_data_document_id = doc['us-patent-grant']['us-bibliographic-data-grant']['pct-or-regional-filling-data']['document-id']
            try:
                #null
                ubdg_pct_or_regional_filling_data_us_date = doc['us-patent-grant']['us-bibliographic-data-grant']['pct-or-regional-filling-data']['us-371c124-date']
            except:
                pass
                #null
        def pctOrReginalPublishingData(self, xml):
            ubdg_pct_or_regional_publishing_data_document_id = doc['us-patent-grant']['us-bibliographic-data-grant']['pct-or-regional-publishing-data']['document-id']
            try:
                #null
                ubdg_pct_or_regional_publishing_data_gazette_reference = doc['us-patent-grant']['us-bibliographic-data-grant']['pct-or-regional-publishing-data']['gazette-reference']
            except:
                pass

                #null
        def drawing(self,xml):
            ubdg_drawing = doc['us-patent-grant']['drawings']
            #null
        def sequenceListDoc(self,xml):
            ubdg_us_sequence_list_doc = doc['us-patent-grant']['us-sequence-list-doc']

        def tableExternalDoc(self,xml):
            ubdg_table_external_doc = doc['us-patent-grant']['table-external-doc']
        def usChemistry(self,xml):
            ubdg_us_chemistry = doc['us-patent-grant']['us-chemistry']

        def usMath(self,xml):
            ubdg_us_math = doc['us-patent-grant']['us-math']

        def abstract(self,xml):
            ubdg_abstract = doc['us-patent-grant']['abstract']
        def megaTable(self,xml):
            ubdg_mega_table =doc['us-patent-grant']['us-megatable-doc']

            #NULL
        def usBotantic(self, xml):
            ubdg_us_botantic_latin_name=doc['us-patent-grant']['us-bibliographic-data-grant']['us-botantic']['latin-name']
            ubdg_us_botantic_variety=doc['us-patent-grant']['us-bibliographic-data-grant']['us-botantic']['variety']

            #NULL
        def agent(self,xml):

            ubdg_parties_agents_agent_sequence = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['@sequence']
            ubdg_parties_agents_agent_rep_type = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['@rep-type']
            ubdg_parties_agents_agent_addressbook_orgname = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['addressbook']['orgname']
            ubdg_parties_agents_agent_addressbook_address_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['addressbook']['address']['country']

            #NULL
        def assignee(self,xml):

            ubdg_assignees_assignee_address_orgname = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['orgname']
            ubdg_assignees_assignee_address_role = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['role']
            ubdg_assignees_assignee_address_address_city = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['address']['city']
            ubdg_assignees_assignee_address_address_state = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['address']['state']
            ubdg_assignees_assignee_address_address_country = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['address']['country']



            #null
        def patcit(self,xml):
            patcit=[]

            for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['citation'])):
                patcit.append((doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['citation'])[i])


            patcit_num = []
            patcit_country = []
            patcit_doc_number = []
            patcit_kind = []
            patcit_name = []
            patcit_date = []
            patcit_category = []
            patcit_classification_country =[]
            patcit_classification_main =[]
            nplcit_num =[]
            nplcit_othercit=[]


            for j in patcit:
                patcit_number = j['patcit']['@num']
                patcit_doc_country = j['patcit']['document-id']['country']
                patcit_doc_docnumber = j['patcit']['document-id']['doc-number']
                patcit_doc_kind = j['patcit']['document-id']['kind']
                patcit_doc_name = j['patcit']['document-id']['name']
                patcit_doc_date = j['patcit']['document-id']['date']
                patcit_c_category =j['patcit']['category']
                patcit_c_classification_country =j['patcit']['classification-national']['country']
                patcit_c_classification_main = j['patcit']['classification-national']['main-classification']
                patcit_num.append(patcit_number)
                patcit_country.append(patcit_doc_country)
                patcit_doc_number.append(patcit_doc_docnumber)
                patcit_kind.append(patcit_doc_kind)
                patcit_name.append(patcit_doc_name)
                patcit_date.append(patcit_doc_date)
                patcit_classification_country.append(patcit_c_classification_country)
                patcit_category.appen(patcit_c_category)
                patcit_classification_main.append(patcit_c_classification_main)
                nplcit_number = j['nplcit']['@num']
                nplcit_othercitation = j['nplcit']['othercit']

                nplcit_num.append(nplcit_number)
                nplcit_othercit.append(nplcit_othercitation)


                #null
        def classification(self,xml):
            try:
                #null
                us_classifications_ipcr = doc['us-patent-grant']['us-bibliographic-data-grant']['us-field-of-classification-search']['us-classifications-ipcr']
            except:
                pass

            classification_national = []
            for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-field-of-classification-search']['classification-national'])):
                classification_national.append((doc['us-patent-grant']['us-bibliographic-data-grant']['us-field-of-classification-search']['classification-national'])[i])

            classification_country = []
            classification_main = []

            for i in classification_national:
                classificiation_c = i['country']
                classificiation_m = i['main-classification']
                classification_country.append(classificiation_c)
                classification_main.append(classificiation_m)

                #null
        def furtherClassification(self,xml):
            further = []
            for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national']['further-classification'])):
                further.append((doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national']['further-classification']))

            further_classification = []

            for i in further:
                further_class = i
                further_classification.append(further_class)

                #null
        def classificationIpcr:

            if range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'])) ==0:

                ubdg_csipcr_cipcr_ipc_ver_indicator_date = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-ipcr']['ipc-version-indicator']['date']
                ubdg_csipcr_cipcr_classification_level = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-level']
                ubdg_csipcr_cipcr_section = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['section']
                ubdg_csipcr_cipcr_class= doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['class']
                ubdg_csipcr_cipcr_subclass =doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['subclass']
                ubdg_csipcr_cipcr_main_group =doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['main-group']
                ubdg_csipcr_cipcr_subgroup = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['subgroup']
                ubdg_csipcr_cipcr_symbol_position = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['symbol-position']
                ubdg_csipcr_cipcr_classification_value = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-value']
                ubdg_csipcr_cipcr_action_date =doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['action-date']['date']
                ubdg_csipcr_cipcr_generating_office_country =doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['generating-office']['country']
                ubdg_csipcr_cipcr_classification_status =doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-status']
                ubdg_csipcr_cipcr_classification_data_source = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-data-source']

            else:
                classifications_ipcr = []
                for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'])):
                    classifications_ipcr.append((doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'])[i])

                classification_ipc_version_indicator_date = []
                classification_level = []
                classification_section = []
                classification_class = []
                classification_subclass =[]
                classification_main_group =[]
                classification_subgroup =[]
                classification_symbol_position =[]
                classification_value = []
                classification_action_date = []
                classification_generating_office_country = []
                classification_status = []
                classification_data_source = []

                for i in classifications_ipcr:
                    ubdg_csipcr_cipcr_ipc_ver_indicator_date = i['ipc-version-indicator']['date']
                    ubdg_csipcr_cipcr_classification_level = i['classification-level']
                    ubdg_csipcr_cipcr_section = i['section']
                    ubdg_csipcr_cipcr_class = i['class']
                    ubdg_csipcr_cipcr_subclass = i['subclass']
                    ubdg_csipcr_cipcr_main_group = i['main-group']
                    ubdg_csipcr_cipcr_subgroup = i['subgroup']
                    ubdg_csipcr_cipcr_symbol_position = i['symbol-position']
                    ubdg_csipcr_cipcr_classification_value = i['classification-value']
                    ubdg_csipcr_cipcr_action_date = i['action-date']['date']
                    ubdg_csipcr_cipcr_generating_office_country = i['generating-office']['country']
                    ubdg_csipcr_cipcr_classification_status = i['classification-status']
                    ubdg_csipcr_cipcr_classification_data_source = i['classification-data-source']
                    classification_ipc_version_indicator_date.append(ubdg_csipcr_cipcr_ipc_ver_indicator_date)
                    classification_level.append(ubdg_csipcr_cipcr_classification_level)
                    classification_section.append(ubdg_csipcr_cipcr_section)
                    classification_class.append(ubdg_csipcr_cipcr_class)
                    classification_subclass.append(ubdg_csipcr_cipcr_subclass)
                    classification_main_group.append(ubdg_csipcr_cipcr_main_group)
                    classification_subgroup.append(ubdg_csipcr_cipcr_subgroup)
                    classification_symbol_position.append(ubdg_csipcr_cipcr_symbol_position)
                    classification_value.append(ubdg_csipcr_cipcr_classification_value)
                    classification_action_date.append(ubdg_csipcr_cipcr_action_date)
                    classification_generating_office_country.append(ubdg_csipcr_cipcr_generating_office_country)
                    classification_status.append(ubdg_csipcr_cipcr_classification_status)
                    classification_data_source.append(ubdg_csipcr_cipcr_classification_data_source)


        def applicant(self,xml):

            #applicant가 1개일 경우
            if range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant'])) == 0:

                ubdg_parties_applicants_applicant_sequence = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['@sequence']
                ubdg_parties_applicants_applicant_app_type = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['@app-type']
                ubdg_parties_applicants_applicant_designation = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['@designation']
                ubdg_parties_applicants_applicant_addressbook_last_name = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['last-name']
                ubdg_parties_applicants_applicant_addressbook_first_name = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['first-name']
                ubdg_parties_applicants_applicant_addressbook_address_street = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['street']
                ubdg_parties_applicants_applicant_addressbook_address_city = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['city']
                ubdg_parties_applicants_applicant_addressbook_address_state = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['state']
                ubdg_parties_applicants_applicant_addressbook_address_postcode = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['postcode']
                ubdg_parties_applicants_applicant_addressbook_address_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['country']
                ubdg_parties_applicants_applicant_nationality_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['nationality']['country']
                ubdg_parties_applicants_applicant_residence_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['residence']['country']

            #applicant가 2개이상일   경우
            else:
                applicant = []
                for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant'])):
                    applicant.append((doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant'])[i])

                applicant_sequence =[]
                applicant_app_type =[]
                applicant_designation =[]
                applicant_address_last_name =[]
                applicant_address_first_name =[]
                applicant_address_city =[]
                applicant_address_state =[]
                applicant_address_country =[]
                applicant_nationality_country =[]
                applicant_residence_country =[]
                applicant_address_street = []
                applicant_address_postcode=[]


                for i in applicant:
                    ubdg_parties_applicants_applicant_sequence = i['@sequence']
                    ubdg_parties_applicants_applicant_app_type = i['@app-type']
                    ubdg_parties_applicants_applicant_designation = i['@designation']
                    ubdg_parties_applicants_applicant_addressbook_last_name = i['addressbook']['last-name']
                    ubdg_parties_applicants_applicant_addressbook_first_name = i['addressbook']['first-name']
                    ubdg_parties_applicants_applicant_addressbook_address_state = i['addressbook']['address']['state']
                    ubdg_parties_applicants_applicant_addressbook_address_street = i['addressbook']['address']['street']
                    ubdg_parties_applicants_applicant_addressbook_address_postcode = i['addressbook']['address']['postcode']
                    ubdg_parties_applicants_applicant_addressbook_address_city = i['addressbook']['address']['city']
                    ubdg_parties_applicants_applicant_addressbook_address_country = i['addressbook']['address']['country']
                    ubdg_parties_applicants_applicant_nationality_country = i['nationality']['country']
                    ubdg_parties_applicants_applicant_residence_country = i['residence']['country']
                    applicant_sequence.append(ubdg_parties_applicants_applicant_sequence)
                    applicant_app_type.append(ubdg_parties_applicants_applicant_app_type)
                    applicant_designation.append(ubdg_parties_applicants_applicant_designation)
                    applicant_address_last_name.append(ubdg_parties_applicants_applicant_addressbook_last_name)
                    applicant_address_first_name.append(ubdg_parties_appli cants_applicant_addressbook_first_name)
                    applicant_address_street.append(ubdg_parties_applicants_applicant_addressbook_address_street)
                    applicant_address_postcode.append(ubdg_parties_applicants_applicant_addressbook_address_postcode)
                    applicant_address_city.append(ubdg_parties_applicants_applicant_addressbook_address_city)
                    applicant_address_state.append(ubdg_parties_applicants_applicant_addressbook_address_state)
                    applicant_address_country.append(ubdg_parties_applicants_applicant_addressbook_address_country)
                    applicant_nationality_country.append(ubdg_parties_applicants_applicant_nationality_country)
                    applicant_residence_country.append(ubdg_parties_applicants_applicant_residence_country)
                    #null
        def beforeRelation(relation):
            us_related_documents = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']

            different_tags = []
            for i in us_related_documents.keys():
                different_tags.append(i)

            relation_list =[]
            for i in different_tags:
                get_relation = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents'][i]
                if isinstance(get_relation, type(list)) is True:
                    for j in range(len(get_relation)-1):
                        for k in get_relation:
                            relation_list.append(k)
                else:
                    relation_list.append(get_relation)
            relation(relation_list)

            #null
        def relation(has_relation):

            ubdg_relateddoc_relation_parentdoc_di_country= []
            ubdg_relateddoc_relation_parentdoc_di_doc_number =[]
            ubdg_relateddoc_relation_parentdoc_di_kind=[]
            ubdg_relateddoc_relation_parentdoc_di_date=[]
            ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_country=[]
            ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_doc_number=[]
            ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_kind=[]
            ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_date=[]
            ubdg_relateddoc_relation_parentdoc_childdoc_country=[]
            ubdg_relateddoc_relation_parentdoc_childdoc_doc_number=[]
            ubdg_relateddoc_relation_parentdoc_parent_status=[]

            for relation_element in has_relation:

                ubdg_relateddoc_relation_parentdoc_di_country.append(relation_element['relation']['parent-doc']['document-id']['country'])
                ubdg_relateddoc_relation_parentdoc_di_doc_number.append(relation_element['relation']['parent-doc']['document-id']['doc-number'])
                ubdg_relateddoc_relation_parentdoc_di_kind.append(relation_element['relation']['parent-doc']['document-id']['kind'])
                ubdg_relateddoc_relation_parentdoc_di_date.append(relation_element['relation']['parent-doc']['document-id']['date'])

                ubdg_relateddoc_relation_parentdoc_childdoc_country.append(relation_element['relation']['child-doc']['document-id']['country'])
                ubdg_relateddoc_relation_parentdoc_childdoc_doc_number.append(relation_element['relation']['child-doc']['document-id']['doc-number'])

                #null
                try:
                    realtion_parent_grant_doc_country = relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['country']
                    realtion_parent_grant_doc_number = relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['doc-number']
                    realtion_parent_grant_doc_kind = relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['kind']
                    realtion_parent_grant_doc_date = relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['date']
                    ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_country.append(realtion_parent_grant_doc_country)
                    ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_doc_number.append(realtion_parent_grant_doc_number)
                    ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_kind.append(realtion_parent_grant_doc_kind)
                    ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_date.append(realtion_parent_grant_doc_date)
                except:
                    pass

                try:
                    relation_parent_status = relation_element['relation']['parent-doc']['parent_status']
                    ubdg_relateddoc_relation_parentdoc_parent_status.append(relation_parent_status)
                except:
                    pass
                    #null
        def usRelation(self,xml):
            ubdg_relateddoc_us_relation_parentdoc_di_country= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['document-id']['country']
            ubdg_relateddoc_us_relation_parentdoc_di_doc_number=doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['doc-number']
            ubdg_relateddoc_us_relation_parentdoc_di_kind= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['kind']
            ubdg_relateddoc_us_relation_parentdoc_di_date= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['date']
            ubdg_relateddoc_us_relation_parentdoc_parentgrantdoc_di_country= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['parent-grant-document']['document-id']['country']
            ubdg_relateddoc_us_relation_parentdoc_parentgrantdoc_di_doc_number= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['parent-grant-document']['document-id']['doc-number']
            ubdg_relateddoc_us_relation_parentdoc_parentgrantdoc_di_kind= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['parent-grant-document']['document-id']['kind']
            ubdg_relateddoc_us_relation_parentdoc_parentgrantdoc_di_date= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['parent-grant-document']['document-id']['date']
            ubdg_relateddoc_us_relation_parentdoc_childdoc_country= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['child-doc']['document-id']['country']
            ubdg_relateddoc_us_relation_parentdoc_childdoc_doc_number= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['child-doc']['document-id']['doc-number']
            ubdg_relateddoc_us_relation_parentdoc_parent_status= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['parent_status']

            #null
        def usProvisionalApplication(self,xml):
            ubdg_provisional_appl_doc_country= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['document-id']['country']
            ubdg_provisional_appl_doc_number= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['document-id']['doc-number']
            ubdg_provisional_appl_doc_kind= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['document-id']['kind']
            ubdg_provisional_appl_doc_date= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['document-id']['country']
            ubdg_provisional_appl_status= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['us-provisional-application-status']
            #null
        def relatedPublication(self,xml):
            ubdg_related_publ_doc_country = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication']['document-id']['country']
            ubdg_related_publ_doc_number = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication']['document-id']['doc-number']
            ubdg_related_publ_doc_kind = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication']['document-id']['kind']
            ubdg_related_publ_doc_date = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication']['document-id']['date']


    class parserVer42(Parser):
        def __init__(self,xml):
            super().__init__(xml)


            #add us-claim-statement
            self.upg_us_claim_statement = doc['us-patent-grant']['us-claim-statement']
            #address_street
            self.ubdg_parties_applicants_applicant_addressbook_address_state = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['state']
            #assignee
            self.ubdg_assignees_assignee_address_orgname =None
            self.ubdg_assignees_assignee_address_role=None
            self.ubdg_assignees_assignee_address_address_city=None
            self.ubdg_assignees_assignee_address_address_state=None
            self.ubdg_assignees_assignee_address_address_country=None
            #agents #null
            self.ubdg_parties_agents_agent_rep_type=None
            self.ubdg_parties_agents_agent_addressbook_orgname=None
            self.ubdg_parties_agents_agent_addressbook_address_country=None
            #further 추가

            self.further=None
            self.further_classification=None
            self.further_class=None


            self.patcit_category= doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['citation']['category']
            self.patcit_classification_country=None
            self.patcit_classification_main=None

            self.us_classifications_ipcr = None
            #applicant
            self.ubdg_parties_applicants_applicant_sequence =None
            self.ubdg_parties_applicants_applicant_app_type=None
            self.ubdg_parties_applicants_applicant_designation=None
            self.ubdg_parties_applicants_applicant_addressbook_last_name=None
            self.ubdg_parties_applicants_applicant_addressbook_first_name=None
            self.ubdg_parties_applicants_applicant_addressbook_address_city=None
            self.ubdg_parties_applicants_applicant_addressbook_address_country=None
            self.ubdg_parties_applicants_applicant_nationality_country=None
            self.ubdg_parties_applicants_applicant_residence_country=None
            self.applicant=None
            self.applicant_sequence=None
            self.pplicant_designation=None
            self.applicant_app_type=None
            self.applicant_address_last_name=None
            self.applicant_address_first_name=None
            self.applicant_address_city=None
            self.applicant_address_state=None
            self.applicant_address_country=None
            self.applicant_nationality_country=None
            self.applicant_residence_country=None
            #null
            self.applicant_address_street=None
            self.applicant_address_postcode=None


            #megaTable
            self.ubdg_mega_table = None

            self.ubdg_us_deceased_inventor_sequence= None
            self.ubdg_us_deceased_inventor_addressbook= None
            self.ubdg_parties_correspondence_address_customer_number= None
            self.ubdg_parties_correspondence_address_addressbook= None

            #inventor
            self.parties_inventors_inventor_sequence=None
            self.ubdg_parties_inventors_inventor_designation=None
            self.ubdg_parties_inventors_inventor_addressbook_last_name=None
            self.ubdg_parties_inventors_inventor_addressbook_first_name=None
            self.ubdg_parties_inventors_inventor_addressbook_address_city=None
            self.ubdg_parties_inventors_inventor_addressbook_address_state=None
            self.ubdg_parties_inventors_inventor_addressbook_address_country=None
            self.self.inventor=None
            self.inventor_sequence=None
            self.inventor_designation=None
            self.inventor_address_last_name=None
            self.inventor_address_first_name=None
            self.inventor_address_city=None
            self.inventor_address_state=None
            self.inventor_address_country=None



        #null
        def assisatntExaminer(self,xml):
            null_variables = []
            null_variables.append(ubdg_examiners_assistant_examiner_last_name)
            null_variables.append(ubdg_examiners_assistant_examiner_first_name)

            null_tag = []
            null_tag.append(doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['assistant-examiner']['last-name'])
            null_tag.append(doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['assistant-examiner']['first-name'])

            for v,t in zip(null_variables, null_tag):
                if v == t:
                    v =  t

                    #null
        def inventors(self,xml):
            if range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor'])) == 0:

                ubdg_parties_inventors_inventor_sequence = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['@sequence']
                ubdg_parties_inventors_inventor_designation = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['@designation']
                ubdg_parties_inventors_inventor_addressbook_last_name = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook']['last-name']
                ubdg_parties_inventors_inventor_addressbook_first_name = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook']['first-name']
                ubdg_parties_inventors_inventor_addressbook_address_city = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook']['address']['city']
                ubdg_parties_inventors_inventor_addressbook_address_state = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook']['address']['state']
                ubdg_parties_inventors_inventor_addressbook_address_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook']['address']['country']

            else:
                inventor = []
                for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor'])):
                    applicant.append((doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor'])[i])

                inventor_sequence =[]
                inventor_designation =[]
                inventor_address_last_name =[]
                inventor_address_first_name =[]
                inventor_address_city =[]
                inventor_address_state =[]
                inventor_address_country =[]

                for i in inventor:
                    ubdg_parties_inventors_inventor_sequence = i['@sequence']
                    ubdg_parties_inventors_inventor_designation = i['@designation']
                    ubdg_parties_inventors_inventor_addressbook_last_name = i['addressbook']['last-name']
                    ubdg_parties_inventors_inventor_addressbook_first_name = i['addressbook']['first-name']
                    ubdg_parties_inventors_inventor_addressbook_address_state = i['addressbook']['address']['state']
                    ubdg_parties_inventors_inventor_addressbook_address_city = i['addressbook']['address']['city']
                    ubdg_parties_inventors_inventor_addressbook_address_country = i['addressbook']['address']['country']
                    inventor_sequence.append(ubdg_parties_inventors_inventor_sequence)
                    inventor_designation.append(ubdg_parties_inventors_inventor_designation)
                    inventor_address_last_name.append(ubdg_parties_inventors_inventor_addressbook_last_name)
                    inventor_address_first_name.append(ubdg_parties_inventors_inventor_addressbook_first_name)
                    inventor_address_city.append(ubdg_parties_inventors_inventor_addressbook_address_city)
                    inventor_address_state.append(ubdg_parties_inventors_inventor_addressbook_address_state)
                    inventor_address_country.append(ubdg_parties_inventors_inventor_addressbook_address_country)



                    #null
        def termOfGrant(self,xml):
            ubdg_utog_len_grant = doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant']['length-of-grant']
            ubdg_utog_text_grant = doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant']['text']
            ubdg_utog_extension_grant = doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant']['us-term-extension']
            ubdg_utog_disclaimer_grant = doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant']['disclaimer']
            ubdg_utog_lapse_grant = doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant']['lapse-of-patent']
            #null
        def classificationsIpcrID(self, xml):
            ubdg_us_botantic_latin_name=doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['@id']
            #null
        def biblioClassifiacationLocarno(self, xml):
            ubdg_classificattion_locarno_edition = doc['us-patent-grant']['us-bibliographic-data-grant']['classification-locarno']['edition']
            ubdg_classificattion_locarno_main_classification = doc['us-patent-grant']['us-bibliographic-data-grant']['classification-locarno']['main-classification']
            #null
        def biblioClassifiacationNational(self,xml):
            ubdg_classificattion_national_country = doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national']['country']
            ubdg_classificattion_national_main_classification = doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national']['main-classification']
            #null
        def nuumberOfClaims(self, xml):
            ubdg_number_of_claims = doc['us-patent-grant']['us-bibliographic-data-grant']['number-of-claims']
            #null
        def Exemplary_claim(self, xml):
            ubdg_us_exemplary_claim = doc['us-patent-grant']['us-bibliographic-data-grant']['us-exemplary-claim']

            #null
        def examiners(self, xml):
            ubdg_examiners_primary_examiner_last_name = doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['last-name']
            ubdg_examiners_primary_examiner_first_name = doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['first-name']
            ubdg_examiners_primary_examiner_department = doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['department']
            #null
        def usFlagSirText(self,xml):
            ubdg_us_sir_flag_sir_text = ['us-patent-grant']['us-bibliographic-data-grant']['us-sir-flag']['@sir-text']
            #null
        def parentFamily (self, xml):
            ubdg_patent_family_priority_application = doc['us-patent-grant']['us-bibliographic-data-grant']['patent-family']['priority-application']
            #null
        def bioDeposit(self, xml):
            ubdg_bio_deposit_depositary = doc['us-patent-grant']['us-bibliographic-data-grant']['depositary']
            ubdg_bio_deposit_bio_accno = doc['us-patent-grant']['us-bibliographic-data-grant']['bio-accno']
            ubdg_bio_deposit_id = doc['us-patent-grant']['us-bibliographic-data-grant']['@id']
            ubdg_bio_deposit_num = doc['us-patent-grant']['us-bibliographic-data-grant']['@num']
            ubdg_bio_deposit_url = doc['us-patent-grant']['us-bibliographic-data-grant']['@url']
            ubdg_bio_deposit_dnum = doc['us-patent-grant']['us-bibliographic-data-grant']['@dnum']
            try:
                #null
                ubdg_bio_deposit_date = doc['us-patent-grant']['us-bibliographic-data-grant']['date']
            except:
                pass
            try:
                #null
                ubdg_bio_deposit_term = doc['us-patent-grant']['us-bibliographic-data-grant']['term']
            except:
                pass
            try:
                #null
                ubdg_bio_deposit_dtext = doc['us-patent-grant']['us-bibliographic-data-grant']['dtext']
            except:
                pass
                #null
        def rule47flag(self,xml ):
            ubdg_rule_47_flag = doc['us-patent-grant']['us-bibliographic-data-grant']['rule-47-flag']

            #null
        def usIssuedOnContinuedProsecutionApplication(self,xml):
            ubdg_us_issued_on_continued_prosecution_application_cpa_text = doc['us-patent-grant']['us-bibliographic-data-grant']['us-issued-on-continued-prosecution-application']['grant-cpa-text']

            #null
        def rule47flag(self,xml ):
            ubdg_rule_47_flag = doc['us-patent-grant']['us-bibliographic-data-grant']['rule-47-flag']
            #null
        def classificationIpc(self, xml):
            ubdg_classification_ipc =doc['us-patent-grant']['us-bibliographic-data-grant']['classification-ipc']

            #null
        def text(self, xml):
            ubdg_text = doc['us-patent-grant']['us-bibliographic-data-grant']['text']

            #null
        def referencesCitedExceptCitation(self, xml):
            ubdg_date_search_completed = doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['date-search-completed']
            ubdg_date_search_report_mailed = doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['date-search-report-mailed']
            ubdg_place_of_search = doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['place-of-search']
            ubdg_search_report_publication =doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['search-report-publication']
            ubdg_searcher = doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['searcher']

            #null
        def usMicroformquantity(self, xml):
            ubdg_us_microform_quantity = doc['us-patent-grant']['us-bibliographic-data-grant']['us-microform-quantity']
            #null
        def usDeceasedInventor(self, xml):
            ubdg_us_deceased_inventor_sequence = doc['us-patent-grant']['us-bibliographic-data-grant']['us-deceased-inventor']['@sequence']
            ubdg_us_deceased_inventor_addressbook = doc['us-patent-grant']['us-bibliographic-data-grant']['us-deceased-inventor']['addressbook']

            #null
        def correspondenceAddress(self,xml):
            ubdg_parties_correspondence_address_customer_number = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['correspondence-address']['customer-number']
            ubdg_parties_correspondence_address_addressbook = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['correspondence-address']['addressbook']

            #null
        def pctOrRegionalFillingData(self,xml):
            ubdg_pct_or_regional_filling_data_document_id = doc['us-patent-grant']['us-bibliographic-data-grant']['pct-or-regional-filling-data']['document-id']
            try:
                #null
                ubdg_pct_or_regional_filling_data_us_date = doc['us-patent-grant']['us-bibliographic-data-grant']['pct-or-regional-filling-data']['us-371c124-date']
            except:
                pass
                #null
        def pctOrReginalPublishingData(self, xml):
            ubdg_pct_or_regional_publishing_data_document_id = doc['us-patent-grant']['us-bibliographic-data-grant']['pct-or-regional-publishing-data']['document-id']
            try:
                #null
                ubdg_pct_or_regional_publishing_data_gazette_reference = doc['us-patent-grant']['us-bibliographic-data-grant']['pct-or-regional-publishing-data']['gazette-reference']
            except:
                pass

                #null
        def drawing(self,xml):
            ubdg_drawing = doc['us-patent-grant']['drawings']
            #null
        def sequenceListDoc(self,xml):
            ubdg_us_sequence_list_doc = doc['us-patent-grant']['us-sequence-list-doc']
            #null
        def tableExternalDoc(self,xml):
            ubdg_table_external_doc = doc['us-patent-grant']['table-external-doc']
            #null
        def usChemistry(self,xml):
            ubdg_us_chemistry = doc['us-patent-grant']['us-chemistry']
            #null
        def usMath(self,xml):
            ubdg_us_math = doc['us-patent-grant']['us-math']
            #null
        def abstract(self,xml):
            ubdg_abstract = doc['us-patent-grant']['abstract']
            #null
        def megaTable(self,xml):
            ubdg_mega_table =doc['us-patent-grant']['us-megatable-doc']
            #NULL
        def usBotantic(self, xml):
            ubdg_us_botantic_latin_name=doc['us-patent-grant']['us-bibliographic-data-grant']['us-botantic']['latin-name']
            ubdg_us_botantic_variety=doc['us-patent-grant']['us-bibliographic-data-grant']['us-botantic']['variety']

            #NULL
        def agent(self,xml):

            ubdg_parties_agents_agent_sequence = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['@sequence']
            ubdg_parties_agents_agent_rep_type = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['@rep-type']
            ubdg_parties_agents_agent_addressbook_orgname = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['addressbook']['orgname']
            ubdg_parties_agents_agent_addressbook_address_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['addressbook']['address']['country']

            #NULL
        def assignee(self,xml):

            ubdg_assignees_assignee_address_orgname = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['orgname']
            ubdg_assignees_assignee_address_role = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['role']
            ubdg_assignees_assignee_address_address_city = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['address']['city']
            ubdg_assignees_assignee_address_address_state = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['address']['state']
            ubdg_assignees_assignee_address_address_country = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['address']['country']



            #citation에 classification natiojnal이랑 main 있음 확인 수정필요
        def patcit(self,xml):
            patcit=[]

            for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['citation'])):
                patcit.append((doc['us-patent-grant']['us-bibliographic-data-grant']['references-cited']['citation'])[i])


            patcit_num = []
            patcit_country = []
            patcit_doc_number = []
            patcit_kind = []
            patcit_name = []
            patcit_date = []
            patcit_category = []
            patcit_classification_country =[]
            patcit_classification_main =[]
            nplcit_num =[]
            nplcit_othercit=[]


            for j in patcit:
                patcit_number = j['patcit']['@num']
                patcit_doc_country = j['patcit']['document-id']['country']
                patcit_doc_docnumber = j['patcit']['document-id']['doc-number']
                patcit_doc_kind = j['patcit']['document-id']['kind']
                patcit_doc_name = j['patcit']['document-id']['name']
                patcit_doc_date = j['patcit']['document-id']['date']
                patcit_c_category =j['patcit']['category']
                patcit_c_classification_country =j['patcit']['classification-national']['country']
                patcit_c_classification_main = j['patcit']['classification-national']['main-classification']
                patcit_num.append(patcit_number)
                patcit_country.append(patcit_doc_country)
                patcit_doc_number.append(patcit_doc_docnumber)
                patcit_kind.append(patcit_doc_kind)
                patcit_name.append(patcit_doc_name)
                patcit_date.append(patcit_doc_date)
                patcit_classification_country.append(patcit_c_classification_country)
                patcit_category.appen(patcit_c_category)
                patcit_classification_main.append(patcit_c_classification_main)
                nplcit_number = j['nplcit']['@num']
                nplcit_othercitation = j['nplcit']['othercit']

                nplcit_num.append(nplcit_number)
                nplcit_othercit.append(nplcit_othercitation)


                #null
        def classification(self,xml):
            try:
                #null
                us_classifications_ipcr = doc['us-patent-grant']['us-bibliographic-data-grant']['us-field-of-classification-search']['us-classifications-ipcr']
            except:
                pass

            classification_national = []
            for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-field-of-classification-search']['classification-national'])):
                classification_national.append((doc['us-patent-grant']['us-bibliographic-data-grant']['us-field-of-classification-search']['classification-national'])[i])

            classification_country = []
            classification_main = []

            for i in classification_national:
                classificiation_c = i['country']
                classificiation_m = i['main-classification']
                classification_country.append(classificiation_c)
                classification_main.append(classificiation_m)


                #null
        def furtherClassification(self,xml):
            further = []
            for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national']['further-classification'])):
                further.append((doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national']['further-classification']))

            further_classification = []

            for i in further:
                further_class = i
                further_classification.append(further_class)

                #null
        def classificationIpcr:

            if range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'])) ==0:

                ubdg_csipcr_cipcr_ipc_ver_indicator_date = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-ipcr']['ipc-version-indicator']['date']
                ubdg_csipcr_cipcr_classification_level = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-level']
                ubdg_csipcr_cipcr_section = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['section']
                ubdg_csipcr_cipcr_class= doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['class']
                ubdg_csipcr_cipcr_subclass =doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['subclass']
                ubdg_csipcr_cipcr_main_group =doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['main-group']
                ubdg_csipcr_cipcr_subgroup = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['subgroup']
                ubdg_csipcr_cipcr_symbol_position = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['symbol-position']
                ubdg_csipcr_cipcr_classification_value = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-value']
                ubdg_csipcr_cipcr_action_date =doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['action-date']['date']
                ubdg_csipcr_cipcr_generating_office_country =doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['generating-office']['country']
                ubdg_csipcr_cipcr_classification_status =doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-status']
                ubdg_csipcr_cipcr_classification_data_source = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-data-source']

            else:
                classifications_ipcr = []
                for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'])):
                    classifications_ipcr.append((doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'])[i])

                classification_ipc_version_indicator_date = []
                classification_level = []
                classification_section = []
                classification_class = []
                classification_subclass =[]
                classification_main_group =[]
                classification_subgroup =[]
                classification_symbol_position =[]
                classification_value = []
                classification_action_date = []
                classification_generating_office_country = []
                classification_status = []
                classification_data_source = []

                for i in classifications_ipcr:
                    ubdg_csipcr_cipcr_ipc_ver_indicator_date = i['ipc-version-indicator']['date']
                    ubdg_csipcr_cipcr_classification_level = i['classification-level']
                    ubdg_csipcr_cipcr_section = i['section']
                    ubdg_csipcr_cipcr_class = i['class']
                    ubdg_csipcr_cipcr_subclass = i['subclass']
                    ubdg_csipcr_cipcr_main_group = i['main-group']
                    ubdg_csipcr_cipcr_subgroup = i['subgroup']
                    ubdg_csipcr_cipcr_symbol_position = i['symbol-position']
                    ubdg_csipcr_cipcr_classification_value = i['classification-value']
                    ubdg_csipcr_cipcr_action_date = i['action-date']['date']
                    ubdg_csipcr_cipcr_generating_office_country = i['generating-office']['country']
                    ubdg_csipcr_cipcr_classification_status = i['classification-status']
                    ubdg_csipcr_cipcr_classification_data_source = i['classification-data-source']
                    classification_ipc_version_indicator_date.append(ubdg_csipcr_cipcr_ipc_ver_indicator_date)
                    classification_level.append(ubdg_csipcr_cipcr_classification_level)
                    classification_section.append(ubdg_csipcr_cipcr_section)
                    classification_class.append(ubdg_csipcr_cipcr_class)
                    classification_subclass.append(ubdg_csipcr_cipcr_subclass)
                    classification_main_group.append(ubdg_csipcr_cipcr_main_group)
                    classification_subgroup.append(ubdg_csipcr_cipcr_subgroup)
                    classification_symbol_position.append(ubdg_csipcr_cipcr_symbol_position)
                    classification_value.append(ubdg_csipcr_cipcr_classification_value)
                    classification_action_date.append(ubdg_csipcr_cipcr_action_date)
                    classification_generating_office_country.append(ubdg_csipcr_cipcr_generating_office_country)
                    classification_status.append(ubdg_csipcr_cipcr_classification_status)
                    classification_data_source.append(ubdg_csipcr_cipcr_classification_data_source)

        def applicant(self,xml):

            #applicant가 1개일 경우
            if range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant'])) == 0:

                ubdg_parties_applicants_applicant_sequence = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['@sequence']
                ubdg_parties_applicants_applicant_app_type = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['@app-type']
                ubdg_parties_applicants_applicant_designation = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['@designation']
                ubdg_parties_applicants_applicant_addressbook_last_name = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['last-name']
                ubdg_parties_applicants_applicant_addressbook_first_name = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['first-name']
                ubdg_parties_applicants_applicant_addressbook_address_street = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['street']
                ubdg_parties_applicants_applicant_addressbook_address_city = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['city']
                ubdg_parties_applicants_applicant_addressbook_address_state = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['state']
                ubdg_parties_applicants_applicant_addressbook_address_postcode = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['postcode']
                ubdg_parties_applicants_applicant_addressbook_address_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['addressbook']['address']['country']
                ubdg_parties_applicants_applicant_nationality_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['nationality']['country']
                ubdg_parties_applicants_applicant_residence_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant']['residence']['country']

            #applicant가 2개이상일   경우
            else:
                applicant = []
                for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant'])):
                    applicant.append((doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['applicants']['applicant'])[i])

                applicant_sequence =[]
                applicant_app_type =[]
                applicant_designation =[]
                applicant_address_last_name =[]
                applicant_address_first_name =[]
                applicant_address_city =[]
                applicant_address_state =[]

                applicant_address_country =[]
                applicant_nationality_country =[]
                applicant_residence_country =[]
                applicant_address_street = []
                applicant_address_postcode=[]


                for i in applicant:
                    ubdg_parties_applicants_applicant_sequence = i['@sequence']
                    ubdg_parties_applicants_applicant_app_type = i['@app-type']
                    ubdg_parties_applicants_applicant_designation = i['@designation']
                    ubdg_parties_applicants_applicant_addressbook_last_name = i['addressbook']['last-name']
                    ubdg_parties_applicants_applicant_addressbook_first_name = i['addressbook']['first-name']
                    ubdg_parties_applicants_applicant_addressbook_address_state = i['addressbook']['address']['state']
                    ubdg_parties_applicants_applicant_addressbook_address_street = i['addressbook']['address']['street']
                    ubdg_parties_applicants_applicant_addressbook_address_postcode = i['addressbook']['address']['postcode']
                    ubdg_parties_applicants_applicant_addressbook_address_city = i['addressbook']['address']['city']
                    ubdg_parties_applicants_applicant_addressbook_address_country = i['addressbook']['address']['country']
                    ubdg_parties_applicants_applicant_nationality_country = i['nationality']['country']
                    ubdg_parties_applicants_applicant_residence_country = i['residence']['country']
                    applicant_sequence.append(ubdg_parties_applicants_applicant_sequence)
                    applicant_app_type.append(ubdg_parties_applicants_applicant_app_type)
                    applicant_designation.append(ubdg_parties_applicants_applicant_designation)
                    applicant_address_last_name.append(ubdg_parties_applicants_applicant_addressbook_last_name)
                    applicant_address_first_name.append(ubdg_parties_appli cants_applicant_addressbook_first_name)
                    applicant_address_street.append(ubdg_parties_applicants_applicant_addressbook_address_street)
                    applicant_address_postcode.append(ubdg_parties_applicants_applicant_addressbook_address_postcode)
                    applicant_address_city.append(ubdg_parties_applicants_applicant_addressbook_address_city)
                    applicant_address_state.append(ubdg_parties_applicants_applicant_addressbook_address_state)
                    applicant_address_country.append(ubdg_parties_applicants_applicant_addressbook_address_country)
                    applicant_nationality_country.append(ubdg_parties_applicants_applicant_nationality_country)
                    applicant_residence_country.append(ubdg_parties_applicants_applicant_residence_country)
                    #null
        def beforeRelation(relation):
            us_related_documents = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']

            different_tags = []
            for i in us_related_documents.keys():
                different_tags.append(i)

            relation_list =[]
            for i in different_tags:
                get_relation = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents'][i]
                if isinstance(get_relation, type(list)) is True:
                    for j in range(len(get_relation)-1):
                        for k in get_relation:
                            relation_list.append(k)
                else:
                    relation_list.append(get_relation)
            relation(relation_list)
            #null
        def relation(has_relation):

            ubdg_relateddoc_relation_parentdoc_di_country= []
            ubdg_relateddoc_relation_parentdoc_di_doc_number =[]
            ubdg_relateddoc_relation_parentdoc_di_kind=[]
            ubdg_relateddoc_relation_parentdoc_di_date=[]
            ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_country=[]
            ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_doc_number=[]
            ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_kind=[]
            ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_date=[]
            ubdg_relateddoc_relation_parentdoc_childdoc_country=[]
            ubdg_relateddoc_relation_parentdoc_childdoc_doc_number=[]
            ubdg_relateddoc_relation_parentdoc_parent_status=[]

            for relation_element in has_relation:

                ubdg_relateddoc_relation_parentdoc_di_country.append(relation_element['relation']['parent-doc']['document-id']['country'])
                ubdg_relateddoc_relation_parentdoc_di_doc_number.append(relation_element['relation']['parent-doc']['document-id']['doc-number'])
                ubdg_relateddoc_relation_parentdoc_di_kind.append(relation_element['relation']['parent-doc']['document-id']['kind'])
                ubdg_relateddoc_relation_parentdoc_di_date.append(relation_element['relation']['parent-doc']['document-id']['date'])

                ubdg_relateddoc_relation_parentdoc_childdoc_country.append(relation_element['relation']['child-doc']['document-id']['country'])
                ubdg_relateddoc_relation_parentdoc_childdoc_doc_number.append(relation_element['relation']['child-doc']['document-id']['doc-number'])

                #null
                try:
                    realtion_parent_grant_doc_country = relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['country']#null
                    realtion_parent_grant_doc_number = relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['doc-number']#null
                    realtion_parent_grant_doc_kind = relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['kind']#null
                    realtion_parent_grant_doc_date = relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['date']#null
                    ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_country.append(realtion_parent_grant_doc_country)
                    ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_doc_number.append(realtion_parent_grant_doc_number)
                    ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_kind.append(realtion_parent_grant_doc_kind)
                    ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_date.append(realtion_parent_grant_doc_date)
                except:
                    pass

                try:
                    #null
                    relation_parent_status = relation_element['relation']['parent-doc']['parent_status']#null
                    ubdg_relateddoc_relation_parentdoc_parent_status.append(relation_parent_status)
                except:
                    pass
                    #null
        def usRelation(self,xml):
            ubdg_relateddoc_us_relation_parentdoc_di_country= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['document-id']['country']
            ubdg_relateddoc_us_relation_parentdoc_di_doc_number=doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['doc-number']
            ubdg_relateddoc_us_relation_parentdoc_di_kind= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['kind']
            ubdg_relateddoc_us_relation_parentdoc_di_date= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['date']
            ubdg_relateddoc_us_relation_parentdoc_parentgrantdoc_di_country= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['parent-grant-document']['document-id']['country']
            ubdg_relateddoc_us_relation_parentdoc_parentgrantdoc_di_doc_number= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['parent-grant-document']['document-id']['doc-number']
            ubdg_relateddoc_us_relation_parentdoc_parentgrantdoc_di_kind= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['parent-grant-document']['document-id']['kind']
            ubdg_relateddoc_us_relation_parentdoc_parentgrantdoc_di_date= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['parent-grant-document']['document-id']['date']
            ubdg_relateddoc_us_relation_parentdoc_childdoc_country= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['child-doc']['document-id']['country']
            ubdg_relateddoc_us_relation_parentdoc_childdoc_doc_number= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['child-doc']['document-id']['doc-number']
            ubdg_relateddoc_us_relation_parentdoc_parent_status= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-divisional-reissue']['us-relation']['parent-doc']['parent_status']

            #null
        def usProvisionalApplication(self,xml):
            ubdg_provisional_appl_doc_country= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['document-id']['country']
            ubdg_provisional_appl_doc_number= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['document-id']['doc-number']
            ubdg_provisional_appl_doc_kind= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['document-id']['kind']
            ubdg_provisional_appl_doc_date= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['document-id']['country']
            ubdg_provisional_appl_status= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['us-provisional-application-status']
            #null
        def relatedPublication(self,xml):
            ubdg_related_publ_doc_country = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication']['document-id']['country']
            ubdg_related_publ_doc_number = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication']['document-id']['doc-number']
            ubdg_related_publ_doc_kind = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication']['document-id']['kind']
            ubdg_related_publ_doc_date = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication']['document-id']['date']


    class parserVer43(Parser):
        def __init__(self,xml):
            super().__init__(xml)

            #add us-claim-statement
            self.upg_us_claim_statement = doc['us-patent-grant']['us-claim-statement']
            #address_street #add us
            self.ubdg_us_parties_us_applicants_us_applicant_addressbook_address_state =doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant']['addressbook']['address']['state']
            #assignee
            self.ubdg_assignees_assignee_address_orgname =None
            self.ubdg_assignees_assignee_address_role=None
            self.ubdg_assignees_assignee_address_address_city=None
            self.ubdg_assignees_assignee_address_address_state=None
            self.ubdg_assignees_assignee_address_address_country=None
            #agents #null
            self.ubdg_parties_agents_agent_rep_type=None
            self.ubdg_parties_agents_agent_addressbook_orgname=None
            self.ubdg_parties_agents_agent_addressbook_address_country=None
            #further 추가

            self.further=None
            self.further_classification=None
            self.further_class=None

            self.patcit_category= doc['us-patent-grant']['us-bibliographic-data-grant']['us-references-cited']['us-citation']['category']
            self.patcit_classification_country=None
            self.patcit_classification_main=None

            self.us_classifications_ipcr = None
            #applicant
            self.ubdg_parties_applicants_applicant_sequence =None
            self.ubdg_parties_applicants_applicant_app_type=None
            self.ubdg_parties_applicants_applicant_designation=None
            self.ubdg_parties_applicants_applicant_addressbook_last_name=None
            self.ubdg_parties_applicants_applicant_addressbook_first_name=None
            self.ubdg_parties_applicants_applicant_addressbook_address_city=None
            self.ubdg_parties_applicants_applicant_addressbook_address_country=None
            self.ubdg_parties_applicants_applicant_residence_country=None
            self.applicant=None
            self.applicant_sequence=None
            self.pplicant_designation=None
            self.applicant_app_type=None
            self.applicant_address_last_name=None
            self.applicant_address_first_name=None
            self.applicant_address_city=None
            self.applicant_address_state=None
            self.applicant_address_country=None
            self.applicant_residence_country=None
            #null
            self.applicant_address_street=None
            ubdg_assignees_assignee_address_orgname = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['orgname']
            self.applicant_address_postcode=None


            #megaTable
            self.ubdg_mega_table = None

            #inventor
            self.parties_inventors_inventor_sequence=None
            self.ubdg_parties_inventors_inventor_designation=None
            self.ubdg_parties_inventors_inventor_addressbook_last_name=None
            self.ubdg_parties_inventors_inventor_addressbook_first_name=None
            self.ubdg_parties_inventors_inventor_addressbook_address_city=None
            self.ubdg_parties_inventors_inventor_addressbook_address_state=None
            self.ubdg_parties_inventors_inventor_addressbook_address_country=None
            self.self.inventor=None
            self.inventor_sequence=None
            self.inventor_designation=None
            self.inventor_address_last_name=None
            self.inventor_address_first_name=None
            self.inventor_address_city=None
            self.inventor_address_state=None
            self.inventor_address_country=None

            self.ubdg_parties_applicants_applicant_applicant_authority_category = None

        #null
        def assisatntExaminer(self,xml):
            null_variables = []
            null_variables.append(ubdg_examiners_assistant_examiner_last_name)
            null_variables.append(ubdg_examiners_assistant_examiner_first_name)

            null_tag = []
            null_tag.append(doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['assistant-examiner']['last-name'])
            null_tag.append(doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['assistant-examiner']['first-name'])

            for v,t in zip(null_variables, null_tag):
                if v == t:
                    v =  t
                    #null
        def termOfGrant(self,xml):
            ubdg_utog_len_grant = self.doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant']['length-of-grant']
            ubdg_utog_text_grant = self.doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant']['text']
            ubdg_utog_extension_grant = self.doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant']['us-term-extension']
            ubdg_utog_disclaimer_grant = self.doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant']['disclaimer']
            ubdg_utog_lapse_grant = self.doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant']['lapse-of-patent']

            #null
        def drawing(self,xml):
            ubdg_drawing = doc['us-patent-grant']['drawings']
            #null
        def sequenceListDoc(self,xml):
            ubdg_us_sequence_list_doc = doc['us-patent-grant']['us-sequence-list-doc']
            #null
        def tableExternalDoc(self,xml):
            ubdg_table_external_doc = doc['us-patent-grant']['table-external-doc']
            #null
        def usChemistry(self,xml):
            ubdg_us_chemistry = doc['us-patent-grant']['us-chemistry']
            #null
        def usMath(self,xml):
            ubdg_us_math = doc['us-patent-grant']['us-math']
            #null
        def abstract(self,xml):
            ubdg_abstract = doc['us-patent-grant']['abstract']
            #null
        def megaTable(self,xml):
            ubdg_mega_table =doc['us-patent-grant']['us-megatable-doc']
            #NULL
        def usBotantic(self, xml):
            ubdg_us_botantic_latin_name=doc['us-patent-grant']['us-bibliographic-data-grant']['us-botantic']['latin-name']
            ubdg_us_botantic_variety=doc['us-patent-grant']['us-bibliographic-data-grant']['us-botantic']['variety']
            #null

        def classificationsIpcrID(self, xml):
            ubdg_us_classification_ipcr_id=doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['@id']
            #null
        def classificationsCpc(self, xml):
            ubdg_us_classification_cpc=doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-cpc']
            #null
        def biblioClassifiacationLocarno(self, xml):
            ubdg_classificattion_locarno_edition = doc['us-patent-grant']['us-bibliographic-data-grant']['classification-locarno']['edition']
            ubdg_classificattion_locarno_main_classification = doc['us-patent-grant']['us-bibliographic-data-grant']['classification-locarno']['main-classification']
            #null
        def biblioClassifiacationNational(self,xml):
            ubdg_classificattion_national_country = doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national']['country']
            ubdg_classificattion_national_main_classification = doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national']['main-classification']
            #null
        def nuumberOfClaims(self, xml):
            ubdg_number_of_claims = doc['us-patent-grant']['us-bibliographic-data-grant']['number-of-claims']
            #null
        def Exemplary_claim(self, xml):
            ubdg_us_exemplary_claim = doc['us-patent-grant']['us-bibliographic-data-grant']['us-exemplary-claim']
            #null
        def figures(self, xml):
            ubdg_figures_number_of_drawing_sheets = doc['us-patent-grant']['us-bibliographic-data-grant']['figures']['number-of-drawing-sheets']
            ubdg_figures_number_of_figures = doc['us-patent-grant']['us-bibliographic-data-grant']['figures']['number-of-figures']
            #null
        def examiners(self, xml):
            ubdg_examiners_primary_examiner_last_name = doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['last-name']
            ubdg_examiners_primary_examiner_first_name = doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['first-name']
            ubdg_examiners_primary_examiner_department = doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['department']
            #null
        def usFlagSirText(self,xml):
            ubdg_us_sir_flag_sir_text = ['us-patent-grant']['us-bibliographic-data-grant']['us-sir-flag']['@sir-text']

            #NULL
        def agent(self,xml):

            ubdg_parties_agents_agent_sequence = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['@sequence']
            ubdg_parties_agents_agent_rep_type = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['@rep-type']
            ubdg_parties_agents_agent_addressbook_orgname = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['addressbook']['orgname']
            ubdg_parties_agents_agent_addressbook_address_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['addressbook']['address']['country']

            #NULL
        def assignee(self,xml):
            ubdg_assignees_assignee_address_orgname = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['orgname']
            ubdg_assignees_assignee_address_role = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['role']
            ubdg_assignees_assignee_address_address_city = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['address']['city']
            ubdg_assignees_assignee_address_address_state = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['address']['state']
            ubdg_assignees_assignee_address_address_country = doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['address']['country']

            #null
        def patcit(self,xml):
            patcit=[]

            for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-references-cited']['us-citation'])):
                patcit.append((doc['us-patent-grant']['us-bibliographic-data-grant']['us-references-cited']['us-citation'])[i])

            patcit_num = []
            patcit_country = []
            patcit_doc_number = []
            patcit_kind = []
            patcit_name = []
            patcit_date = []
            patcit_category = []
            patcit_classification_country =[]
            patcit_classification_main =[]
            nplcit_num =[]
            nplcit_othercit=[]

            for j in patcit:
                patcit_number = j['patcit']['@num']
                patcit_doc_country = j['patcit']['document-id']['country']
                patcit_doc_docnumber = j['patcit']['document-id']['doc-number']
                patcit_doc_kind = j['patcit']['document-id']['kind']
                patcit_doc_name = j['patcit']['document-id']['name']
                patcit_doc_date = j['patcit']['document-id']['date']
                patcit_c_category =j['patcit']['category']
                patcit_c_classification_country =j['patcit']['classification-national']['country']
                patcit_c_classification_main = j['patcit']['classification-national']['main-classification']
                patcit_num.append(patcit_number)
                patcit_country.append(patcit_doc_country)
                patcit_doc_number.append(patcit_doc_docnumber)
                patcit_kind.append(patcit_doc_kind)
                patcit_name.append(patcit_doc_name)
                patcit_date.append(patcit_doc_date)
                patcit_classification_country.append(patcit_c_classification_country)
                patcit_category.appen(patcit_c_category)
                patcit_classification_main.append(patcit_c_classification_main)
                nplcit_number = j['nplcit']['@num']
                nplcit_othercitation = j['nplcit']['othercit']

                nplcit_num.append(nplcit_number)
                nplcit_othercit.append(nplcit_othercitation)

                #null
        def classification(self,xml):
            try:
                #null
                us_classifications_ipcr = doc['us-patent-grant']['us-bibliographic-data-grant']['us-field-of-classification-search']['us-classifications-ipcr']
            except:
                pass

            classification_national = []
            for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-field-of-classification-search']['classification-national'])):
                classification_national.append((doc['us-patent-grant']['us-bibliographic-data-grant']['us-field-of-classification-search']['classification-national'])[i])

            classification_country = []
            classification_main = []

            for i in classification_national:
                classificiation_c = i['country']
                classificiation_m = i['main-classification']
                classification_country.append(classificiation_c)
                classification_main.append(classificiation_m)


                #null
        def furtherClassification(self,xml):
            further = []
            for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national']['further-classification'])):
                further.append((doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national']['further-classification']))

            further_classification = []

            for i in further:
                further_class = i
                further_classification.append(further_class)

                #null
        def classificationIpcr:

            if range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'])) ==0:

                ubdg_csipcr_cipcr_ipc_ver_indicator_date = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-ipcr']['ipc-version-indicator']['date']
                ubdg_csipcr_cipcr_classification_level = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-level']
                ubdg_csipcr_cipcr_section = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['section']
                ubdg_csipcr_cipcr_class= doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['class']
                ubdg_csipcr_cipcr_subclass =doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['subclass']
                ubdg_csipcr_cipcr_main_group =doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['main-group']
                ubdg_csipcr_cipcr_subgroup = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['subgroup']
                ubdg_csipcr_cipcr_symbol_position = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['symbol-position']
                ubdg_csipcr_cipcr_classification_value = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-value']
                ubdg_csipcr_cipcr_action_date =doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['action-date']['date']
                ubdg_csipcr_cipcr_generating_office_country =doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['generating-office']['country']
                ubdg_csipcr_cipcr_classification_status =doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-status']
                ubdg_csipcr_cipcr_classification_data_source = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-data-source']

            else:
                classifications_ipcr = []
                for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'])):
                    classifications_ipcr.append((doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'])[i])

                classification_ipc_version_indicator_date = []
                classification_level = []
                classification_section = []
                classification_class = []
                classification_subclass =[]
                classification_main_group =[]
                classification_subgroup =[]
                classification_symbol_position =[]
                classification_value = []
                classification_action_date = []
                classification_generating_office_country = []
                classification_status = []
                classification_data_source = []

                for i in classifications_ipcr:
                    ubdg_csipcr_cipcr_ipc_ver_indicator_date = i['ipc-version-indicator']['date']
                    ubdg_csipcr_cipcr_classification_level = i['classification-level']
                    ubdg_csipcr_cipcr_section = i['section']
                    ubdg_csipcr_cipcr_class = i['class']
                    ubdg_csipcr_cipcr_subclass = i['subclass']
                    ubdg_csipcr_cipcr_main_group = i['main-group']
                    ubdg_csipcr_cipcr_subgroup = i['subgroup']
                    ubdg_csipcr_cipcr_symbol_position = i['symbol-position']
                    ubdg_csipcr_cipcr_classification_value = i['classification-value']
                    ubdg_csipcr_cipcr_action_date = i['action-date']['date']
                    ubdg_csipcr_cipcr_generating_office_country = i['generating-office']['country']
                    ubdg_csipcr_cipcr_classification_status = i['classification-status']
                    ubdg_csipcr_cipcr_classification_data_source = i['classification-data-source']
                    classification_ipc_version_indicator_date.append(ubdg_csipcr_cipcr_ipc_ver_indicator_date)
                    classification_level.append(ubdg_csipcr_cipcr_classification_level)
                    classification_section.append(ubdg_csipcr_cipcr_section)
                    classification_class.append(ubdg_csipcr_cipcr_class)
                    classification_subclass.append(ubdg_csipcr_cipcr_subclass)
                    classification_main_group.append(ubdg_csipcr_cipcr_main_group)
                    classification_subgroup.append(ubdg_csipcr_cipcr_subgroup)
                    classification_symbol_position.append(ubdg_csipcr_cipcr_symbol_position)
                    classification_value.append(ubdg_csipcr_cipcr_classification_value)
                    classification_action_date.append(ubdg_csipcr_cipcr_action_date)
                    classification_generating_office_country.append(ubdg_csipcr_cipcr_generating_office_country)
                    classification_status.append(ubdg_csipcr_cipcr_classification_status)
                    classification_data_source.append(ubdg_csipcr_cipcr_classification_data_source)


        def applicant(self,xml):

            #applicant가 1개일 경우
            if range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'])) == 0:

                ubdg_parties_applicants_applicant_sequence = doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant']['@sequence']
                ubdg_parties_applicants_applicant_app_type = doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant']['@app-type']
                ubdg_parties_applicants_applicant_designation = doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant']['@designation']
                ubdg_parties_applicants_applicant_addressbook_last_name = doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant']['addressbook']['last-name']
                ubdg_parties_applicants_applicant_addressbook_first_name = doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant']['addressbook']['first-name']
                ubdg_parties_applicants_applicant_addressbook_address_street = doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant']['addressbook']['address']['street']
                ubdg_parties_applicants_applicant_addressbook_address_city = doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant']['addressbook']['address']['city']
                ubdg_parties_applicants_applicant_addressbook_address_state = doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant']['addressbook']['address']['state']
                ubdg_parties_applicants_applicant_addressbook_address_postcode = doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant']['addressbook']['address']['postcode']
                ubdg_parties_applicants_applicant_addressbook_address_country = doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant']['addressbook']['address']['country']
                ubdg_parties_applicants_applicant_residence_country = doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant']['residence']['country']
                try:
                    ubdg_parties_applicants_applicant_applicant_authority_category = doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant']['@applicant-authority-category]
                    #applicant가 2개이상일   경우
                    else:
                    applicant = []
                    for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'])):
                        applicant.append((doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'])[i])

                    applicant_sequence =[]
                    applicant_app_type =[]
                    applicant_designation =[]
                    applicant_address_last_name =[]
                    applicant_address_first_name =[]
                    applicant_address_city =[]
                    applicant_address_state =[]
                    applicant_address_country =[]
                    applicant_residence_country =[]
                    applicant_address_street = []
                    applicant_address_postcode=[]
                    applicant_authority_category =[]


                    for i in applicant:
                        ubdg_parties_applicants_applicant_sequence = i['@sequence']
                        ubdg_parties_applicants_applicant_app_type = i['@app-type']
                        ubdg_parties_applicants_applicant_designation = i['@designation']
                        ubdg_parties_applicants_applicant_addressbook_last_name = i['addressbook']['last-name']
                        ubdg_parties_applicants_applicant_addressbook_first_name = i['addressbook']['first-name']
                        ubdg_parties_applicants_applicant_addressbook_address_state = i['addressbook']['address']['state']
                        ubdg_parties_applicants_applicant_addressbook_address_street = i['addressbook']['address']['street']
                        ubdg_parties_applicants_applicant_addressbook_address_postcode = i['addressbook']['address']['postcode']
                        ubdg_parties_applicants_applicant_addressbook_address_city = i['addressbook']['address']['city']
                        ubdg_parties_applicants_applicant_addressbook_address_country = i['addressbook']['address']['country']
                        ubdg_parties_applicants_applicant_nationality_country = i['nationality']['country']
                        ubdg_parties_applicants_applicant_residence_country = i['residence']['country']
                        applicant_sequence.append(ubdg_parties_applicants_applicant_sequence)
                        applicant_app_type.append(ubdg_parties_applicants_applicant_app_type)
                        applicant_designation.append(ubdg_parties_applicants_applicant_designation)
                        applicant_address_last_name.append(ubdg_parties_applicants_applicant_addressbook_last_name)
                        applicant_address_first_name.append(ubdg_parties_appli cants_applicant_addressbook_first_name)
                        applicant_address_street.append(ubdg_parties_applicants_applicant_addressbook_address_street)
                        applicant_address_postcode.append(ubdg_parties_applicants_applicant_addressbook_address_postcode)
                        applicant_address_city.append(ubdg_parties_applicants_applicant_addressbook_address_city)
                        applicant_address_state.append(ubdg_parties_applicants_applicant_addressbook_address_state)
                        applicant_address_country.append(ubdg_parties_applicants_applicant_addressbook_address_country)
                        applicant_residence_country.append(ubdg_parties_applicants_applicant_residence_country)
                        try:
                            ubdg_parties_applicants_applicant_applicant_authority_category=i['@applicant-authority-category']
                            applicant_authority_category.append(ubdg_parties_applicants_applicant_applicant_authority_category)
                        except:
                            pass
                            #null
        def beforeRelation(relation):
            us_related_documents = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']

            different_tags = []
            for i in us_related_documents.keys():
                different_tags.append(i)

            relation_list =[]
            for i in different_tags:
                get_relation = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents'][i]
                if isinstance(get_relation, type(list)) is True:
                    for j in range(len(get_relation)-1):
                        for k in get_relation:
                            relation_list.append(k)
                else:
                    relation_list.append(get_relation)
            relation(relation_list)
            #null
        def relation(has_relation):

            ubdg_relateddoc_relation_parentdoc_di_country= []
            ubdg_relateddoc_relation_parentdoc_di_doc_number =[]
            ubdg_relateddoc_relation_parentdoc_di_kind=[]
            ubdg_relateddoc_relation_parentdoc_di_date=[]
            ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_country=[]
            ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_doc_number=[]
            ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_kind=[]
            ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_date=[]
            ubdg_relateddoc_relation_parentdoc_childdoc_country=[]
            ubdg_relateddoc_relation_parentdoc_childdoc_doc_number=[]
            ubdg_relateddoc_relation_parentdoc_parent_status=[]

            for relation_element in has_relation:

                ubdg_relateddoc_relation_parentdoc_di_country.append(relation_element['relation']['parent-doc']['document-id']['country'])
                ubdg_relateddoc_relation_parentdoc_di_doc_number.append(relation_element['relation']['parent-doc']['document-id']['doc-number'])
                ubdg_relateddoc_relation_parentdoc_di_kind.append(relation_element['relation']['parent-doc']['document-id']['kind'])
                ubdg_relateddoc_relation_parentdoc_di_date.append(relation_element['relation']['parent-doc']['document-id']['date'])

                ubdg_relateddoc_relation_parentdoc_childdoc_country.append(relation_element['relation']['child-doc']['document-id']['country'])
                ubdg_relateddoc_relation_parentdoc_childdoc_doc_number.append(relation_element['relation']['child-doc']['document-id']['doc-number'])

                #null
                try:
                    #null
                    realtion_parent_grant_doc_number = relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['doc-number']#null
                    realtion_parent_grant_doc_kind = relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['kind']#null
                    realtion_parent_grant_doc_date = relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['date']#null
                    ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_country.append(realtion_parent_grant_doc_country)
                    ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_doc_number.append(realtion_parent_grant_doc_number)
                    ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_kind.append(realtion_parent_grant_doc_kind)
                    ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_date.append(realtion_parent_grant_doc_date)
                except:
                    pass

                try:
                    #null
                    relation_parent_status = relation_element['relation']['parent-doc']['parent_status']#null
                    ubdg_relateddoc_relation_parentdoc_parent_status.append(relation_parent_status)
                except:
                    pass



                    #null
        def usProvisionalApplication(self,xml):
            ubdg_provisional_appl_doc_country= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['document-id']['country']
            ubdg_provisional_appl_doc_number= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['document-id']['doc-number']
            ubdg_provisional_appl_doc_kind= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['document-id']['kind']
            ubdg_provisional_appl_doc_date= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['document-id']['country']
            ubdg_provisional_appl_status= doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application']['us-provisional-application-status']
            #null
        def relatedPublication(self,xml):
            ubdg_related_publ_doc_country = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication']['document-id']['country']
            ubdg_related_publ_doc_number = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication']['document-id']['doc-number']
            ubdg_related_publ_doc_kind = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication']['document-id']['kind']
            ubdg_related_publ_doc_date = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication']['document-id']['date']



            #become mandatory
        def inventors(self,xml):
            if range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor'])) == 0:

                ubdg_parties_inventors_inventor_sequence = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['@sequence']
                ubdg_parties_inventors_inventor_designation = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['@designation']
                ubdg_parties_inventors_inventor_addressbook_last_name = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook']['last-name']
                ubdg_parties_inventors_inventor_addressbook_first_name = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook']['first-name']
                ubdg_parties_inventors_inventor_addressbook_address_city = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook']['address']['city']
                ubdg_parties_inventors_inventor_addressbook_address_state = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook']['address']['state']
                ubdg_parties_inventors_inventor_addressbook_address_country = doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook']['address']['country']

            else:
                inventor = []
                for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor'])):
                    applicant.append((doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor'])[i])

                inventor_sequence =[]
                inventor_designation =[]
                inventor_address_last_name =[]
                inventor_address_first_name =[]
                inventor_address_city =[]
                inventor_address_state =[]
                inventor_address_country =[]

                for i in inventor:
                    ubdg_parties_inventors_inventor_sequence = i['@sequence']
                    ubdg_parties_inventors_inventor_designation = i['@designation']
                    ubdg_parties_inventors_inventor_addressbook_last_name = i['addressbook']['last-name']
                    ubdg_parties_inventors_inventor_addressbook_first_name = i['addressbook']['first-name']
                    ubdg_parties_inventors_inventor_addressbook_address_state = i['addressbook']['address']['state']
                    ubdg_parties_inventors_inventor_addressbook_address_city = i['addressbook']['address']['city']
                    ubdg_parties_inventors_inventor_addressbook_address_country = i['addressbook']['address']['country']
                    inventor_sequence.append(ubdg_parties_inventors_inventor_sequence)
                    inventor_designation.append(ubdg_parties_inventors_inventor_designation)
                    inventor_address_last_name.append(ubdg_parties_inventors_inventor_addressbook_last_name)
                    inventor_address_first_name.append(ubdg_parties_inventors_inventor_addressbook_first_name)
                    inventor_address_city.append(ubdg_parties_inventors_inventor_addressbook_address_city)
                    inventor_address_state.append(ubdg_parties_inventors_inventor_addressbook_address_state)
                    inventor_address_country.append(ubdg_parties_inventors_inventor_addressbook_address_country)



        def claim(self,xml):
            ubdg_priority_claims_sequence = doc['us-patent-grant']['us-bibliographic-data-grant']['priority-claims']['priority-claim']['@sequence']
            ubdg_priority_claims_kind = doc['us-patent-grant']['us-bibliographic-data-grant']['priority-claims']['priority-claim']['@kind']
            ubdg_priority_claims_country = doc['us-patent-grant']['us-bibliographic-data-grant']['priority-claims']['priority-claim']['country']
            ubdg_priority_claims_doc_number = doc['us-patent-grant']['us-bibliographic-data-grant']['priority-claims']['priority-claim']['doc-number']
            ubdg_priority_claims_date = doc['us-patent-grant']['us-bibliographic-data-grant']['priority-claims']['priority-claim']['date']

    class parserVer44(Parser):
        def __init__(self, xml):
            super().__init__(xml)

            # add us-claim-statement
            self.upg_us_claim_statement = doc['us-patent-grant']['us-claim-statement']
            # address_street #add us
            self.ubdg_us_parties_us_applicants_us_applicant_addressbook_address_state = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                    'addressbook']['address']['state']
            # assignee
            self.ubdg_assignees_assignee_address_orgname = None
            self.ubdg_assignees_assignee_address_role = None
            self.ubdg_assignees_assignee_address_address_city = None
            self.ubdg_assignees_assignee_address_address_state = None
            self.ubdg_assignees_assignee_address_address_country = None
            # agents #null
            self.ubdg_parties_agents_agent_rep_type = None
            self.ubdg_parties_agents_agent_addressbook_orgname = None
            self.ubdg_parties_agents_agent_addressbook_address_country = None
            # further 추가

            self.further = None
            self.further_classification = None
            self.further_class = None

            self.patcit_category = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-references-cited']['us-citation']['category']
            self.patcit_classification_country = None
            self.patcit_classification_main = None

            self.us_classifications_ipcr = None
            # applicant
            self.ubdg_parties_applicants_applicant_sequence = None
            self.ubdg_parties_applicants_applicant_app_type = None
            self.ubdg_parties_applicants_applicant_designation = None
            self.ubdg_parties_applicants_applicant_addressbook_last_name = None
            self.ubdg_parties_applicants_applicant_addressbook_first_name = None
            self.ubdg_parties_applicants_applicant_addressbook_address_city = None
            self.ubdg_parties_applicants_applicant_addressbook_address_country = None
            self.ubdg_parties_applicants_applicant_residence_country = None
            self.applicant = None
            self.applicant_sequence = None
            self.pplicant_designation = None
            self.applicant_app_type = None
            self.applicant_address_last_name = None
            self.applicant_address_first_name = None
            self.applicant_address_city = None
            self.applicant_address_state = None
            self.applicant_address_country = None
            self.applicant_residence_country = None
            # null
            self.applicant_address_street = None
            ubdg_assignees_assignee_address_orgname = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['orgname']
            self.applicant_address_postcode = None

            # megaTable
            self.ubdg_mega_table = None

            # inventor
            self.parties_inventors_inventor_sequence = None
            self.ubdg_parties_inventors_inventor_designation = None
            self.ubdg_parties_inventors_inventor_addressbook_last_name = None
            self.ubdg_parties_inventors_inventor_addressbook_first_name = None
            self.ubdg_parties_inventors_inventor_addressbook_address_city = None
            self.ubdg_parties_inventors_inventor_addressbook_address_state = None
            self.ubdg_parties_inventors_inventor_addressbook_address_country = None
            self.self.inventor = None
            self.inventor_sequence = None
            self.inventor_designation = None
            self.inventor_address_last_name = None
            self.inventor_address_first_name = None
            self.inventor_address_city = None
            self.inventor_address_state = None
            self.inventor_address_country = None

            self.ubdg_parties_applicants_applicant_applicant_authority_category = None


            self.ubdg_utog_prior_disclosure_grant = None

            self.us_classification_cpc_text = None
            self.us_classification_cpc_combination = None

    # null
    def assisatntExaminer(self, xml):
        null_variables = []
        null_variables.append(ubdg_examiners_assistant_examiner_last_name)
        null_variables.append(ubdg_examiners_assistant_examiner_first_name)

        null_tag = []
        null_tag.append(
            doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['assistant-examiner']['last-name'])
        null_tag.append(
            doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['assistant-examiner']['first-name'])

        for v, t in zip(null_variables, null_tag):
            if v == t:
                v = t
                # null

    def termOfGrant(self, xml):
        ubdg_utog_len_grant = self.doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant'][
            'length-of-grant']
        ubdg_utog_text_grant = self.doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant']['text']
        ubdg_utog_extension_grant = self.doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant'][
            'us-term-extension']
        ubdg_utog_disclaimer_grant = self.doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant'][
            'disclaimer']
        ubdg_utog_lapse_grant = self.doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant'][
            'lapse-of-patent']
        ubdg_utog_prior_disclosure_grant = self.doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant'][
            'prior-disclosure-affidavit-filed']

        # null

    def drawing(self, xml):
        ubdg_drawing = doc['us-patent-grant']['drawings']
        # null

    def sequenceListDoc(self, xml):
        ubdg_us_sequence_list_doc = doc['us-patent-grant']['us-sequence-list-doc']
        # null

    def tableExternalDoc(self, xml):
        ubdg_table_external_doc = doc['us-patent-grant']['table-external-doc']
        # null

    def usChemistry(self, xml):
        ubdg_us_chemistry = doc['us-patent-grant']['us-chemistry']
        # null

    def usMath(self, xml):
        ubdg_us_math = doc['us-patent-grant']['us-math']
        # null

    def abstract(self, xml):
        ubdg_abstract = doc['us-patent-grant']['abstract']
        # null

    def megaTable(self, xml):
        ubdg_mega_table = doc['us-patent-grant']['us-megatable-doc']
        # NULL

    def usBotantic(self, xml):
        ubdg_us_botantic_latin_name = doc['us-patent-grant']['us-bibliographic-data-grant']['us-botantic']['latin-name']
        ubdg_us_botantic_variety = doc['us-patent-grant']['us-bibliographic-data-grant']['us-botantic']['variety']
        # null

    def classificationsIpcrID(self, xml):
        ubdg_us_classification_ipcr_id = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'][
            '@id']
        # null

    def classificationsCpc(self, xml):
        ubdg_us_classification_cpc = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-cpc']
        # null

    def biblioClassifiacationLocarno(self, xml):
        ubdg_classificattion_locarno_edition = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['classification-locarno']['edition']
        ubdg_classificattion_locarno_main_classification = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['classification-locarno']['main-classification']
        # null

    def biblioClassifiacationNational(self, xml):
        ubdg_classificattion_national_country = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national']['country']
        ubdg_classificattion_national_main_classification = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national']['main-classification']
        # null

    def nuumberOfClaims(self, xml):
        ubdg_number_of_claims = doc['us-patent-grant']['us-bibliographic-data-grant']['number-of-claims']
        # null

    def Exemplary_claim(self, xml):
        ubdg_us_exemplary_claim = doc['us-patent-grant']['us-bibliographic-data-grant']['us-exemplary-claim']
        # null

    def figures(self, xml):
        ubdg_figures_number_of_drawing_sheets = doc['us-patent-grant']['us-bibliographic-data-grant']['figures'][
            'number-of-drawing-sheets']
        ubdg_figures_number_of_figures = doc['us-patent-grant']['us-bibliographic-data-grant']['figures'][
            'number-of-figures']
        # null

    def examiners(self, xml):
        ubdg_examiners_primary_examiner_last_name = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['last-name']
        ubdg_examiners_primary_examiner_first_name = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['first-name']
        ubdg_examiners_primary_examiner_department = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['department']
        # null

    def usFlagSirText(self, xml):
        ubdg_us_sir_flag_sir_text = ['us-patent-grant']['us-bibliographic-data-grant']['us-sir-flag']['@sir-text']

        # NULL

    def agent(self, xml):

        ubdg_parties_agents_agent_sequence = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['@sequence']
        ubdg_parties_agents_agent_rep_type = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['@rep-type']
        ubdg_parties_agents_agent_addressbook_orgname = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['addressbook']['orgname']
        ubdg_parties_agents_agent_addressbook_address_country = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['addressbook']['address'][
                'country']

        # NULL

    def assignee(self, xml):
        ubdg_assignees_assignee_address_orgname = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['orgname']
        ubdg_assignees_assignee_address_role = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['role']
        ubdg_assignees_assignee_address_address_city = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['address']['city']
        ubdg_assignees_assignee_address_address_state = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['address'][
                'state']
        ubdg_assignees_assignee_address_address_country = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['address'][
                'country']

        # null

    def patcit(self, xml):
        patcit = []

        for i in range(
                len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-references-cited']['us-citation'])):
            patcit.append(
                (doc['us-patent-grant']['us-bibliographic-data-grant']['us-references-cited']['us-citation'])[i])

        patcit_num = []
        patcit_country = []
        patcit_doc_number = []
        patcit_kind = []
        patcit_name = []
        patcit_date = []
        patcit_category = []
        patcit_classification_country = []
        patcit_classification_main = []
        nplcit_num = []
        nplcit_othercit = []

        for j in patcit:
            patcit_number = j['patcit']['@num']
            patcit_doc_country = j['patcit']['document-id']['country']
            patcit_doc_docnumber = j['patcit']['document-id']['doc-number']
            patcit_doc_kind = j['patcit']['document-id']['kind']
            patcit_doc_name = j['patcit']['document-id']['name']
            patcit_doc_date = j['patcit']['document-id']['date']
            patcit_c_category = j['patcit']['category']
            patcit_c_classification_country = j['patcit']['classification-national']['country']
            patcit_c_classification_main = j['patcit']['classification-national']['main-classification']
            patcit_num.append(patcit_number)
            patcit_country.append(patcit_doc_country)
            patcit_doc_number.append(patcit_doc_docnumber)
            patcit_kind.append(patcit_doc_kind)
            patcit_name.append(patcit_doc_name)
            patcit_date.append(patcit_doc_date)
            patcit_classification_country.append(patcit_c_classification_country)
            patcit_category.appen(patcit_c_category)
            patcit_classification_main.append(patcit_c_classification_main)
            nplcit_number = j['nplcit']['@num']
            nplcit_othercitation = j['nplcit']['othercit']

            nplcit_num.append(nplcit_number)
            nplcit_othercit.append(nplcit_othercitation)

            # null

    def classification(self, xml):
        try:
            # null
            us_classifications_ipcr = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-field-of-classification-search'][
                    'us-classifications-ipcr']

        except:
            pass

        classification_national = []
        for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-field-of-classification-search'][
                               'classification-national'])):
            classification_national.append((doc['us-patent-grant']['us-bibliographic-data-grant'][
                                                'us-field-of-classification-search']['classification-national'])[i])

        classification_country = []
        classification_main = []


        for i in classification_national:
            classificiation_c = i['country']
            classificiation_m = i['main-classification']

            classification_country.append(classificiation_c)
            classification_main.append(classificiation_m)

    # null
    def classificationCpc(self, xml):
        try:
            us_classification_cpc_text = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-field-of-classification-search'][
                    'classification-cpc-text']

            classification_cpc_text = []
            for i in range(len(us_classification_cpc_text)):
                classification_cpc_text.append((doc['us-patent-grant']['us-bibliographic-data-grant'][
                                                    'us-field-of-classification-search']['classification-cpc-text'])[i])
        except:
            pass

        try:
            us_classification_cpc_combination = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-field-of-classification-search'][
                    'classification-cpc-combination-text']

            classification_cpc_combination = []
            for i in range(len(us_classification_cpc_combination)):
                classification_cpc_combination.append((doc['us-patent-grant']['us-bibliographic-data-grant'][
                                                           'us-field-of-classification-search']['classification-cpc-combination-text'])[i])
        except:
            pass




    # null
    def furtherClassification(self, xml):
        further = []
        for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national'][
                               'further-classification'])):
            further.append((doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national'][
                                'further-classification']))

        further_classification = []

        for i in further:
            further_class = i
            further_classification.append(further_class)

            # null

    def classificationIpcr:

        if range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'])) == 0:

            ubdg_csipcr_cipcr_ipc_ver_indicator_date = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-ipcr'][
                    'ipc-version-indicator']['date']
            ubdg_csipcr_cipcr_classification_level = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-level']
            ubdg_csipcr_cipcr_section = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'][
                'section']
            ubdg_csipcr_cipcr_class = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'][
                'class']
            ubdg_csipcr_cipcr_subclass = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'][
                'subclass']
            ubdg_csipcr_cipcr_main_group = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['main-group']
            ubdg_csipcr_cipcr_subgroup = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'][
                'subgroup']
            ubdg_csipcr_cipcr_symbol_position = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['symbol-position']
            ubdg_csipcr_cipcr_classification_value = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-value']
            ubdg_csipcr_cipcr_action_date = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['action-date']['date']
            ubdg_csipcr_cipcr_generating_office_country = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['generating-office'][
                    'country']
            ubdg_csipcr_cipcr_classification_status = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-status']
            ubdg_csipcr_cipcr_classification_data_source = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-data-source']

        else:
            classifications_ipcr = []
            for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'])):
                classifications_ipcr.append(
                    (doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'])[i])

            classification_ipc_version_indicator_date = []
            classification_level = []
            classification_section = []
            classification_class = []
            classification_subclass = []
            classification_main_group = []
            classification_subgroup = []
            classification_symbol_position = []
            classification_value = []
            classification_action_date = []
            classification_generating_office_country = []
            classification_status = []
            classification_data_source = []

            for i in classifications_ipcr:
                ubdg_csipcr_cipcr_ipc_ver_indicator_date = i['ipc-version-indicator']['date']
                ubdg_csipcr_cipcr_classification_level = i['classification-level']
                ubdg_csipcr_cipcr_section = i['section']
                ubdg_csipcr_cipcr_class = i['class']
                ubdg_csipcr_cipcr_subclass = i['subclass']
                ubdg_csipcr_cipcr_main_group = i['main-group']
                ubdg_csipcr_cipcr_subgroup = i['subgroup']
                ubdg_csipcr_cipcr_symbol_position = i['symbol-position']
                ubdg_csipcr_cipcr_classification_value = i['classification-value']
                ubdg_csipcr_cipcr_action_date = i['action-date']['date']
                ubdg_csipcr_cipcr_generating_office_country = i['generating-office']['country']
                ubdg_csipcr_cipcr_classification_status = i['classification-status']
                ubdg_csipcr_cipcr_classification_data_source = i['classification-data-source']
                classification_ipc_version_indicator_date.append(ubdg_csipcr_cipcr_ipc_ver_indicator_date)
                classification_level.append(ubdg_csipcr_cipcr_classification_level)
                classification_section.append(ubdg_csipcr_cipcr_section)
                classification_class.append(ubdg_csipcr_cipcr_class)
                classification_subclass.append(ubdg_csipcr_cipcr_subclass)
                classification_main_group.append(ubdg_csipcr_cipcr_main_group)
                classification_subgroup.append(ubdg_csipcr_cipcr_subgroup)
                classification_symbol_position.append(ubdg_csipcr_cipcr_symbol_position)
                classification_value.append(ubdg_csipcr_cipcr_classification_value)
                classification_action_date.append(ubdg_csipcr_cipcr_action_date)
                classification_generating_office_country.append(ubdg_csipcr_cipcr_generating_office_country)
                classification_status.append(ubdg_csipcr_cipcr_classification_status)
                classification_data_source.append(ubdg_csipcr_cipcr_classification_data_source)

    def applicant(self, xml):

        # applicant가 1개일 경우
        if range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants'][
                         'us-applicant'])) == 0:

            ubdg_parties_applicants_applicant_sequence = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                    '@sequence']
            ubdg_parties_applicants_applicant_app_type = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                    '@app-type']
            ubdg_parties_applicants_applicant_designation = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                    '@designation']
            ubdg_parties_applicants_applicant_addressbook_last_name = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                    'addressbook']['last-name']
            ubdg_parties_applicants_applicant_addressbook_first_name = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                    'addressbook']['first-name']
            ubdg_parties_applicants_applicant_addressbook_address_street = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                    'addressbook']['address']['street']
            ubdg_parties_applicants_applicant_addressbook_address_city = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                    'addressbook']['address']['city']
            ubdg_parties_applicants_applicant_addressbook_address_state = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                    'addressbook']['address']['state']
            ubdg_parties_applicants_applicant_addressbook_address_postcode = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                    'addressbook']['address']['postcode']
            ubdg_parties_applicants_applicant_addressbook_address_country = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                    'addressbook']['address']['country']
            ubdg_parties_applicants_applicant_residence_country = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                    'residence']['country']
            try:
                ubdg_parties_applicants_applicant_applicant_authority_category =
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                    '@applicant-authority-category]
                # applicant가 2개이상일   경우
                else:
                applicant = []
                for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants'][
                                       'us-applicant'])):
                    applicant.append((doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties'][
                                          'us-applicants']['us-applicant'])[i])

                applicant_sequence = []
                applicant_app_type = []
                applicant_designation = []
                applicant_address_last_name = []
                applicant_address_first_name = []
                applicant_address_city = []
                applicant_address_state = []
                applicant_address_country = []
                applicant_residence_country = []
                applicant_address_street = []
                applicant_address_postcode = []
                applicant_authority_category = []

                for i in applicant:
                    ubdg_parties_applicants_applicant_sequence = i['@sequence']
                    ubdg_parties_applicants_applicant_app_type = i['@app-type']
                    ubdg_parties_applicants_applicant_designation = i['@designation']
                    ubdg_parties_applicants_applicant_addressbook_last_name = i['addressbook']['last-name']
                    ubdg_parties_applicants_applicant_addressbook_first_name = i['addressbook']['first-name']
                    ubdg_parties_applicants_applicant_addressbook_address_state = i['addressbook']['address']['state']
                    ubdg_parties_applicants_applicant_addressbook_address_street = i['addressbook']['address']['street']
                    ubdg_parties_applicants_applicant_addressbook_address_postcode = i['addressbook']['address']['postcode']
                    ubdg_parties_applicants_applicant_addressbook_address_city = i['addressbook']['address']['city']
                    ubdg_parties_applicants_applicant_addressbook_address_country = i['addressbook']['address']['country']
                    ubdg_parties_applicants_applicant_nationality_country = i['nationality']['country']
                    ubdg_parties_applicants_applicant_residence_country = i['residence']['country']
                    applicant_sequence.append(ubdg_parties_applicants_applicant_sequence)
                    applicant_app_type.append(ubdg_parties_applicants_applicant_app_type)
                    applicant_designation.append(ubdg_parties_applicants_applicant_designation)
                    applicant_address_last_name.append(ubdg_parties_applicants_applicant_addressbook_last_name)
                    applicant_address_first_name.append(ubdg_parties_appli
                    cants_applicant_addressbook_first_name)
                    applicant_address_street.append(ubdg_parties_applicants_applicant_addressbook_address_street)
                    applicant_address_postcode.append(ubdg_parties_applicants_applicant_addressbook_address_postcode)
                    applicant_address_city.append(ubdg_parties_applicants_applicant_addressbook_address_city)
                    applicant_address_state.append(ubdg_parties_applicants_applicant_addressbook_address_state)
                    applicant_address_country.append(ubdg_parties_applicants_applicant_addressbook_address_country)
                    applicant_residence_country.append(ubdg_parties_applicants_applicant_residence_country)
                    try:
                        ubdg_parties_applicants_applicant_applicant_authority_category = i['@applicant-authority-category']
                        applicant_authority_category.append(ubdg_parties_applicants_applicant_applicant_authority_category)
                    except:
                        pass
                        # null

    def beforeRelation(relation):
        us_related_documents = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']

        different_tags = []
        for i in us_related_documents.keys():
            different_tags.append(i)

        relation_list = []
        for i in different_tags:
            get_relation = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents'][i]
            if isinstance(get_relation, type(list)) is True:
                for j in range(len(get_relation) - 1):
                    for k in get_relation:
                        relation_list.append(k)
            else:
                relation_list.append(get_relation)
        relation(relation_list)
        # null

    def relation(has_relation):

        ubdg_relateddoc_relation_parentdoc_di_country = []
        ubdg_relateddoc_relation_parentdoc_di_doc_number = []
        ubdg_relateddoc_relation_parentdoc_di_kind = []
        ubdg_relateddoc_relation_parentdoc_di_date = []
        ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_country = []
        ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_doc_number = []
        ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_kind = []
        ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_date = []
        ubdg_relateddoc_relation_parentdoc_childdoc_country = []
        ubdg_relateddoc_relation_parentdoc_childdoc_doc_number = []
        ubdg_relateddoc_relation_parentdoc_parent_status = []

        for relation_element in has_relation:

            ubdg_relateddoc_relation_parentdoc_di_country.append(
                relation_element['relation']['parent-doc']['document-id']['country'])
            ubdg_relateddoc_relation_parentdoc_di_doc_number.append(
                relation_element['relation']['parent-doc']['document-id']['doc-number'])
            ubdg_relateddoc_relation_parentdoc_di_kind.append(
                relation_element['relation']['parent-doc']['document-id']['kind'])
            ubdg_relateddoc_relation_parentdoc_di_date.append(
                relation_element['relation']['parent-doc']['document-id']['date'])

            ubdg_relateddoc_relation_parentdoc_childdoc_country.append(
                relation_element['relation']['child-doc']['document-id']['country'])
            ubdg_relateddoc_relation_parentdoc_childdoc_doc_number.append(
                relation_element['relation']['child-doc']['document-id']['doc-number'])

            # null
            try:
                # null
                realtion_parent_grant_doc_number = \
                    relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['doc-number']  # null
                realtion_parent_grant_doc_kind = \
                    relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['kind']  # null
                realtion_parent_grant_doc_date = \
                    relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['date']  # null
                ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_country.append(realtion_parent_grant_doc_country)
                ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_doc_number.append(realtion_parent_grant_doc_number)
                ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_kind.append(realtion_parent_grant_doc_kind)
                ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_date.append(realtion_parent_grant_doc_date)
            except:
                pass

            try:
                # null
                relation_parent_status = relation_element['relation']['parent-doc']['parent_status']  # null
                ubdg_relateddoc_relation_parentdoc_parent_status.append(relation_parent_status)
            except:
                pass



                # null

    def usProvisionalApplication(self, xml):
        ubdg_provisional_appl_doc_country = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application'][
                'document-id']['country']
        ubdg_provisional_appl_doc_number = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application'][
                'document-id']['doc-number']
        ubdg_provisional_appl_doc_kind = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application'][
                'document-id']['kind']
        ubdg_provisional_appl_doc_date = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application'][
                'document-id']['country']
        ubdg_provisional_appl_status = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application'][
                'us-provisional-application-status']
        # null

    def relatedPublication(self, xml):
        ubdg_related_publ_doc_country = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication'][
                'document-id']['country']
        ubdg_related_publ_doc_number = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication'][
                'document-id']['doc-number']
        ubdg_related_publ_doc_kind = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication'][
                'document-id']['kind']
        ubdg_related_publ_doc_date = \
            doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication'][
                'document-id']['date']



        # become mandatory

    def inventors(self, xml):
        if range(
                len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor'])) == 0:

            ubdg_parties_inventors_inventor_sequence = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['@sequence']
            ubdg_parties_inventors_inventor_designation = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['@designation']
            ubdg_parties_inventors_inventor_addressbook_last_name = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook'][
                    'last-name']
            ubdg_parties_inventors_inventor_addressbook_first_name = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook'][
                    'first-name']
            ubdg_parties_inventors_inventor_addressbook_address_city = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook'][
                    'address']['city']
            ubdg_parties_inventors_inventor_addressbook_address_state = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook'][
                    'address']['state']
            ubdg_parties_inventors_inventor_addressbook_address_country = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook'][
                    'address']['country']

        else:
            inventor = []
            for i in range(
                    len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor'])):
                applicant.append(
                    (doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor'])[i])

            inventor_sequence = []
            inventor_designation = []
            inventor_address_last_name = []
            inventor_address_first_name = []
            inventor_address_city = []
            inventor_address_state = []
            inventor_address_country = []

            for i in inventor:
                ubdg_parties_inventors_inventor_sequence = i['@sequence']
                ubdg_parties_inventors_inventor_designation = i['@designation']
                ubdg_parties_inventors_inventor_addressbook_last_name = i['addressbook']['last-name']
                ubdg_parties_inventors_inventor_addressbook_first_name = i['addressbook']['first-name']
                ubdg_parties_inventors_inventor_addressbook_address_state = i['addressbook']['address']['state']
                ubdg_parties_inventors_inventor_addressbook_address_city = i['addressbook']['address']['city']
                ubdg_parties_inventors_inventor_addressbook_address_country = i['addressbook']['address']['country']
                inventor_sequence.append(ubdg_parties_inventors_inventor_sequence)
                inventor_designation.append(ubdg_parties_inventors_inventor_designation)
                inventor_address_last_name.append(ubdg_parties_inventors_inventor_addressbook_last_name)
                inventor_address_first_name.append(ubdg_parties_inventors_inventor_addressbook_first_name)
                inventor_address_city.append(ubdg_parties_inventors_inventor_addressbook_address_city)
                inventor_address_state.append(ubdg_parties_inventors_inventor_addressbook_address_state)
                inventor_address_country.append(ubdg_parties_inventors_inventor_addressbook_address_country)

    def claim(self, xml):
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


    class parserVer45(Parser):
        def __init__(self, xml):
            super().__init__(xml)

            # add us-claim-statement
            self.upg_us_claim_statement = doc['us-patent-grant']['us-claim-statement']
            # address_street #add us
            self.ubdg_us_parties_us_applicants_us_applicant_addressbook_address_state = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                    'addressbook']['address']['state']
            # assignee
            self.ubdg_assignees_assignee_address_orgname = None
            self.ubdg_assignees_assignee_address_role = None
            self.ubdg_assignees_assignee_address_address_city = None
            self.ubdg_assignees_assignee_address_address_state = None
            self.ubdg_assignees_assignee_address_address_country = None
            # agents #null
            self.ubdg_parties_agents_agent_rep_type = None
            self.ubdg_parties_agents_agent_addressbook_orgname = None
            self.ubdg_parties_agents_agent_addressbook_address_country = None
            # further 추가

            self.further = None
            self.further_classification = None
            self.further_class = None

            self.patcit_category = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-references-cited']['us-citation']['category']
            self.patcit_classification_country = None
            self.patcit_classification_main = None

            self.us_classifications_ipcr = None
            # applicant
            self.ubdg_parties_applicants_applicant_sequence = None
            self.ubdg_parties_applicants_applicant_app_type = None
            self.ubdg_parties_applicants_applicant_designation = None
            self.ubdg_parties_applicants_applicant_addressbook_last_name = None
            self.ubdg_parties_applicants_applicant_addressbook_first_name = None
            self.ubdg_parties_applicants_applicant_addressbook_address_city = None
            self.ubdg_parties_applicants_applicant_addressbook_address_country = None
            self.ubdg_parties_applicants_applicant_residence_country = None
            self.applicant = None
            self.applicant_sequence = None
            self.pplicant_designation = None
            self.applicant_app_type = None
            self.applicant_address_last_name = None
            self.applicant_address_first_name = None
            self.applicant_address_city = None
            self.applicant_address_state = None
            self.applicant_address_country = None
            self.applicant_residence_country = None
            # null
            self.applicant_address_street = None
            ubdg_assignees_assignee_address_orgname = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['orgname']
            self.applicant_address_postcode = None

            # megaTable
            self.ubdg_mega_table = None

            # inventor
            self.parties_inventors_inventor_sequence = None
            self.ubdg_parties_inventors_inventor_designation = None
            self.ubdg_parties_inventors_inventor_addressbook_last_name = None
            self.ubdg_parties_inventors_inventor_addressbook_first_name = None
            self.ubdg_parties_inventors_inventor_addressbook_address_city = None
            self.ubdg_parties_inventors_inventor_addressbook_address_state = None
            self.ubdg_parties_inventors_inventor_addressbook_address_country = None
            self.self.inventor = None
            self.inventor_sequence = None
            self.inventor_designation = None
            self.inventor_address_last_name = None
            self.inventor_address_first_name = None
            self.inventor_address_city = None
            self.inventor_address_state = None
            self.inventor_address_country = None

            self.ubdg_parties_applicants_applicant_applicant_authority_category = None


            self.ubdg_utog_prior_disclosure_grant = None

            self.us_classification_cpc_text = None
            self.us_classification_cpc_combination = None

            self.relation_parentdoc_international_filing_date = None
            self.relation_parentdoc_childdoc_international_filing_date = None

            self.ubdg_hague_inter_filing_date = None
            self.ubdg_hague_inter_regist_publ_date = None
            self.ubdg_hague_inter_regist_num = None
            self.ubdg_hague_inter_regist_date = None

            self.ubdg_pct_reg_fil_data_di_country = None
            self.ubdg_pct_reg_fil_data_di_doc_num = None
            self.ubdg_pct_reg_fil_data_di_kind = None
            self.ubdg_pct_reg_fil_data_di_date = None
            self.ubdg_pct_reg_fil_data_di_124_date = None
            self.ubdg_pct_reg_fil_data_di_12_date = None
        # null
        def assisatntExaminer(self, xml):
            null_variables = []
            null_variables.append(ubdg_examiners_assistant_examiner_last_name)
            null_variables.append(ubdg_examiners_assistant_examiner_first_name)

            null_tag = []
            null_tag.append(
                doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['assistant-examiner']['last-name'])
            null_tag.append(
                doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['assistant-examiner']['first-name'])

            for v, t in zip(null_variables, null_tag):
                if v == t:
                    v = t
                    # null

        def termOfGrant(self, xml):
            ubdg_utog_len_grant = self.doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant'][
                'length-of-grant']
            ubdg_utog_text_grant = self.doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant']['text']
            ubdg_utog_extension_grant = self.doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant'][
                'us-term-extension']
            ubdg_utog_disclaimer_grant = self.doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant'][
                'disclaimer']
            ubdg_utog_lapse_grant = self.doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant'][
                'lapse-of-patent']
            ubdg_utog_prior_disclosure_grant = self.doc['us-patent-grant']['us-bibliographic-data-grant']['us-term-of-grant'][
                'prior-disclosure-affidavit-filed']

            # null

        def drawing(self, xml):
            ubdg_drawing = doc['us-patent-grant']['drawings']
            # null

        def sequenceListDoc(self, xml):
            ubdg_us_sequence_list_doc = doc['us-patent-grant']['us-sequence-list-doc']
            # null

        def tableExternalDoc(self, xml):
            ubdg_table_external_doc = doc['us-patent-grant']['table-external-doc']
            # null

        def usChemistry(self, xml):
            ubdg_us_chemistry = doc['us-patent-grant']['us-chemistry']
            # null

        def usMath(self, xml):
            ubdg_us_math = doc['us-patent-grant']['us-math']
            # null

        def abstract(self, xml):
            ubdg_abstract = doc['us-patent-grant']['abstract']
            # null

        def megaTable(self, xml):
            ubdg_mega_table = doc['us-patent-grant']['us-megatable-doc']
            # NULL

        def usBotantic(self, xml):
            ubdg_us_botantic_latin_name = doc['us-patent-grant']['us-bibliographic-data-grant']['us-botantic']['latin-name']
            ubdg_us_botantic_variety = doc['us-patent-grant']['us-bibliographic-data-grant']['us-botantic']['variety']
            # null

        def classificationsIpcrID(self, xml):
            ubdg_us_classification_ipcr_id = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'][
                '@id']
            # null

        def classificationsCpc(self, xml):
            ubdg_us_classification_cpc = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-cpc']
            # null

        def biblioClassifiacationLocarno(self, xml):
            ubdg_classificattion_locarno_edition = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['classification-locarno']['edition']
            ubdg_classificattion_locarno_main_classification = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['classification-locarno']['main-classification']
            # null

        def biblioClassifiacationNational(self, xml):
            ubdg_classificattion_national_country = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national']['country']
            ubdg_classificattion_national_main_classification = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national']['main-classification']
            # null

        def nuumberOfClaims(self, xml):
            ubdg_number_of_claims = doc['us-patent-grant']['us-bibliographic-data-grant']['number-of-claims']
            # null

        def Exemplary_claim(self, xml):
            ubdg_us_exemplary_claim = doc['us-patent-grant']['us-bibliographic-data-grant']['us-exemplary-claim']
            # null

        def figures(self, xml):
            ubdg_figures_number_of_drawing_sheets = doc['us-patent-grant']['us-bibliographic-data-grant']['figures'][
                'number-of-drawing-sheets']
            ubdg_figures_number_of_figures = doc['us-patent-grant']['us-bibliographic-data-grant']['figures'][
                'number-of-figures']
            # null

        def examiners(self, xml):
            ubdg_examiners_primary_examiner_last_name = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['last-name']
            ubdg_examiners_primary_examiner_first_name = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['first-name']
            ubdg_examiners_primary_examiner_department = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['examiners']['primary-examiner']['department']
            # null

        def usFlagSirText(self, xml):
            ubdg_us_sir_flag_sir_text = ['us-patent-grant']['us-bibliographic-data-grant']['us-sir-flag']['@sir-text']

            # NULL

        def agent(self, xml):

            ubdg_parties_agents_agent_sequence = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['@sequence']
            ubdg_parties_agents_agent_rep_type = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['@rep-type']
            ubdg_parties_agents_agent_addressbook_orgname = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['addressbook']['orgname']
            try:
                ubdg_parties_agents_agent_addressbook_address_country = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['agents']['agent']['addressbook']['address'][
                        'country']

            # NULL

        def assignee(self, xml):
            ubdg_assignees_assignee_address_orgname = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['orgname']
            ubdg_assignees_assignee_address_role = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['role']

            try:
                ubdg_assignees_assignee_address_address_city = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['address']['city']
                ubdg_assignees_assignee_address_address_state = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['address'][
                        'state']
                ubdg_assignees_assignee_address_address_country = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['assignees']['assignee']['addressbook']['address'][
                        'country']
            except: pass

            # null

        def patcit(self, xml):
            patcit = []

            for i in range(
                    len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-references-cited']['us-citation'])):
                patcit.append(
                    (doc['us-patent-grant']['us-bibliographic-data-grant']['us-references-cited']['us-citation'])[i])

            patcit_num = []
            patcit_country = []
            patcit_doc_number = []
            patcit_kind = []
            patcit_name = []
            patcit_date = []
            patcit_category = []
            patcit_classification_country = []
            patcit_classification_main = []
            nplcit_num = []
            nplcit_othercit = []

            for j in patcit:
                patcit_number = j['patcit']['@num']
                patcit_doc_country = j['patcit']['document-id']['country']
                patcit_doc_docnumber = j['patcit']['document-id']['doc-number']
                patcit_doc_kind = j['patcit']['document-id']['kind']
                patcit_doc_name = j['patcit']['document-id']['name']
                patcit_doc_date = j['patcit']['document-id']['date']
                patcit_c_category = j['patcit']['category']
                patcit_c_classification_country = j['patcit']['classification-national']['country']
                patcit_c_classification_main = j['patcit']['classification-national']['main-classification']
                patcit_num.append(patcit_number)
                patcit_country.append(patcit_doc_country)
                patcit_doc_number.append(patcit_doc_docnumber)
                patcit_kind.append(patcit_doc_kind)
                patcit_name.append(patcit_doc_name)
                patcit_date.append(patcit_doc_date)
                patcit_classification_country.append(patcit_c_classification_country)
                patcit_category.appen(patcit_c_category)
                patcit_classification_main.append(patcit_c_classification_main)
                nplcit_number = j['nplcit']['@num']
                nplcit_othercitation = j['nplcit']['othercit']

                nplcit_num.append(nplcit_number)
                nplcit_othercit.append(nplcit_othercitation)

                # null

        def classification(self, xml):
            try:
                # null
                us_classifications_ipcr = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['us-field-of-classification-search'][
                        'us-classifications-ipcr']

            except:
                pass

            classification_national = []
            for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-field-of-classification-search'][
                                   'classification-national'])):
                classification_national.append((doc['us-patent-grant']['us-bibliographic-data-grant'][
                                                    'us-field-of-classification-search']['classification-national'])[i])

            classification_country = []
            classification_main = []


            for i in classification_national:
                classificiation_c = i['country']
                classificiation_m = i['main-classification']

                classification_country.append(classificiation_c)
                classification_main.append(classificiation_m)

        # null
        def classificationCpc(self, xml):
            try:
                us_classification_cpc_text = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['us-field-of-classification-search'][
                        'classification-cpc-text']

                classification_cpc_text = []
                for i in range(len(us_classification_cpc_text)):
                    classification_cpc_text.append((doc['us-patent-grant']['us-bibliographic-data-grant'][
                                                        'us-field-of-classification-search']['classification-cpc-text'])[i])
            except:
                pass

            try:
                us_classification_cpc_combination = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['us-field-of-classification-search'][
                        'classification-cpc-combination-text']

                classification_cpc_combination = []
                for i in range(len(us_classification_cpc_combination)):
                    classification_cpc_combination.append((doc['us-patent-grant']['us-bibliographic-data-grant'][
                                                               'us-field-of-classification-search']['classification-cpc-combination-text'])[i])
            except:
                pass




        # null
        def furtherClassification(self, xml):
            further = []
            for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national'][
                                   'further-classification'])):
                further.append((doc['us-patent-grant']['us-bibliographic-data-grant']['classification-national'][
                                    'further-classification']))

            further_classification = []

            for i in further:
                further_class = i
                further_classification.append(further_class)

                # null

        def classificationIpcr:

            if range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'])) == 0:

                ubdg_csipcr_cipcr_ipc_ver_indicator_date = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-ipcr'][
                        'ipc-version-indicator']['date']
                ubdg_csipcr_cipcr_classification_level = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-level']
                ubdg_csipcr_cipcr_section = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'][
                    'section']
                ubdg_csipcr_cipcr_class = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'][
                    'class']
                ubdg_csipcr_cipcr_subclass = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'][
                    'subclass']
                ubdg_csipcr_cipcr_main_group = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['main-group']
                ubdg_csipcr_cipcr_subgroup = doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'][
                    'subgroup']
                ubdg_csipcr_cipcr_symbol_position = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['symbol-position']
                ubdg_csipcr_cipcr_classification_value = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-value']
                ubdg_csipcr_cipcr_action_date = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['action-date']['date']
                ubdg_csipcr_cipcr_generating_office_country = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['generating-office'][
                        'country']
                ubdg_csipcr_cipcr_classification_status = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-status']
                ubdg_csipcr_cipcr_classification_data_source = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr']['classification-data-source']

            else:
                classifications_ipcr = []
                for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'])):
                    classifications_ipcr.append(
                        (doc['us-patent-grant']['us-bibliographic-data-grant']['classifications-ipcr'])[i])

                classification_ipc_version_indicator_date = []
                classification_level = []
                classification_section = []
                classification_class = []
                classification_subclass = []
                classification_main_group = []
                classification_subgroup = []
                classification_symbol_position = []
                classification_value = []
                classification_action_date = []
                classification_generating_office_country = []
                classification_status = []
                classification_data_source = []

                for i in classifications_ipcr:
                    ubdg_csipcr_cipcr_ipc_ver_indicator_date = i['ipc-version-indicator']['date']
                    ubdg_csipcr_cipcr_classification_level = i['classification-level']
                    ubdg_csipcr_cipcr_section = i['section']
                    ubdg_csipcr_cipcr_class = i['class']
                    ubdg_csipcr_cipcr_subclass = i['subclass']
                    ubdg_csipcr_cipcr_main_group = i['main-group']
                    ubdg_csipcr_cipcr_subgroup = i['subgroup']
                    ubdg_csipcr_cipcr_symbol_position = i['symbol-position']
                    ubdg_csipcr_cipcr_classification_value = i['classification-value']
                    ubdg_csipcr_cipcr_action_date = i['action-date']['date']
                    ubdg_csipcr_cipcr_generating_office_country = i['generating-office']['country']
                    ubdg_csipcr_cipcr_classification_status = i['classification-status']
                    ubdg_csipcr_cipcr_classification_data_source = i['classification-data-source']
                    classification_ipc_version_indicator_date.append(ubdg_csipcr_cipcr_ipc_ver_indicator_date)
                    classification_level.append(ubdg_csipcr_cipcr_classification_level)
                    classification_section.append(ubdg_csipcr_cipcr_section)
                    classification_class.append(ubdg_csipcr_cipcr_class)
                    classification_subclass.append(ubdg_csipcr_cipcr_subclass)
                    classification_main_group.append(ubdg_csipcr_cipcr_main_group)
                    classification_subgroup.append(ubdg_csipcr_cipcr_subgroup)
                    classification_symbol_position.append(ubdg_csipcr_cipcr_symbol_position)
                    classification_value.append(ubdg_csipcr_cipcr_classification_value)
                    classification_action_date.append(ubdg_csipcr_cipcr_action_date)
                    classification_generating_office_country.append(ubdg_csipcr_cipcr_generating_office_country)
                    classification_status.append(ubdg_csipcr_cipcr_classification_status)
                    classification_data_source.append(ubdg_csipcr_cipcr_classification_data_source)

        def applicant(self, xml):

            # applicant가 1개일 경우
            if range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants'][
                             'us-applicant'])) == 0:

                ubdg_parties_applicants_applicant_sequence = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                        '@sequence']
                ubdg_parties_applicants_applicant_app_type = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                        '@app-type']
                ubdg_parties_applicants_applicant_designation = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                        '@designation']
                ubdg_parties_applicants_applicant_addressbook_last_name = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                        'addressbook']['last-name']
                ubdg_parties_applicants_applicant_addressbook_first_name = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                        'addressbook']['first-name']
                try:
                    ubdg_parties_applicants_applicant_addressbook_address_street = \
                        doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                            'addressbook']['address']['street']
                    ubdg_parties_applicants_applicant_addressbook_address_city = \
                        doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                            'addressbook']['address']['city']
                    ubdg_parties_applicants_applicant_addressbook_address_state = \
                        doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                            'addressbook']['address']['state']
                    ubdg_parties_applicants_applicant_addressbook_address_postcode = \
                        doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                            'addressbook']['address']['postcode']
                    ubdg_parties_applicants_applicant_addressbook_address_country = \
                        doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                            'addressbook']['address']['country']
                    ubdg_parties_applicants_applicant_residence_country = \
                        doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                            'residence']['country']
                except: pass

                try:
                    ubdg_parties_applicants_applicant_applicant_authority_category =
                    doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants']['us-applicant'][
                        '@applicant-authority-category]
                    # applicant가 2개이상일   경우
                    else:
                    applicant = []
                    for i in range(len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['us-applicants'][
                                           'us-applicant'])):
                        applicant.append((doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties'][
                                              'us-applicants']['us-applicant'])[i])

                    applicant_sequence = []
                    applicant_app_type = []
                    applicant_designation = []
                    applicant_address_last_name = []
                    applicant_address_first_name = []
                    applicant_address_city = []
                    applicant_address_state = []
                    applicant_address_country = []
                    applicant_residence_country = []
                    applicant_address_street = []
                    applicant_address_postcode = []
                    applicant_authority_category = []

                    for i in applicant:
                        ubdg_parties_applicants_applicant_sequence = i['@sequence']
                        ubdg_parties_applicants_applicant_app_type = i['@app-type']
                        ubdg_parties_applicants_applicant_designation = i['@designation']
                        ubdg_parties_applicants_applicant_addressbook_last_name = i['addressbook']['last-name']
                        ubdg_parties_applicants_applicant_addressbook_first_name = i['addressbook']['first-name']
                        ubdg_parties_applicants_applicant_nationality_country = i['nationality']['country']

                        applicant_sequence.append(ubdg_parties_applicants_applicant_sequence)
                        applicant_app_type.append(ubdg_parties_applicants_applicant_app_type)
                        applicant_designation.append(ubdg_parties_applicants_applicant_designation)
                        applicant_address_last_name.append(ubdg_parties_applicants_applicant_addressbook_last_name)
                        applicant_address_first_name.append(ubdg_parties_applicants_applicant_addressbook_first_name)

                        try:
                            ubdg_parties_applicants_applicant_addressbook_address_state = i['addressbook']['address']['state']
                            ubdg_parties_applicants_applicant_addressbook_address_street = i['addressbook']['address']['street']
                            ubdg_parties_applicants_applicant_addressbook_address_postcode = i['addressbook']['address'][
                                'postcode']
                            ubdg_parties_applicants_applicant_addressbook_address_city = i['addressbook']['address']['city']
                            ubdg_parties_applicants_applicant_addressbook_address_country = i['addressbook']['address'][
                                'country']
                            ubdg_parties_applicants_applicant_residence_country = i['residence']['country']
                            ubdg_parties_applicants_applicant_applicant_authority_category = i[
                                '@applicant-authority-category']
                            applicant_address_street.append(ubdg_parties_applicants_applicant_addressbook_address_street)
                            applicant_address_postcode.append(
                                ubdg_parties_applicants_applicant_addressbook_address_postcode)
                            applicant_address_city.append(ubdg_parties_applicants_applicant_addressbook_address_city)
                            applicant_address_state.append(ubdg_parties_applicants_applicant_addressbook_address_state)
                            applicant_address_country.append(ubdg_parties_applicants_applicant_addressbook_address_country)
                            applicant_residence_country.append(ubdg_parties_applicants_applicant_residence_country)
                            applicant_authority_category.append(ubdg_parties_applicants_applicant_applicant_authority_category)
                        except:
                            pass
                            # null

        def beforeRelation(relation):
            us_related_documents = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']

            different_tags = []
            for i in us_related_documents.keys():
                different_tags.append(i)

            relation_list = []
            for i in different_tags:
                get_relation = doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents'][i]
                if isinstance(get_relation, type(list)) is True:
                    for j in range(len(get_relation) - 1):
                        for k in get_relation:
                            relation_list.append(k)
                else:
                    relation_list.append(get_relation)
            relation(relation_list)
            # null

        def relation(has_relation):

            ubdg_relateddoc_relation_parentdoc_di_country = []
            ubdg_relateddoc_relation_parentdoc_di_doc_number = []
            ubdg_relateddoc_relation_parentdoc_di_kind = []
            ubdg_relateddoc_relation_parentdoc_di_date = []
            ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_country = []
            ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_doc_number = []
            ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_kind = []
            ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_date = []
            ubdg_relateddoc_relation_parentdoc_childdoc_country = []
            ubdg_relateddoc_relation_parentdoc_childdoc_doc_number = []
            ubdg_relateddoc_relation_parentdoc_childdoc_inter_filing_date =[]
            ubdg_relateddoc_relation_parentdoc_parent_status = []
            ubdg_relateddoc_relation_parentdoc_inter_filing_date = []

            for relation_element in has_relation:

                ubdg_relateddoc_relation_parentdoc_di_country.append(
                    relation_element['relation']['parent-doc']['document-id']['country'])
                ubdg_relateddoc_relation_parentdoc_di_doc_number.append(
                    relation_element['relation']['parent-doc']['document-id']['doc-number'])
                ubdg_relateddoc_relation_parentdoc_di_kind.append(
                    relation_element['relation']['parent-doc']['document-id']['kind'])
                ubdg_relateddoc_relation_parentdoc_di_date.append(
                    relation_element['relation']['parent-doc']['document-id']['date'])

                ubdg_relateddoc_relation_parentdoc_childdoc_country.append(
                    relation_element['relation']['child-doc']['document-id']['country'])
                ubdg_relateddoc_relation_parentdoc_childdoc_doc_number.append(
                    relation_element['relation']['child-doc']['document-id']['doc-number'])

                # null
                try:
                    # null
                    relation_parent_grant_doc_number = \
                        relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['doc-number']  # null
                    relation_parent_grant_doc_kind = \
                        relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['kind']  # null
                    relation_parent_grant_doc_date = \
                        relation_element['relation']['parent-doc']['parent-grant-document']['document-id']['date']  # null
                    ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_country.append(relation_parent_grant_doc_country)
                    ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_doc_number.append(relation_parent_grant_doc_number)
                    ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_kind.append(relation_parent_grant_doc_kind)
                    ubdg_relateddoc_relation_parentdoc_parentgrantdoc_di_date.append(relation_parent_grant_doc_date)
                except:
                    pass

                try:
                    # null
                    relation_parent_status = relation_element['relation']['parent-doc']['parent_status']  # null
                    ubdg_relateddoc_relation_parentdoc_parent_status.append(relation_parent_status)
                except:
                    pass

                try:
                    relation_parentdoc_international_filing_date = \
                        relation_element['relation']['parent-doc']['international-filing-date']['date']
                    ubdg_relateddoc_relation_parentdoc_inter_filing_date.append(relation_parentdoc_international_filing_date)
                except:
                    pass

                try:
                    relation_parentdoc_childdoc_international_filing_date = \
                        relation_element['relation']['child-doc']['international-filing-date']['date']
                    ubdg_relateddoc_relation_parentdoc_childdoc_inter_filing_date.append(
                        relation_parentdoc_childdoc_international_filing_date)
                except:
                    pass





                    # null

        def usProvisionalApplication(self, xml):
            ubdg_provisional_appl_doc_country = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application'][
                    'document-id']['country']
            ubdg_provisional_appl_doc_number = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application'][
                    'document-id']['doc-number']
            ubdg_provisional_appl_doc_kind = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application'][
                    'document-id']['kind']
            ubdg_provisional_appl_doc_date = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application'][
                    'document-id']['country']
            ubdg_provisional_appl_status = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['us-provisional-application'][
                    'us-provisional-application-status']
            # null

        def relatedPublication(self, xml):
            ubdg_related_publ_doc_country = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication'][
                    'document-id']['country']
            ubdg_related_publ_doc_number = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication'][
                    'document-id']['doc-number']
            ubdg_related_publ_doc_kind = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication'][
                    'document-id']['kind']
            ubdg_related_publ_doc_date = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['us-related-documents']['related-publication'][
                    'document-id']['date']



            # become mandatory

        def inventors(self, xml):
            if range(
                    len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor'])) == 0:

                ubdg_parties_inventors_inventor_sequence = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['@sequence']
                ubdg_parties_inventors_inventor_designation = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['@designation']
                ubdg_parties_inventors_inventor_addressbook_last_name = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook'][
                        'last-name']
                ubdg_parties_inventors_inventor_addressbook_first_name = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook'][
                        'first-name']
                ubdg_parties_inventors_inventor_addressbook_address_city = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook'][
                        'address']['city']
                ubdg_parties_inventors_inventor_addressbook_address_state = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook'][
                        'address']['state']
                ubdg_parties_inventors_inventor_addressbook_address_country = \
                    doc['us-patent-grant']['us-bibliographic-data-grant']['parties']['inventors']['inventor']['addressbook'][
                        'address']['country']

            else:
                inventor = []
                for i in range(
                        len(doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor'])):
                    applicant.append(
                        (doc['us-patent-grant']['us-bibliographic-data-grant']['us-parties']['inventors']['inventor'])[i])

                inventor_sequence = []
                inventor_designation = []
                inventor_address_last_name = []
                inventor_address_first_name = []
                inventor_address_city = []
                inventor_address_state = []
                inventor_address_country = []

                for i in inventor:
                    ubdg_parties_inventors_inventor_sequence = i['@sequence']
                    ubdg_parties_inventors_inventor_designation = i['@designation']
                    ubdg_parties_inventors_inventor_addressbook_last_name = i['addressbook']['last-name']
                    ubdg_parties_inventors_inventor_addressbook_first_name = i['addressbook']['first-name']

                    inventor_sequence.append(ubdg_parties_inventors_inventor_sequence)
                    inventor_designation.append(ubdg_parties_inventors_inventor_designation)
                    inventor_address_last_name.append(ubdg_parties_inventors_inventor_addressbook_last_name)
                    inventor_address_first_name.append(ubdg_parties_inventors_inventor_addressbook_first_name)

                    try:
                        ubdg_parties_inventors_inventor_addressbook_address_state = i['addressbook']['address']['state']
                        ubdg_parties_inventors_inventor_addressbook_address_city = i['addressbook']['address']['city']
                        ubdg_parties_inventors_inventor_addressbook_address_country = i['addressbook']['address']['country']
                        inventor_address_city.append(ubdg_parties_inventors_inventor_addressbook_address_city)
                        inventor_address_state.append(ubdg_parties_inventors_inventor_addressbook_address_state)
                        inventor_address_country.append(ubdg_parties_inventors_inventor_addressbook_address_country)
                    except: pass


        def claim(self, xml):
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

        def hagueAgreementData:
            ubdg_hague_inter_filing_date = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['hague-agreement-data']['international-filing-date']
            ubdg_hague_inter_regist_publ_date = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['hague-agreement-data']['international-registration-publication-date']
            ubdg_hague_inter_regist_num = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['hague-agreement-data']['international-registration-number']
            ubdg_hague_inter_regist_date = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['hague-agreement-data']['international-registration-date']

        def pctOrReginalFilngData:
            ubdg_pct_reg_fil_data_di_country = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['pct-or-regional-filing-data']['document-id']['country']
            ubdg_pct_reg_fil_data_di_doc_num = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['pct-or-regional-filing-data']['document-id'][
                    'doc-number']
            ubdg_pct_reg_fil_data_di_kind = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['pct-or-regional-filing-data']['document-id'][
                    'kind']
            ubdg_pct_reg_fil_data_di_date = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['pct-or-regional-filing-data']['document-id'][
                    'date']
            ubdg_pct_reg_fil_data_di_124_date = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['pct-or-regional-filing-data']['document-id'][
                    'us-371c124-date']['date']
            ubdg_pct_reg_fil_data_di_12_date = \
                doc['us-patent-grant']['us-bibliographic-data-grant']['pct-or-regional-filing-data']['document-id'][
                    'us-371c12-date']['date']
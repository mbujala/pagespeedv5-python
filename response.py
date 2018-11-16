from openpyxl import Workbook

def page_speed_response(data):
    wb = Workbook()
    ws = wb.active

    def loading_experience(data):
        first_input_delay_rate = data['loadingExperience']['metrics']['FIRST_INPUT_DELAY_MS']['category']
        ws['A1'] = first_input_delay_rate
        first_input_delay_load_time = data['loadingExperience']['metrics']['FIRST_INPUT_DELAY_MS']['percentile']
        first_input_delay_fast_load = round(data['loadingExperience']['metrics']['FIRST_INPUT_DELAY_MS']['distributions'][0]['proportion'],2)*100
        first_input_delay_average_load = round(data['loadingExperience']['metrics']['FIRST_INPUT_DELAY_MS']['distributions'][1]['proportion'],2)*100
        first_input_delay_slow_load = round(data['loadingExperience']['metrics']['FIRST_INPUT_DELAY_MS']['distributions'][2]['proportion'],2)*100

        first_contentful_paint_rate = data['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['category']
        first_contentful_paint_load_time = data['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['percentile']
        first_contentful_paint_fast_load = round(data['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['distributions'][0]['proportion'],2)*100
        first_contentful_paint_average_load = round(data['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['distributions'][1]['proportion'],2)*100
        first_contentful_paint_slow_load= round(data['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['distributions'][2]['proportion'],2)*100

        overall_rate = data['loadingExperience']['overall_category']


    def best_practices(data):
        print(data['lighthouseResult']['audits']['is-on-https']['title'])


    def seo_audit(data):
        print(data['lighthouseResult']['audits']['robots-txt']['title'])

    loading_experience(data)
    best_practices(data)
    seo_audit(data)
    wb.save("page-speed-data.xlsx")